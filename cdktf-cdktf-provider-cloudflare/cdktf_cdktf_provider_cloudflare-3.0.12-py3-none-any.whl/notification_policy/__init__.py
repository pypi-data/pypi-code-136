'''
# `cloudflare_notification_policy`

Refer to the Terraform Registory for docs: [`cloudflare_notification_policy`](https://www.terraform.io/docs/providers/cloudflare/r/notification_policy).
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


class NotificationPolicy(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.notificationPolicy.NotificationPolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy cloudflare_notification_policy}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        account_id: builtins.str,
        alert_type: builtins.str,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        email_integration: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["NotificationPolicyEmailIntegration", typing.Dict[str, typing.Any]]]]] = None,
        filters: typing.Optional[typing.Union["NotificationPolicyFilters", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        pagerduty_integration: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["NotificationPolicyPagerdutyIntegration", typing.Dict[str, typing.Any]]]]] = None,
        webhooks_integration: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["NotificationPolicyWebhooksIntegration", typing.Dict[str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy cloudflare_notification_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param account_id: The account identifier to target for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#account_id NotificationPolicy#account_id}
        :param alert_type: The event type that will trigger the dispatch of a notification. See the developer documentation for descriptions of `available alert types <https://developers.cloudflare.com/fundamentals/notifications/notification-available/>`_. Available values: ``billing_usage_alert``, ``health_check_status_notification``, ``g6_pool_toggle_alert``, ``real_origin_monitoring``, ``universal_ssl_event_type``, ``dedicated_ssl_certificate_event_type``, ``custom_ssl_certificate_event_type``, ``access_custom_certificate_expiration_type``, ``zone_aop_custom_certificate_expiration_type``, ``bgp_hijack_notification``, ``http_alert_origin_error``, ``workers_alert``, ``weekly_account_overview``, ``expiring_service_token_alert``, ``secondary_dns_all_primaries_failing``, ``secondary_dns_zone_validation_warning``, ``secondary_dns_primaries_failing``, ``secondary_dns_zone_successfully_updated``, ``dos_attack_l7``, ``dos_attack_l4``, ``advanced_ddos_attack_l7_alert``, ``advanced_ddos_attack_l4_alert``, ``fbm_volumetric_attack``, ``fbm_auto_advertisement``, ``load_balancing_pool_enablement_alert``, ``load_balancing_health_alert``, ``g6_health_alert``, ``http_alert_edge_error``, ``clickhouse_alert_fw_anomaly``, ``clickhouse_alert_fw_ent_anomaly``, ``failing_logpush_job_disabled_alert``, ``scriptmonitor_alert_new_hosts``, ``scriptmonitor_alert_new_scripts``, ``scriptmonitor_alert_new_malicious_scripts``, ``scriptmonitor_alert_new_malicious_url``, ``scriptmonitor_alert_new_code_change_detections``, ``scriptmonitor_alert_new_max_length_script_url``, ``scriptmonitor_alert_new_malicious_hosts``, ``sentinel_alert``, ``hostname_aop_custom_certificate_expiration_type``, ``stream_live_notifications``, ``block_notification_new_block``, ``block_notification_review_rejected``, ``block_notification_review_accepted``, ``web_analytics_metrics_update``, ``workers_uptime``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#alert_type NotificationPolicy#alert_type}
        :param enabled: The status of the notification policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#enabled NotificationPolicy#enabled}
        :param name: The name of the notification policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#name NotificationPolicy#name}
        :param description: Description of the notification policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#description NotificationPolicy#description}
        :param email_integration: email_integration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#email_integration NotificationPolicy#email_integration}
        :param filters: filters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#filters NotificationPolicy#filters}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#id NotificationPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param pagerduty_integration: pagerduty_integration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#pagerduty_integration NotificationPolicy#pagerduty_integration}
        :param webhooks_integration: webhooks_integration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#webhooks_integration NotificationPolicy#webhooks_integration}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NotificationPolicy.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = NotificationPolicyConfig(
            account_id=account_id,
            alert_type=alert_type,
            enabled=enabled,
            name=name,
            description=description,
            email_integration=email_integration,
            filters=filters,
            id=id,
            pagerduty_integration=pagerduty_integration,
            webhooks_integration=webhooks_integration,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putEmailIntegration")
    def put_email_integration(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["NotificationPolicyEmailIntegration", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NotificationPolicy.put_email_integration)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEmailIntegration", [value]))

    @jsii.member(jsii_name="putFilters")
    def put_filters(
        self,
        *,
        enabled: typing.Optional[typing.Sequence[builtins.str]] = None,
        event_source: typing.Optional[typing.Sequence[builtins.str]] = None,
        event_type: typing.Optional[typing.Sequence[builtins.str]] = None,
        health_check_id: typing.Optional[typing.Sequence[builtins.str]] = None,
        input_id: typing.Optional[typing.Sequence[builtins.str]] = None,
        limit: typing.Optional[typing.Sequence[builtins.str]] = None,
        new_health: typing.Optional[typing.Sequence[builtins.str]] = None,
        packets_per_second: typing.Optional[typing.Sequence[builtins.str]] = None,
        pool_id: typing.Optional[typing.Sequence[builtins.str]] = None,
        product: typing.Optional[typing.Sequence[builtins.str]] = None,
        protocol: typing.Optional[typing.Sequence[builtins.str]] = None,
        requests_per_second: typing.Optional[typing.Sequence[builtins.str]] = None,
        services: typing.Optional[typing.Sequence[builtins.str]] = None,
        slo: typing.Optional[typing.Sequence[builtins.str]] = None,
        status: typing.Optional[typing.Sequence[builtins.str]] = None,
        target_host: typing.Optional[typing.Sequence[builtins.str]] = None,
        target_zone_name: typing.Optional[typing.Sequence[builtins.str]] = None,
        zones: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param enabled: State of the pool to alert on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#enabled NotificationPolicy#enabled}
        :param event_source: Source configuration to alert on for pool or origin. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#event_source NotificationPolicy#event_source}
        :param event_type: Stream event type to alert on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#event_type NotificationPolicy#event_type}
        :param health_check_id: Identifier health check. Required when using ``filters.0.status``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#health_check_id NotificationPolicy#health_check_id}
        :param input_id: Stream input id to alert on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#input_id NotificationPolicy#input_id}
        :param limit: A numerical limit. Example: ``100``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#limit NotificationPolicy#limit}
        :param new_health: Health status to alert on for pool or origin. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#new_health NotificationPolicy#new_health}
        :param packets_per_second: Packets per second threshold for dos alert. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#packets_per_second NotificationPolicy#packets_per_second}
        :param pool_id: Load balancer pool identifier. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#pool_id NotificationPolicy#pool_id}
        :param product: Product name. Available values: ``worker_requests``, ``worker_durable_objects_requests``, ``worker_durable_objects_duration``, ``worker_durable_objects_data_transfer``, ``worker_durable_objects_stored_data``, ``worker_durable_objects_storage_deletes``, ``worker_durable_objects_storage_writes``, ``worker_durable_objects_storage_reads``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#product NotificationPolicy#product}
        :param protocol: Protocol to alert on for dos. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#protocol NotificationPolicy#protocol}
        :param requests_per_second: Requests per second threshold for dos alert. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#requests_per_second NotificationPolicy#requests_per_second}
        :param services: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#services NotificationPolicy#services}.
        :param slo: A numerical limit. Example: ``99.9``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#slo NotificationPolicy#slo}
        :param status: Status to alert on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#status NotificationPolicy#status}
        :param target_host: Target host to alert on for dos. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#target_host NotificationPolicy#target_host}
        :param target_zone_name: Target domain to alert on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#target_zone_name NotificationPolicy#target_zone_name}
        :param zones: A list of zone identifiers. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#zones NotificationPolicy#zones}
        '''
        value = NotificationPolicyFilters(
            enabled=enabled,
            event_source=event_source,
            event_type=event_type,
            health_check_id=health_check_id,
            input_id=input_id,
            limit=limit,
            new_health=new_health,
            packets_per_second=packets_per_second,
            pool_id=pool_id,
            product=product,
            protocol=protocol,
            requests_per_second=requests_per_second,
            services=services,
            slo=slo,
            status=status,
            target_host=target_host,
            target_zone_name=target_zone_name,
            zones=zones,
        )

        return typing.cast(None, jsii.invoke(self, "putFilters", [value]))

    @jsii.member(jsii_name="putPagerdutyIntegration")
    def put_pagerduty_integration(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["NotificationPolicyPagerdutyIntegration", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NotificationPolicy.put_pagerduty_integration)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPagerdutyIntegration", [value]))

    @jsii.member(jsii_name="putWebhooksIntegration")
    def put_webhooks_integration(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["NotificationPolicyWebhooksIntegration", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NotificationPolicy.put_webhooks_integration)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWebhooksIntegration", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEmailIntegration")
    def reset_email_integration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailIntegration", []))

    @jsii.member(jsii_name="resetFilters")
    def reset_filters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilters", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPagerdutyIntegration")
    def reset_pagerduty_integration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPagerdutyIntegration", []))

    @jsii.member(jsii_name="resetWebhooksIntegration")
    def reset_webhooks_integration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWebhooksIntegration", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="created")
    def created(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "created"))

    @builtins.property
    @jsii.member(jsii_name="emailIntegration")
    def email_integration(self) -> "NotificationPolicyEmailIntegrationList":
        return typing.cast("NotificationPolicyEmailIntegrationList", jsii.get(self, "emailIntegration"))

    @builtins.property
    @jsii.member(jsii_name="filters")
    def filters(self) -> "NotificationPolicyFiltersOutputReference":
        return typing.cast("NotificationPolicyFiltersOutputReference", jsii.get(self, "filters"))

    @builtins.property
    @jsii.member(jsii_name="modified")
    def modified(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "modified"))

    @builtins.property
    @jsii.member(jsii_name="pagerdutyIntegration")
    def pagerduty_integration(self) -> "NotificationPolicyPagerdutyIntegrationList":
        return typing.cast("NotificationPolicyPagerdutyIntegrationList", jsii.get(self, "pagerdutyIntegration"))

    @builtins.property
    @jsii.member(jsii_name="webhooksIntegration")
    def webhooks_integration(self) -> "NotificationPolicyWebhooksIntegrationList":
        return typing.cast("NotificationPolicyWebhooksIntegrationList", jsii.get(self, "webhooksIntegration"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="alertTypeInput")
    def alert_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alertTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="emailIntegrationInput")
    def email_integration_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NotificationPolicyEmailIntegration"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NotificationPolicyEmailIntegration"]]], jsii.get(self, "emailIntegrationInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="filtersInput")
    def filters_input(self) -> typing.Optional["NotificationPolicyFilters"]:
        return typing.cast(typing.Optional["NotificationPolicyFilters"], jsii.get(self, "filtersInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="pagerdutyIntegrationInput")
    def pagerduty_integration_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NotificationPolicyPagerdutyIntegration"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NotificationPolicyPagerdutyIntegration"]]], jsii.get(self, "pagerdutyIntegrationInput"))

    @builtins.property
    @jsii.member(jsii_name="webhooksIntegrationInput")
    def webhooks_integration_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NotificationPolicyWebhooksIntegration"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NotificationPolicyWebhooksIntegration"]]], jsii.get(self, "webhooksIntegrationInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationPolicy, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="alertType")
    def alert_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "alertType"))

    @alert_type.setter
    def alert_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationPolicy, "alert_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alertType", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationPolicy, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationPolicy, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationPolicy, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationPolicy, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.notificationPolicy.NotificationPolicyConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "account_id": "accountId",
        "alert_type": "alertType",
        "enabled": "enabled",
        "name": "name",
        "description": "description",
        "email_integration": "emailIntegration",
        "filters": "filters",
        "id": "id",
        "pagerduty_integration": "pagerdutyIntegration",
        "webhooks_integration": "webhooksIntegration",
    },
)
class NotificationPolicyConfig(cdktf.TerraformMetaArguments):
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
        account_id: builtins.str,
        alert_type: builtins.str,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        email_integration: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["NotificationPolicyEmailIntegration", typing.Dict[str, typing.Any]]]]] = None,
        filters: typing.Optional[typing.Union["NotificationPolicyFilters", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        pagerduty_integration: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["NotificationPolicyPagerdutyIntegration", typing.Dict[str, typing.Any]]]]] = None,
        webhooks_integration: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["NotificationPolicyWebhooksIntegration", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param account_id: The account identifier to target for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#account_id NotificationPolicy#account_id}
        :param alert_type: The event type that will trigger the dispatch of a notification. See the developer documentation for descriptions of `available alert types <https://developers.cloudflare.com/fundamentals/notifications/notification-available/>`_. Available values: ``billing_usage_alert``, ``health_check_status_notification``, ``g6_pool_toggle_alert``, ``real_origin_monitoring``, ``universal_ssl_event_type``, ``dedicated_ssl_certificate_event_type``, ``custom_ssl_certificate_event_type``, ``access_custom_certificate_expiration_type``, ``zone_aop_custom_certificate_expiration_type``, ``bgp_hijack_notification``, ``http_alert_origin_error``, ``workers_alert``, ``weekly_account_overview``, ``expiring_service_token_alert``, ``secondary_dns_all_primaries_failing``, ``secondary_dns_zone_validation_warning``, ``secondary_dns_primaries_failing``, ``secondary_dns_zone_successfully_updated``, ``dos_attack_l7``, ``dos_attack_l4``, ``advanced_ddos_attack_l7_alert``, ``advanced_ddos_attack_l4_alert``, ``fbm_volumetric_attack``, ``fbm_auto_advertisement``, ``load_balancing_pool_enablement_alert``, ``load_balancing_health_alert``, ``g6_health_alert``, ``http_alert_edge_error``, ``clickhouse_alert_fw_anomaly``, ``clickhouse_alert_fw_ent_anomaly``, ``failing_logpush_job_disabled_alert``, ``scriptmonitor_alert_new_hosts``, ``scriptmonitor_alert_new_scripts``, ``scriptmonitor_alert_new_malicious_scripts``, ``scriptmonitor_alert_new_malicious_url``, ``scriptmonitor_alert_new_code_change_detections``, ``scriptmonitor_alert_new_max_length_script_url``, ``scriptmonitor_alert_new_malicious_hosts``, ``sentinel_alert``, ``hostname_aop_custom_certificate_expiration_type``, ``stream_live_notifications``, ``block_notification_new_block``, ``block_notification_review_rejected``, ``block_notification_review_accepted``, ``web_analytics_metrics_update``, ``workers_uptime``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#alert_type NotificationPolicy#alert_type}
        :param enabled: The status of the notification policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#enabled NotificationPolicy#enabled}
        :param name: The name of the notification policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#name NotificationPolicy#name}
        :param description: Description of the notification policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#description NotificationPolicy#description}
        :param email_integration: email_integration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#email_integration NotificationPolicy#email_integration}
        :param filters: filters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#filters NotificationPolicy#filters}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#id NotificationPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param pagerduty_integration: pagerduty_integration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#pagerduty_integration NotificationPolicy#pagerduty_integration}
        :param webhooks_integration: webhooks_integration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#webhooks_integration NotificationPolicy#webhooks_integration}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(filters, dict):
            filters = NotificationPolicyFilters(**filters)
        if __debug__:
            type_hints = typing.get_type_hints(NotificationPolicyConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument alert_type", value=alert_type, expected_type=type_hints["alert_type"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument email_integration", value=email_integration, expected_type=type_hints["email_integration"])
            check_type(argname="argument filters", value=filters, expected_type=type_hints["filters"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument pagerduty_integration", value=pagerduty_integration, expected_type=type_hints["pagerduty_integration"])
            check_type(argname="argument webhooks_integration", value=webhooks_integration, expected_type=type_hints["webhooks_integration"])
        self._values: typing.Dict[str, typing.Any] = {
            "account_id": account_id,
            "alert_type": alert_type,
            "enabled": enabled,
            "name": name,
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
        if description is not None:
            self._values["description"] = description
        if email_integration is not None:
            self._values["email_integration"] = email_integration
        if filters is not None:
            self._values["filters"] = filters
        if id is not None:
            self._values["id"] = id
        if pagerduty_integration is not None:
            self._values["pagerduty_integration"] = pagerduty_integration
        if webhooks_integration is not None:
            self._values["webhooks_integration"] = webhooks_integration

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
    def account_id(self) -> builtins.str:
        '''The account identifier to target for the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#account_id NotificationPolicy#account_id}
        '''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alert_type(self) -> builtins.str:
        '''The event type that will trigger the dispatch of a notification.

        See the developer documentation for descriptions of `available alert types <https://developers.cloudflare.com/fundamentals/notifications/notification-available/>`_. Available values: ``billing_usage_alert``, ``health_check_status_notification``, ``g6_pool_toggle_alert``, ``real_origin_monitoring``, ``universal_ssl_event_type``, ``dedicated_ssl_certificate_event_type``, ``custom_ssl_certificate_event_type``, ``access_custom_certificate_expiration_type``, ``zone_aop_custom_certificate_expiration_type``, ``bgp_hijack_notification``, ``http_alert_origin_error``, ``workers_alert``, ``weekly_account_overview``, ``expiring_service_token_alert``, ``secondary_dns_all_primaries_failing``, ``secondary_dns_zone_validation_warning``, ``secondary_dns_primaries_failing``, ``secondary_dns_zone_successfully_updated``, ``dos_attack_l7``, ``dos_attack_l4``, ``advanced_ddos_attack_l7_alert``, ``advanced_ddos_attack_l4_alert``, ``fbm_volumetric_attack``, ``fbm_auto_advertisement``, ``load_balancing_pool_enablement_alert``, ``load_balancing_health_alert``, ``g6_health_alert``, ``http_alert_edge_error``, ``clickhouse_alert_fw_anomaly``, ``clickhouse_alert_fw_ent_anomaly``, ``failing_logpush_job_disabled_alert``, ``scriptmonitor_alert_new_hosts``, ``scriptmonitor_alert_new_scripts``, ``scriptmonitor_alert_new_malicious_scripts``, ``scriptmonitor_alert_new_malicious_url``, ``scriptmonitor_alert_new_code_change_detections``, ``scriptmonitor_alert_new_max_length_script_url``, ``scriptmonitor_alert_new_malicious_hosts``, ``sentinel_alert``, ``hostname_aop_custom_certificate_expiration_type``, ``stream_live_notifications``, ``block_notification_new_block``, ``block_notification_review_rejected``, ``block_notification_review_accepted``, ``web_analytics_metrics_update``, ``workers_uptime``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#alert_type NotificationPolicy#alert_type}
        '''
        result = self._values.get("alert_type")
        assert result is not None, "Required property 'alert_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''The status of the notification policy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#enabled NotificationPolicy#enabled}
        '''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the notification policy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#name NotificationPolicy#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of the notification policy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#description NotificationPolicy#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def email_integration(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NotificationPolicyEmailIntegration"]]]:
        '''email_integration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#email_integration NotificationPolicy#email_integration}
        '''
        result = self._values.get("email_integration")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NotificationPolicyEmailIntegration"]]], result)

    @builtins.property
    def filters(self) -> typing.Optional["NotificationPolicyFilters"]:
        '''filters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#filters NotificationPolicy#filters}
        '''
        result = self._values.get("filters")
        return typing.cast(typing.Optional["NotificationPolicyFilters"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#id NotificationPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pagerduty_integration(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NotificationPolicyPagerdutyIntegration"]]]:
        '''pagerduty_integration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#pagerduty_integration NotificationPolicy#pagerduty_integration}
        '''
        result = self._values.get("pagerduty_integration")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NotificationPolicyPagerdutyIntegration"]]], result)

    @builtins.property
    def webhooks_integration(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NotificationPolicyWebhooksIntegration"]]]:
        '''webhooks_integration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#webhooks_integration NotificationPolicy#webhooks_integration}
        '''
        result = self._values.get("webhooks_integration")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NotificationPolicyWebhooksIntegration"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NotificationPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.notificationPolicy.NotificationPolicyEmailIntegration",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class NotificationPolicyEmailIntegration:
    def __init__(
        self,
        *,
        id: builtins.str,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#id NotificationPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#name NotificationPolicy#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NotificationPolicyEmailIntegration.__init__)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "id": id,
        }
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#id NotificationPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#name NotificationPolicy#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NotificationPolicyEmailIntegration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NotificationPolicyEmailIntegrationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.notificationPolicy.NotificationPolicyEmailIntegrationList",
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
            type_hints = typing.get_type_hints(NotificationPolicyEmailIntegrationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "NotificationPolicyEmailIntegrationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NotificationPolicyEmailIntegrationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("NotificationPolicyEmailIntegrationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationPolicyEmailIntegrationList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(NotificationPolicyEmailIntegrationList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(NotificationPolicyEmailIntegrationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NotificationPolicyEmailIntegration]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NotificationPolicyEmailIntegration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NotificationPolicyEmailIntegration]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationPolicyEmailIntegrationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NotificationPolicyEmailIntegrationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.notificationPolicy.NotificationPolicyEmailIntegrationOutputReference",
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
            type_hints = typing.get_type_hints(NotificationPolicyEmailIntegrationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationPolicyEmailIntegrationOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationPolicyEmailIntegrationOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[NotificationPolicyEmailIntegration, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[NotificationPolicyEmailIntegration, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[NotificationPolicyEmailIntegration, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationPolicyEmailIntegrationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.notificationPolicy.NotificationPolicyFilters",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "event_source": "eventSource",
        "event_type": "eventType",
        "health_check_id": "healthCheckId",
        "input_id": "inputId",
        "limit": "limit",
        "new_health": "newHealth",
        "packets_per_second": "packetsPerSecond",
        "pool_id": "poolId",
        "product": "product",
        "protocol": "protocol",
        "requests_per_second": "requestsPerSecond",
        "services": "services",
        "slo": "slo",
        "status": "status",
        "target_host": "targetHost",
        "target_zone_name": "targetZoneName",
        "zones": "zones",
    },
)
class NotificationPolicyFilters:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Sequence[builtins.str]] = None,
        event_source: typing.Optional[typing.Sequence[builtins.str]] = None,
        event_type: typing.Optional[typing.Sequence[builtins.str]] = None,
        health_check_id: typing.Optional[typing.Sequence[builtins.str]] = None,
        input_id: typing.Optional[typing.Sequence[builtins.str]] = None,
        limit: typing.Optional[typing.Sequence[builtins.str]] = None,
        new_health: typing.Optional[typing.Sequence[builtins.str]] = None,
        packets_per_second: typing.Optional[typing.Sequence[builtins.str]] = None,
        pool_id: typing.Optional[typing.Sequence[builtins.str]] = None,
        product: typing.Optional[typing.Sequence[builtins.str]] = None,
        protocol: typing.Optional[typing.Sequence[builtins.str]] = None,
        requests_per_second: typing.Optional[typing.Sequence[builtins.str]] = None,
        services: typing.Optional[typing.Sequence[builtins.str]] = None,
        slo: typing.Optional[typing.Sequence[builtins.str]] = None,
        status: typing.Optional[typing.Sequence[builtins.str]] = None,
        target_host: typing.Optional[typing.Sequence[builtins.str]] = None,
        target_zone_name: typing.Optional[typing.Sequence[builtins.str]] = None,
        zones: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param enabled: State of the pool to alert on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#enabled NotificationPolicy#enabled}
        :param event_source: Source configuration to alert on for pool or origin. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#event_source NotificationPolicy#event_source}
        :param event_type: Stream event type to alert on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#event_type NotificationPolicy#event_type}
        :param health_check_id: Identifier health check. Required when using ``filters.0.status``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#health_check_id NotificationPolicy#health_check_id}
        :param input_id: Stream input id to alert on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#input_id NotificationPolicy#input_id}
        :param limit: A numerical limit. Example: ``100``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#limit NotificationPolicy#limit}
        :param new_health: Health status to alert on for pool or origin. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#new_health NotificationPolicy#new_health}
        :param packets_per_second: Packets per second threshold for dos alert. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#packets_per_second NotificationPolicy#packets_per_second}
        :param pool_id: Load balancer pool identifier. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#pool_id NotificationPolicy#pool_id}
        :param product: Product name. Available values: ``worker_requests``, ``worker_durable_objects_requests``, ``worker_durable_objects_duration``, ``worker_durable_objects_data_transfer``, ``worker_durable_objects_stored_data``, ``worker_durable_objects_storage_deletes``, ``worker_durable_objects_storage_writes``, ``worker_durable_objects_storage_reads``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#product NotificationPolicy#product}
        :param protocol: Protocol to alert on for dos. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#protocol NotificationPolicy#protocol}
        :param requests_per_second: Requests per second threshold for dos alert. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#requests_per_second NotificationPolicy#requests_per_second}
        :param services: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#services NotificationPolicy#services}.
        :param slo: A numerical limit. Example: ``99.9``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#slo NotificationPolicy#slo}
        :param status: Status to alert on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#status NotificationPolicy#status}
        :param target_host: Target host to alert on for dos. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#target_host NotificationPolicy#target_host}
        :param target_zone_name: Target domain to alert on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#target_zone_name NotificationPolicy#target_zone_name}
        :param zones: A list of zone identifiers. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#zones NotificationPolicy#zones}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NotificationPolicyFilters.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument event_source", value=event_source, expected_type=type_hints["event_source"])
            check_type(argname="argument event_type", value=event_type, expected_type=type_hints["event_type"])
            check_type(argname="argument health_check_id", value=health_check_id, expected_type=type_hints["health_check_id"])
            check_type(argname="argument input_id", value=input_id, expected_type=type_hints["input_id"])
            check_type(argname="argument limit", value=limit, expected_type=type_hints["limit"])
            check_type(argname="argument new_health", value=new_health, expected_type=type_hints["new_health"])
            check_type(argname="argument packets_per_second", value=packets_per_second, expected_type=type_hints["packets_per_second"])
            check_type(argname="argument pool_id", value=pool_id, expected_type=type_hints["pool_id"])
            check_type(argname="argument product", value=product, expected_type=type_hints["product"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument requests_per_second", value=requests_per_second, expected_type=type_hints["requests_per_second"])
            check_type(argname="argument services", value=services, expected_type=type_hints["services"])
            check_type(argname="argument slo", value=slo, expected_type=type_hints["slo"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument target_host", value=target_host, expected_type=type_hints["target_host"])
            check_type(argname="argument target_zone_name", value=target_zone_name, expected_type=type_hints["target_zone_name"])
            check_type(argname="argument zones", value=zones, expected_type=type_hints["zones"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if event_source is not None:
            self._values["event_source"] = event_source
        if event_type is not None:
            self._values["event_type"] = event_type
        if health_check_id is not None:
            self._values["health_check_id"] = health_check_id
        if input_id is not None:
            self._values["input_id"] = input_id
        if limit is not None:
            self._values["limit"] = limit
        if new_health is not None:
            self._values["new_health"] = new_health
        if packets_per_second is not None:
            self._values["packets_per_second"] = packets_per_second
        if pool_id is not None:
            self._values["pool_id"] = pool_id
        if product is not None:
            self._values["product"] = product
        if protocol is not None:
            self._values["protocol"] = protocol
        if requests_per_second is not None:
            self._values["requests_per_second"] = requests_per_second
        if services is not None:
            self._values["services"] = services
        if slo is not None:
            self._values["slo"] = slo
        if status is not None:
            self._values["status"] = status
        if target_host is not None:
            self._values["target_host"] = target_host
        if target_zone_name is not None:
            self._values["target_zone_name"] = target_zone_name
        if zones is not None:
            self._values["zones"] = zones

    @builtins.property
    def enabled(self) -> typing.Optional[typing.List[builtins.str]]:
        '''State of the pool to alert on.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#enabled NotificationPolicy#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def event_source(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Source configuration to alert on for pool or origin.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#event_source NotificationPolicy#event_source}
        '''
        result = self._values.get("event_source")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def event_type(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Stream event type to alert on.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#event_type NotificationPolicy#event_type}
        '''
        result = self._values.get("event_type")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def health_check_id(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Identifier health check. Required when using ``filters.0.status``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#health_check_id NotificationPolicy#health_check_id}
        '''
        result = self._values.get("health_check_id")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def input_id(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Stream input id to alert on.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#input_id NotificationPolicy#input_id}
        '''
        result = self._values.get("input_id")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def limit(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A numerical limit. Example: ``100``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#limit NotificationPolicy#limit}
        '''
        result = self._values.get("limit")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def new_health(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Health status to alert on for pool or origin.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#new_health NotificationPolicy#new_health}
        '''
        result = self._values.get("new_health")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def packets_per_second(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Packets per second threshold for dos alert.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#packets_per_second NotificationPolicy#packets_per_second}
        '''
        result = self._values.get("packets_per_second")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def pool_id(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Load balancer pool identifier.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#pool_id NotificationPolicy#pool_id}
        '''
        result = self._values.get("pool_id")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def product(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Product name. Available values: ``worker_requests``, ``worker_durable_objects_requests``, ``worker_durable_objects_duration``, ``worker_durable_objects_data_transfer``, ``worker_durable_objects_stored_data``, ``worker_durable_objects_storage_deletes``, ``worker_durable_objects_storage_writes``, ``worker_durable_objects_storage_reads``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#product NotificationPolicy#product}
        '''
        result = self._values.get("product")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def protocol(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Protocol to alert on for dos.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#protocol NotificationPolicy#protocol}
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def requests_per_second(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Requests per second threshold for dos alert.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#requests_per_second NotificationPolicy#requests_per_second}
        '''
        result = self._values.get("requests_per_second")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def services(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#services NotificationPolicy#services}.'''
        result = self._values.get("services")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def slo(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A numerical limit. Example: ``99.9``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#slo NotificationPolicy#slo}
        '''
        result = self._values.get("slo")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def status(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Status to alert on.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#status NotificationPolicy#status}
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def target_host(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Target host to alert on for dos.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#target_host NotificationPolicy#target_host}
        '''
        result = self._values.get("target_host")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def target_zone_name(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Target domain to alert on.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#target_zone_name NotificationPolicy#target_zone_name}
        '''
        result = self._values.get("target_zone_name")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def zones(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of zone identifiers.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#zones NotificationPolicy#zones}
        '''
        result = self._values.get("zones")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NotificationPolicyFilters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NotificationPolicyFiltersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.notificationPolicy.NotificationPolicyFiltersOutputReference",
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
            type_hints = typing.get_type_hints(NotificationPolicyFiltersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetEventSource")
    def reset_event_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventSource", []))

    @jsii.member(jsii_name="resetEventType")
    def reset_event_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventType", []))

    @jsii.member(jsii_name="resetHealthCheckId")
    def reset_health_check_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheckId", []))

    @jsii.member(jsii_name="resetInputId")
    def reset_input_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInputId", []))

    @jsii.member(jsii_name="resetLimit")
    def reset_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLimit", []))

    @jsii.member(jsii_name="resetNewHealth")
    def reset_new_health(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNewHealth", []))

    @jsii.member(jsii_name="resetPacketsPerSecond")
    def reset_packets_per_second(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPacketsPerSecond", []))

    @jsii.member(jsii_name="resetPoolId")
    def reset_pool_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPoolId", []))

    @jsii.member(jsii_name="resetProduct")
    def reset_product(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProduct", []))

    @jsii.member(jsii_name="resetProtocol")
    def reset_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtocol", []))

    @jsii.member(jsii_name="resetRequestsPerSecond")
    def reset_requests_per_second(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestsPerSecond", []))

    @jsii.member(jsii_name="resetServices")
    def reset_services(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServices", []))

    @jsii.member(jsii_name="resetSlo")
    def reset_slo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSlo", []))

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

    @jsii.member(jsii_name="resetTargetHost")
    def reset_target_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetHost", []))

    @jsii.member(jsii_name="resetTargetZoneName")
    def reset_target_zone_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetZoneName", []))

    @jsii.member(jsii_name="resetZones")
    def reset_zones(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZones", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="eventSourceInput")
    def event_source_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "eventSourceInput"))

    @builtins.property
    @jsii.member(jsii_name="eventTypeInput")
    def event_type_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "eventTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckIdInput")
    def health_check_id_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "healthCheckIdInput"))

    @builtins.property
    @jsii.member(jsii_name="inputIdInput")
    def input_id_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "inputIdInput"))

    @builtins.property
    @jsii.member(jsii_name="limitInput")
    def limit_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "limitInput"))

    @builtins.property
    @jsii.member(jsii_name="newHealthInput")
    def new_health_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "newHealthInput"))

    @builtins.property
    @jsii.member(jsii_name="packetsPerSecondInput")
    def packets_per_second_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "packetsPerSecondInput"))

    @builtins.property
    @jsii.member(jsii_name="poolIdInput")
    def pool_id_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "poolIdInput"))

    @builtins.property
    @jsii.member(jsii_name="productInput")
    def product_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "productInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="requestsPerSecondInput")
    def requests_per_second_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "requestsPerSecondInput"))

    @builtins.property
    @jsii.member(jsii_name="servicesInput")
    def services_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "servicesInput"))

    @builtins.property
    @jsii.member(jsii_name="sloInput")
    def slo_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sloInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="targetHostInput")
    def target_host_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "targetHostInput"))

    @builtins.property
    @jsii.member(jsii_name="targetZoneNameInput")
    def target_zone_name_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "targetZoneNameInput"))

    @builtins.property
    @jsii.member(jsii_name="zonesInput")
    def zones_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "zonesInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationPolicyFiltersOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="eventSource")
    def event_source(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "eventSource"))

    @event_source.setter
    def event_source(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationPolicyFiltersOutputReference, "event_source").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventSource", value)

    @builtins.property
    @jsii.member(jsii_name="eventType")
    def event_type(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "eventType"))

    @event_type.setter
    def event_type(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationPolicyFiltersOutputReference, "event_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventType", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheckId")
    def health_check_id(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "healthCheckId"))

    @health_check_id.setter
    def health_check_id(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationPolicyFiltersOutputReference, "health_check_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheckId", value)

    @builtins.property
    @jsii.member(jsii_name="inputId")
    def input_id(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "inputId"))

    @input_id.setter
    def input_id(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationPolicyFiltersOutputReference, "input_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inputId", value)

    @builtins.property
    @jsii.member(jsii_name="limit")
    def limit(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "limit"))

    @limit.setter
    def limit(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationPolicyFiltersOutputReference, "limit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "limit", value)

    @builtins.property
    @jsii.member(jsii_name="newHealth")
    def new_health(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "newHealth"))

    @new_health.setter
    def new_health(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationPolicyFiltersOutputReference, "new_health").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "newHealth", value)

    @builtins.property
    @jsii.member(jsii_name="packetsPerSecond")
    def packets_per_second(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "packetsPerSecond"))

    @packets_per_second.setter
    def packets_per_second(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationPolicyFiltersOutputReference, "packets_per_second").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "packetsPerSecond", value)

    @builtins.property
    @jsii.member(jsii_name="poolId")
    def pool_id(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "poolId"))

    @pool_id.setter
    def pool_id(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationPolicyFiltersOutputReference, "pool_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "poolId", value)

    @builtins.property
    @jsii.member(jsii_name="product")
    def product(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "product"))

    @product.setter
    def product(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationPolicyFiltersOutputReference, "product").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "product", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationPolicyFiltersOutputReference, "protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="requestsPerSecond")
    def requests_per_second(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "requestsPerSecond"))

    @requests_per_second.setter
    def requests_per_second(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationPolicyFiltersOutputReference, "requests_per_second").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestsPerSecond", value)

    @builtins.property
    @jsii.member(jsii_name="services")
    def services(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "services"))

    @services.setter
    def services(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationPolicyFiltersOutputReference, "services").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "services", value)

    @builtins.property
    @jsii.member(jsii_name="slo")
    def slo(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "slo"))

    @slo.setter
    def slo(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationPolicyFiltersOutputReference, "slo").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "slo", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationPolicyFiltersOutputReference, "status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="targetHost")
    def target_host(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "targetHost"))

    @target_host.setter
    def target_host(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationPolicyFiltersOutputReference, "target_host").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetHost", value)

    @builtins.property
    @jsii.member(jsii_name="targetZoneName")
    def target_zone_name(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "targetZoneName"))

    @target_zone_name.setter
    def target_zone_name(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationPolicyFiltersOutputReference, "target_zone_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetZoneName", value)

    @builtins.property
    @jsii.member(jsii_name="zones")
    def zones(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "zones"))

    @zones.setter
    def zones(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationPolicyFiltersOutputReference, "zones").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zones", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[NotificationPolicyFilters]:
        return typing.cast(typing.Optional[NotificationPolicyFilters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[NotificationPolicyFilters]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationPolicyFiltersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.notificationPolicy.NotificationPolicyPagerdutyIntegration",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class NotificationPolicyPagerdutyIntegration:
    def __init__(
        self,
        *,
        id: builtins.str,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#id NotificationPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#name NotificationPolicy#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NotificationPolicyPagerdutyIntegration.__init__)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "id": id,
        }
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#id NotificationPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#name NotificationPolicy#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NotificationPolicyPagerdutyIntegration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NotificationPolicyPagerdutyIntegrationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.notificationPolicy.NotificationPolicyPagerdutyIntegrationList",
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
            type_hints = typing.get_type_hints(NotificationPolicyPagerdutyIntegrationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "NotificationPolicyPagerdutyIntegrationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NotificationPolicyPagerdutyIntegrationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("NotificationPolicyPagerdutyIntegrationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationPolicyPagerdutyIntegrationList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(NotificationPolicyPagerdutyIntegrationList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(NotificationPolicyPagerdutyIntegrationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NotificationPolicyPagerdutyIntegration]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NotificationPolicyPagerdutyIntegration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NotificationPolicyPagerdutyIntegration]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationPolicyPagerdutyIntegrationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NotificationPolicyPagerdutyIntegrationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.notificationPolicy.NotificationPolicyPagerdutyIntegrationOutputReference",
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
            type_hints = typing.get_type_hints(NotificationPolicyPagerdutyIntegrationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationPolicyPagerdutyIntegrationOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationPolicyPagerdutyIntegrationOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[NotificationPolicyPagerdutyIntegration, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[NotificationPolicyPagerdutyIntegration, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[NotificationPolicyPagerdutyIntegration, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationPolicyPagerdutyIntegrationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.notificationPolicy.NotificationPolicyWebhooksIntegration",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class NotificationPolicyWebhooksIntegration:
    def __init__(
        self,
        *,
        id: builtins.str,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#id NotificationPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#name NotificationPolicy#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NotificationPolicyWebhooksIntegration.__init__)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "id": id,
        }
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#id NotificationPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/notification_policy#name NotificationPolicy#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NotificationPolicyWebhooksIntegration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NotificationPolicyWebhooksIntegrationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.notificationPolicy.NotificationPolicyWebhooksIntegrationList",
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
            type_hints = typing.get_type_hints(NotificationPolicyWebhooksIntegrationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "NotificationPolicyWebhooksIntegrationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NotificationPolicyWebhooksIntegrationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("NotificationPolicyWebhooksIntegrationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationPolicyWebhooksIntegrationList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(NotificationPolicyWebhooksIntegrationList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(NotificationPolicyWebhooksIntegrationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NotificationPolicyWebhooksIntegration]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NotificationPolicyWebhooksIntegration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NotificationPolicyWebhooksIntegration]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationPolicyWebhooksIntegrationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NotificationPolicyWebhooksIntegrationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.notificationPolicy.NotificationPolicyWebhooksIntegrationOutputReference",
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
            type_hints = typing.get_type_hints(NotificationPolicyWebhooksIntegrationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationPolicyWebhooksIntegrationOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationPolicyWebhooksIntegrationOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[NotificationPolicyWebhooksIntegration, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[NotificationPolicyWebhooksIntegration, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[NotificationPolicyWebhooksIntegration, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NotificationPolicyWebhooksIntegrationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "NotificationPolicy",
    "NotificationPolicyConfig",
    "NotificationPolicyEmailIntegration",
    "NotificationPolicyEmailIntegrationList",
    "NotificationPolicyEmailIntegrationOutputReference",
    "NotificationPolicyFilters",
    "NotificationPolicyFiltersOutputReference",
    "NotificationPolicyPagerdutyIntegration",
    "NotificationPolicyPagerdutyIntegrationList",
    "NotificationPolicyPagerdutyIntegrationOutputReference",
    "NotificationPolicyWebhooksIntegration",
    "NotificationPolicyWebhooksIntegrationList",
    "NotificationPolicyWebhooksIntegrationOutputReference",
]

publication.publish()
