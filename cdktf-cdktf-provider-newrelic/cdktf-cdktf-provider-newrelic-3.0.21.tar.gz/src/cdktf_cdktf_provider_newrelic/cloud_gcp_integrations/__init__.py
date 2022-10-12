'''
# `newrelic_cloud_gcp_integrations`

Refer to the Terraform Registory for docs: [`newrelic_cloud_gcp_integrations`](https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations).
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


class CloudGcpIntegrations(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrations",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations newrelic_cloud_gcp_integrations}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        linked_account_id: jsii.Number,
        account_id: typing.Optional[jsii.Number] = None,
        app_engine: typing.Optional[typing.Union["CloudGcpIntegrationsAppEngine", typing.Dict[str, typing.Any]]] = None,
        big_query: typing.Optional[typing.Union["CloudGcpIntegrationsBigQuery", typing.Dict[str, typing.Any]]] = None,
        big_table: typing.Optional[typing.Union["CloudGcpIntegrationsBigTable", typing.Dict[str, typing.Any]]] = None,
        composer: typing.Optional[typing.Union["CloudGcpIntegrationsComposer", typing.Dict[str, typing.Any]]] = None,
        data_flow: typing.Optional[typing.Union["CloudGcpIntegrationsDataFlow", typing.Dict[str, typing.Any]]] = None,
        data_proc: typing.Optional[typing.Union["CloudGcpIntegrationsDataProc", typing.Dict[str, typing.Any]]] = None,
        data_store: typing.Optional[typing.Union["CloudGcpIntegrationsDataStore", typing.Dict[str, typing.Any]]] = None,
        fire_base_database: typing.Optional[typing.Union["CloudGcpIntegrationsFireBaseDatabase", typing.Dict[str, typing.Any]]] = None,
        fire_base_hosting: typing.Optional[typing.Union["CloudGcpIntegrationsFireBaseHosting", typing.Dict[str, typing.Any]]] = None,
        fire_base_storage: typing.Optional[typing.Union["CloudGcpIntegrationsFireBaseStorage", typing.Dict[str, typing.Any]]] = None,
        fire_store: typing.Optional[typing.Union["CloudGcpIntegrationsFireStore", typing.Dict[str, typing.Any]]] = None,
        functions: typing.Optional[typing.Union["CloudGcpIntegrationsFunctions", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        interconnect: typing.Optional[typing.Union["CloudGcpIntegrationsInterconnect", typing.Dict[str, typing.Any]]] = None,
        kubernetes: typing.Optional[typing.Union["CloudGcpIntegrationsKubernetes", typing.Dict[str, typing.Any]]] = None,
        load_balancing: typing.Optional[typing.Union["CloudGcpIntegrationsLoadBalancing", typing.Dict[str, typing.Any]]] = None,
        mem_cache: typing.Optional[typing.Union["CloudGcpIntegrationsMemCache", typing.Dict[str, typing.Any]]] = None,
        pub_sub: typing.Optional[typing.Union["CloudGcpIntegrationsPubSub", typing.Dict[str, typing.Any]]] = None,
        redis: typing.Optional[typing.Union["CloudGcpIntegrationsRedis", typing.Dict[str, typing.Any]]] = None,
        router: typing.Optional[typing.Union["CloudGcpIntegrationsRouter", typing.Dict[str, typing.Any]]] = None,
        run: typing.Optional[typing.Union["CloudGcpIntegrationsRun", typing.Dict[str, typing.Any]]] = None,
        spanner: typing.Optional[typing.Union["CloudGcpIntegrationsSpanner", typing.Dict[str, typing.Any]]] = None,
        sql: typing.Optional[typing.Union["CloudGcpIntegrationsSql", typing.Dict[str, typing.Any]]] = None,
        storage: typing.Optional[typing.Union["CloudGcpIntegrationsStorage", typing.Dict[str, typing.Any]]] = None,
        virtual_machines: typing.Optional[typing.Union["CloudGcpIntegrationsVirtualMachines", typing.Dict[str, typing.Any]]] = None,
        vpc_access: typing.Optional[typing.Union["CloudGcpIntegrationsVpcAccess", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations newrelic_cloud_gcp_integrations} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param linked_account_id: Id of the linked gcp account in New Relic. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#linked_account_id CloudGcpIntegrations#linked_account_id}
        :param account_id: ID of the newrelic account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#account_id CloudGcpIntegrations#account_id}
        :param app_engine: app_engine block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#app_engine CloudGcpIntegrations#app_engine}
        :param big_query: big_query block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#big_query CloudGcpIntegrations#big_query}
        :param big_table: big_table block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#big_table CloudGcpIntegrations#big_table}
        :param composer: composer block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#composer CloudGcpIntegrations#composer}
        :param data_flow: data_flow block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#data_flow CloudGcpIntegrations#data_flow}
        :param data_proc: data_proc block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#data_proc CloudGcpIntegrations#data_proc}
        :param data_store: data_store block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#data_store CloudGcpIntegrations#data_store}
        :param fire_base_database: fire_base_database block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#fire_base_database CloudGcpIntegrations#fire_base_database}
        :param fire_base_hosting: fire_base_hosting block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#fire_base_hosting CloudGcpIntegrations#fire_base_hosting}
        :param fire_base_storage: fire_base_storage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#fire_base_storage CloudGcpIntegrations#fire_base_storage}
        :param fire_store: fire_store block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#fire_store CloudGcpIntegrations#fire_store}
        :param functions: functions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#functions CloudGcpIntegrations#functions}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#id CloudGcpIntegrations#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param interconnect: interconnect block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#interconnect CloudGcpIntegrations#interconnect}
        :param kubernetes: kubernetes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#kubernetes CloudGcpIntegrations#kubernetes}
        :param load_balancing: load_balancing block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#load_balancing CloudGcpIntegrations#load_balancing}
        :param mem_cache: mem_cache block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#mem_cache CloudGcpIntegrations#mem_cache}
        :param pub_sub: pub_sub block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#pub_sub CloudGcpIntegrations#pub_sub}
        :param redis: redis block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#redis CloudGcpIntegrations#redis}
        :param router: router block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#router CloudGcpIntegrations#router}
        :param run: run block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#run CloudGcpIntegrations#run}
        :param spanner: spanner block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#spanner CloudGcpIntegrations#spanner}
        :param sql: sql block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#sql CloudGcpIntegrations#sql}
        :param storage: storage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#storage CloudGcpIntegrations#storage}
        :param virtual_machines: virtual_machines block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#virtual_machines CloudGcpIntegrations#virtual_machines}
        :param vpc_access: vpc_access block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#vpc_access CloudGcpIntegrations#vpc_access}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudGcpIntegrations.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CloudGcpIntegrationsConfig(
            linked_account_id=linked_account_id,
            account_id=account_id,
            app_engine=app_engine,
            big_query=big_query,
            big_table=big_table,
            composer=composer,
            data_flow=data_flow,
            data_proc=data_proc,
            data_store=data_store,
            fire_base_database=fire_base_database,
            fire_base_hosting=fire_base_hosting,
            fire_base_storage=fire_base_storage,
            fire_store=fire_store,
            functions=functions,
            id=id,
            interconnect=interconnect,
            kubernetes=kubernetes,
            load_balancing=load_balancing,
            mem_cache=mem_cache,
            pub_sub=pub_sub,
            redis=redis,
            router=router,
            run=run,
            spanner=spanner,
            sql=sql,
            storage=storage,
            virtual_machines=virtual_machines,
            vpc_access=vpc_access,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAppEngine")
    def put_app_engine(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        value = CloudGcpIntegrationsAppEngine(
            metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putAppEngine", [value]))

    @jsii.member(jsii_name="putBigQuery")
    def put_big_query(
        self,
        *,
        fetch_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param fetch_tags: to fetch tags of the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#fetch_tags CloudGcpIntegrations#fetch_tags}
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        value = CloudGcpIntegrationsBigQuery(
            fetch_tags=fetch_tags, metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putBigQuery", [value]))

    @jsii.member(jsii_name="putBigTable")
    def put_big_table(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        value = CloudGcpIntegrationsBigTable(
            metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putBigTable", [value]))

    @jsii.member(jsii_name="putComposer")
    def put_composer(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        value = CloudGcpIntegrationsComposer(
            metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putComposer", [value]))

    @jsii.member(jsii_name="putDataFlow")
    def put_data_flow(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        value = CloudGcpIntegrationsDataFlow(
            metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putDataFlow", [value]))

    @jsii.member(jsii_name="putDataProc")
    def put_data_proc(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        value = CloudGcpIntegrationsDataProc(
            metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putDataProc", [value]))

    @jsii.member(jsii_name="putDataStore")
    def put_data_store(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        value = CloudGcpIntegrationsDataStore(
            metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putDataStore", [value]))

    @jsii.member(jsii_name="putFireBaseDatabase")
    def put_fire_base_database(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        value = CloudGcpIntegrationsFireBaseDatabase(
            metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putFireBaseDatabase", [value]))

    @jsii.member(jsii_name="putFireBaseHosting")
    def put_fire_base_hosting(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        value = CloudGcpIntegrationsFireBaseHosting(
            metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putFireBaseHosting", [value]))

    @jsii.member(jsii_name="putFireBaseStorage")
    def put_fire_base_storage(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        value = CloudGcpIntegrationsFireBaseStorage(
            metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putFireBaseStorage", [value]))

    @jsii.member(jsii_name="putFireStore")
    def put_fire_store(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        value = CloudGcpIntegrationsFireStore(
            metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putFireStore", [value]))

    @jsii.member(jsii_name="putFunctions")
    def put_functions(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        value = CloudGcpIntegrationsFunctions(
            metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putFunctions", [value]))

    @jsii.member(jsii_name="putInterconnect")
    def put_interconnect(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        value = CloudGcpIntegrationsInterconnect(
            metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putInterconnect", [value]))

    @jsii.member(jsii_name="putKubernetes")
    def put_kubernetes(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        value = CloudGcpIntegrationsKubernetes(
            metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putKubernetes", [value]))

    @jsii.member(jsii_name="putLoadBalancing")
    def put_load_balancing(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        value = CloudGcpIntegrationsLoadBalancing(
            metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putLoadBalancing", [value]))

    @jsii.member(jsii_name="putMemCache")
    def put_mem_cache(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        value = CloudGcpIntegrationsMemCache(
            metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putMemCache", [value]))

    @jsii.member(jsii_name="putPubSub")
    def put_pub_sub(
        self,
        *,
        fetch_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param fetch_tags: to fetch tags of the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#fetch_tags CloudGcpIntegrations#fetch_tags}
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        value = CloudGcpIntegrationsPubSub(
            fetch_tags=fetch_tags, metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putPubSub", [value]))

    @jsii.member(jsii_name="putRedis")
    def put_redis(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        value = CloudGcpIntegrationsRedis(
            metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putRedis", [value]))

    @jsii.member(jsii_name="putRouter")
    def put_router(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        value = CloudGcpIntegrationsRouter(
            metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putRouter", [value]))

    @jsii.member(jsii_name="putRun")
    def put_run(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        value = CloudGcpIntegrationsRun(
            metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putRun", [value]))

    @jsii.member(jsii_name="putSpanner")
    def put_spanner(
        self,
        *,
        fetch_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param fetch_tags: to fetch tags of the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#fetch_tags CloudGcpIntegrations#fetch_tags}
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        value = CloudGcpIntegrationsSpanner(
            fetch_tags=fetch_tags, metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putSpanner", [value]))

    @jsii.member(jsii_name="putSql")
    def put_sql(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        value = CloudGcpIntegrationsSql(
            metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putSql", [value]))

    @jsii.member(jsii_name="putStorage")
    def put_storage(
        self,
        *,
        fetch_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param fetch_tags: to fetch tags of the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#fetch_tags CloudGcpIntegrations#fetch_tags}
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        value = CloudGcpIntegrationsStorage(
            fetch_tags=fetch_tags, metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putStorage", [value]))

    @jsii.member(jsii_name="putVirtualMachines")
    def put_virtual_machines(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        value = CloudGcpIntegrationsVirtualMachines(
            metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putVirtualMachines", [value]))

    @jsii.member(jsii_name="putVpcAccess")
    def put_vpc_access(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        value = CloudGcpIntegrationsVpcAccess(
            metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putVpcAccess", [value]))

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @jsii.member(jsii_name="resetAppEngine")
    def reset_app_engine(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppEngine", []))

    @jsii.member(jsii_name="resetBigQuery")
    def reset_big_query(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBigQuery", []))

    @jsii.member(jsii_name="resetBigTable")
    def reset_big_table(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBigTable", []))

    @jsii.member(jsii_name="resetComposer")
    def reset_composer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComposer", []))

    @jsii.member(jsii_name="resetDataFlow")
    def reset_data_flow(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataFlow", []))

    @jsii.member(jsii_name="resetDataProc")
    def reset_data_proc(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataProc", []))

    @jsii.member(jsii_name="resetDataStore")
    def reset_data_store(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataStore", []))

    @jsii.member(jsii_name="resetFireBaseDatabase")
    def reset_fire_base_database(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFireBaseDatabase", []))

    @jsii.member(jsii_name="resetFireBaseHosting")
    def reset_fire_base_hosting(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFireBaseHosting", []))

    @jsii.member(jsii_name="resetFireBaseStorage")
    def reset_fire_base_storage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFireBaseStorage", []))

    @jsii.member(jsii_name="resetFireStore")
    def reset_fire_store(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFireStore", []))

    @jsii.member(jsii_name="resetFunctions")
    def reset_functions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFunctions", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInterconnect")
    def reset_interconnect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterconnect", []))

    @jsii.member(jsii_name="resetKubernetes")
    def reset_kubernetes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKubernetes", []))

    @jsii.member(jsii_name="resetLoadBalancing")
    def reset_load_balancing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancing", []))

    @jsii.member(jsii_name="resetMemCache")
    def reset_mem_cache(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemCache", []))

    @jsii.member(jsii_name="resetPubSub")
    def reset_pub_sub(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPubSub", []))

    @jsii.member(jsii_name="resetRedis")
    def reset_redis(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedis", []))

    @jsii.member(jsii_name="resetRouter")
    def reset_router(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRouter", []))

    @jsii.member(jsii_name="resetRun")
    def reset_run(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRun", []))

    @jsii.member(jsii_name="resetSpanner")
    def reset_spanner(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpanner", []))

    @jsii.member(jsii_name="resetSql")
    def reset_sql(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSql", []))

    @jsii.member(jsii_name="resetStorage")
    def reset_storage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorage", []))

    @jsii.member(jsii_name="resetVirtualMachines")
    def reset_virtual_machines(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualMachines", []))

    @jsii.member(jsii_name="resetVpcAccess")
    def reset_vpc_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcAccess", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="appEngine")
    def app_engine(self) -> "CloudGcpIntegrationsAppEngineOutputReference":
        return typing.cast("CloudGcpIntegrationsAppEngineOutputReference", jsii.get(self, "appEngine"))

    @builtins.property
    @jsii.member(jsii_name="bigQuery")
    def big_query(self) -> "CloudGcpIntegrationsBigQueryOutputReference":
        return typing.cast("CloudGcpIntegrationsBigQueryOutputReference", jsii.get(self, "bigQuery"))

    @builtins.property
    @jsii.member(jsii_name="bigTable")
    def big_table(self) -> "CloudGcpIntegrationsBigTableOutputReference":
        return typing.cast("CloudGcpIntegrationsBigTableOutputReference", jsii.get(self, "bigTable"))

    @builtins.property
    @jsii.member(jsii_name="composer")
    def composer(self) -> "CloudGcpIntegrationsComposerOutputReference":
        return typing.cast("CloudGcpIntegrationsComposerOutputReference", jsii.get(self, "composer"))

    @builtins.property
    @jsii.member(jsii_name="dataFlow")
    def data_flow(self) -> "CloudGcpIntegrationsDataFlowOutputReference":
        return typing.cast("CloudGcpIntegrationsDataFlowOutputReference", jsii.get(self, "dataFlow"))

    @builtins.property
    @jsii.member(jsii_name="dataProc")
    def data_proc(self) -> "CloudGcpIntegrationsDataProcOutputReference":
        return typing.cast("CloudGcpIntegrationsDataProcOutputReference", jsii.get(self, "dataProc"))

    @builtins.property
    @jsii.member(jsii_name="dataStore")
    def data_store(self) -> "CloudGcpIntegrationsDataStoreOutputReference":
        return typing.cast("CloudGcpIntegrationsDataStoreOutputReference", jsii.get(self, "dataStore"))

    @builtins.property
    @jsii.member(jsii_name="fireBaseDatabase")
    def fire_base_database(
        self,
    ) -> "CloudGcpIntegrationsFireBaseDatabaseOutputReference":
        return typing.cast("CloudGcpIntegrationsFireBaseDatabaseOutputReference", jsii.get(self, "fireBaseDatabase"))

    @builtins.property
    @jsii.member(jsii_name="fireBaseHosting")
    def fire_base_hosting(self) -> "CloudGcpIntegrationsFireBaseHostingOutputReference":
        return typing.cast("CloudGcpIntegrationsFireBaseHostingOutputReference", jsii.get(self, "fireBaseHosting"))

    @builtins.property
    @jsii.member(jsii_name="fireBaseStorage")
    def fire_base_storage(self) -> "CloudGcpIntegrationsFireBaseStorageOutputReference":
        return typing.cast("CloudGcpIntegrationsFireBaseStorageOutputReference", jsii.get(self, "fireBaseStorage"))

    @builtins.property
    @jsii.member(jsii_name="fireStore")
    def fire_store(self) -> "CloudGcpIntegrationsFireStoreOutputReference":
        return typing.cast("CloudGcpIntegrationsFireStoreOutputReference", jsii.get(self, "fireStore"))

    @builtins.property
    @jsii.member(jsii_name="functions")
    def functions(self) -> "CloudGcpIntegrationsFunctionsOutputReference":
        return typing.cast("CloudGcpIntegrationsFunctionsOutputReference", jsii.get(self, "functions"))

    @builtins.property
    @jsii.member(jsii_name="interconnect")
    def interconnect(self) -> "CloudGcpIntegrationsInterconnectOutputReference":
        return typing.cast("CloudGcpIntegrationsInterconnectOutputReference", jsii.get(self, "interconnect"))

    @builtins.property
    @jsii.member(jsii_name="kubernetes")
    def kubernetes(self) -> "CloudGcpIntegrationsKubernetesOutputReference":
        return typing.cast("CloudGcpIntegrationsKubernetesOutputReference", jsii.get(self, "kubernetes"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancing")
    def load_balancing(self) -> "CloudGcpIntegrationsLoadBalancingOutputReference":
        return typing.cast("CloudGcpIntegrationsLoadBalancingOutputReference", jsii.get(self, "loadBalancing"))

    @builtins.property
    @jsii.member(jsii_name="memCache")
    def mem_cache(self) -> "CloudGcpIntegrationsMemCacheOutputReference":
        return typing.cast("CloudGcpIntegrationsMemCacheOutputReference", jsii.get(self, "memCache"))

    @builtins.property
    @jsii.member(jsii_name="pubSub")
    def pub_sub(self) -> "CloudGcpIntegrationsPubSubOutputReference":
        return typing.cast("CloudGcpIntegrationsPubSubOutputReference", jsii.get(self, "pubSub"))

    @builtins.property
    @jsii.member(jsii_name="redis")
    def redis(self) -> "CloudGcpIntegrationsRedisOutputReference":
        return typing.cast("CloudGcpIntegrationsRedisOutputReference", jsii.get(self, "redis"))

    @builtins.property
    @jsii.member(jsii_name="router")
    def router(self) -> "CloudGcpIntegrationsRouterOutputReference":
        return typing.cast("CloudGcpIntegrationsRouterOutputReference", jsii.get(self, "router"))

    @builtins.property
    @jsii.member(jsii_name="run")
    def run(self) -> "CloudGcpIntegrationsRunOutputReference":
        return typing.cast("CloudGcpIntegrationsRunOutputReference", jsii.get(self, "run"))

    @builtins.property
    @jsii.member(jsii_name="spanner")
    def spanner(self) -> "CloudGcpIntegrationsSpannerOutputReference":
        return typing.cast("CloudGcpIntegrationsSpannerOutputReference", jsii.get(self, "spanner"))

    @builtins.property
    @jsii.member(jsii_name="sql")
    def sql(self) -> "CloudGcpIntegrationsSqlOutputReference":
        return typing.cast("CloudGcpIntegrationsSqlOutputReference", jsii.get(self, "sql"))

    @builtins.property
    @jsii.member(jsii_name="storage")
    def storage(self) -> "CloudGcpIntegrationsStorageOutputReference":
        return typing.cast("CloudGcpIntegrationsStorageOutputReference", jsii.get(self, "storage"))

    @builtins.property
    @jsii.member(jsii_name="virtualMachines")
    def virtual_machines(self) -> "CloudGcpIntegrationsVirtualMachinesOutputReference":
        return typing.cast("CloudGcpIntegrationsVirtualMachinesOutputReference", jsii.get(self, "virtualMachines"))

    @builtins.property
    @jsii.member(jsii_name="vpcAccess")
    def vpc_access(self) -> "CloudGcpIntegrationsVpcAccessOutputReference":
        return typing.cast("CloudGcpIntegrationsVpcAccessOutputReference", jsii.get(self, "vpcAccess"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="appEngineInput")
    def app_engine_input(self) -> typing.Optional["CloudGcpIntegrationsAppEngine"]:
        return typing.cast(typing.Optional["CloudGcpIntegrationsAppEngine"], jsii.get(self, "appEngineInput"))

    @builtins.property
    @jsii.member(jsii_name="bigQueryInput")
    def big_query_input(self) -> typing.Optional["CloudGcpIntegrationsBigQuery"]:
        return typing.cast(typing.Optional["CloudGcpIntegrationsBigQuery"], jsii.get(self, "bigQueryInput"))

    @builtins.property
    @jsii.member(jsii_name="bigTableInput")
    def big_table_input(self) -> typing.Optional["CloudGcpIntegrationsBigTable"]:
        return typing.cast(typing.Optional["CloudGcpIntegrationsBigTable"], jsii.get(self, "bigTableInput"))

    @builtins.property
    @jsii.member(jsii_name="composerInput")
    def composer_input(self) -> typing.Optional["CloudGcpIntegrationsComposer"]:
        return typing.cast(typing.Optional["CloudGcpIntegrationsComposer"], jsii.get(self, "composerInput"))

    @builtins.property
    @jsii.member(jsii_name="dataFlowInput")
    def data_flow_input(self) -> typing.Optional["CloudGcpIntegrationsDataFlow"]:
        return typing.cast(typing.Optional["CloudGcpIntegrationsDataFlow"], jsii.get(self, "dataFlowInput"))

    @builtins.property
    @jsii.member(jsii_name="dataProcInput")
    def data_proc_input(self) -> typing.Optional["CloudGcpIntegrationsDataProc"]:
        return typing.cast(typing.Optional["CloudGcpIntegrationsDataProc"], jsii.get(self, "dataProcInput"))

    @builtins.property
    @jsii.member(jsii_name="dataStoreInput")
    def data_store_input(self) -> typing.Optional["CloudGcpIntegrationsDataStore"]:
        return typing.cast(typing.Optional["CloudGcpIntegrationsDataStore"], jsii.get(self, "dataStoreInput"))

    @builtins.property
    @jsii.member(jsii_name="fireBaseDatabaseInput")
    def fire_base_database_input(
        self,
    ) -> typing.Optional["CloudGcpIntegrationsFireBaseDatabase"]:
        return typing.cast(typing.Optional["CloudGcpIntegrationsFireBaseDatabase"], jsii.get(self, "fireBaseDatabaseInput"))

    @builtins.property
    @jsii.member(jsii_name="fireBaseHostingInput")
    def fire_base_hosting_input(
        self,
    ) -> typing.Optional["CloudGcpIntegrationsFireBaseHosting"]:
        return typing.cast(typing.Optional["CloudGcpIntegrationsFireBaseHosting"], jsii.get(self, "fireBaseHostingInput"))

    @builtins.property
    @jsii.member(jsii_name="fireBaseStorageInput")
    def fire_base_storage_input(
        self,
    ) -> typing.Optional["CloudGcpIntegrationsFireBaseStorage"]:
        return typing.cast(typing.Optional["CloudGcpIntegrationsFireBaseStorage"], jsii.get(self, "fireBaseStorageInput"))

    @builtins.property
    @jsii.member(jsii_name="fireStoreInput")
    def fire_store_input(self) -> typing.Optional["CloudGcpIntegrationsFireStore"]:
        return typing.cast(typing.Optional["CloudGcpIntegrationsFireStore"], jsii.get(self, "fireStoreInput"))

    @builtins.property
    @jsii.member(jsii_name="functionsInput")
    def functions_input(self) -> typing.Optional["CloudGcpIntegrationsFunctions"]:
        return typing.cast(typing.Optional["CloudGcpIntegrationsFunctions"], jsii.get(self, "functionsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="interconnectInput")
    def interconnect_input(self) -> typing.Optional["CloudGcpIntegrationsInterconnect"]:
        return typing.cast(typing.Optional["CloudGcpIntegrationsInterconnect"], jsii.get(self, "interconnectInput"))

    @builtins.property
    @jsii.member(jsii_name="kubernetesInput")
    def kubernetes_input(self) -> typing.Optional["CloudGcpIntegrationsKubernetes"]:
        return typing.cast(typing.Optional["CloudGcpIntegrationsKubernetes"], jsii.get(self, "kubernetesInput"))

    @builtins.property
    @jsii.member(jsii_name="linkedAccountIdInput")
    def linked_account_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "linkedAccountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancingInput")
    def load_balancing_input(
        self,
    ) -> typing.Optional["CloudGcpIntegrationsLoadBalancing"]:
        return typing.cast(typing.Optional["CloudGcpIntegrationsLoadBalancing"], jsii.get(self, "loadBalancingInput"))

    @builtins.property
    @jsii.member(jsii_name="memCacheInput")
    def mem_cache_input(self) -> typing.Optional["CloudGcpIntegrationsMemCache"]:
        return typing.cast(typing.Optional["CloudGcpIntegrationsMemCache"], jsii.get(self, "memCacheInput"))

    @builtins.property
    @jsii.member(jsii_name="pubSubInput")
    def pub_sub_input(self) -> typing.Optional["CloudGcpIntegrationsPubSub"]:
        return typing.cast(typing.Optional["CloudGcpIntegrationsPubSub"], jsii.get(self, "pubSubInput"))

    @builtins.property
    @jsii.member(jsii_name="redisInput")
    def redis_input(self) -> typing.Optional["CloudGcpIntegrationsRedis"]:
        return typing.cast(typing.Optional["CloudGcpIntegrationsRedis"], jsii.get(self, "redisInput"))

    @builtins.property
    @jsii.member(jsii_name="routerInput")
    def router_input(self) -> typing.Optional["CloudGcpIntegrationsRouter"]:
        return typing.cast(typing.Optional["CloudGcpIntegrationsRouter"], jsii.get(self, "routerInput"))

    @builtins.property
    @jsii.member(jsii_name="runInput")
    def run_input(self) -> typing.Optional["CloudGcpIntegrationsRun"]:
        return typing.cast(typing.Optional["CloudGcpIntegrationsRun"], jsii.get(self, "runInput"))

    @builtins.property
    @jsii.member(jsii_name="spannerInput")
    def spanner_input(self) -> typing.Optional["CloudGcpIntegrationsSpanner"]:
        return typing.cast(typing.Optional["CloudGcpIntegrationsSpanner"], jsii.get(self, "spannerInput"))

    @builtins.property
    @jsii.member(jsii_name="sqlInput")
    def sql_input(self) -> typing.Optional["CloudGcpIntegrationsSql"]:
        return typing.cast(typing.Optional["CloudGcpIntegrationsSql"], jsii.get(self, "sqlInput"))

    @builtins.property
    @jsii.member(jsii_name="storageInput")
    def storage_input(self) -> typing.Optional["CloudGcpIntegrationsStorage"]:
        return typing.cast(typing.Optional["CloudGcpIntegrationsStorage"], jsii.get(self, "storageInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualMachinesInput")
    def virtual_machines_input(
        self,
    ) -> typing.Optional["CloudGcpIntegrationsVirtualMachines"]:
        return typing.cast(typing.Optional["CloudGcpIntegrationsVirtualMachines"], jsii.get(self, "virtualMachinesInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcAccessInput")
    def vpc_access_input(self) -> typing.Optional["CloudGcpIntegrationsVpcAccess"]:
        return typing.cast(typing.Optional["CloudGcpIntegrationsVpcAccess"], jsii.get(self, "vpcAccessInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrations, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrations, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="linkedAccountId")
    def linked_account_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "linkedAccountId"))

    @linked_account_id.setter
    def linked_account_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrations, "linked_account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "linkedAccountId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsAppEngine",
    jsii_struct_bases=[],
    name_mapping={"metrics_polling_interval": "metricsPollingInterval"},
)
class CloudGcpIntegrationsAppEngine:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudGcpIntegrationsAppEngine.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''the data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudGcpIntegrationsAppEngine(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudGcpIntegrationsAppEngineOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsAppEngineOutputReference",
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
            type_hints = typing.get_type_hints(CloudGcpIntegrationsAppEngineOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsAppEngineOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudGcpIntegrationsAppEngine]:
        return typing.cast(typing.Optional[CloudGcpIntegrationsAppEngine], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudGcpIntegrationsAppEngine],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsAppEngineOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsBigQuery",
    jsii_struct_bases=[],
    name_mapping={
        "fetch_tags": "fetchTags",
        "metrics_polling_interval": "metricsPollingInterval",
    },
)
class CloudGcpIntegrationsBigQuery:
    def __init__(
        self,
        *,
        fetch_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param fetch_tags: to fetch tags of the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#fetch_tags CloudGcpIntegrations#fetch_tags}
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudGcpIntegrationsBigQuery.__init__)
            check_type(argname="argument fetch_tags", value=fetch_tags, expected_type=type_hints["fetch_tags"])
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[str, typing.Any] = {}
        if fetch_tags is not None:
            self._values["fetch_tags"] = fetch_tags
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def fetch_tags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''to fetch tags of the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#fetch_tags CloudGcpIntegrations#fetch_tags}
        '''
        result = self._values.get("fetch_tags")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''the data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudGcpIntegrationsBigQuery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudGcpIntegrationsBigQueryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsBigQueryOutputReference",
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
            type_hints = typing.get_type_hints(CloudGcpIntegrationsBigQueryOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFetchTags")
    def reset_fetch_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFetchTags", []))

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="fetchTagsInput")
    def fetch_tags_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "fetchTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="fetchTags")
    def fetch_tags(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "fetchTags"))

    @fetch_tags.setter
    def fetch_tags(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsBigQueryOutputReference, "fetch_tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fetchTags", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsBigQueryOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudGcpIntegrationsBigQuery]:
        return typing.cast(typing.Optional[CloudGcpIntegrationsBigQuery], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudGcpIntegrationsBigQuery],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsBigQueryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsBigTable",
    jsii_struct_bases=[],
    name_mapping={"metrics_polling_interval": "metricsPollingInterval"},
)
class CloudGcpIntegrationsBigTable:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudGcpIntegrationsBigTable.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''the data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudGcpIntegrationsBigTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudGcpIntegrationsBigTableOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsBigTableOutputReference",
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
            type_hints = typing.get_type_hints(CloudGcpIntegrationsBigTableOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsBigTableOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudGcpIntegrationsBigTable]:
        return typing.cast(typing.Optional[CloudGcpIntegrationsBigTable], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudGcpIntegrationsBigTable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsBigTableOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsComposer",
    jsii_struct_bases=[],
    name_mapping={"metrics_polling_interval": "metricsPollingInterval"},
)
class CloudGcpIntegrationsComposer:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudGcpIntegrationsComposer.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''the data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudGcpIntegrationsComposer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudGcpIntegrationsComposerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsComposerOutputReference",
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
            type_hints = typing.get_type_hints(CloudGcpIntegrationsComposerOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsComposerOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudGcpIntegrationsComposer]:
        return typing.cast(typing.Optional[CloudGcpIntegrationsComposer], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudGcpIntegrationsComposer],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsComposerOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsConfig",
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
        "app_engine": "appEngine",
        "big_query": "bigQuery",
        "big_table": "bigTable",
        "composer": "composer",
        "data_flow": "dataFlow",
        "data_proc": "dataProc",
        "data_store": "dataStore",
        "fire_base_database": "fireBaseDatabase",
        "fire_base_hosting": "fireBaseHosting",
        "fire_base_storage": "fireBaseStorage",
        "fire_store": "fireStore",
        "functions": "functions",
        "id": "id",
        "interconnect": "interconnect",
        "kubernetes": "kubernetes",
        "load_balancing": "loadBalancing",
        "mem_cache": "memCache",
        "pub_sub": "pubSub",
        "redis": "redis",
        "router": "router",
        "run": "run",
        "spanner": "spanner",
        "sql": "sql",
        "storage": "storage",
        "virtual_machines": "virtualMachines",
        "vpc_access": "vpcAccess",
    },
)
class CloudGcpIntegrationsConfig(cdktf.TerraformMetaArguments):
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
        app_engine: typing.Optional[typing.Union[CloudGcpIntegrationsAppEngine, typing.Dict[str, typing.Any]]] = None,
        big_query: typing.Optional[typing.Union[CloudGcpIntegrationsBigQuery, typing.Dict[str, typing.Any]]] = None,
        big_table: typing.Optional[typing.Union[CloudGcpIntegrationsBigTable, typing.Dict[str, typing.Any]]] = None,
        composer: typing.Optional[typing.Union[CloudGcpIntegrationsComposer, typing.Dict[str, typing.Any]]] = None,
        data_flow: typing.Optional[typing.Union["CloudGcpIntegrationsDataFlow", typing.Dict[str, typing.Any]]] = None,
        data_proc: typing.Optional[typing.Union["CloudGcpIntegrationsDataProc", typing.Dict[str, typing.Any]]] = None,
        data_store: typing.Optional[typing.Union["CloudGcpIntegrationsDataStore", typing.Dict[str, typing.Any]]] = None,
        fire_base_database: typing.Optional[typing.Union["CloudGcpIntegrationsFireBaseDatabase", typing.Dict[str, typing.Any]]] = None,
        fire_base_hosting: typing.Optional[typing.Union["CloudGcpIntegrationsFireBaseHosting", typing.Dict[str, typing.Any]]] = None,
        fire_base_storage: typing.Optional[typing.Union["CloudGcpIntegrationsFireBaseStorage", typing.Dict[str, typing.Any]]] = None,
        fire_store: typing.Optional[typing.Union["CloudGcpIntegrationsFireStore", typing.Dict[str, typing.Any]]] = None,
        functions: typing.Optional[typing.Union["CloudGcpIntegrationsFunctions", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        interconnect: typing.Optional[typing.Union["CloudGcpIntegrationsInterconnect", typing.Dict[str, typing.Any]]] = None,
        kubernetes: typing.Optional[typing.Union["CloudGcpIntegrationsKubernetes", typing.Dict[str, typing.Any]]] = None,
        load_balancing: typing.Optional[typing.Union["CloudGcpIntegrationsLoadBalancing", typing.Dict[str, typing.Any]]] = None,
        mem_cache: typing.Optional[typing.Union["CloudGcpIntegrationsMemCache", typing.Dict[str, typing.Any]]] = None,
        pub_sub: typing.Optional[typing.Union["CloudGcpIntegrationsPubSub", typing.Dict[str, typing.Any]]] = None,
        redis: typing.Optional[typing.Union["CloudGcpIntegrationsRedis", typing.Dict[str, typing.Any]]] = None,
        router: typing.Optional[typing.Union["CloudGcpIntegrationsRouter", typing.Dict[str, typing.Any]]] = None,
        run: typing.Optional[typing.Union["CloudGcpIntegrationsRun", typing.Dict[str, typing.Any]]] = None,
        spanner: typing.Optional[typing.Union["CloudGcpIntegrationsSpanner", typing.Dict[str, typing.Any]]] = None,
        sql: typing.Optional[typing.Union["CloudGcpIntegrationsSql", typing.Dict[str, typing.Any]]] = None,
        storage: typing.Optional[typing.Union["CloudGcpIntegrationsStorage", typing.Dict[str, typing.Any]]] = None,
        virtual_machines: typing.Optional[typing.Union["CloudGcpIntegrationsVirtualMachines", typing.Dict[str, typing.Any]]] = None,
        vpc_access: typing.Optional[typing.Union["CloudGcpIntegrationsVpcAccess", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param linked_account_id: Id of the linked gcp account in New Relic. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#linked_account_id CloudGcpIntegrations#linked_account_id}
        :param account_id: ID of the newrelic account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#account_id CloudGcpIntegrations#account_id}
        :param app_engine: app_engine block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#app_engine CloudGcpIntegrations#app_engine}
        :param big_query: big_query block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#big_query CloudGcpIntegrations#big_query}
        :param big_table: big_table block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#big_table CloudGcpIntegrations#big_table}
        :param composer: composer block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#composer CloudGcpIntegrations#composer}
        :param data_flow: data_flow block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#data_flow CloudGcpIntegrations#data_flow}
        :param data_proc: data_proc block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#data_proc CloudGcpIntegrations#data_proc}
        :param data_store: data_store block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#data_store CloudGcpIntegrations#data_store}
        :param fire_base_database: fire_base_database block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#fire_base_database CloudGcpIntegrations#fire_base_database}
        :param fire_base_hosting: fire_base_hosting block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#fire_base_hosting CloudGcpIntegrations#fire_base_hosting}
        :param fire_base_storage: fire_base_storage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#fire_base_storage CloudGcpIntegrations#fire_base_storage}
        :param fire_store: fire_store block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#fire_store CloudGcpIntegrations#fire_store}
        :param functions: functions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#functions CloudGcpIntegrations#functions}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#id CloudGcpIntegrations#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param interconnect: interconnect block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#interconnect CloudGcpIntegrations#interconnect}
        :param kubernetes: kubernetes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#kubernetes CloudGcpIntegrations#kubernetes}
        :param load_balancing: load_balancing block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#load_balancing CloudGcpIntegrations#load_balancing}
        :param mem_cache: mem_cache block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#mem_cache CloudGcpIntegrations#mem_cache}
        :param pub_sub: pub_sub block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#pub_sub CloudGcpIntegrations#pub_sub}
        :param redis: redis block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#redis CloudGcpIntegrations#redis}
        :param router: router block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#router CloudGcpIntegrations#router}
        :param run: run block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#run CloudGcpIntegrations#run}
        :param spanner: spanner block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#spanner CloudGcpIntegrations#spanner}
        :param sql: sql block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#sql CloudGcpIntegrations#sql}
        :param storage: storage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#storage CloudGcpIntegrations#storage}
        :param virtual_machines: virtual_machines block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#virtual_machines CloudGcpIntegrations#virtual_machines}
        :param vpc_access: vpc_access block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#vpc_access CloudGcpIntegrations#vpc_access}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(app_engine, dict):
            app_engine = CloudGcpIntegrationsAppEngine(**app_engine)
        if isinstance(big_query, dict):
            big_query = CloudGcpIntegrationsBigQuery(**big_query)
        if isinstance(big_table, dict):
            big_table = CloudGcpIntegrationsBigTable(**big_table)
        if isinstance(composer, dict):
            composer = CloudGcpIntegrationsComposer(**composer)
        if isinstance(data_flow, dict):
            data_flow = CloudGcpIntegrationsDataFlow(**data_flow)
        if isinstance(data_proc, dict):
            data_proc = CloudGcpIntegrationsDataProc(**data_proc)
        if isinstance(data_store, dict):
            data_store = CloudGcpIntegrationsDataStore(**data_store)
        if isinstance(fire_base_database, dict):
            fire_base_database = CloudGcpIntegrationsFireBaseDatabase(**fire_base_database)
        if isinstance(fire_base_hosting, dict):
            fire_base_hosting = CloudGcpIntegrationsFireBaseHosting(**fire_base_hosting)
        if isinstance(fire_base_storage, dict):
            fire_base_storage = CloudGcpIntegrationsFireBaseStorage(**fire_base_storage)
        if isinstance(fire_store, dict):
            fire_store = CloudGcpIntegrationsFireStore(**fire_store)
        if isinstance(functions, dict):
            functions = CloudGcpIntegrationsFunctions(**functions)
        if isinstance(interconnect, dict):
            interconnect = CloudGcpIntegrationsInterconnect(**interconnect)
        if isinstance(kubernetes, dict):
            kubernetes = CloudGcpIntegrationsKubernetes(**kubernetes)
        if isinstance(load_balancing, dict):
            load_balancing = CloudGcpIntegrationsLoadBalancing(**load_balancing)
        if isinstance(mem_cache, dict):
            mem_cache = CloudGcpIntegrationsMemCache(**mem_cache)
        if isinstance(pub_sub, dict):
            pub_sub = CloudGcpIntegrationsPubSub(**pub_sub)
        if isinstance(redis, dict):
            redis = CloudGcpIntegrationsRedis(**redis)
        if isinstance(router, dict):
            router = CloudGcpIntegrationsRouter(**router)
        if isinstance(run, dict):
            run = CloudGcpIntegrationsRun(**run)
        if isinstance(spanner, dict):
            spanner = CloudGcpIntegrationsSpanner(**spanner)
        if isinstance(sql, dict):
            sql = CloudGcpIntegrationsSql(**sql)
        if isinstance(storage, dict):
            storage = CloudGcpIntegrationsStorage(**storage)
        if isinstance(virtual_machines, dict):
            virtual_machines = CloudGcpIntegrationsVirtualMachines(**virtual_machines)
        if isinstance(vpc_access, dict):
            vpc_access = CloudGcpIntegrationsVpcAccess(**vpc_access)
        if __debug__:
            type_hints = typing.get_type_hints(CloudGcpIntegrationsConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument linked_account_id", value=linked_account_id, expected_type=type_hints["linked_account_id"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument app_engine", value=app_engine, expected_type=type_hints["app_engine"])
            check_type(argname="argument big_query", value=big_query, expected_type=type_hints["big_query"])
            check_type(argname="argument big_table", value=big_table, expected_type=type_hints["big_table"])
            check_type(argname="argument composer", value=composer, expected_type=type_hints["composer"])
            check_type(argname="argument data_flow", value=data_flow, expected_type=type_hints["data_flow"])
            check_type(argname="argument data_proc", value=data_proc, expected_type=type_hints["data_proc"])
            check_type(argname="argument data_store", value=data_store, expected_type=type_hints["data_store"])
            check_type(argname="argument fire_base_database", value=fire_base_database, expected_type=type_hints["fire_base_database"])
            check_type(argname="argument fire_base_hosting", value=fire_base_hosting, expected_type=type_hints["fire_base_hosting"])
            check_type(argname="argument fire_base_storage", value=fire_base_storage, expected_type=type_hints["fire_base_storage"])
            check_type(argname="argument fire_store", value=fire_store, expected_type=type_hints["fire_store"])
            check_type(argname="argument functions", value=functions, expected_type=type_hints["functions"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument interconnect", value=interconnect, expected_type=type_hints["interconnect"])
            check_type(argname="argument kubernetes", value=kubernetes, expected_type=type_hints["kubernetes"])
            check_type(argname="argument load_balancing", value=load_balancing, expected_type=type_hints["load_balancing"])
            check_type(argname="argument mem_cache", value=mem_cache, expected_type=type_hints["mem_cache"])
            check_type(argname="argument pub_sub", value=pub_sub, expected_type=type_hints["pub_sub"])
            check_type(argname="argument redis", value=redis, expected_type=type_hints["redis"])
            check_type(argname="argument router", value=router, expected_type=type_hints["router"])
            check_type(argname="argument run", value=run, expected_type=type_hints["run"])
            check_type(argname="argument spanner", value=spanner, expected_type=type_hints["spanner"])
            check_type(argname="argument sql", value=sql, expected_type=type_hints["sql"])
            check_type(argname="argument storage", value=storage, expected_type=type_hints["storage"])
            check_type(argname="argument virtual_machines", value=virtual_machines, expected_type=type_hints["virtual_machines"])
            check_type(argname="argument vpc_access", value=vpc_access, expected_type=type_hints["vpc_access"])
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
        if app_engine is not None:
            self._values["app_engine"] = app_engine
        if big_query is not None:
            self._values["big_query"] = big_query
        if big_table is not None:
            self._values["big_table"] = big_table
        if composer is not None:
            self._values["composer"] = composer
        if data_flow is not None:
            self._values["data_flow"] = data_flow
        if data_proc is not None:
            self._values["data_proc"] = data_proc
        if data_store is not None:
            self._values["data_store"] = data_store
        if fire_base_database is not None:
            self._values["fire_base_database"] = fire_base_database
        if fire_base_hosting is not None:
            self._values["fire_base_hosting"] = fire_base_hosting
        if fire_base_storage is not None:
            self._values["fire_base_storage"] = fire_base_storage
        if fire_store is not None:
            self._values["fire_store"] = fire_store
        if functions is not None:
            self._values["functions"] = functions
        if id is not None:
            self._values["id"] = id
        if interconnect is not None:
            self._values["interconnect"] = interconnect
        if kubernetes is not None:
            self._values["kubernetes"] = kubernetes
        if load_balancing is not None:
            self._values["load_balancing"] = load_balancing
        if mem_cache is not None:
            self._values["mem_cache"] = mem_cache
        if pub_sub is not None:
            self._values["pub_sub"] = pub_sub
        if redis is not None:
            self._values["redis"] = redis
        if router is not None:
            self._values["router"] = router
        if run is not None:
            self._values["run"] = run
        if spanner is not None:
            self._values["spanner"] = spanner
        if sql is not None:
            self._values["sql"] = sql
        if storage is not None:
            self._values["storage"] = storage
        if virtual_machines is not None:
            self._values["virtual_machines"] = virtual_machines
        if vpc_access is not None:
            self._values["vpc_access"] = vpc_access

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
        '''Id of the linked gcp account in New Relic.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#linked_account_id CloudGcpIntegrations#linked_account_id}
        '''
        result = self._values.get("linked_account_id")
        assert result is not None, "Required property 'linked_account_id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def account_id(self) -> typing.Optional[jsii.Number]:
        '''ID of the newrelic account.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#account_id CloudGcpIntegrations#account_id}
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def app_engine(self) -> typing.Optional[CloudGcpIntegrationsAppEngine]:
        '''app_engine block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#app_engine CloudGcpIntegrations#app_engine}
        '''
        result = self._values.get("app_engine")
        return typing.cast(typing.Optional[CloudGcpIntegrationsAppEngine], result)

    @builtins.property
    def big_query(self) -> typing.Optional[CloudGcpIntegrationsBigQuery]:
        '''big_query block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#big_query CloudGcpIntegrations#big_query}
        '''
        result = self._values.get("big_query")
        return typing.cast(typing.Optional[CloudGcpIntegrationsBigQuery], result)

    @builtins.property
    def big_table(self) -> typing.Optional[CloudGcpIntegrationsBigTable]:
        '''big_table block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#big_table CloudGcpIntegrations#big_table}
        '''
        result = self._values.get("big_table")
        return typing.cast(typing.Optional[CloudGcpIntegrationsBigTable], result)

    @builtins.property
    def composer(self) -> typing.Optional[CloudGcpIntegrationsComposer]:
        '''composer block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#composer CloudGcpIntegrations#composer}
        '''
        result = self._values.get("composer")
        return typing.cast(typing.Optional[CloudGcpIntegrationsComposer], result)

    @builtins.property
    def data_flow(self) -> typing.Optional["CloudGcpIntegrationsDataFlow"]:
        '''data_flow block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#data_flow CloudGcpIntegrations#data_flow}
        '''
        result = self._values.get("data_flow")
        return typing.cast(typing.Optional["CloudGcpIntegrationsDataFlow"], result)

    @builtins.property
    def data_proc(self) -> typing.Optional["CloudGcpIntegrationsDataProc"]:
        '''data_proc block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#data_proc CloudGcpIntegrations#data_proc}
        '''
        result = self._values.get("data_proc")
        return typing.cast(typing.Optional["CloudGcpIntegrationsDataProc"], result)

    @builtins.property
    def data_store(self) -> typing.Optional["CloudGcpIntegrationsDataStore"]:
        '''data_store block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#data_store CloudGcpIntegrations#data_store}
        '''
        result = self._values.get("data_store")
        return typing.cast(typing.Optional["CloudGcpIntegrationsDataStore"], result)

    @builtins.property
    def fire_base_database(
        self,
    ) -> typing.Optional["CloudGcpIntegrationsFireBaseDatabase"]:
        '''fire_base_database block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#fire_base_database CloudGcpIntegrations#fire_base_database}
        '''
        result = self._values.get("fire_base_database")
        return typing.cast(typing.Optional["CloudGcpIntegrationsFireBaseDatabase"], result)

    @builtins.property
    def fire_base_hosting(
        self,
    ) -> typing.Optional["CloudGcpIntegrationsFireBaseHosting"]:
        '''fire_base_hosting block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#fire_base_hosting CloudGcpIntegrations#fire_base_hosting}
        '''
        result = self._values.get("fire_base_hosting")
        return typing.cast(typing.Optional["CloudGcpIntegrationsFireBaseHosting"], result)

    @builtins.property
    def fire_base_storage(
        self,
    ) -> typing.Optional["CloudGcpIntegrationsFireBaseStorage"]:
        '''fire_base_storage block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#fire_base_storage CloudGcpIntegrations#fire_base_storage}
        '''
        result = self._values.get("fire_base_storage")
        return typing.cast(typing.Optional["CloudGcpIntegrationsFireBaseStorage"], result)

    @builtins.property
    def fire_store(self) -> typing.Optional["CloudGcpIntegrationsFireStore"]:
        '''fire_store block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#fire_store CloudGcpIntegrations#fire_store}
        '''
        result = self._values.get("fire_store")
        return typing.cast(typing.Optional["CloudGcpIntegrationsFireStore"], result)

    @builtins.property
    def functions(self) -> typing.Optional["CloudGcpIntegrationsFunctions"]:
        '''functions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#functions CloudGcpIntegrations#functions}
        '''
        result = self._values.get("functions")
        return typing.cast(typing.Optional["CloudGcpIntegrationsFunctions"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#id CloudGcpIntegrations#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def interconnect(self) -> typing.Optional["CloudGcpIntegrationsInterconnect"]:
        '''interconnect block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#interconnect CloudGcpIntegrations#interconnect}
        '''
        result = self._values.get("interconnect")
        return typing.cast(typing.Optional["CloudGcpIntegrationsInterconnect"], result)

    @builtins.property
    def kubernetes(self) -> typing.Optional["CloudGcpIntegrationsKubernetes"]:
        '''kubernetes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#kubernetes CloudGcpIntegrations#kubernetes}
        '''
        result = self._values.get("kubernetes")
        return typing.cast(typing.Optional["CloudGcpIntegrationsKubernetes"], result)

    @builtins.property
    def load_balancing(self) -> typing.Optional["CloudGcpIntegrationsLoadBalancing"]:
        '''load_balancing block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#load_balancing CloudGcpIntegrations#load_balancing}
        '''
        result = self._values.get("load_balancing")
        return typing.cast(typing.Optional["CloudGcpIntegrationsLoadBalancing"], result)

    @builtins.property
    def mem_cache(self) -> typing.Optional["CloudGcpIntegrationsMemCache"]:
        '''mem_cache block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#mem_cache CloudGcpIntegrations#mem_cache}
        '''
        result = self._values.get("mem_cache")
        return typing.cast(typing.Optional["CloudGcpIntegrationsMemCache"], result)

    @builtins.property
    def pub_sub(self) -> typing.Optional["CloudGcpIntegrationsPubSub"]:
        '''pub_sub block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#pub_sub CloudGcpIntegrations#pub_sub}
        '''
        result = self._values.get("pub_sub")
        return typing.cast(typing.Optional["CloudGcpIntegrationsPubSub"], result)

    @builtins.property
    def redis(self) -> typing.Optional["CloudGcpIntegrationsRedis"]:
        '''redis block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#redis CloudGcpIntegrations#redis}
        '''
        result = self._values.get("redis")
        return typing.cast(typing.Optional["CloudGcpIntegrationsRedis"], result)

    @builtins.property
    def router(self) -> typing.Optional["CloudGcpIntegrationsRouter"]:
        '''router block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#router CloudGcpIntegrations#router}
        '''
        result = self._values.get("router")
        return typing.cast(typing.Optional["CloudGcpIntegrationsRouter"], result)

    @builtins.property
    def run(self) -> typing.Optional["CloudGcpIntegrationsRun"]:
        '''run block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#run CloudGcpIntegrations#run}
        '''
        result = self._values.get("run")
        return typing.cast(typing.Optional["CloudGcpIntegrationsRun"], result)

    @builtins.property
    def spanner(self) -> typing.Optional["CloudGcpIntegrationsSpanner"]:
        '''spanner block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#spanner CloudGcpIntegrations#spanner}
        '''
        result = self._values.get("spanner")
        return typing.cast(typing.Optional["CloudGcpIntegrationsSpanner"], result)

    @builtins.property
    def sql(self) -> typing.Optional["CloudGcpIntegrationsSql"]:
        '''sql block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#sql CloudGcpIntegrations#sql}
        '''
        result = self._values.get("sql")
        return typing.cast(typing.Optional["CloudGcpIntegrationsSql"], result)

    @builtins.property
    def storage(self) -> typing.Optional["CloudGcpIntegrationsStorage"]:
        '''storage block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#storage CloudGcpIntegrations#storage}
        '''
        result = self._values.get("storage")
        return typing.cast(typing.Optional["CloudGcpIntegrationsStorage"], result)

    @builtins.property
    def virtual_machines(
        self,
    ) -> typing.Optional["CloudGcpIntegrationsVirtualMachines"]:
        '''virtual_machines block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#virtual_machines CloudGcpIntegrations#virtual_machines}
        '''
        result = self._values.get("virtual_machines")
        return typing.cast(typing.Optional["CloudGcpIntegrationsVirtualMachines"], result)

    @builtins.property
    def vpc_access(self) -> typing.Optional["CloudGcpIntegrationsVpcAccess"]:
        '''vpc_access block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#vpc_access CloudGcpIntegrations#vpc_access}
        '''
        result = self._values.get("vpc_access")
        return typing.cast(typing.Optional["CloudGcpIntegrationsVpcAccess"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudGcpIntegrationsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsDataFlow",
    jsii_struct_bases=[],
    name_mapping={"metrics_polling_interval": "metricsPollingInterval"},
)
class CloudGcpIntegrationsDataFlow:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudGcpIntegrationsDataFlow.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''the data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudGcpIntegrationsDataFlow(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudGcpIntegrationsDataFlowOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsDataFlowOutputReference",
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
            type_hints = typing.get_type_hints(CloudGcpIntegrationsDataFlowOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsDataFlowOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudGcpIntegrationsDataFlow]:
        return typing.cast(typing.Optional[CloudGcpIntegrationsDataFlow], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudGcpIntegrationsDataFlow],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsDataFlowOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsDataProc",
    jsii_struct_bases=[],
    name_mapping={"metrics_polling_interval": "metricsPollingInterval"},
)
class CloudGcpIntegrationsDataProc:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudGcpIntegrationsDataProc.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''the data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudGcpIntegrationsDataProc(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudGcpIntegrationsDataProcOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsDataProcOutputReference",
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
            type_hints = typing.get_type_hints(CloudGcpIntegrationsDataProcOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsDataProcOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudGcpIntegrationsDataProc]:
        return typing.cast(typing.Optional[CloudGcpIntegrationsDataProc], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudGcpIntegrationsDataProc],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsDataProcOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsDataStore",
    jsii_struct_bases=[],
    name_mapping={"metrics_polling_interval": "metricsPollingInterval"},
)
class CloudGcpIntegrationsDataStore:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudGcpIntegrationsDataStore.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''the data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudGcpIntegrationsDataStore(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudGcpIntegrationsDataStoreOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsDataStoreOutputReference",
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
            type_hints = typing.get_type_hints(CloudGcpIntegrationsDataStoreOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsDataStoreOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudGcpIntegrationsDataStore]:
        return typing.cast(typing.Optional[CloudGcpIntegrationsDataStore], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudGcpIntegrationsDataStore],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsDataStoreOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsFireBaseDatabase",
    jsii_struct_bases=[],
    name_mapping={"metrics_polling_interval": "metricsPollingInterval"},
)
class CloudGcpIntegrationsFireBaseDatabase:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudGcpIntegrationsFireBaseDatabase.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''the data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudGcpIntegrationsFireBaseDatabase(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudGcpIntegrationsFireBaseDatabaseOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsFireBaseDatabaseOutputReference",
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
            type_hints = typing.get_type_hints(CloudGcpIntegrationsFireBaseDatabaseOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsFireBaseDatabaseOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudGcpIntegrationsFireBaseDatabase]:
        return typing.cast(typing.Optional[CloudGcpIntegrationsFireBaseDatabase], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudGcpIntegrationsFireBaseDatabase],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsFireBaseDatabaseOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsFireBaseHosting",
    jsii_struct_bases=[],
    name_mapping={"metrics_polling_interval": "metricsPollingInterval"},
)
class CloudGcpIntegrationsFireBaseHosting:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudGcpIntegrationsFireBaseHosting.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''the data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudGcpIntegrationsFireBaseHosting(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudGcpIntegrationsFireBaseHostingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsFireBaseHostingOutputReference",
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
            type_hints = typing.get_type_hints(CloudGcpIntegrationsFireBaseHostingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsFireBaseHostingOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudGcpIntegrationsFireBaseHosting]:
        return typing.cast(typing.Optional[CloudGcpIntegrationsFireBaseHosting], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudGcpIntegrationsFireBaseHosting],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsFireBaseHostingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsFireBaseStorage",
    jsii_struct_bases=[],
    name_mapping={"metrics_polling_interval": "metricsPollingInterval"},
)
class CloudGcpIntegrationsFireBaseStorage:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudGcpIntegrationsFireBaseStorage.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''the data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudGcpIntegrationsFireBaseStorage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudGcpIntegrationsFireBaseStorageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsFireBaseStorageOutputReference",
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
            type_hints = typing.get_type_hints(CloudGcpIntegrationsFireBaseStorageOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsFireBaseStorageOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudGcpIntegrationsFireBaseStorage]:
        return typing.cast(typing.Optional[CloudGcpIntegrationsFireBaseStorage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudGcpIntegrationsFireBaseStorage],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsFireBaseStorageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsFireStore",
    jsii_struct_bases=[],
    name_mapping={"metrics_polling_interval": "metricsPollingInterval"},
)
class CloudGcpIntegrationsFireStore:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudGcpIntegrationsFireStore.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''the data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudGcpIntegrationsFireStore(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudGcpIntegrationsFireStoreOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsFireStoreOutputReference",
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
            type_hints = typing.get_type_hints(CloudGcpIntegrationsFireStoreOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsFireStoreOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudGcpIntegrationsFireStore]:
        return typing.cast(typing.Optional[CloudGcpIntegrationsFireStore], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudGcpIntegrationsFireStore],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsFireStoreOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsFunctions",
    jsii_struct_bases=[],
    name_mapping={"metrics_polling_interval": "metricsPollingInterval"},
)
class CloudGcpIntegrationsFunctions:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudGcpIntegrationsFunctions.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''the data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudGcpIntegrationsFunctions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudGcpIntegrationsFunctionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsFunctionsOutputReference",
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
            type_hints = typing.get_type_hints(CloudGcpIntegrationsFunctionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsFunctionsOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudGcpIntegrationsFunctions]:
        return typing.cast(typing.Optional[CloudGcpIntegrationsFunctions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudGcpIntegrationsFunctions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsFunctionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsInterconnect",
    jsii_struct_bases=[],
    name_mapping={"metrics_polling_interval": "metricsPollingInterval"},
)
class CloudGcpIntegrationsInterconnect:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudGcpIntegrationsInterconnect.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''the data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudGcpIntegrationsInterconnect(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudGcpIntegrationsInterconnectOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsInterconnectOutputReference",
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
            type_hints = typing.get_type_hints(CloudGcpIntegrationsInterconnectOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsInterconnectOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudGcpIntegrationsInterconnect]:
        return typing.cast(typing.Optional[CloudGcpIntegrationsInterconnect], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudGcpIntegrationsInterconnect],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsInterconnectOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsKubernetes",
    jsii_struct_bases=[],
    name_mapping={"metrics_polling_interval": "metricsPollingInterval"},
)
class CloudGcpIntegrationsKubernetes:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudGcpIntegrationsKubernetes.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''the data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudGcpIntegrationsKubernetes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudGcpIntegrationsKubernetesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsKubernetesOutputReference",
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
            type_hints = typing.get_type_hints(CloudGcpIntegrationsKubernetesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsKubernetesOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudGcpIntegrationsKubernetes]:
        return typing.cast(typing.Optional[CloudGcpIntegrationsKubernetes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudGcpIntegrationsKubernetes],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsKubernetesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsLoadBalancing",
    jsii_struct_bases=[],
    name_mapping={"metrics_polling_interval": "metricsPollingInterval"},
)
class CloudGcpIntegrationsLoadBalancing:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudGcpIntegrationsLoadBalancing.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''the data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudGcpIntegrationsLoadBalancing(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudGcpIntegrationsLoadBalancingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsLoadBalancingOutputReference",
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
            type_hints = typing.get_type_hints(CloudGcpIntegrationsLoadBalancingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsLoadBalancingOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudGcpIntegrationsLoadBalancing]:
        return typing.cast(typing.Optional[CloudGcpIntegrationsLoadBalancing], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudGcpIntegrationsLoadBalancing],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsLoadBalancingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsMemCache",
    jsii_struct_bases=[],
    name_mapping={"metrics_polling_interval": "metricsPollingInterval"},
)
class CloudGcpIntegrationsMemCache:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudGcpIntegrationsMemCache.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''the data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudGcpIntegrationsMemCache(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudGcpIntegrationsMemCacheOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsMemCacheOutputReference",
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
            type_hints = typing.get_type_hints(CloudGcpIntegrationsMemCacheOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsMemCacheOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudGcpIntegrationsMemCache]:
        return typing.cast(typing.Optional[CloudGcpIntegrationsMemCache], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudGcpIntegrationsMemCache],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsMemCacheOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsPubSub",
    jsii_struct_bases=[],
    name_mapping={
        "fetch_tags": "fetchTags",
        "metrics_polling_interval": "metricsPollingInterval",
    },
)
class CloudGcpIntegrationsPubSub:
    def __init__(
        self,
        *,
        fetch_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param fetch_tags: to fetch tags of the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#fetch_tags CloudGcpIntegrations#fetch_tags}
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudGcpIntegrationsPubSub.__init__)
            check_type(argname="argument fetch_tags", value=fetch_tags, expected_type=type_hints["fetch_tags"])
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[str, typing.Any] = {}
        if fetch_tags is not None:
            self._values["fetch_tags"] = fetch_tags
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def fetch_tags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''to fetch tags of the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#fetch_tags CloudGcpIntegrations#fetch_tags}
        '''
        result = self._values.get("fetch_tags")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''the data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudGcpIntegrationsPubSub(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudGcpIntegrationsPubSubOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsPubSubOutputReference",
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
            type_hints = typing.get_type_hints(CloudGcpIntegrationsPubSubOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFetchTags")
    def reset_fetch_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFetchTags", []))

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="fetchTagsInput")
    def fetch_tags_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "fetchTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="fetchTags")
    def fetch_tags(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "fetchTags"))

    @fetch_tags.setter
    def fetch_tags(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsPubSubOutputReference, "fetch_tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fetchTags", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsPubSubOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudGcpIntegrationsPubSub]:
        return typing.cast(typing.Optional[CloudGcpIntegrationsPubSub], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudGcpIntegrationsPubSub],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsPubSubOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsRedis",
    jsii_struct_bases=[],
    name_mapping={"metrics_polling_interval": "metricsPollingInterval"},
)
class CloudGcpIntegrationsRedis:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudGcpIntegrationsRedis.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''the data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudGcpIntegrationsRedis(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudGcpIntegrationsRedisOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsRedisOutputReference",
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
            type_hints = typing.get_type_hints(CloudGcpIntegrationsRedisOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsRedisOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudGcpIntegrationsRedis]:
        return typing.cast(typing.Optional[CloudGcpIntegrationsRedis], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[CloudGcpIntegrationsRedis]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsRedisOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsRouter",
    jsii_struct_bases=[],
    name_mapping={"metrics_polling_interval": "metricsPollingInterval"},
)
class CloudGcpIntegrationsRouter:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudGcpIntegrationsRouter.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''the data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudGcpIntegrationsRouter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudGcpIntegrationsRouterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsRouterOutputReference",
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
            type_hints = typing.get_type_hints(CloudGcpIntegrationsRouterOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsRouterOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudGcpIntegrationsRouter]:
        return typing.cast(typing.Optional[CloudGcpIntegrationsRouter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudGcpIntegrationsRouter],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsRouterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsRun",
    jsii_struct_bases=[],
    name_mapping={"metrics_polling_interval": "metricsPollingInterval"},
)
class CloudGcpIntegrationsRun:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudGcpIntegrationsRun.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''the data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudGcpIntegrationsRun(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudGcpIntegrationsRunOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsRunOutputReference",
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
            type_hints = typing.get_type_hints(CloudGcpIntegrationsRunOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsRunOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudGcpIntegrationsRun]:
        return typing.cast(typing.Optional[CloudGcpIntegrationsRun], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[CloudGcpIntegrationsRun]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsRunOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsSpanner",
    jsii_struct_bases=[],
    name_mapping={
        "fetch_tags": "fetchTags",
        "metrics_polling_interval": "metricsPollingInterval",
    },
)
class CloudGcpIntegrationsSpanner:
    def __init__(
        self,
        *,
        fetch_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param fetch_tags: to fetch tags of the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#fetch_tags CloudGcpIntegrations#fetch_tags}
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudGcpIntegrationsSpanner.__init__)
            check_type(argname="argument fetch_tags", value=fetch_tags, expected_type=type_hints["fetch_tags"])
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[str, typing.Any] = {}
        if fetch_tags is not None:
            self._values["fetch_tags"] = fetch_tags
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def fetch_tags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''to fetch tags of the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#fetch_tags CloudGcpIntegrations#fetch_tags}
        '''
        result = self._values.get("fetch_tags")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''the data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudGcpIntegrationsSpanner(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudGcpIntegrationsSpannerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsSpannerOutputReference",
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
            type_hints = typing.get_type_hints(CloudGcpIntegrationsSpannerOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFetchTags")
    def reset_fetch_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFetchTags", []))

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="fetchTagsInput")
    def fetch_tags_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "fetchTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="fetchTags")
    def fetch_tags(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "fetchTags"))

    @fetch_tags.setter
    def fetch_tags(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsSpannerOutputReference, "fetch_tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fetchTags", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsSpannerOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudGcpIntegrationsSpanner]:
        return typing.cast(typing.Optional[CloudGcpIntegrationsSpanner], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudGcpIntegrationsSpanner],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsSpannerOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsSql",
    jsii_struct_bases=[],
    name_mapping={"metrics_polling_interval": "metricsPollingInterval"},
)
class CloudGcpIntegrationsSql:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudGcpIntegrationsSql.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''the data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudGcpIntegrationsSql(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudGcpIntegrationsSqlOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsSqlOutputReference",
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
            type_hints = typing.get_type_hints(CloudGcpIntegrationsSqlOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsSqlOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudGcpIntegrationsSql]:
        return typing.cast(typing.Optional[CloudGcpIntegrationsSql], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[CloudGcpIntegrationsSql]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsSqlOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsStorage",
    jsii_struct_bases=[],
    name_mapping={
        "fetch_tags": "fetchTags",
        "metrics_polling_interval": "metricsPollingInterval",
    },
)
class CloudGcpIntegrationsStorage:
    def __init__(
        self,
        *,
        fetch_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param fetch_tags: to fetch tags of the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#fetch_tags CloudGcpIntegrations#fetch_tags}
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudGcpIntegrationsStorage.__init__)
            check_type(argname="argument fetch_tags", value=fetch_tags, expected_type=type_hints["fetch_tags"])
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[str, typing.Any] = {}
        if fetch_tags is not None:
            self._values["fetch_tags"] = fetch_tags
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def fetch_tags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''to fetch tags of the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#fetch_tags CloudGcpIntegrations#fetch_tags}
        '''
        result = self._values.get("fetch_tags")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''the data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudGcpIntegrationsStorage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudGcpIntegrationsStorageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsStorageOutputReference",
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
            type_hints = typing.get_type_hints(CloudGcpIntegrationsStorageOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFetchTags")
    def reset_fetch_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFetchTags", []))

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="fetchTagsInput")
    def fetch_tags_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "fetchTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="fetchTags")
    def fetch_tags(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "fetchTags"))

    @fetch_tags.setter
    def fetch_tags(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsStorageOutputReference, "fetch_tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fetchTags", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsStorageOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudGcpIntegrationsStorage]:
        return typing.cast(typing.Optional[CloudGcpIntegrationsStorage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudGcpIntegrationsStorage],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsStorageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsVirtualMachines",
    jsii_struct_bases=[],
    name_mapping={"metrics_polling_interval": "metricsPollingInterval"},
)
class CloudGcpIntegrationsVirtualMachines:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudGcpIntegrationsVirtualMachines.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''the data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudGcpIntegrationsVirtualMachines(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudGcpIntegrationsVirtualMachinesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsVirtualMachinesOutputReference",
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
            type_hints = typing.get_type_hints(CloudGcpIntegrationsVirtualMachinesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsVirtualMachinesOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudGcpIntegrationsVirtualMachines]:
        return typing.cast(typing.Optional[CloudGcpIntegrationsVirtualMachines], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudGcpIntegrationsVirtualMachines],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsVirtualMachinesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsVpcAccess",
    jsii_struct_bases=[],
    name_mapping={"metrics_polling_interval": "metricsPollingInterval"},
)
class CloudGcpIntegrationsVpcAccess:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: the data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudGcpIntegrationsVpcAccess.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''the data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_gcp_integrations#metrics_polling_interval CloudGcpIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudGcpIntegrationsVpcAccess(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudGcpIntegrationsVpcAccessOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudGcpIntegrations.CloudGcpIntegrationsVpcAccessOutputReference",
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
            type_hints = typing.get_type_hints(CloudGcpIntegrationsVpcAccessOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsVpcAccessOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudGcpIntegrationsVpcAccess]:
        return typing.cast(typing.Optional[CloudGcpIntegrationsVpcAccess], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudGcpIntegrationsVpcAccess],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudGcpIntegrationsVpcAccessOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CloudGcpIntegrations",
    "CloudGcpIntegrationsAppEngine",
    "CloudGcpIntegrationsAppEngineOutputReference",
    "CloudGcpIntegrationsBigQuery",
    "CloudGcpIntegrationsBigQueryOutputReference",
    "CloudGcpIntegrationsBigTable",
    "CloudGcpIntegrationsBigTableOutputReference",
    "CloudGcpIntegrationsComposer",
    "CloudGcpIntegrationsComposerOutputReference",
    "CloudGcpIntegrationsConfig",
    "CloudGcpIntegrationsDataFlow",
    "CloudGcpIntegrationsDataFlowOutputReference",
    "CloudGcpIntegrationsDataProc",
    "CloudGcpIntegrationsDataProcOutputReference",
    "CloudGcpIntegrationsDataStore",
    "CloudGcpIntegrationsDataStoreOutputReference",
    "CloudGcpIntegrationsFireBaseDatabase",
    "CloudGcpIntegrationsFireBaseDatabaseOutputReference",
    "CloudGcpIntegrationsFireBaseHosting",
    "CloudGcpIntegrationsFireBaseHostingOutputReference",
    "CloudGcpIntegrationsFireBaseStorage",
    "CloudGcpIntegrationsFireBaseStorageOutputReference",
    "CloudGcpIntegrationsFireStore",
    "CloudGcpIntegrationsFireStoreOutputReference",
    "CloudGcpIntegrationsFunctions",
    "CloudGcpIntegrationsFunctionsOutputReference",
    "CloudGcpIntegrationsInterconnect",
    "CloudGcpIntegrationsInterconnectOutputReference",
    "CloudGcpIntegrationsKubernetes",
    "CloudGcpIntegrationsKubernetesOutputReference",
    "CloudGcpIntegrationsLoadBalancing",
    "CloudGcpIntegrationsLoadBalancingOutputReference",
    "CloudGcpIntegrationsMemCache",
    "CloudGcpIntegrationsMemCacheOutputReference",
    "CloudGcpIntegrationsPubSub",
    "CloudGcpIntegrationsPubSubOutputReference",
    "CloudGcpIntegrationsRedis",
    "CloudGcpIntegrationsRedisOutputReference",
    "CloudGcpIntegrationsRouter",
    "CloudGcpIntegrationsRouterOutputReference",
    "CloudGcpIntegrationsRun",
    "CloudGcpIntegrationsRunOutputReference",
    "CloudGcpIntegrationsSpanner",
    "CloudGcpIntegrationsSpannerOutputReference",
    "CloudGcpIntegrationsSql",
    "CloudGcpIntegrationsSqlOutputReference",
    "CloudGcpIntegrationsStorage",
    "CloudGcpIntegrationsStorageOutputReference",
    "CloudGcpIntegrationsVirtualMachines",
    "CloudGcpIntegrationsVirtualMachinesOutputReference",
    "CloudGcpIntegrationsVpcAccess",
    "CloudGcpIntegrationsVpcAccessOutputReference",
]

publication.publish()
