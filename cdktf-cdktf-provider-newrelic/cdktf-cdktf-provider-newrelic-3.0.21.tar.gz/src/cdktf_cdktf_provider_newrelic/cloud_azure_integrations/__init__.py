'''
# `newrelic_cloud_azure_integrations`

Refer to the Terraform Registory for docs: [`newrelic_cloud_azure_integrations`](https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations).
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


class CloudAzureIntegrations(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrations",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations newrelic_cloud_azure_integrations}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        linked_account_id: jsii.Number,
        account_id: typing.Optional[jsii.Number] = None,
        api_management: typing.Optional[typing.Union["CloudAzureIntegrationsApiManagement", typing.Dict[str, typing.Any]]] = None,
        app_gateway: typing.Optional[typing.Union["CloudAzureIntegrationsAppGateway", typing.Dict[str, typing.Any]]] = None,
        app_service: typing.Optional[typing.Union["CloudAzureIntegrationsAppService", typing.Dict[str, typing.Any]]] = None,
        containers: typing.Optional[typing.Union["CloudAzureIntegrationsContainers", typing.Dict[str, typing.Any]]] = None,
        cosmos_db: typing.Optional[typing.Union["CloudAzureIntegrationsCosmosDb", typing.Dict[str, typing.Any]]] = None,
        cost_management: typing.Optional[typing.Union["CloudAzureIntegrationsCostManagement", typing.Dict[str, typing.Any]]] = None,
        data_factory: typing.Optional[typing.Union["CloudAzureIntegrationsDataFactory", typing.Dict[str, typing.Any]]] = None,
        event_hub: typing.Optional[typing.Union["CloudAzureIntegrationsEventHub", typing.Dict[str, typing.Any]]] = None,
        express_route: typing.Optional[typing.Union["CloudAzureIntegrationsExpressRoute", typing.Dict[str, typing.Any]]] = None,
        firewalls: typing.Optional[typing.Union["CloudAzureIntegrationsFirewalls", typing.Dict[str, typing.Any]]] = None,
        front_door: typing.Optional[typing.Union["CloudAzureIntegrationsFrontDoor", typing.Dict[str, typing.Any]]] = None,
        functions: typing.Optional[typing.Union["CloudAzureIntegrationsFunctions", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        key_vault: typing.Optional[typing.Union["CloudAzureIntegrationsKeyVault", typing.Dict[str, typing.Any]]] = None,
        load_balancer: typing.Optional[typing.Union["CloudAzureIntegrationsLoadBalancer", typing.Dict[str, typing.Any]]] = None,
        logic_apps: typing.Optional[typing.Union["CloudAzureIntegrationsLogicApps", typing.Dict[str, typing.Any]]] = None,
        machine_learning: typing.Optional[typing.Union["CloudAzureIntegrationsMachineLearning", typing.Dict[str, typing.Any]]] = None,
        maria_db: typing.Optional[typing.Union["CloudAzureIntegrationsMariaDb", typing.Dict[str, typing.Any]]] = None,
        mysql: typing.Optional[typing.Union["CloudAzureIntegrationsMysql", typing.Dict[str, typing.Any]]] = None,
        postgresql: typing.Optional[typing.Union["CloudAzureIntegrationsPostgresql", typing.Dict[str, typing.Any]]] = None,
        power_bi_dedicated: typing.Optional[typing.Union["CloudAzureIntegrationsPowerBiDedicated", typing.Dict[str, typing.Any]]] = None,
        redis_cache: typing.Optional[typing.Union["CloudAzureIntegrationsRedisCache", typing.Dict[str, typing.Any]]] = None,
        service_bus: typing.Optional[typing.Union["CloudAzureIntegrationsServiceBus", typing.Dict[str, typing.Any]]] = None,
        sql: typing.Optional[typing.Union["CloudAzureIntegrationsSql", typing.Dict[str, typing.Any]]] = None,
        sql_managed: typing.Optional[typing.Union["CloudAzureIntegrationsSqlManaged", typing.Dict[str, typing.Any]]] = None,
        storage: typing.Optional[typing.Union["CloudAzureIntegrationsStorage", typing.Dict[str, typing.Any]]] = None,
        virtual_machine: typing.Optional[typing.Union["CloudAzureIntegrationsVirtualMachine", typing.Dict[str, typing.Any]]] = None,
        virtual_networks: typing.Optional[typing.Union["CloudAzureIntegrationsVirtualNetworks", typing.Dict[str, typing.Any]]] = None,
        vms: typing.Optional[typing.Union["CloudAzureIntegrationsVms", typing.Dict[str, typing.Any]]] = None,
        vpn_gateway: typing.Optional[typing.Union["CloudAzureIntegrationsVpnGateway", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations newrelic_cloud_azure_integrations} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param linked_account_id: The ID of the linked Azure account in New Relic. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#linked_account_id CloudAzureIntegrations#linked_account_id}
        :param account_id: The ID of the account in New Relic. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#account_id CloudAzureIntegrations#account_id}
        :param api_management: api_management block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#api_management CloudAzureIntegrations#api_management}
        :param app_gateway: app_gateway block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#app_gateway CloudAzureIntegrations#app_gateway}
        :param app_service: app_service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#app_service CloudAzureIntegrations#app_service}
        :param containers: containers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#containers CloudAzureIntegrations#containers}
        :param cosmos_db: cosmos_db block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#cosmos_db CloudAzureIntegrations#cosmos_db}
        :param cost_management: cost_management block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#cost_management CloudAzureIntegrations#cost_management}
        :param data_factory: data_factory block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#data_factory CloudAzureIntegrations#data_factory}
        :param event_hub: event_hub block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#event_hub CloudAzureIntegrations#event_hub}
        :param express_route: express_route block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#express_route CloudAzureIntegrations#express_route}
        :param firewalls: firewalls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#firewalls CloudAzureIntegrations#firewalls}
        :param front_door: front_door block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#front_door CloudAzureIntegrations#front_door}
        :param functions: functions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#functions CloudAzureIntegrations#functions}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#id CloudAzureIntegrations#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param key_vault: key_vault block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#key_vault CloudAzureIntegrations#key_vault}
        :param load_balancer: load_balancer block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#load_balancer CloudAzureIntegrations#load_balancer}
        :param logic_apps: logic_apps block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#logic_apps CloudAzureIntegrations#logic_apps}
        :param machine_learning: machine_learning block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#machine_learning CloudAzureIntegrations#machine_learning}
        :param maria_db: maria_db block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#maria_db CloudAzureIntegrations#maria_db}
        :param mysql: mysql block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#mysql CloudAzureIntegrations#mysql}
        :param postgresql: postgresql block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#postgresql CloudAzureIntegrations#postgresql}
        :param power_bi_dedicated: power_bi_dedicated block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#power_bi_dedicated CloudAzureIntegrations#power_bi_dedicated}
        :param redis_cache: redis_cache block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#redis_cache CloudAzureIntegrations#redis_cache}
        :param service_bus: service_bus block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#service_bus CloudAzureIntegrations#service_bus}
        :param sql: sql block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#sql CloudAzureIntegrations#sql}
        :param sql_managed: sql_managed block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#sql_managed CloudAzureIntegrations#sql_managed}
        :param storage: storage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#storage CloudAzureIntegrations#storage}
        :param virtual_machine: virtual_machine block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#virtual_machine CloudAzureIntegrations#virtual_machine}
        :param virtual_networks: virtual_networks block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#virtual_networks CloudAzureIntegrations#virtual_networks}
        :param vms: vms block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#vms CloudAzureIntegrations#vms}
        :param vpn_gateway: vpn_gateway block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#vpn_gateway CloudAzureIntegrations#vpn_gateway}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAzureIntegrations.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CloudAzureIntegrationsConfig(
            linked_account_id=linked_account_id,
            account_id=account_id,
            api_management=api_management,
            app_gateway=app_gateway,
            app_service=app_service,
            containers=containers,
            cosmos_db=cosmos_db,
            cost_management=cost_management,
            data_factory=data_factory,
            event_hub=event_hub,
            express_route=express_route,
            firewalls=firewalls,
            front_door=front_door,
            functions=functions,
            id=id,
            key_vault=key_vault,
            load_balancer=load_balancer,
            logic_apps=logic_apps,
            machine_learning=machine_learning,
            maria_db=maria_db,
            mysql=mysql,
            postgresql=postgresql,
            power_bi_dedicated=power_bi_dedicated,
            redis_cache=redis_cache,
            service_bus=service_bus,
            sql=sql,
            sql_managed=sql_managed,
            storage=storage,
            virtual_machine=virtual_machine,
            virtual_networks=virtual_networks,
            vms=vms,
            vpn_gateway=vpn_gateway,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putApiManagement")
    def put_api_management(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        value = CloudAzureIntegrationsApiManagement(
            metrics_polling_interval=metrics_polling_interval,
            resource_groups=resource_groups,
        )

        return typing.cast(None, jsii.invoke(self, "putApiManagement", [value]))

    @jsii.member(jsii_name="putAppGateway")
    def put_app_gateway(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        value = CloudAzureIntegrationsAppGateway(
            metrics_polling_interval=metrics_polling_interval,
            resource_groups=resource_groups,
        )

        return typing.cast(None, jsii.invoke(self, "putAppGateway", [value]))

    @jsii.member(jsii_name="putAppService")
    def put_app_service(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        value = CloudAzureIntegrationsAppService(
            metrics_polling_interval=metrics_polling_interval,
            resource_groups=resource_groups,
        )

        return typing.cast(None, jsii.invoke(self, "putAppService", [value]))

    @jsii.member(jsii_name="putContainers")
    def put_containers(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        value = CloudAzureIntegrationsContainers(
            metrics_polling_interval=metrics_polling_interval,
            resource_groups=resource_groups,
        )

        return typing.cast(None, jsii.invoke(self, "putContainers", [value]))

    @jsii.member(jsii_name="putCosmosDb")
    def put_cosmos_db(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        value = CloudAzureIntegrationsCosmosDb(
            metrics_polling_interval=metrics_polling_interval,
            resource_groups=resource_groups,
        )

        return typing.cast(None, jsii.invoke(self, "putCosmosDb", [value]))

    @jsii.member(jsii_name="putCostManagement")
    def put_cost_management(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        tag_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param tag_keys: Specify if additional cost data per tag should be collected. This field is case sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#tag_keys CloudAzureIntegrations#tag_keys}
        '''
        value = CloudAzureIntegrationsCostManagement(
            metrics_polling_interval=metrics_polling_interval, tag_keys=tag_keys
        )

        return typing.cast(None, jsii.invoke(self, "putCostManagement", [value]))

    @jsii.member(jsii_name="putDataFactory")
    def put_data_factory(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        value = CloudAzureIntegrationsDataFactory(
            metrics_polling_interval=metrics_polling_interval,
            resource_groups=resource_groups,
        )

        return typing.cast(None, jsii.invoke(self, "putDataFactory", [value]))

    @jsii.member(jsii_name="putEventHub")
    def put_event_hub(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        value = CloudAzureIntegrationsEventHub(
            metrics_polling_interval=metrics_polling_interval,
            resource_groups=resource_groups,
        )

        return typing.cast(None, jsii.invoke(self, "putEventHub", [value]))

    @jsii.member(jsii_name="putExpressRoute")
    def put_express_route(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        value = CloudAzureIntegrationsExpressRoute(
            metrics_polling_interval=metrics_polling_interval,
            resource_groups=resource_groups,
        )

        return typing.cast(None, jsii.invoke(self, "putExpressRoute", [value]))

    @jsii.member(jsii_name="putFirewalls")
    def put_firewalls(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        value = CloudAzureIntegrationsFirewalls(
            metrics_polling_interval=metrics_polling_interval,
            resource_groups=resource_groups,
        )

        return typing.cast(None, jsii.invoke(self, "putFirewalls", [value]))

    @jsii.member(jsii_name="putFrontDoor")
    def put_front_door(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        value = CloudAzureIntegrationsFrontDoor(
            metrics_polling_interval=metrics_polling_interval,
            resource_groups=resource_groups,
        )

        return typing.cast(None, jsii.invoke(self, "putFrontDoor", [value]))

    @jsii.member(jsii_name="putFunctions")
    def put_functions(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        value = CloudAzureIntegrationsFunctions(
            metrics_polling_interval=metrics_polling_interval,
            resource_groups=resource_groups,
        )

        return typing.cast(None, jsii.invoke(self, "putFunctions", [value]))

    @jsii.member(jsii_name="putKeyVault")
    def put_key_vault(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        value = CloudAzureIntegrationsKeyVault(
            metrics_polling_interval=metrics_polling_interval,
            resource_groups=resource_groups,
        )

        return typing.cast(None, jsii.invoke(self, "putKeyVault", [value]))

    @jsii.member(jsii_name="putLoadBalancer")
    def put_load_balancer(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        value = CloudAzureIntegrationsLoadBalancer(
            metrics_polling_interval=metrics_polling_interval,
            resource_groups=resource_groups,
        )

        return typing.cast(None, jsii.invoke(self, "putLoadBalancer", [value]))

    @jsii.member(jsii_name="putLogicApps")
    def put_logic_apps(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        value = CloudAzureIntegrationsLogicApps(
            metrics_polling_interval=metrics_polling_interval,
            resource_groups=resource_groups,
        )

        return typing.cast(None, jsii.invoke(self, "putLogicApps", [value]))

    @jsii.member(jsii_name="putMachineLearning")
    def put_machine_learning(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        value = CloudAzureIntegrationsMachineLearning(
            metrics_polling_interval=metrics_polling_interval,
            resource_groups=resource_groups,
        )

        return typing.cast(None, jsii.invoke(self, "putMachineLearning", [value]))

    @jsii.member(jsii_name="putMariaDb")
    def put_maria_db(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        value = CloudAzureIntegrationsMariaDb(
            metrics_polling_interval=metrics_polling_interval,
            resource_groups=resource_groups,
        )

        return typing.cast(None, jsii.invoke(self, "putMariaDb", [value]))

    @jsii.member(jsii_name="putMysql")
    def put_mysql(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        value = CloudAzureIntegrationsMysql(
            metrics_polling_interval=metrics_polling_interval,
            resource_groups=resource_groups,
        )

        return typing.cast(None, jsii.invoke(self, "putMysql", [value]))

    @jsii.member(jsii_name="putPostgresql")
    def put_postgresql(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        value = CloudAzureIntegrationsPostgresql(
            metrics_polling_interval=metrics_polling_interval,
            resource_groups=resource_groups,
        )

        return typing.cast(None, jsii.invoke(self, "putPostgresql", [value]))

    @jsii.member(jsii_name="putPowerBiDedicated")
    def put_power_bi_dedicated(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        value = CloudAzureIntegrationsPowerBiDedicated(
            metrics_polling_interval=metrics_polling_interval,
            resource_groups=resource_groups,
        )

        return typing.cast(None, jsii.invoke(self, "putPowerBiDedicated", [value]))

    @jsii.member(jsii_name="putRedisCache")
    def put_redis_cache(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        value = CloudAzureIntegrationsRedisCache(
            metrics_polling_interval=metrics_polling_interval,
            resource_groups=resource_groups,
        )

        return typing.cast(None, jsii.invoke(self, "putRedisCache", [value]))

    @jsii.member(jsii_name="putServiceBus")
    def put_service_bus(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        value = CloudAzureIntegrationsServiceBus(
            metrics_polling_interval=metrics_polling_interval,
            resource_groups=resource_groups,
        )

        return typing.cast(None, jsii.invoke(self, "putServiceBus", [value]))

    @jsii.member(jsii_name="putSql")
    def put_sql(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        value = CloudAzureIntegrationsSql(
            metrics_polling_interval=metrics_polling_interval,
            resource_groups=resource_groups,
        )

        return typing.cast(None, jsii.invoke(self, "putSql", [value]))

    @jsii.member(jsii_name="putSqlManaged")
    def put_sql_managed(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        value = CloudAzureIntegrationsSqlManaged(
            metrics_polling_interval=metrics_polling_interval,
            resource_groups=resource_groups,
        )

        return typing.cast(None, jsii.invoke(self, "putSqlManaged", [value]))

    @jsii.member(jsii_name="putStorage")
    def put_storage(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        value = CloudAzureIntegrationsStorage(
            metrics_polling_interval=metrics_polling_interval,
            resource_groups=resource_groups,
        )

        return typing.cast(None, jsii.invoke(self, "putStorage", [value]))

    @jsii.member(jsii_name="putVirtualMachine")
    def put_virtual_machine(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        value = CloudAzureIntegrationsVirtualMachine(
            metrics_polling_interval=metrics_polling_interval,
            resource_groups=resource_groups,
        )

        return typing.cast(None, jsii.invoke(self, "putVirtualMachine", [value]))

    @jsii.member(jsii_name="putVirtualNetworks")
    def put_virtual_networks(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        value = CloudAzureIntegrationsVirtualNetworks(
            metrics_polling_interval=metrics_polling_interval,
            resource_groups=resource_groups,
        )

        return typing.cast(None, jsii.invoke(self, "putVirtualNetworks", [value]))

    @jsii.member(jsii_name="putVms")
    def put_vms(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        value = CloudAzureIntegrationsVms(
            metrics_polling_interval=metrics_polling_interval,
            resource_groups=resource_groups,
        )

        return typing.cast(None, jsii.invoke(self, "putVms", [value]))

    @jsii.member(jsii_name="putVpnGateway")
    def put_vpn_gateway(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        value = CloudAzureIntegrationsVpnGateway(
            metrics_polling_interval=metrics_polling_interval,
            resource_groups=resource_groups,
        )

        return typing.cast(None, jsii.invoke(self, "putVpnGateway", [value]))

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @jsii.member(jsii_name="resetApiManagement")
    def reset_api_management(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiManagement", []))

    @jsii.member(jsii_name="resetAppGateway")
    def reset_app_gateway(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppGateway", []))

    @jsii.member(jsii_name="resetAppService")
    def reset_app_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppService", []))

    @jsii.member(jsii_name="resetContainers")
    def reset_containers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainers", []))

    @jsii.member(jsii_name="resetCosmosDb")
    def reset_cosmos_db(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCosmosDb", []))

    @jsii.member(jsii_name="resetCostManagement")
    def reset_cost_management(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCostManagement", []))

    @jsii.member(jsii_name="resetDataFactory")
    def reset_data_factory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataFactory", []))

    @jsii.member(jsii_name="resetEventHub")
    def reset_event_hub(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventHub", []))

    @jsii.member(jsii_name="resetExpressRoute")
    def reset_express_route(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpressRoute", []))

    @jsii.member(jsii_name="resetFirewalls")
    def reset_firewalls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFirewalls", []))

    @jsii.member(jsii_name="resetFrontDoor")
    def reset_front_door(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFrontDoor", []))

    @jsii.member(jsii_name="resetFunctions")
    def reset_functions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFunctions", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKeyVault")
    def reset_key_vault(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyVault", []))

    @jsii.member(jsii_name="resetLoadBalancer")
    def reset_load_balancer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancer", []))

    @jsii.member(jsii_name="resetLogicApps")
    def reset_logic_apps(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogicApps", []))

    @jsii.member(jsii_name="resetMachineLearning")
    def reset_machine_learning(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMachineLearning", []))

    @jsii.member(jsii_name="resetMariaDb")
    def reset_maria_db(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMariaDb", []))

    @jsii.member(jsii_name="resetMysql")
    def reset_mysql(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMysql", []))

    @jsii.member(jsii_name="resetPostgresql")
    def reset_postgresql(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPostgresql", []))

    @jsii.member(jsii_name="resetPowerBiDedicated")
    def reset_power_bi_dedicated(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPowerBiDedicated", []))

    @jsii.member(jsii_name="resetRedisCache")
    def reset_redis_cache(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedisCache", []))

    @jsii.member(jsii_name="resetServiceBus")
    def reset_service_bus(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceBus", []))

    @jsii.member(jsii_name="resetSql")
    def reset_sql(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSql", []))

    @jsii.member(jsii_name="resetSqlManaged")
    def reset_sql_managed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSqlManaged", []))

    @jsii.member(jsii_name="resetStorage")
    def reset_storage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorage", []))

    @jsii.member(jsii_name="resetVirtualMachine")
    def reset_virtual_machine(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualMachine", []))

    @jsii.member(jsii_name="resetVirtualNetworks")
    def reset_virtual_networks(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualNetworks", []))

    @jsii.member(jsii_name="resetVms")
    def reset_vms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVms", []))

    @jsii.member(jsii_name="resetVpnGateway")
    def reset_vpn_gateway(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpnGateway", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="apiManagement")
    def api_management(self) -> "CloudAzureIntegrationsApiManagementOutputReference":
        return typing.cast("CloudAzureIntegrationsApiManagementOutputReference", jsii.get(self, "apiManagement"))

    @builtins.property
    @jsii.member(jsii_name="appGateway")
    def app_gateway(self) -> "CloudAzureIntegrationsAppGatewayOutputReference":
        return typing.cast("CloudAzureIntegrationsAppGatewayOutputReference", jsii.get(self, "appGateway"))

    @builtins.property
    @jsii.member(jsii_name="appService")
    def app_service(self) -> "CloudAzureIntegrationsAppServiceOutputReference":
        return typing.cast("CloudAzureIntegrationsAppServiceOutputReference", jsii.get(self, "appService"))

    @builtins.property
    @jsii.member(jsii_name="containers")
    def containers(self) -> "CloudAzureIntegrationsContainersOutputReference":
        return typing.cast("CloudAzureIntegrationsContainersOutputReference", jsii.get(self, "containers"))

    @builtins.property
    @jsii.member(jsii_name="cosmosDb")
    def cosmos_db(self) -> "CloudAzureIntegrationsCosmosDbOutputReference":
        return typing.cast("CloudAzureIntegrationsCosmosDbOutputReference", jsii.get(self, "cosmosDb"))

    @builtins.property
    @jsii.member(jsii_name="costManagement")
    def cost_management(self) -> "CloudAzureIntegrationsCostManagementOutputReference":
        return typing.cast("CloudAzureIntegrationsCostManagementOutputReference", jsii.get(self, "costManagement"))

    @builtins.property
    @jsii.member(jsii_name="dataFactory")
    def data_factory(self) -> "CloudAzureIntegrationsDataFactoryOutputReference":
        return typing.cast("CloudAzureIntegrationsDataFactoryOutputReference", jsii.get(self, "dataFactory"))

    @builtins.property
    @jsii.member(jsii_name="eventHub")
    def event_hub(self) -> "CloudAzureIntegrationsEventHubOutputReference":
        return typing.cast("CloudAzureIntegrationsEventHubOutputReference", jsii.get(self, "eventHub"))

    @builtins.property
    @jsii.member(jsii_name="expressRoute")
    def express_route(self) -> "CloudAzureIntegrationsExpressRouteOutputReference":
        return typing.cast("CloudAzureIntegrationsExpressRouteOutputReference", jsii.get(self, "expressRoute"))

    @builtins.property
    @jsii.member(jsii_name="firewalls")
    def firewalls(self) -> "CloudAzureIntegrationsFirewallsOutputReference":
        return typing.cast("CloudAzureIntegrationsFirewallsOutputReference", jsii.get(self, "firewalls"))

    @builtins.property
    @jsii.member(jsii_name="frontDoor")
    def front_door(self) -> "CloudAzureIntegrationsFrontDoorOutputReference":
        return typing.cast("CloudAzureIntegrationsFrontDoorOutputReference", jsii.get(self, "frontDoor"))

    @builtins.property
    @jsii.member(jsii_name="functions")
    def functions(self) -> "CloudAzureIntegrationsFunctionsOutputReference":
        return typing.cast("CloudAzureIntegrationsFunctionsOutputReference", jsii.get(self, "functions"))

    @builtins.property
    @jsii.member(jsii_name="keyVault")
    def key_vault(self) -> "CloudAzureIntegrationsKeyVaultOutputReference":
        return typing.cast("CloudAzureIntegrationsKeyVaultOutputReference", jsii.get(self, "keyVault"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancer")
    def load_balancer(self) -> "CloudAzureIntegrationsLoadBalancerOutputReference":
        return typing.cast("CloudAzureIntegrationsLoadBalancerOutputReference", jsii.get(self, "loadBalancer"))

    @builtins.property
    @jsii.member(jsii_name="logicApps")
    def logic_apps(self) -> "CloudAzureIntegrationsLogicAppsOutputReference":
        return typing.cast("CloudAzureIntegrationsLogicAppsOutputReference", jsii.get(self, "logicApps"))

    @builtins.property
    @jsii.member(jsii_name="machineLearning")
    def machine_learning(
        self,
    ) -> "CloudAzureIntegrationsMachineLearningOutputReference":
        return typing.cast("CloudAzureIntegrationsMachineLearningOutputReference", jsii.get(self, "machineLearning"))

    @builtins.property
    @jsii.member(jsii_name="mariaDb")
    def maria_db(self) -> "CloudAzureIntegrationsMariaDbOutputReference":
        return typing.cast("CloudAzureIntegrationsMariaDbOutputReference", jsii.get(self, "mariaDb"))

    @builtins.property
    @jsii.member(jsii_name="mysql")
    def mysql(self) -> "CloudAzureIntegrationsMysqlOutputReference":
        return typing.cast("CloudAzureIntegrationsMysqlOutputReference", jsii.get(self, "mysql"))

    @builtins.property
    @jsii.member(jsii_name="postgresql")
    def postgresql(self) -> "CloudAzureIntegrationsPostgresqlOutputReference":
        return typing.cast("CloudAzureIntegrationsPostgresqlOutputReference", jsii.get(self, "postgresql"))

    @builtins.property
    @jsii.member(jsii_name="powerBiDedicated")
    def power_bi_dedicated(
        self,
    ) -> "CloudAzureIntegrationsPowerBiDedicatedOutputReference":
        return typing.cast("CloudAzureIntegrationsPowerBiDedicatedOutputReference", jsii.get(self, "powerBiDedicated"))

    @builtins.property
    @jsii.member(jsii_name="redisCache")
    def redis_cache(self) -> "CloudAzureIntegrationsRedisCacheOutputReference":
        return typing.cast("CloudAzureIntegrationsRedisCacheOutputReference", jsii.get(self, "redisCache"))

    @builtins.property
    @jsii.member(jsii_name="serviceBus")
    def service_bus(self) -> "CloudAzureIntegrationsServiceBusOutputReference":
        return typing.cast("CloudAzureIntegrationsServiceBusOutputReference", jsii.get(self, "serviceBus"))

    @builtins.property
    @jsii.member(jsii_name="sql")
    def sql(self) -> "CloudAzureIntegrationsSqlOutputReference":
        return typing.cast("CloudAzureIntegrationsSqlOutputReference", jsii.get(self, "sql"))

    @builtins.property
    @jsii.member(jsii_name="sqlManaged")
    def sql_managed(self) -> "CloudAzureIntegrationsSqlManagedOutputReference":
        return typing.cast("CloudAzureIntegrationsSqlManagedOutputReference", jsii.get(self, "sqlManaged"))

    @builtins.property
    @jsii.member(jsii_name="storage")
    def storage(self) -> "CloudAzureIntegrationsStorageOutputReference":
        return typing.cast("CloudAzureIntegrationsStorageOutputReference", jsii.get(self, "storage"))

    @builtins.property
    @jsii.member(jsii_name="virtualMachine")
    def virtual_machine(self) -> "CloudAzureIntegrationsVirtualMachineOutputReference":
        return typing.cast("CloudAzureIntegrationsVirtualMachineOutputReference", jsii.get(self, "virtualMachine"))

    @builtins.property
    @jsii.member(jsii_name="virtualNetworks")
    def virtual_networks(
        self,
    ) -> "CloudAzureIntegrationsVirtualNetworksOutputReference":
        return typing.cast("CloudAzureIntegrationsVirtualNetworksOutputReference", jsii.get(self, "virtualNetworks"))

    @builtins.property
    @jsii.member(jsii_name="vms")
    def vms(self) -> "CloudAzureIntegrationsVmsOutputReference":
        return typing.cast("CloudAzureIntegrationsVmsOutputReference", jsii.get(self, "vms"))

    @builtins.property
    @jsii.member(jsii_name="vpnGateway")
    def vpn_gateway(self) -> "CloudAzureIntegrationsVpnGatewayOutputReference":
        return typing.cast("CloudAzureIntegrationsVpnGatewayOutputReference", jsii.get(self, "vpnGateway"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="apiManagementInput")
    def api_management_input(
        self,
    ) -> typing.Optional["CloudAzureIntegrationsApiManagement"]:
        return typing.cast(typing.Optional["CloudAzureIntegrationsApiManagement"], jsii.get(self, "apiManagementInput"))

    @builtins.property
    @jsii.member(jsii_name="appGatewayInput")
    def app_gateway_input(self) -> typing.Optional["CloudAzureIntegrationsAppGateway"]:
        return typing.cast(typing.Optional["CloudAzureIntegrationsAppGateway"], jsii.get(self, "appGatewayInput"))

    @builtins.property
    @jsii.member(jsii_name="appServiceInput")
    def app_service_input(self) -> typing.Optional["CloudAzureIntegrationsAppService"]:
        return typing.cast(typing.Optional["CloudAzureIntegrationsAppService"], jsii.get(self, "appServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="containersInput")
    def containers_input(self) -> typing.Optional["CloudAzureIntegrationsContainers"]:
        return typing.cast(typing.Optional["CloudAzureIntegrationsContainers"], jsii.get(self, "containersInput"))

    @builtins.property
    @jsii.member(jsii_name="cosmosDbInput")
    def cosmos_db_input(self) -> typing.Optional["CloudAzureIntegrationsCosmosDb"]:
        return typing.cast(typing.Optional["CloudAzureIntegrationsCosmosDb"], jsii.get(self, "cosmosDbInput"))

    @builtins.property
    @jsii.member(jsii_name="costManagementInput")
    def cost_management_input(
        self,
    ) -> typing.Optional["CloudAzureIntegrationsCostManagement"]:
        return typing.cast(typing.Optional["CloudAzureIntegrationsCostManagement"], jsii.get(self, "costManagementInput"))

    @builtins.property
    @jsii.member(jsii_name="dataFactoryInput")
    def data_factory_input(
        self,
    ) -> typing.Optional["CloudAzureIntegrationsDataFactory"]:
        return typing.cast(typing.Optional["CloudAzureIntegrationsDataFactory"], jsii.get(self, "dataFactoryInput"))

    @builtins.property
    @jsii.member(jsii_name="eventHubInput")
    def event_hub_input(self) -> typing.Optional["CloudAzureIntegrationsEventHub"]:
        return typing.cast(typing.Optional["CloudAzureIntegrationsEventHub"], jsii.get(self, "eventHubInput"))

    @builtins.property
    @jsii.member(jsii_name="expressRouteInput")
    def express_route_input(
        self,
    ) -> typing.Optional["CloudAzureIntegrationsExpressRoute"]:
        return typing.cast(typing.Optional["CloudAzureIntegrationsExpressRoute"], jsii.get(self, "expressRouteInput"))

    @builtins.property
    @jsii.member(jsii_name="firewallsInput")
    def firewalls_input(self) -> typing.Optional["CloudAzureIntegrationsFirewalls"]:
        return typing.cast(typing.Optional["CloudAzureIntegrationsFirewalls"], jsii.get(self, "firewallsInput"))

    @builtins.property
    @jsii.member(jsii_name="frontDoorInput")
    def front_door_input(self) -> typing.Optional["CloudAzureIntegrationsFrontDoor"]:
        return typing.cast(typing.Optional["CloudAzureIntegrationsFrontDoor"], jsii.get(self, "frontDoorInput"))

    @builtins.property
    @jsii.member(jsii_name="functionsInput")
    def functions_input(self) -> typing.Optional["CloudAzureIntegrationsFunctions"]:
        return typing.cast(typing.Optional["CloudAzureIntegrationsFunctions"], jsii.get(self, "functionsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultInput")
    def key_vault_input(self) -> typing.Optional["CloudAzureIntegrationsKeyVault"]:
        return typing.cast(typing.Optional["CloudAzureIntegrationsKeyVault"], jsii.get(self, "keyVaultInput"))

    @builtins.property
    @jsii.member(jsii_name="linkedAccountIdInput")
    def linked_account_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "linkedAccountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerInput")
    def load_balancer_input(
        self,
    ) -> typing.Optional["CloudAzureIntegrationsLoadBalancer"]:
        return typing.cast(typing.Optional["CloudAzureIntegrationsLoadBalancer"], jsii.get(self, "loadBalancerInput"))

    @builtins.property
    @jsii.member(jsii_name="logicAppsInput")
    def logic_apps_input(self) -> typing.Optional["CloudAzureIntegrationsLogicApps"]:
        return typing.cast(typing.Optional["CloudAzureIntegrationsLogicApps"], jsii.get(self, "logicAppsInput"))

    @builtins.property
    @jsii.member(jsii_name="machineLearningInput")
    def machine_learning_input(
        self,
    ) -> typing.Optional["CloudAzureIntegrationsMachineLearning"]:
        return typing.cast(typing.Optional["CloudAzureIntegrationsMachineLearning"], jsii.get(self, "machineLearningInput"))

    @builtins.property
    @jsii.member(jsii_name="mariaDbInput")
    def maria_db_input(self) -> typing.Optional["CloudAzureIntegrationsMariaDb"]:
        return typing.cast(typing.Optional["CloudAzureIntegrationsMariaDb"], jsii.get(self, "mariaDbInput"))

    @builtins.property
    @jsii.member(jsii_name="mysqlInput")
    def mysql_input(self) -> typing.Optional["CloudAzureIntegrationsMysql"]:
        return typing.cast(typing.Optional["CloudAzureIntegrationsMysql"], jsii.get(self, "mysqlInput"))

    @builtins.property
    @jsii.member(jsii_name="postgresqlInput")
    def postgresql_input(self) -> typing.Optional["CloudAzureIntegrationsPostgresql"]:
        return typing.cast(typing.Optional["CloudAzureIntegrationsPostgresql"], jsii.get(self, "postgresqlInput"))

    @builtins.property
    @jsii.member(jsii_name="powerBiDedicatedInput")
    def power_bi_dedicated_input(
        self,
    ) -> typing.Optional["CloudAzureIntegrationsPowerBiDedicated"]:
        return typing.cast(typing.Optional["CloudAzureIntegrationsPowerBiDedicated"], jsii.get(self, "powerBiDedicatedInput"))

    @builtins.property
    @jsii.member(jsii_name="redisCacheInput")
    def redis_cache_input(self) -> typing.Optional["CloudAzureIntegrationsRedisCache"]:
        return typing.cast(typing.Optional["CloudAzureIntegrationsRedisCache"], jsii.get(self, "redisCacheInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceBusInput")
    def service_bus_input(self) -> typing.Optional["CloudAzureIntegrationsServiceBus"]:
        return typing.cast(typing.Optional["CloudAzureIntegrationsServiceBus"], jsii.get(self, "serviceBusInput"))

    @builtins.property
    @jsii.member(jsii_name="sqlInput")
    def sql_input(self) -> typing.Optional["CloudAzureIntegrationsSql"]:
        return typing.cast(typing.Optional["CloudAzureIntegrationsSql"], jsii.get(self, "sqlInput"))

    @builtins.property
    @jsii.member(jsii_name="sqlManagedInput")
    def sql_managed_input(self) -> typing.Optional["CloudAzureIntegrationsSqlManaged"]:
        return typing.cast(typing.Optional["CloudAzureIntegrationsSqlManaged"], jsii.get(self, "sqlManagedInput"))

    @builtins.property
    @jsii.member(jsii_name="storageInput")
    def storage_input(self) -> typing.Optional["CloudAzureIntegrationsStorage"]:
        return typing.cast(typing.Optional["CloudAzureIntegrationsStorage"], jsii.get(self, "storageInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualMachineInput")
    def virtual_machine_input(
        self,
    ) -> typing.Optional["CloudAzureIntegrationsVirtualMachine"]:
        return typing.cast(typing.Optional["CloudAzureIntegrationsVirtualMachine"], jsii.get(self, "virtualMachineInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualNetworksInput")
    def virtual_networks_input(
        self,
    ) -> typing.Optional["CloudAzureIntegrationsVirtualNetworks"]:
        return typing.cast(typing.Optional["CloudAzureIntegrationsVirtualNetworks"], jsii.get(self, "virtualNetworksInput"))

    @builtins.property
    @jsii.member(jsii_name="vmsInput")
    def vms_input(self) -> typing.Optional["CloudAzureIntegrationsVms"]:
        return typing.cast(typing.Optional["CloudAzureIntegrationsVms"], jsii.get(self, "vmsInput"))

    @builtins.property
    @jsii.member(jsii_name="vpnGatewayInput")
    def vpn_gateway_input(self) -> typing.Optional["CloudAzureIntegrationsVpnGateway"]:
        return typing.cast(typing.Optional["CloudAzureIntegrationsVpnGateway"], jsii.get(self, "vpnGatewayInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrations, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrations, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="linkedAccountId")
    def linked_account_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "linkedAccountId"))

    @linked_account_id.setter
    def linked_account_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrations, "linked_account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "linkedAccountId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsApiManagement",
    jsii_struct_bases=[],
    name_mapping={
        "metrics_polling_interval": "metricsPollingInterval",
        "resource_groups": "resourceGroups",
    },
)
class CloudAzureIntegrationsApiManagement:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAzureIntegrationsApiManagement.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument resource_groups", value=resource_groups, expected_type=type_hints["resource_groups"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if resource_groups is not None:
            self._values["resource_groups"] = resource_groups

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resource_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        result = self._values.get("resource_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAzureIntegrationsApiManagement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAzureIntegrationsApiManagementOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsApiManagementOutputReference",
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
            type_hints = typing.get_type_hints(CloudAzureIntegrationsApiManagementOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @jsii.member(jsii_name="resetResourceGroups")
    def reset_resource_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceGroups", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupsInput")
    def resource_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourceGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsApiManagementOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroups")
    def resource_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resourceGroups"))

    @resource_groups.setter
    def resource_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsApiManagementOutputReference, "resource_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroups", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAzureIntegrationsApiManagement]:
        return typing.cast(typing.Optional[CloudAzureIntegrationsApiManagement], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAzureIntegrationsApiManagement],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsApiManagementOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsAppGateway",
    jsii_struct_bases=[],
    name_mapping={
        "metrics_polling_interval": "metricsPollingInterval",
        "resource_groups": "resourceGroups",
    },
)
class CloudAzureIntegrationsAppGateway:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAzureIntegrationsAppGateway.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument resource_groups", value=resource_groups, expected_type=type_hints["resource_groups"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if resource_groups is not None:
            self._values["resource_groups"] = resource_groups

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resource_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        result = self._values.get("resource_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAzureIntegrationsAppGateway(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAzureIntegrationsAppGatewayOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsAppGatewayOutputReference",
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
            type_hints = typing.get_type_hints(CloudAzureIntegrationsAppGatewayOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @jsii.member(jsii_name="resetResourceGroups")
    def reset_resource_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceGroups", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupsInput")
    def resource_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourceGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsAppGatewayOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroups")
    def resource_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resourceGroups"))

    @resource_groups.setter
    def resource_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsAppGatewayOutputReference, "resource_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroups", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAzureIntegrationsAppGateway]:
        return typing.cast(typing.Optional[CloudAzureIntegrationsAppGateway], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAzureIntegrationsAppGateway],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsAppGatewayOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsAppService",
    jsii_struct_bases=[],
    name_mapping={
        "metrics_polling_interval": "metricsPollingInterval",
        "resource_groups": "resourceGroups",
    },
)
class CloudAzureIntegrationsAppService:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAzureIntegrationsAppService.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument resource_groups", value=resource_groups, expected_type=type_hints["resource_groups"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if resource_groups is not None:
            self._values["resource_groups"] = resource_groups

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resource_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        result = self._values.get("resource_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAzureIntegrationsAppService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAzureIntegrationsAppServiceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsAppServiceOutputReference",
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
            type_hints = typing.get_type_hints(CloudAzureIntegrationsAppServiceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @jsii.member(jsii_name="resetResourceGroups")
    def reset_resource_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceGroups", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupsInput")
    def resource_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourceGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsAppServiceOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroups")
    def resource_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resourceGroups"))

    @resource_groups.setter
    def resource_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsAppServiceOutputReference, "resource_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroups", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAzureIntegrationsAppService]:
        return typing.cast(typing.Optional[CloudAzureIntegrationsAppService], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAzureIntegrationsAppService],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsAppServiceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "linked_account_id": "linkedAccountId",
        "account_id": "accountId",
        "api_management": "apiManagement",
        "app_gateway": "appGateway",
        "app_service": "appService",
        "containers": "containers",
        "cosmos_db": "cosmosDb",
        "cost_management": "costManagement",
        "data_factory": "dataFactory",
        "event_hub": "eventHub",
        "express_route": "expressRoute",
        "firewalls": "firewalls",
        "front_door": "frontDoor",
        "functions": "functions",
        "id": "id",
        "key_vault": "keyVault",
        "load_balancer": "loadBalancer",
        "logic_apps": "logicApps",
        "machine_learning": "machineLearning",
        "maria_db": "mariaDb",
        "mysql": "mysql",
        "postgresql": "postgresql",
        "power_bi_dedicated": "powerBiDedicated",
        "redis_cache": "redisCache",
        "service_bus": "serviceBus",
        "sql": "sql",
        "sql_managed": "sqlManaged",
        "storage": "storage",
        "virtual_machine": "virtualMachine",
        "virtual_networks": "virtualNetworks",
        "vms": "vms",
        "vpn_gateway": "vpnGateway",
    },
)
class CloudAzureIntegrationsConfig(cdktf.TerraformMetaArguments):
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
        linked_account_id: jsii.Number,
        account_id: typing.Optional[jsii.Number] = None,
        api_management: typing.Optional[typing.Union[CloudAzureIntegrationsApiManagement, typing.Dict[str, typing.Any]]] = None,
        app_gateway: typing.Optional[typing.Union[CloudAzureIntegrationsAppGateway, typing.Dict[str, typing.Any]]] = None,
        app_service: typing.Optional[typing.Union[CloudAzureIntegrationsAppService, typing.Dict[str, typing.Any]]] = None,
        containers: typing.Optional[typing.Union["CloudAzureIntegrationsContainers", typing.Dict[str, typing.Any]]] = None,
        cosmos_db: typing.Optional[typing.Union["CloudAzureIntegrationsCosmosDb", typing.Dict[str, typing.Any]]] = None,
        cost_management: typing.Optional[typing.Union["CloudAzureIntegrationsCostManagement", typing.Dict[str, typing.Any]]] = None,
        data_factory: typing.Optional[typing.Union["CloudAzureIntegrationsDataFactory", typing.Dict[str, typing.Any]]] = None,
        event_hub: typing.Optional[typing.Union["CloudAzureIntegrationsEventHub", typing.Dict[str, typing.Any]]] = None,
        express_route: typing.Optional[typing.Union["CloudAzureIntegrationsExpressRoute", typing.Dict[str, typing.Any]]] = None,
        firewalls: typing.Optional[typing.Union["CloudAzureIntegrationsFirewalls", typing.Dict[str, typing.Any]]] = None,
        front_door: typing.Optional[typing.Union["CloudAzureIntegrationsFrontDoor", typing.Dict[str, typing.Any]]] = None,
        functions: typing.Optional[typing.Union["CloudAzureIntegrationsFunctions", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        key_vault: typing.Optional[typing.Union["CloudAzureIntegrationsKeyVault", typing.Dict[str, typing.Any]]] = None,
        load_balancer: typing.Optional[typing.Union["CloudAzureIntegrationsLoadBalancer", typing.Dict[str, typing.Any]]] = None,
        logic_apps: typing.Optional[typing.Union["CloudAzureIntegrationsLogicApps", typing.Dict[str, typing.Any]]] = None,
        machine_learning: typing.Optional[typing.Union["CloudAzureIntegrationsMachineLearning", typing.Dict[str, typing.Any]]] = None,
        maria_db: typing.Optional[typing.Union["CloudAzureIntegrationsMariaDb", typing.Dict[str, typing.Any]]] = None,
        mysql: typing.Optional[typing.Union["CloudAzureIntegrationsMysql", typing.Dict[str, typing.Any]]] = None,
        postgresql: typing.Optional[typing.Union["CloudAzureIntegrationsPostgresql", typing.Dict[str, typing.Any]]] = None,
        power_bi_dedicated: typing.Optional[typing.Union["CloudAzureIntegrationsPowerBiDedicated", typing.Dict[str, typing.Any]]] = None,
        redis_cache: typing.Optional[typing.Union["CloudAzureIntegrationsRedisCache", typing.Dict[str, typing.Any]]] = None,
        service_bus: typing.Optional[typing.Union["CloudAzureIntegrationsServiceBus", typing.Dict[str, typing.Any]]] = None,
        sql: typing.Optional[typing.Union["CloudAzureIntegrationsSql", typing.Dict[str, typing.Any]]] = None,
        sql_managed: typing.Optional[typing.Union["CloudAzureIntegrationsSqlManaged", typing.Dict[str, typing.Any]]] = None,
        storage: typing.Optional[typing.Union["CloudAzureIntegrationsStorage", typing.Dict[str, typing.Any]]] = None,
        virtual_machine: typing.Optional[typing.Union["CloudAzureIntegrationsVirtualMachine", typing.Dict[str, typing.Any]]] = None,
        virtual_networks: typing.Optional[typing.Union["CloudAzureIntegrationsVirtualNetworks", typing.Dict[str, typing.Any]]] = None,
        vms: typing.Optional[typing.Union["CloudAzureIntegrationsVms", typing.Dict[str, typing.Any]]] = None,
        vpn_gateway: typing.Optional[typing.Union["CloudAzureIntegrationsVpnGateway", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param linked_account_id: The ID of the linked Azure account in New Relic. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#linked_account_id CloudAzureIntegrations#linked_account_id}
        :param account_id: The ID of the account in New Relic. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#account_id CloudAzureIntegrations#account_id}
        :param api_management: api_management block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#api_management CloudAzureIntegrations#api_management}
        :param app_gateway: app_gateway block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#app_gateway CloudAzureIntegrations#app_gateway}
        :param app_service: app_service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#app_service CloudAzureIntegrations#app_service}
        :param containers: containers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#containers CloudAzureIntegrations#containers}
        :param cosmos_db: cosmos_db block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#cosmos_db CloudAzureIntegrations#cosmos_db}
        :param cost_management: cost_management block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#cost_management CloudAzureIntegrations#cost_management}
        :param data_factory: data_factory block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#data_factory CloudAzureIntegrations#data_factory}
        :param event_hub: event_hub block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#event_hub CloudAzureIntegrations#event_hub}
        :param express_route: express_route block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#express_route CloudAzureIntegrations#express_route}
        :param firewalls: firewalls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#firewalls CloudAzureIntegrations#firewalls}
        :param front_door: front_door block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#front_door CloudAzureIntegrations#front_door}
        :param functions: functions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#functions CloudAzureIntegrations#functions}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#id CloudAzureIntegrations#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param key_vault: key_vault block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#key_vault CloudAzureIntegrations#key_vault}
        :param load_balancer: load_balancer block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#load_balancer CloudAzureIntegrations#load_balancer}
        :param logic_apps: logic_apps block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#logic_apps CloudAzureIntegrations#logic_apps}
        :param machine_learning: machine_learning block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#machine_learning CloudAzureIntegrations#machine_learning}
        :param maria_db: maria_db block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#maria_db CloudAzureIntegrations#maria_db}
        :param mysql: mysql block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#mysql CloudAzureIntegrations#mysql}
        :param postgresql: postgresql block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#postgresql CloudAzureIntegrations#postgresql}
        :param power_bi_dedicated: power_bi_dedicated block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#power_bi_dedicated CloudAzureIntegrations#power_bi_dedicated}
        :param redis_cache: redis_cache block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#redis_cache CloudAzureIntegrations#redis_cache}
        :param service_bus: service_bus block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#service_bus CloudAzureIntegrations#service_bus}
        :param sql: sql block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#sql CloudAzureIntegrations#sql}
        :param sql_managed: sql_managed block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#sql_managed CloudAzureIntegrations#sql_managed}
        :param storage: storage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#storage CloudAzureIntegrations#storage}
        :param virtual_machine: virtual_machine block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#virtual_machine CloudAzureIntegrations#virtual_machine}
        :param virtual_networks: virtual_networks block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#virtual_networks CloudAzureIntegrations#virtual_networks}
        :param vms: vms block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#vms CloudAzureIntegrations#vms}
        :param vpn_gateway: vpn_gateway block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#vpn_gateway CloudAzureIntegrations#vpn_gateway}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(api_management, dict):
            api_management = CloudAzureIntegrationsApiManagement(**api_management)
        if isinstance(app_gateway, dict):
            app_gateway = CloudAzureIntegrationsAppGateway(**app_gateway)
        if isinstance(app_service, dict):
            app_service = CloudAzureIntegrationsAppService(**app_service)
        if isinstance(containers, dict):
            containers = CloudAzureIntegrationsContainers(**containers)
        if isinstance(cosmos_db, dict):
            cosmos_db = CloudAzureIntegrationsCosmosDb(**cosmos_db)
        if isinstance(cost_management, dict):
            cost_management = CloudAzureIntegrationsCostManagement(**cost_management)
        if isinstance(data_factory, dict):
            data_factory = CloudAzureIntegrationsDataFactory(**data_factory)
        if isinstance(event_hub, dict):
            event_hub = CloudAzureIntegrationsEventHub(**event_hub)
        if isinstance(express_route, dict):
            express_route = CloudAzureIntegrationsExpressRoute(**express_route)
        if isinstance(firewalls, dict):
            firewalls = CloudAzureIntegrationsFirewalls(**firewalls)
        if isinstance(front_door, dict):
            front_door = CloudAzureIntegrationsFrontDoor(**front_door)
        if isinstance(functions, dict):
            functions = CloudAzureIntegrationsFunctions(**functions)
        if isinstance(key_vault, dict):
            key_vault = CloudAzureIntegrationsKeyVault(**key_vault)
        if isinstance(load_balancer, dict):
            load_balancer = CloudAzureIntegrationsLoadBalancer(**load_balancer)
        if isinstance(logic_apps, dict):
            logic_apps = CloudAzureIntegrationsLogicApps(**logic_apps)
        if isinstance(machine_learning, dict):
            machine_learning = CloudAzureIntegrationsMachineLearning(**machine_learning)
        if isinstance(maria_db, dict):
            maria_db = CloudAzureIntegrationsMariaDb(**maria_db)
        if isinstance(mysql, dict):
            mysql = CloudAzureIntegrationsMysql(**mysql)
        if isinstance(postgresql, dict):
            postgresql = CloudAzureIntegrationsPostgresql(**postgresql)
        if isinstance(power_bi_dedicated, dict):
            power_bi_dedicated = CloudAzureIntegrationsPowerBiDedicated(**power_bi_dedicated)
        if isinstance(redis_cache, dict):
            redis_cache = CloudAzureIntegrationsRedisCache(**redis_cache)
        if isinstance(service_bus, dict):
            service_bus = CloudAzureIntegrationsServiceBus(**service_bus)
        if isinstance(sql, dict):
            sql = CloudAzureIntegrationsSql(**sql)
        if isinstance(sql_managed, dict):
            sql_managed = CloudAzureIntegrationsSqlManaged(**sql_managed)
        if isinstance(storage, dict):
            storage = CloudAzureIntegrationsStorage(**storage)
        if isinstance(virtual_machine, dict):
            virtual_machine = CloudAzureIntegrationsVirtualMachine(**virtual_machine)
        if isinstance(virtual_networks, dict):
            virtual_networks = CloudAzureIntegrationsVirtualNetworks(**virtual_networks)
        if isinstance(vms, dict):
            vms = CloudAzureIntegrationsVms(**vms)
        if isinstance(vpn_gateway, dict):
            vpn_gateway = CloudAzureIntegrationsVpnGateway(**vpn_gateway)
        if __debug__:
            type_hints = typing.get_type_hints(CloudAzureIntegrationsConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument linked_account_id", value=linked_account_id, expected_type=type_hints["linked_account_id"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument api_management", value=api_management, expected_type=type_hints["api_management"])
            check_type(argname="argument app_gateway", value=app_gateway, expected_type=type_hints["app_gateway"])
            check_type(argname="argument app_service", value=app_service, expected_type=type_hints["app_service"])
            check_type(argname="argument containers", value=containers, expected_type=type_hints["containers"])
            check_type(argname="argument cosmos_db", value=cosmos_db, expected_type=type_hints["cosmos_db"])
            check_type(argname="argument cost_management", value=cost_management, expected_type=type_hints["cost_management"])
            check_type(argname="argument data_factory", value=data_factory, expected_type=type_hints["data_factory"])
            check_type(argname="argument event_hub", value=event_hub, expected_type=type_hints["event_hub"])
            check_type(argname="argument express_route", value=express_route, expected_type=type_hints["express_route"])
            check_type(argname="argument firewalls", value=firewalls, expected_type=type_hints["firewalls"])
            check_type(argname="argument front_door", value=front_door, expected_type=type_hints["front_door"])
            check_type(argname="argument functions", value=functions, expected_type=type_hints["functions"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument key_vault", value=key_vault, expected_type=type_hints["key_vault"])
            check_type(argname="argument load_balancer", value=load_balancer, expected_type=type_hints["load_balancer"])
            check_type(argname="argument logic_apps", value=logic_apps, expected_type=type_hints["logic_apps"])
            check_type(argname="argument machine_learning", value=machine_learning, expected_type=type_hints["machine_learning"])
            check_type(argname="argument maria_db", value=maria_db, expected_type=type_hints["maria_db"])
            check_type(argname="argument mysql", value=mysql, expected_type=type_hints["mysql"])
            check_type(argname="argument postgresql", value=postgresql, expected_type=type_hints["postgresql"])
            check_type(argname="argument power_bi_dedicated", value=power_bi_dedicated, expected_type=type_hints["power_bi_dedicated"])
            check_type(argname="argument redis_cache", value=redis_cache, expected_type=type_hints["redis_cache"])
            check_type(argname="argument service_bus", value=service_bus, expected_type=type_hints["service_bus"])
            check_type(argname="argument sql", value=sql, expected_type=type_hints["sql"])
            check_type(argname="argument sql_managed", value=sql_managed, expected_type=type_hints["sql_managed"])
            check_type(argname="argument storage", value=storage, expected_type=type_hints["storage"])
            check_type(argname="argument virtual_machine", value=virtual_machine, expected_type=type_hints["virtual_machine"])
            check_type(argname="argument virtual_networks", value=virtual_networks, expected_type=type_hints["virtual_networks"])
            check_type(argname="argument vms", value=vms, expected_type=type_hints["vms"])
            check_type(argname="argument vpn_gateway", value=vpn_gateway, expected_type=type_hints["vpn_gateway"])
        self._values: typing.Dict[str, typing.Any] = {
            "linked_account_id": linked_account_id,
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
        if account_id is not None:
            self._values["account_id"] = account_id
        if api_management is not None:
            self._values["api_management"] = api_management
        if app_gateway is not None:
            self._values["app_gateway"] = app_gateway
        if app_service is not None:
            self._values["app_service"] = app_service
        if containers is not None:
            self._values["containers"] = containers
        if cosmos_db is not None:
            self._values["cosmos_db"] = cosmos_db
        if cost_management is not None:
            self._values["cost_management"] = cost_management
        if data_factory is not None:
            self._values["data_factory"] = data_factory
        if event_hub is not None:
            self._values["event_hub"] = event_hub
        if express_route is not None:
            self._values["express_route"] = express_route
        if firewalls is not None:
            self._values["firewalls"] = firewalls
        if front_door is not None:
            self._values["front_door"] = front_door
        if functions is not None:
            self._values["functions"] = functions
        if id is not None:
            self._values["id"] = id
        if key_vault is not None:
            self._values["key_vault"] = key_vault
        if load_balancer is not None:
            self._values["load_balancer"] = load_balancer
        if logic_apps is not None:
            self._values["logic_apps"] = logic_apps
        if machine_learning is not None:
            self._values["machine_learning"] = machine_learning
        if maria_db is not None:
            self._values["maria_db"] = maria_db
        if mysql is not None:
            self._values["mysql"] = mysql
        if postgresql is not None:
            self._values["postgresql"] = postgresql
        if power_bi_dedicated is not None:
            self._values["power_bi_dedicated"] = power_bi_dedicated
        if redis_cache is not None:
            self._values["redis_cache"] = redis_cache
        if service_bus is not None:
            self._values["service_bus"] = service_bus
        if sql is not None:
            self._values["sql"] = sql
        if sql_managed is not None:
            self._values["sql_managed"] = sql_managed
        if storage is not None:
            self._values["storage"] = storage
        if virtual_machine is not None:
            self._values["virtual_machine"] = virtual_machine
        if virtual_networks is not None:
            self._values["virtual_networks"] = virtual_networks
        if vms is not None:
            self._values["vms"] = vms
        if vpn_gateway is not None:
            self._values["vpn_gateway"] = vpn_gateway

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
    def linked_account_id(self) -> jsii.Number:
        '''The ID of the linked Azure account in New Relic.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#linked_account_id CloudAzureIntegrations#linked_account_id}
        '''
        result = self._values.get("linked_account_id")
        assert result is not None, "Required property 'linked_account_id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def account_id(self) -> typing.Optional[jsii.Number]:
        '''The ID of the account in New Relic.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#account_id CloudAzureIntegrations#account_id}
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def api_management(self) -> typing.Optional[CloudAzureIntegrationsApiManagement]:
        '''api_management block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#api_management CloudAzureIntegrations#api_management}
        '''
        result = self._values.get("api_management")
        return typing.cast(typing.Optional[CloudAzureIntegrationsApiManagement], result)

    @builtins.property
    def app_gateway(self) -> typing.Optional[CloudAzureIntegrationsAppGateway]:
        '''app_gateway block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#app_gateway CloudAzureIntegrations#app_gateway}
        '''
        result = self._values.get("app_gateway")
        return typing.cast(typing.Optional[CloudAzureIntegrationsAppGateway], result)

    @builtins.property
    def app_service(self) -> typing.Optional[CloudAzureIntegrationsAppService]:
        '''app_service block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#app_service CloudAzureIntegrations#app_service}
        '''
        result = self._values.get("app_service")
        return typing.cast(typing.Optional[CloudAzureIntegrationsAppService], result)

    @builtins.property
    def containers(self) -> typing.Optional["CloudAzureIntegrationsContainers"]:
        '''containers block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#containers CloudAzureIntegrations#containers}
        '''
        result = self._values.get("containers")
        return typing.cast(typing.Optional["CloudAzureIntegrationsContainers"], result)

    @builtins.property
    def cosmos_db(self) -> typing.Optional["CloudAzureIntegrationsCosmosDb"]:
        '''cosmos_db block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#cosmos_db CloudAzureIntegrations#cosmos_db}
        '''
        result = self._values.get("cosmos_db")
        return typing.cast(typing.Optional["CloudAzureIntegrationsCosmosDb"], result)

    @builtins.property
    def cost_management(
        self,
    ) -> typing.Optional["CloudAzureIntegrationsCostManagement"]:
        '''cost_management block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#cost_management CloudAzureIntegrations#cost_management}
        '''
        result = self._values.get("cost_management")
        return typing.cast(typing.Optional["CloudAzureIntegrationsCostManagement"], result)

    @builtins.property
    def data_factory(self) -> typing.Optional["CloudAzureIntegrationsDataFactory"]:
        '''data_factory block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#data_factory CloudAzureIntegrations#data_factory}
        '''
        result = self._values.get("data_factory")
        return typing.cast(typing.Optional["CloudAzureIntegrationsDataFactory"], result)

    @builtins.property
    def event_hub(self) -> typing.Optional["CloudAzureIntegrationsEventHub"]:
        '''event_hub block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#event_hub CloudAzureIntegrations#event_hub}
        '''
        result = self._values.get("event_hub")
        return typing.cast(typing.Optional["CloudAzureIntegrationsEventHub"], result)

    @builtins.property
    def express_route(self) -> typing.Optional["CloudAzureIntegrationsExpressRoute"]:
        '''express_route block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#express_route CloudAzureIntegrations#express_route}
        '''
        result = self._values.get("express_route")
        return typing.cast(typing.Optional["CloudAzureIntegrationsExpressRoute"], result)

    @builtins.property
    def firewalls(self) -> typing.Optional["CloudAzureIntegrationsFirewalls"]:
        '''firewalls block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#firewalls CloudAzureIntegrations#firewalls}
        '''
        result = self._values.get("firewalls")
        return typing.cast(typing.Optional["CloudAzureIntegrationsFirewalls"], result)

    @builtins.property
    def front_door(self) -> typing.Optional["CloudAzureIntegrationsFrontDoor"]:
        '''front_door block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#front_door CloudAzureIntegrations#front_door}
        '''
        result = self._values.get("front_door")
        return typing.cast(typing.Optional["CloudAzureIntegrationsFrontDoor"], result)

    @builtins.property
    def functions(self) -> typing.Optional["CloudAzureIntegrationsFunctions"]:
        '''functions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#functions CloudAzureIntegrations#functions}
        '''
        result = self._values.get("functions")
        return typing.cast(typing.Optional["CloudAzureIntegrationsFunctions"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#id CloudAzureIntegrations#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_vault(self) -> typing.Optional["CloudAzureIntegrationsKeyVault"]:
        '''key_vault block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#key_vault CloudAzureIntegrations#key_vault}
        '''
        result = self._values.get("key_vault")
        return typing.cast(typing.Optional["CloudAzureIntegrationsKeyVault"], result)

    @builtins.property
    def load_balancer(self) -> typing.Optional["CloudAzureIntegrationsLoadBalancer"]:
        '''load_balancer block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#load_balancer CloudAzureIntegrations#load_balancer}
        '''
        result = self._values.get("load_balancer")
        return typing.cast(typing.Optional["CloudAzureIntegrationsLoadBalancer"], result)

    @builtins.property
    def logic_apps(self) -> typing.Optional["CloudAzureIntegrationsLogicApps"]:
        '''logic_apps block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#logic_apps CloudAzureIntegrations#logic_apps}
        '''
        result = self._values.get("logic_apps")
        return typing.cast(typing.Optional["CloudAzureIntegrationsLogicApps"], result)

    @builtins.property
    def machine_learning(
        self,
    ) -> typing.Optional["CloudAzureIntegrationsMachineLearning"]:
        '''machine_learning block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#machine_learning CloudAzureIntegrations#machine_learning}
        '''
        result = self._values.get("machine_learning")
        return typing.cast(typing.Optional["CloudAzureIntegrationsMachineLearning"], result)

    @builtins.property
    def maria_db(self) -> typing.Optional["CloudAzureIntegrationsMariaDb"]:
        '''maria_db block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#maria_db CloudAzureIntegrations#maria_db}
        '''
        result = self._values.get("maria_db")
        return typing.cast(typing.Optional["CloudAzureIntegrationsMariaDb"], result)

    @builtins.property
    def mysql(self) -> typing.Optional["CloudAzureIntegrationsMysql"]:
        '''mysql block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#mysql CloudAzureIntegrations#mysql}
        '''
        result = self._values.get("mysql")
        return typing.cast(typing.Optional["CloudAzureIntegrationsMysql"], result)

    @builtins.property
    def postgresql(self) -> typing.Optional["CloudAzureIntegrationsPostgresql"]:
        '''postgresql block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#postgresql CloudAzureIntegrations#postgresql}
        '''
        result = self._values.get("postgresql")
        return typing.cast(typing.Optional["CloudAzureIntegrationsPostgresql"], result)

    @builtins.property
    def power_bi_dedicated(
        self,
    ) -> typing.Optional["CloudAzureIntegrationsPowerBiDedicated"]:
        '''power_bi_dedicated block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#power_bi_dedicated CloudAzureIntegrations#power_bi_dedicated}
        '''
        result = self._values.get("power_bi_dedicated")
        return typing.cast(typing.Optional["CloudAzureIntegrationsPowerBiDedicated"], result)

    @builtins.property
    def redis_cache(self) -> typing.Optional["CloudAzureIntegrationsRedisCache"]:
        '''redis_cache block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#redis_cache CloudAzureIntegrations#redis_cache}
        '''
        result = self._values.get("redis_cache")
        return typing.cast(typing.Optional["CloudAzureIntegrationsRedisCache"], result)

    @builtins.property
    def service_bus(self) -> typing.Optional["CloudAzureIntegrationsServiceBus"]:
        '''service_bus block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#service_bus CloudAzureIntegrations#service_bus}
        '''
        result = self._values.get("service_bus")
        return typing.cast(typing.Optional["CloudAzureIntegrationsServiceBus"], result)

    @builtins.property
    def sql(self) -> typing.Optional["CloudAzureIntegrationsSql"]:
        '''sql block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#sql CloudAzureIntegrations#sql}
        '''
        result = self._values.get("sql")
        return typing.cast(typing.Optional["CloudAzureIntegrationsSql"], result)

    @builtins.property
    def sql_managed(self) -> typing.Optional["CloudAzureIntegrationsSqlManaged"]:
        '''sql_managed block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#sql_managed CloudAzureIntegrations#sql_managed}
        '''
        result = self._values.get("sql_managed")
        return typing.cast(typing.Optional["CloudAzureIntegrationsSqlManaged"], result)

    @builtins.property
    def storage(self) -> typing.Optional["CloudAzureIntegrationsStorage"]:
        '''storage block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#storage CloudAzureIntegrations#storage}
        '''
        result = self._values.get("storage")
        return typing.cast(typing.Optional["CloudAzureIntegrationsStorage"], result)

    @builtins.property
    def virtual_machine(
        self,
    ) -> typing.Optional["CloudAzureIntegrationsVirtualMachine"]:
        '''virtual_machine block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#virtual_machine CloudAzureIntegrations#virtual_machine}
        '''
        result = self._values.get("virtual_machine")
        return typing.cast(typing.Optional["CloudAzureIntegrationsVirtualMachine"], result)

    @builtins.property
    def virtual_networks(
        self,
    ) -> typing.Optional["CloudAzureIntegrationsVirtualNetworks"]:
        '''virtual_networks block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#virtual_networks CloudAzureIntegrations#virtual_networks}
        '''
        result = self._values.get("virtual_networks")
        return typing.cast(typing.Optional["CloudAzureIntegrationsVirtualNetworks"], result)

    @builtins.property
    def vms(self) -> typing.Optional["CloudAzureIntegrationsVms"]:
        '''vms block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#vms CloudAzureIntegrations#vms}
        '''
        result = self._values.get("vms")
        return typing.cast(typing.Optional["CloudAzureIntegrationsVms"], result)

    @builtins.property
    def vpn_gateway(self) -> typing.Optional["CloudAzureIntegrationsVpnGateway"]:
        '''vpn_gateway block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#vpn_gateway CloudAzureIntegrations#vpn_gateway}
        '''
        result = self._values.get("vpn_gateway")
        return typing.cast(typing.Optional["CloudAzureIntegrationsVpnGateway"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAzureIntegrationsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsContainers",
    jsii_struct_bases=[],
    name_mapping={
        "metrics_polling_interval": "metricsPollingInterval",
        "resource_groups": "resourceGroups",
    },
)
class CloudAzureIntegrationsContainers:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAzureIntegrationsContainers.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument resource_groups", value=resource_groups, expected_type=type_hints["resource_groups"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if resource_groups is not None:
            self._values["resource_groups"] = resource_groups

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resource_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        result = self._values.get("resource_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAzureIntegrationsContainers(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAzureIntegrationsContainersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsContainersOutputReference",
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
            type_hints = typing.get_type_hints(CloudAzureIntegrationsContainersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @jsii.member(jsii_name="resetResourceGroups")
    def reset_resource_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceGroups", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupsInput")
    def resource_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourceGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsContainersOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroups")
    def resource_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resourceGroups"))

    @resource_groups.setter
    def resource_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsContainersOutputReference, "resource_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroups", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAzureIntegrationsContainers]:
        return typing.cast(typing.Optional[CloudAzureIntegrationsContainers], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAzureIntegrationsContainers],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsContainersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsCosmosDb",
    jsii_struct_bases=[],
    name_mapping={
        "metrics_polling_interval": "metricsPollingInterval",
        "resource_groups": "resourceGroups",
    },
)
class CloudAzureIntegrationsCosmosDb:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAzureIntegrationsCosmosDb.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument resource_groups", value=resource_groups, expected_type=type_hints["resource_groups"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if resource_groups is not None:
            self._values["resource_groups"] = resource_groups

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resource_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        result = self._values.get("resource_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAzureIntegrationsCosmosDb(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAzureIntegrationsCosmosDbOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsCosmosDbOutputReference",
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
            type_hints = typing.get_type_hints(CloudAzureIntegrationsCosmosDbOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @jsii.member(jsii_name="resetResourceGroups")
    def reset_resource_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceGroups", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupsInput")
    def resource_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourceGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsCosmosDbOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroups")
    def resource_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resourceGroups"))

    @resource_groups.setter
    def resource_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsCosmosDbOutputReference, "resource_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroups", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAzureIntegrationsCosmosDb]:
        return typing.cast(typing.Optional[CloudAzureIntegrationsCosmosDb], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAzureIntegrationsCosmosDb],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsCosmosDbOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsCostManagement",
    jsii_struct_bases=[],
    name_mapping={
        "metrics_polling_interval": "metricsPollingInterval",
        "tag_keys": "tagKeys",
    },
)
class CloudAzureIntegrationsCostManagement:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        tag_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param tag_keys: Specify if additional cost data per tag should be collected. This field is case sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#tag_keys CloudAzureIntegrations#tag_keys}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAzureIntegrationsCostManagement.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument tag_keys", value=tag_keys, expected_type=type_hints["tag_keys"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if tag_keys is not None:
            self._values["tag_keys"] = tag_keys

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tag_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify if additional cost data per tag should be collected. This field is case sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#tag_keys CloudAzureIntegrations#tag_keys}
        '''
        result = self._values.get("tag_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAzureIntegrationsCostManagement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAzureIntegrationsCostManagementOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsCostManagementOutputReference",
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
            type_hints = typing.get_type_hints(CloudAzureIntegrationsCostManagementOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @jsii.member(jsii_name="resetTagKeys")
    def reset_tag_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagKeys", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="tagKeysInput")
    def tag_keys_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagKeysInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsCostManagementOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="tagKeys")
    def tag_keys(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tagKeys"))

    @tag_keys.setter
    def tag_keys(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsCostManagementOutputReference, "tag_keys").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagKeys", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAzureIntegrationsCostManagement]:
        return typing.cast(typing.Optional[CloudAzureIntegrationsCostManagement], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAzureIntegrationsCostManagement],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsCostManagementOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsDataFactory",
    jsii_struct_bases=[],
    name_mapping={
        "metrics_polling_interval": "metricsPollingInterval",
        "resource_groups": "resourceGroups",
    },
)
class CloudAzureIntegrationsDataFactory:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAzureIntegrationsDataFactory.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument resource_groups", value=resource_groups, expected_type=type_hints["resource_groups"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if resource_groups is not None:
            self._values["resource_groups"] = resource_groups

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resource_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        result = self._values.get("resource_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAzureIntegrationsDataFactory(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAzureIntegrationsDataFactoryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsDataFactoryOutputReference",
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
            type_hints = typing.get_type_hints(CloudAzureIntegrationsDataFactoryOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @jsii.member(jsii_name="resetResourceGroups")
    def reset_resource_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceGroups", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupsInput")
    def resource_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourceGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsDataFactoryOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroups")
    def resource_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resourceGroups"))

    @resource_groups.setter
    def resource_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsDataFactoryOutputReference, "resource_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroups", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAzureIntegrationsDataFactory]:
        return typing.cast(typing.Optional[CloudAzureIntegrationsDataFactory], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAzureIntegrationsDataFactory],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsDataFactoryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsEventHub",
    jsii_struct_bases=[],
    name_mapping={
        "metrics_polling_interval": "metricsPollingInterval",
        "resource_groups": "resourceGroups",
    },
)
class CloudAzureIntegrationsEventHub:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAzureIntegrationsEventHub.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument resource_groups", value=resource_groups, expected_type=type_hints["resource_groups"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if resource_groups is not None:
            self._values["resource_groups"] = resource_groups

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resource_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        result = self._values.get("resource_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAzureIntegrationsEventHub(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAzureIntegrationsEventHubOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsEventHubOutputReference",
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
            type_hints = typing.get_type_hints(CloudAzureIntegrationsEventHubOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @jsii.member(jsii_name="resetResourceGroups")
    def reset_resource_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceGroups", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupsInput")
    def resource_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourceGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsEventHubOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroups")
    def resource_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resourceGroups"))

    @resource_groups.setter
    def resource_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsEventHubOutputReference, "resource_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroups", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAzureIntegrationsEventHub]:
        return typing.cast(typing.Optional[CloudAzureIntegrationsEventHub], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAzureIntegrationsEventHub],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsEventHubOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsExpressRoute",
    jsii_struct_bases=[],
    name_mapping={
        "metrics_polling_interval": "metricsPollingInterval",
        "resource_groups": "resourceGroups",
    },
)
class CloudAzureIntegrationsExpressRoute:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAzureIntegrationsExpressRoute.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument resource_groups", value=resource_groups, expected_type=type_hints["resource_groups"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if resource_groups is not None:
            self._values["resource_groups"] = resource_groups

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resource_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        result = self._values.get("resource_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAzureIntegrationsExpressRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAzureIntegrationsExpressRouteOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsExpressRouteOutputReference",
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
            type_hints = typing.get_type_hints(CloudAzureIntegrationsExpressRouteOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @jsii.member(jsii_name="resetResourceGroups")
    def reset_resource_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceGroups", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupsInput")
    def resource_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourceGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsExpressRouteOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroups")
    def resource_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resourceGroups"))

    @resource_groups.setter
    def resource_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsExpressRouteOutputReference, "resource_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroups", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAzureIntegrationsExpressRoute]:
        return typing.cast(typing.Optional[CloudAzureIntegrationsExpressRoute], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAzureIntegrationsExpressRoute],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsExpressRouteOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsFirewalls",
    jsii_struct_bases=[],
    name_mapping={
        "metrics_polling_interval": "metricsPollingInterval",
        "resource_groups": "resourceGroups",
    },
)
class CloudAzureIntegrationsFirewalls:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAzureIntegrationsFirewalls.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument resource_groups", value=resource_groups, expected_type=type_hints["resource_groups"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if resource_groups is not None:
            self._values["resource_groups"] = resource_groups

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resource_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        result = self._values.get("resource_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAzureIntegrationsFirewalls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAzureIntegrationsFirewallsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsFirewallsOutputReference",
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
            type_hints = typing.get_type_hints(CloudAzureIntegrationsFirewallsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @jsii.member(jsii_name="resetResourceGroups")
    def reset_resource_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceGroups", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupsInput")
    def resource_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourceGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsFirewallsOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroups")
    def resource_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resourceGroups"))

    @resource_groups.setter
    def resource_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsFirewallsOutputReference, "resource_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroups", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAzureIntegrationsFirewalls]:
        return typing.cast(typing.Optional[CloudAzureIntegrationsFirewalls], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAzureIntegrationsFirewalls],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsFirewallsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsFrontDoor",
    jsii_struct_bases=[],
    name_mapping={
        "metrics_polling_interval": "metricsPollingInterval",
        "resource_groups": "resourceGroups",
    },
)
class CloudAzureIntegrationsFrontDoor:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAzureIntegrationsFrontDoor.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument resource_groups", value=resource_groups, expected_type=type_hints["resource_groups"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if resource_groups is not None:
            self._values["resource_groups"] = resource_groups

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resource_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        result = self._values.get("resource_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAzureIntegrationsFrontDoor(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAzureIntegrationsFrontDoorOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsFrontDoorOutputReference",
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
            type_hints = typing.get_type_hints(CloudAzureIntegrationsFrontDoorOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @jsii.member(jsii_name="resetResourceGroups")
    def reset_resource_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceGroups", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupsInput")
    def resource_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourceGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsFrontDoorOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroups")
    def resource_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resourceGroups"))

    @resource_groups.setter
    def resource_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsFrontDoorOutputReference, "resource_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroups", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAzureIntegrationsFrontDoor]:
        return typing.cast(typing.Optional[CloudAzureIntegrationsFrontDoor], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAzureIntegrationsFrontDoor],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsFrontDoorOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsFunctions",
    jsii_struct_bases=[],
    name_mapping={
        "metrics_polling_interval": "metricsPollingInterval",
        "resource_groups": "resourceGroups",
    },
)
class CloudAzureIntegrationsFunctions:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAzureIntegrationsFunctions.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument resource_groups", value=resource_groups, expected_type=type_hints["resource_groups"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if resource_groups is not None:
            self._values["resource_groups"] = resource_groups

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resource_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        result = self._values.get("resource_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAzureIntegrationsFunctions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAzureIntegrationsFunctionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsFunctionsOutputReference",
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
            type_hints = typing.get_type_hints(CloudAzureIntegrationsFunctionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @jsii.member(jsii_name="resetResourceGroups")
    def reset_resource_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceGroups", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupsInput")
    def resource_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourceGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsFunctionsOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroups")
    def resource_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resourceGroups"))

    @resource_groups.setter
    def resource_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsFunctionsOutputReference, "resource_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroups", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAzureIntegrationsFunctions]:
        return typing.cast(typing.Optional[CloudAzureIntegrationsFunctions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAzureIntegrationsFunctions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsFunctionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsKeyVault",
    jsii_struct_bases=[],
    name_mapping={
        "metrics_polling_interval": "metricsPollingInterval",
        "resource_groups": "resourceGroups",
    },
)
class CloudAzureIntegrationsKeyVault:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAzureIntegrationsKeyVault.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument resource_groups", value=resource_groups, expected_type=type_hints["resource_groups"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if resource_groups is not None:
            self._values["resource_groups"] = resource_groups

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resource_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        result = self._values.get("resource_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAzureIntegrationsKeyVault(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAzureIntegrationsKeyVaultOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsKeyVaultOutputReference",
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
            type_hints = typing.get_type_hints(CloudAzureIntegrationsKeyVaultOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @jsii.member(jsii_name="resetResourceGroups")
    def reset_resource_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceGroups", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupsInput")
    def resource_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourceGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsKeyVaultOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroups")
    def resource_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resourceGroups"))

    @resource_groups.setter
    def resource_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsKeyVaultOutputReference, "resource_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroups", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAzureIntegrationsKeyVault]:
        return typing.cast(typing.Optional[CloudAzureIntegrationsKeyVault], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAzureIntegrationsKeyVault],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsKeyVaultOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsLoadBalancer",
    jsii_struct_bases=[],
    name_mapping={
        "metrics_polling_interval": "metricsPollingInterval",
        "resource_groups": "resourceGroups",
    },
)
class CloudAzureIntegrationsLoadBalancer:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAzureIntegrationsLoadBalancer.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument resource_groups", value=resource_groups, expected_type=type_hints["resource_groups"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if resource_groups is not None:
            self._values["resource_groups"] = resource_groups

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resource_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        result = self._values.get("resource_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAzureIntegrationsLoadBalancer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAzureIntegrationsLoadBalancerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsLoadBalancerOutputReference",
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
            type_hints = typing.get_type_hints(CloudAzureIntegrationsLoadBalancerOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @jsii.member(jsii_name="resetResourceGroups")
    def reset_resource_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceGroups", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupsInput")
    def resource_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourceGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsLoadBalancerOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroups")
    def resource_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resourceGroups"))

    @resource_groups.setter
    def resource_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsLoadBalancerOutputReference, "resource_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroups", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAzureIntegrationsLoadBalancer]:
        return typing.cast(typing.Optional[CloudAzureIntegrationsLoadBalancer], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAzureIntegrationsLoadBalancer],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsLoadBalancerOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsLogicApps",
    jsii_struct_bases=[],
    name_mapping={
        "metrics_polling_interval": "metricsPollingInterval",
        "resource_groups": "resourceGroups",
    },
)
class CloudAzureIntegrationsLogicApps:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAzureIntegrationsLogicApps.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument resource_groups", value=resource_groups, expected_type=type_hints["resource_groups"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if resource_groups is not None:
            self._values["resource_groups"] = resource_groups

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resource_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        result = self._values.get("resource_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAzureIntegrationsLogicApps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAzureIntegrationsLogicAppsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsLogicAppsOutputReference",
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
            type_hints = typing.get_type_hints(CloudAzureIntegrationsLogicAppsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @jsii.member(jsii_name="resetResourceGroups")
    def reset_resource_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceGroups", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupsInput")
    def resource_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourceGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsLogicAppsOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroups")
    def resource_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resourceGroups"))

    @resource_groups.setter
    def resource_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsLogicAppsOutputReference, "resource_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroups", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAzureIntegrationsLogicApps]:
        return typing.cast(typing.Optional[CloudAzureIntegrationsLogicApps], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAzureIntegrationsLogicApps],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsLogicAppsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsMachineLearning",
    jsii_struct_bases=[],
    name_mapping={
        "metrics_polling_interval": "metricsPollingInterval",
        "resource_groups": "resourceGroups",
    },
)
class CloudAzureIntegrationsMachineLearning:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAzureIntegrationsMachineLearning.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument resource_groups", value=resource_groups, expected_type=type_hints["resource_groups"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if resource_groups is not None:
            self._values["resource_groups"] = resource_groups

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resource_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        result = self._values.get("resource_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAzureIntegrationsMachineLearning(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAzureIntegrationsMachineLearningOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsMachineLearningOutputReference",
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
            type_hints = typing.get_type_hints(CloudAzureIntegrationsMachineLearningOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @jsii.member(jsii_name="resetResourceGroups")
    def reset_resource_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceGroups", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupsInput")
    def resource_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourceGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsMachineLearningOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroups")
    def resource_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resourceGroups"))

    @resource_groups.setter
    def resource_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsMachineLearningOutputReference, "resource_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroups", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAzureIntegrationsMachineLearning]:
        return typing.cast(typing.Optional[CloudAzureIntegrationsMachineLearning], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAzureIntegrationsMachineLearning],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsMachineLearningOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsMariaDb",
    jsii_struct_bases=[],
    name_mapping={
        "metrics_polling_interval": "metricsPollingInterval",
        "resource_groups": "resourceGroups",
    },
)
class CloudAzureIntegrationsMariaDb:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAzureIntegrationsMariaDb.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument resource_groups", value=resource_groups, expected_type=type_hints["resource_groups"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if resource_groups is not None:
            self._values["resource_groups"] = resource_groups

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resource_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        result = self._values.get("resource_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAzureIntegrationsMariaDb(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAzureIntegrationsMariaDbOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsMariaDbOutputReference",
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
            type_hints = typing.get_type_hints(CloudAzureIntegrationsMariaDbOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @jsii.member(jsii_name="resetResourceGroups")
    def reset_resource_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceGroups", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupsInput")
    def resource_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourceGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsMariaDbOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroups")
    def resource_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resourceGroups"))

    @resource_groups.setter
    def resource_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsMariaDbOutputReference, "resource_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroups", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAzureIntegrationsMariaDb]:
        return typing.cast(typing.Optional[CloudAzureIntegrationsMariaDb], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAzureIntegrationsMariaDb],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsMariaDbOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsMysql",
    jsii_struct_bases=[],
    name_mapping={
        "metrics_polling_interval": "metricsPollingInterval",
        "resource_groups": "resourceGroups",
    },
)
class CloudAzureIntegrationsMysql:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAzureIntegrationsMysql.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument resource_groups", value=resource_groups, expected_type=type_hints["resource_groups"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if resource_groups is not None:
            self._values["resource_groups"] = resource_groups

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resource_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        result = self._values.get("resource_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAzureIntegrationsMysql(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAzureIntegrationsMysqlOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsMysqlOutputReference",
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
            type_hints = typing.get_type_hints(CloudAzureIntegrationsMysqlOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @jsii.member(jsii_name="resetResourceGroups")
    def reset_resource_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceGroups", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupsInput")
    def resource_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourceGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsMysqlOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroups")
    def resource_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resourceGroups"))

    @resource_groups.setter
    def resource_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsMysqlOutputReference, "resource_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroups", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAzureIntegrationsMysql]:
        return typing.cast(typing.Optional[CloudAzureIntegrationsMysql], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAzureIntegrationsMysql],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsMysqlOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsPostgresql",
    jsii_struct_bases=[],
    name_mapping={
        "metrics_polling_interval": "metricsPollingInterval",
        "resource_groups": "resourceGroups",
    },
)
class CloudAzureIntegrationsPostgresql:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAzureIntegrationsPostgresql.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument resource_groups", value=resource_groups, expected_type=type_hints["resource_groups"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if resource_groups is not None:
            self._values["resource_groups"] = resource_groups

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resource_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        result = self._values.get("resource_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAzureIntegrationsPostgresql(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAzureIntegrationsPostgresqlOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsPostgresqlOutputReference",
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
            type_hints = typing.get_type_hints(CloudAzureIntegrationsPostgresqlOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @jsii.member(jsii_name="resetResourceGroups")
    def reset_resource_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceGroups", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupsInput")
    def resource_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourceGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsPostgresqlOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroups")
    def resource_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resourceGroups"))

    @resource_groups.setter
    def resource_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsPostgresqlOutputReference, "resource_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroups", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAzureIntegrationsPostgresql]:
        return typing.cast(typing.Optional[CloudAzureIntegrationsPostgresql], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAzureIntegrationsPostgresql],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsPostgresqlOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsPowerBiDedicated",
    jsii_struct_bases=[],
    name_mapping={
        "metrics_polling_interval": "metricsPollingInterval",
        "resource_groups": "resourceGroups",
    },
)
class CloudAzureIntegrationsPowerBiDedicated:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAzureIntegrationsPowerBiDedicated.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument resource_groups", value=resource_groups, expected_type=type_hints["resource_groups"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if resource_groups is not None:
            self._values["resource_groups"] = resource_groups

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resource_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        result = self._values.get("resource_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAzureIntegrationsPowerBiDedicated(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAzureIntegrationsPowerBiDedicatedOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsPowerBiDedicatedOutputReference",
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
            type_hints = typing.get_type_hints(CloudAzureIntegrationsPowerBiDedicatedOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @jsii.member(jsii_name="resetResourceGroups")
    def reset_resource_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceGroups", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupsInput")
    def resource_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourceGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsPowerBiDedicatedOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroups")
    def resource_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resourceGroups"))

    @resource_groups.setter
    def resource_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsPowerBiDedicatedOutputReference, "resource_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroups", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAzureIntegrationsPowerBiDedicated]:
        return typing.cast(typing.Optional[CloudAzureIntegrationsPowerBiDedicated], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAzureIntegrationsPowerBiDedicated],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsPowerBiDedicatedOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsRedisCache",
    jsii_struct_bases=[],
    name_mapping={
        "metrics_polling_interval": "metricsPollingInterval",
        "resource_groups": "resourceGroups",
    },
)
class CloudAzureIntegrationsRedisCache:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAzureIntegrationsRedisCache.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument resource_groups", value=resource_groups, expected_type=type_hints["resource_groups"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if resource_groups is not None:
            self._values["resource_groups"] = resource_groups

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resource_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        result = self._values.get("resource_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAzureIntegrationsRedisCache(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAzureIntegrationsRedisCacheOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsRedisCacheOutputReference",
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
            type_hints = typing.get_type_hints(CloudAzureIntegrationsRedisCacheOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @jsii.member(jsii_name="resetResourceGroups")
    def reset_resource_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceGroups", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupsInput")
    def resource_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourceGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsRedisCacheOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroups")
    def resource_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resourceGroups"))

    @resource_groups.setter
    def resource_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsRedisCacheOutputReference, "resource_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroups", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAzureIntegrationsRedisCache]:
        return typing.cast(typing.Optional[CloudAzureIntegrationsRedisCache], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAzureIntegrationsRedisCache],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsRedisCacheOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsServiceBus",
    jsii_struct_bases=[],
    name_mapping={
        "metrics_polling_interval": "metricsPollingInterval",
        "resource_groups": "resourceGroups",
    },
)
class CloudAzureIntegrationsServiceBus:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAzureIntegrationsServiceBus.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument resource_groups", value=resource_groups, expected_type=type_hints["resource_groups"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if resource_groups is not None:
            self._values["resource_groups"] = resource_groups

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resource_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        result = self._values.get("resource_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAzureIntegrationsServiceBus(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAzureIntegrationsServiceBusOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsServiceBusOutputReference",
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
            type_hints = typing.get_type_hints(CloudAzureIntegrationsServiceBusOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @jsii.member(jsii_name="resetResourceGroups")
    def reset_resource_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceGroups", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupsInput")
    def resource_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourceGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsServiceBusOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroups")
    def resource_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resourceGroups"))

    @resource_groups.setter
    def resource_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsServiceBusOutputReference, "resource_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroups", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAzureIntegrationsServiceBus]:
        return typing.cast(typing.Optional[CloudAzureIntegrationsServiceBus], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAzureIntegrationsServiceBus],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsServiceBusOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsSql",
    jsii_struct_bases=[],
    name_mapping={
        "metrics_polling_interval": "metricsPollingInterval",
        "resource_groups": "resourceGroups",
    },
)
class CloudAzureIntegrationsSql:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAzureIntegrationsSql.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument resource_groups", value=resource_groups, expected_type=type_hints["resource_groups"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if resource_groups is not None:
            self._values["resource_groups"] = resource_groups

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resource_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        result = self._values.get("resource_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAzureIntegrationsSql(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsSqlManaged",
    jsii_struct_bases=[],
    name_mapping={
        "metrics_polling_interval": "metricsPollingInterval",
        "resource_groups": "resourceGroups",
    },
)
class CloudAzureIntegrationsSqlManaged:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAzureIntegrationsSqlManaged.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument resource_groups", value=resource_groups, expected_type=type_hints["resource_groups"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if resource_groups is not None:
            self._values["resource_groups"] = resource_groups

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resource_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        result = self._values.get("resource_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAzureIntegrationsSqlManaged(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAzureIntegrationsSqlManagedOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsSqlManagedOutputReference",
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
            type_hints = typing.get_type_hints(CloudAzureIntegrationsSqlManagedOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @jsii.member(jsii_name="resetResourceGroups")
    def reset_resource_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceGroups", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupsInput")
    def resource_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourceGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsSqlManagedOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroups")
    def resource_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resourceGroups"))

    @resource_groups.setter
    def resource_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsSqlManagedOutputReference, "resource_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroups", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAzureIntegrationsSqlManaged]:
        return typing.cast(typing.Optional[CloudAzureIntegrationsSqlManaged], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAzureIntegrationsSqlManaged],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsSqlManagedOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudAzureIntegrationsSqlOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsSqlOutputReference",
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
            type_hints = typing.get_type_hints(CloudAzureIntegrationsSqlOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @jsii.member(jsii_name="resetResourceGroups")
    def reset_resource_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceGroups", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupsInput")
    def resource_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourceGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsSqlOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroups")
    def resource_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resourceGroups"))

    @resource_groups.setter
    def resource_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsSqlOutputReference, "resource_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroups", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAzureIntegrationsSql]:
        return typing.cast(typing.Optional[CloudAzureIntegrationsSql], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[CloudAzureIntegrationsSql]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsSqlOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsStorage",
    jsii_struct_bases=[],
    name_mapping={
        "metrics_polling_interval": "metricsPollingInterval",
        "resource_groups": "resourceGroups",
    },
)
class CloudAzureIntegrationsStorage:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAzureIntegrationsStorage.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument resource_groups", value=resource_groups, expected_type=type_hints["resource_groups"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if resource_groups is not None:
            self._values["resource_groups"] = resource_groups

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resource_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        result = self._values.get("resource_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAzureIntegrationsStorage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAzureIntegrationsStorageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsStorageOutputReference",
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
            type_hints = typing.get_type_hints(CloudAzureIntegrationsStorageOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @jsii.member(jsii_name="resetResourceGroups")
    def reset_resource_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceGroups", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupsInput")
    def resource_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourceGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsStorageOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroups")
    def resource_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resourceGroups"))

    @resource_groups.setter
    def resource_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsStorageOutputReference, "resource_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroups", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAzureIntegrationsStorage]:
        return typing.cast(typing.Optional[CloudAzureIntegrationsStorage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAzureIntegrationsStorage],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsStorageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsVirtualMachine",
    jsii_struct_bases=[],
    name_mapping={
        "metrics_polling_interval": "metricsPollingInterval",
        "resource_groups": "resourceGroups",
    },
)
class CloudAzureIntegrationsVirtualMachine:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAzureIntegrationsVirtualMachine.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument resource_groups", value=resource_groups, expected_type=type_hints["resource_groups"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if resource_groups is not None:
            self._values["resource_groups"] = resource_groups

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resource_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        result = self._values.get("resource_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAzureIntegrationsVirtualMachine(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAzureIntegrationsVirtualMachineOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsVirtualMachineOutputReference",
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
            type_hints = typing.get_type_hints(CloudAzureIntegrationsVirtualMachineOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @jsii.member(jsii_name="resetResourceGroups")
    def reset_resource_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceGroups", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupsInput")
    def resource_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourceGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsVirtualMachineOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroups")
    def resource_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resourceGroups"))

    @resource_groups.setter
    def resource_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsVirtualMachineOutputReference, "resource_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroups", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAzureIntegrationsVirtualMachine]:
        return typing.cast(typing.Optional[CloudAzureIntegrationsVirtualMachine], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAzureIntegrationsVirtualMachine],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsVirtualMachineOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsVirtualNetworks",
    jsii_struct_bases=[],
    name_mapping={
        "metrics_polling_interval": "metricsPollingInterval",
        "resource_groups": "resourceGroups",
    },
)
class CloudAzureIntegrationsVirtualNetworks:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAzureIntegrationsVirtualNetworks.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument resource_groups", value=resource_groups, expected_type=type_hints["resource_groups"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if resource_groups is not None:
            self._values["resource_groups"] = resource_groups

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resource_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        result = self._values.get("resource_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAzureIntegrationsVirtualNetworks(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAzureIntegrationsVirtualNetworksOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsVirtualNetworksOutputReference",
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
            type_hints = typing.get_type_hints(CloudAzureIntegrationsVirtualNetworksOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @jsii.member(jsii_name="resetResourceGroups")
    def reset_resource_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceGroups", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupsInput")
    def resource_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourceGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsVirtualNetworksOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroups")
    def resource_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resourceGroups"))

    @resource_groups.setter
    def resource_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsVirtualNetworksOutputReference, "resource_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroups", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAzureIntegrationsVirtualNetworks]:
        return typing.cast(typing.Optional[CloudAzureIntegrationsVirtualNetworks], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAzureIntegrationsVirtualNetworks],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsVirtualNetworksOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsVms",
    jsii_struct_bases=[],
    name_mapping={
        "metrics_polling_interval": "metricsPollingInterval",
        "resource_groups": "resourceGroups",
    },
)
class CloudAzureIntegrationsVms:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAzureIntegrationsVms.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument resource_groups", value=resource_groups, expected_type=type_hints["resource_groups"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if resource_groups is not None:
            self._values["resource_groups"] = resource_groups

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resource_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        result = self._values.get("resource_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAzureIntegrationsVms(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAzureIntegrationsVmsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsVmsOutputReference",
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
            type_hints = typing.get_type_hints(CloudAzureIntegrationsVmsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @jsii.member(jsii_name="resetResourceGroups")
    def reset_resource_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceGroups", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupsInput")
    def resource_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourceGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsVmsOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroups")
    def resource_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resourceGroups"))

    @resource_groups.setter
    def resource_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsVmsOutputReference, "resource_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroups", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAzureIntegrationsVms]:
        return typing.cast(typing.Optional[CloudAzureIntegrationsVms], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[CloudAzureIntegrationsVms]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsVmsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsVpnGateway",
    jsii_struct_bases=[],
    name_mapping={
        "metrics_polling_interval": "metricsPollingInterval",
        "resource_groups": "resourceGroups",
    },
)
class CloudAzureIntegrationsVpnGateway:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        resource_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        :param resource_groups: Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAzureIntegrationsVpnGateway.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument resource_groups", value=resource_groups, expected_type=type_hints["resource_groups"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if resource_groups is not None:
            self._values["resource_groups"] = resource_groups

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#metrics_polling_interval CloudAzureIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resource_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each Resource group associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_azure_integrations#resource_groups CloudAzureIntegrations#resource_groups}
        '''
        result = self._values.get("resource_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAzureIntegrationsVpnGateway(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAzureIntegrationsVpnGatewayOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAzureIntegrations.CloudAzureIntegrationsVpnGatewayOutputReference",
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
            type_hints = typing.get_type_hints(CloudAzureIntegrationsVpnGatewayOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @jsii.member(jsii_name="resetResourceGroups")
    def reset_resource_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceGroups", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupsInput")
    def resource_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourceGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsVpnGatewayOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroups")
    def resource_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resourceGroups"))

    @resource_groups.setter
    def resource_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsVpnGatewayOutputReference, "resource_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroups", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAzureIntegrationsVpnGateway]:
        return typing.cast(typing.Optional[CloudAzureIntegrationsVpnGateway], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAzureIntegrationsVpnGateway],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAzureIntegrationsVpnGatewayOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CloudAzureIntegrations",
    "CloudAzureIntegrationsApiManagement",
    "CloudAzureIntegrationsApiManagementOutputReference",
    "CloudAzureIntegrationsAppGateway",
    "CloudAzureIntegrationsAppGatewayOutputReference",
    "CloudAzureIntegrationsAppService",
    "CloudAzureIntegrationsAppServiceOutputReference",
    "CloudAzureIntegrationsConfig",
    "CloudAzureIntegrationsContainers",
    "CloudAzureIntegrationsContainersOutputReference",
    "CloudAzureIntegrationsCosmosDb",
    "CloudAzureIntegrationsCosmosDbOutputReference",
    "CloudAzureIntegrationsCostManagement",
    "CloudAzureIntegrationsCostManagementOutputReference",
    "CloudAzureIntegrationsDataFactory",
    "CloudAzureIntegrationsDataFactoryOutputReference",
    "CloudAzureIntegrationsEventHub",
    "CloudAzureIntegrationsEventHubOutputReference",
    "CloudAzureIntegrationsExpressRoute",
    "CloudAzureIntegrationsExpressRouteOutputReference",
    "CloudAzureIntegrationsFirewalls",
    "CloudAzureIntegrationsFirewallsOutputReference",
    "CloudAzureIntegrationsFrontDoor",
    "CloudAzureIntegrationsFrontDoorOutputReference",
    "CloudAzureIntegrationsFunctions",
    "CloudAzureIntegrationsFunctionsOutputReference",
    "CloudAzureIntegrationsKeyVault",
    "CloudAzureIntegrationsKeyVaultOutputReference",
    "CloudAzureIntegrationsLoadBalancer",
    "CloudAzureIntegrationsLoadBalancerOutputReference",
    "CloudAzureIntegrationsLogicApps",
    "CloudAzureIntegrationsLogicAppsOutputReference",
    "CloudAzureIntegrationsMachineLearning",
    "CloudAzureIntegrationsMachineLearningOutputReference",
    "CloudAzureIntegrationsMariaDb",
    "CloudAzureIntegrationsMariaDbOutputReference",
    "CloudAzureIntegrationsMysql",
    "CloudAzureIntegrationsMysqlOutputReference",
    "CloudAzureIntegrationsPostgresql",
    "CloudAzureIntegrationsPostgresqlOutputReference",
    "CloudAzureIntegrationsPowerBiDedicated",
    "CloudAzureIntegrationsPowerBiDedicatedOutputReference",
    "CloudAzureIntegrationsRedisCache",
    "CloudAzureIntegrationsRedisCacheOutputReference",
    "CloudAzureIntegrationsServiceBus",
    "CloudAzureIntegrationsServiceBusOutputReference",
    "CloudAzureIntegrationsSql",
    "CloudAzureIntegrationsSqlManaged",
    "CloudAzureIntegrationsSqlManagedOutputReference",
    "CloudAzureIntegrationsSqlOutputReference",
    "CloudAzureIntegrationsStorage",
    "CloudAzureIntegrationsStorageOutputReference",
    "CloudAzureIntegrationsVirtualMachine",
    "CloudAzureIntegrationsVirtualMachineOutputReference",
    "CloudAzureIntegrationsVirtualNetworks",
    "CloudAzureIntegrationsVirtualNetworksOutputReference",
    "CloudAzureIntegrationsVms",
    "CloudAzureIntegrationsVmsOutputReference",
    "CloudAzureIntegrationsVpnGateway",
    "CloudAzureIntegrationsVpnGatewayOutputReference",
]

publication.publish()
