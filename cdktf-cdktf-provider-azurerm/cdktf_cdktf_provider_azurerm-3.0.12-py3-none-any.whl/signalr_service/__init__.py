'''
# `azurerm_signalr_service`

Refer to the Terraform Registory for docs: [`azurerm_signalr_service`](https://www.terraform.io/docs/providers/azurerm/r/signalr_service).
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


class SignalrService(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.signalrService.SignalrService",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service azurerm_signalr_service}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        sku: typing.Union["SignalrServiceSku", typing.Dict[str, typing.Any]],
        connectivity_logs_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cors: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SignalrServiceCors", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        live_trace: typing.Optional[typing.Union["SignalrServiceLiveTrace", typing.Dict[str, typing.Any]]] = None,
        live_trace_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        messaging_logs_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        service_mode: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["SignalrServiceTimeouts", typing.Dict[str, typing.Any]]] = None,
        upstream_endpoint: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SignalrServiceUpstreamEndpoint", typing.Dict[str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service azurerm_signalr_service} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#location SignalrService#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#name SignalrService#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#resource_group_name SignalrService#resource_group_name}.
        :param sku: sku block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#sku SignalrService#sku}
        :param connectivity_logs_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#connectivity_logs_enabled SignalrService#connectivity_logs_enabled}.
        :param cors: cors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#cors SignalrService#cors}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#id SignalrService#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param live_trace: live_trace block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#live_trace SignalrService#live_trace}
        :param live_trace_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#live_trace_enabled SignalrService#live_trace_enabled}.
        :param messaging_logs_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#messaging_logs_enabled SignalrService#messaging_logs_enabled}.
        :param service_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#service_mode SignalrService#service_mode}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#tags SignalrService#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#timeouts SignalrService#timeouts}
        :param upstream_endpoint: upstream_endpoint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#upstream_endpoint SignalrService#upstream_endpoint}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SignalrService.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SignalrServiceConfig(
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            sku=sku,
            connectivity_logs_enabled=connectivity_logs_enabled,
            cors=cors,
            id=id,
            live_trace=live_trace,
            live_trace_enabled=live_trace_enabled,
            messaging_logs_enabled=messaging_logs_enabled,
            service_mode=service_mode,
            tags=tags,
            timeouts=timeouts,
            upstream_endpoint=upstream_endpoint,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCors")
    def put_cors(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SignalrServiceCors", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SignalrService.put_cors)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCors", [value]))

    @jsii.member(jsii_name="putLiveTrace")
    def put_live_trace(
        self,
        *,
        connectivity_logs_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        http_request_logs_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        messaging_logs_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connectivity_logs_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#connectivity_logs_enabled SignalrService#connectivity_logs_enabled}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#enabled SignalrService#enabled}.
        :param http_request_logs_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#http_request_logs_enabled SignalrService#http_request_logs_enabled}.
        :param messaging_logs_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#messaging_logs_enabled SignalrService#messaging_logs_enabled}.
        '''
        value = SignalrServiceLiveTrace(
            connectivity_logs_enabled=connectivity_logs_enabled,
            enabled=enabled,
            http_request_logs_enabled=http_request_logs_enabled,
            messaging_logs_enabled=messaging_logs_enabled,
        )

        return typing.cast(None, jsii.invoke(self, "putLiveTrace", [value]))

    @jsii.member(jsii_name="putSku")
    def put_sku(self, *, capacity: jsii.Number, name: builtins.str) -> None:
        '''
        :param capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#capacity SignalrService#capacity}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#name SignalrService#name}.
        '''
        value = SignalrServiceSku(capacity=capacity, name=name)

        return typing.cast(None, jsii.invoke(self, "putSku", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#create SignalrService#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#delete SignalrService#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#read SignalrService#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#update SignalrService#update}.
        '''
        value = SignalrServiceTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putUpstreamEndpoint")
    def put_upstream_endpoint(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SignalrServiceUpstreamEndpoint", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SignalrService.put_upstream_endpoint)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUpstreamEndpoint", [value]))

    @jsii.member(jsii_name="resetConnectivityLogsEnabled")
    def reset_connectivity_logs_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectivityLogsEnabled", []))

    @jsii.member(jsii_name="resetCors")
    def reset_cors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCors", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLiveTrace")
    def reset_live_trace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLiveTrace", []))

    @jsii.member(jsii_name="resetLiveTraceEnabled")
    def reset_live_trace_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLiveTraceEnabled", []))

    @jsii.member(jsii_name="resetMessagingLogsEnabled")
    def reset_messaging_logs_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessagingLogsEnabled", []))

    @jsii.member(jsii_name="resetServiceMode")
    def reset_service_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceMode", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetUpstreamEndpoint")
    def reset_upstream_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpstreamEndpoint", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="cors")
    def cors(self) -> "SignalrServiceCorsList":
        return typing.cast("SignalrServiceCorsList", jsii.get(self, "cors"))

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostname"))

    @builtins.property
    @jsii.member(jsii_name="ipAddress")
    def ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipAddress"))

    @builtins.property
    @jsii.member(jsii_name="liveTrace")
    def live_trace(self) -> "SignalrServiceLiveTraceOutputReference":
        return typing.cast("SignalrServiceLiveTraceOutputReference", jsii.get(self, "liveTrace"))

    @builtins.property
    @jsii.member(jsii_name="primaryAccessKey")
    def primary_access_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryAccessKey"))

    @builtins.property
    @jsii.member(jsii_name="primaryConnectionString")
    def primary_connection_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryConnectionString"))

    @builtins.property
    @jsii.member(jsii_name="publicPort")
    def public_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "publicPort"))

    @builtins.property
    @jsii.member(jsii_name="secondaryAccessKey")
    def secondary_access_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondaryAccessKey"))

    @builtins.property
    @jsii.member(jsii_name="secondaryConnectionString")
    def secondary_connection_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondaryConnectionString"))

    @builtins.property
    @jsii.member(jsii_name="serverPort")
    def server_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "serverPort"))

    @builtins.property
    @jsii.member(jsii_name="sku")
    def sku(self) -> "SignalrServiceSkuOutputReference":
        return typing.cast("SignalrServiceSkuOutputReference", jsii.get(self, "sku"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "SignalrServiceTimeoutsOutputReference":
        return typing.cast("SignalrServiceTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="upstreamEndpoint")
    def upstream_endpoint(self) -> "SignalrServiceUpstreamEndpointList":
        return typing.cast("SignalrServiceUpstreamEndpointList", jsii.get(self, "upstreamEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="connectivityLogsEnabledInput")
    def connectivity_logs_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "connectivityLogsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="corsInput")
    def cors_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SignalrServiceCors"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SignalrServiceCors"]]], jsii.get(self, "corsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="liveTraceEnabledInput")
    def live_trace_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "liveTraceEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="liveTraceInput")
    def live_trace_input(self) -> typing.Optional["SignalrServiceLiveTrace"]:
        return typing.cast(typing.Optional["SignalrServiceLiveTrace"], jsii.get(self, "liveTraceInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="messagingLogsEnabledInput")
    def messaging_logs_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "messagingLogsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceModeInput")
    def service_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceModeInput"))

    @builtins.property
    @jsii.member(jsii_name="skuInput")
    def sku_input(self) -> typing.Optional["SignalrServiceSku"]:
        return typing.cast(typing.Optional["SignalrServiceSku"], jsii.get(self, "skuInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["SignalrServiceTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["SignalrServiceTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="upstreamEndpointInput")
    def upstream_endpoint_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SignalrServiceUpstreamEndpoint"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SignalrServiceUpstreamEndpoint"]]], jsii.get(self, "upstreamEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="connectivityLogsEnabled")
    def connectivity_logs_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "connectivityLogsEnabled"))

    @connectivity_logs_enabled.setter
    def connectivity_logs_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrService, "connectivity_logs_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectivityLogsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrService, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="liveTraceEnabled")
    def live_trace_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "liveTraceEnabled"))

    @live_trace_enabled.setter
    def live_trace_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrService, "live_trace_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "liveTraceEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrService, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="messagingLogsEnabled")
    def messaging_logs_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "messagingLogsEnabled"))

    @messaging_logs_enabled.setter
    def messaging_logs_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrService, "messaging_logs_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "messagingLogsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrService, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrService, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="serviceMode")
    def service_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceMode"))

    @service_mode.setter
    def service_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrService, "service_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceMode", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrService, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.signalrService.SignalrServiceConfig",
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
        "sku": "sku",
        "connectivity_logs_enabled": "connectivityLogsEnabled",
        "cors": "cors",
        "id": "id",
        "live_trace": "liveTrace",
        "live_trace_enabled": "liveTraceEnabled",
        "messaging_logs_enabled": "messagingLogsEnabled",
        "service_mode": "serviceMode",
        "tags": "tags",
        "timeouts": "timeouts",
        "upstream_endpoint": "upstreamEndpoint",
    },
)
class SignalrServiceConfig(cdktf.TerraformMetaArguments):
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
        sku: typing.Union["SignalrServiceSku", typing.Dict[str, typing.Any]],
        connectivity_logs_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cors: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SignalrServiceCors", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        live_trace: typing.Optional[typing.Union["SignalrServiceLiveTrace", typing.Dict[str, typing.Any]]] = None,
        live_trace_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        messaging_logs_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        service_mode: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["SignalrServiceTimeouts", typing.Dict[str, typing.Any]]] = None,
        upstream_endpoint: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SignalrServiceUpstreamEndpoint", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#location SignalrService#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#name SignalrService#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#resource_group_name SignalrService#resource_group_name}.
        :param sku: sku block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#sku SignalrService#sku}
        :param connectivity_logs_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#connectivity_logs_enabled SignalrService#connectivity_logs_enabled}.
        :param cors: cors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#cors SignalrService#cors}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#id SignalrService#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param live_trace: live_trace block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#live_trace SignalrService#live_trace}
        :param live_trace_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#live_trace_enabled SignalrService#live_trace_enabled}.
        :param messaging_logs_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#messaging_logs_enabled SignalrService#messaging_logs_enabled}.
        :param service_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#service_mode SignalrService#service_mode}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#tags SignalrService#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#timeouts SignalrService#timeouts}
        :param upstream_endpoint: upstream_endpoint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#upstream_endpoint SignalrService#upstream_endpoint}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(sku, dict):
            sku = SignalrServiceSku(**sku)
        if isinstance(live_trace, dict):
            live_trace = SignalrServiceLiveTrace(**live_trace)
        if isinstance(timeouts, dict):
            timeouts = SignalrServiceTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(SignalrServiceConfig.__init__)
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
            check_type(argname="argument sku", value=sku, expected_type=type_hints["sku"])
            check_type(argname="argument connectivity_logs_enabled", value=connectivity_logs_enabled, expected_type=type_hints["connectivity_logs_enabled"])
            check_type(argname="argument cors", value=cors, expected_type=type_hints["cors"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument live_trace", value=live_trace, expected_type=type_hints["live_trace"])
            check_type(argname="argument live_trace_enabled", value=live_trace_enabled, expected_type=type_hints["live_trace_enabled"])
            check_type(argname="argument messaging_logs_enabled", value=messaging_logs_enabled, expected_type=type_hints["messaging_logs_enabled"])
            check_type(argname="argument service_mode", value=service_mode, expected_type=type_hints["service_mode"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument upstream_endpoint", value=upstream_endpoint, expected_type=type_hints["upstream_endpoint"])
        self._values: typing.Dict[str, typing.Any] = {
            "location": location,
            "name": name,
            "resource_group_name": resource_group_name,
            "sku": sku,
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
        if connectivity_logs_enabled is not None:
            self._values["connectivity_logs_enabled"] = connectivity_logs_enabled
        if cors is not None:
            self._values["cors"] = cors
        if id is not None:
            self._values["id"] = id
        if live_trace is not None:
            self._values["live_trace"] = live_trace
        if live_trace_enabled is not None:
            self._values["live_trace_enabled"] = live_trace_enabled
        if messaging_logs_enabled is not None:
            self._values["messaging_logs_enabled"] = messaging_logs_enabled
        if service_mode is not None:
            self._values["service_mode"] = service_mode
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if upstream_endpoint is not None:
            self._values["upstream_endpoint"] = upstream_endpoint

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#location SignalrService#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#name SignalrService#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#resource_group_name SignalrService#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sku(self) -> "SignalrServiceSku":
        '''sku block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#sku SignalrService#sku}
        '''
        result = self._values.get("sku")
        assert result is not None, "Required property 'sku' is missing"
        return typing.cast("SignalrServiceSku", result)

    @builtins.property
    def connectivity_logs_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#connectivity_logs_enabled SignalrService#connectivity_logs_enabled}.'''
        result = self._values.get("connectivity_logs_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def cors(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SignalrServiceCors"]]]:
        '''cors block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#cors SignalrService#cors}
        '''
        result = self._values.get("cors")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SignalrServiceCors"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#id SignalrService#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def live_trace(self) -> typing.Optional["SignalrServiceLiveTrace"]:
        '''live_trace block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#live_trace SignalrService#live_trace}
        '''
        result = self._values.get("live_trace")
        return typing.cast(typing.Optional["SignalrServiceLiveTrace"], result)

    @builtins.property
    def live_trace_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#live_trace_enabled SignalrService#live_trace_enabled}.'''
        result = self._values.get("live_trace_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def messaging_logs_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#messaging_logs_enabled SignalrService#messaging_logs_enabled}.'''
        result = self._values.get("messaging_logs_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def service_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#service_mode SignalrService#service_mode}.'''
        result = self._values.get("service_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#tags SignalrService#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["SignalrServiceTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#timeouts SignalrService#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["SignalrServiceTimeouts"], result)

    @builtins.property
    def upstream_endpoint(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SignalrServiceUpstreamEndpoint"]]]:
        '''upstream_endpoint block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#upstream_endpoint SignalrService#upstream_endpoint}
        '''
        result = self._values.get("upstream_endpoint")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SignalrServiceUpstreamEndpoint"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SignalrServiceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.signalrService.SignalrServiceCors",
    jsii_struct_bases=[],
    name_mapping={"allowed_origins": "allowedOrigins"},
)
class SignalrServiceCors:
    def __init__(self, *, allowed_origins: typing.Sequence[builtins.str]) -> None:
        '''
        :param allowed_origins: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#allowed_origins SignalrService#allowed_origins}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SignalrServiceCors.__init__)
            check_type(argname="argument allowed_origins", value=allowed_origins, expected_type=type_hints["allowed_origins"])
        self._values: typing.Dict[str, typing.Any] = {
            "allowed_origins": allowed_origins,
        }

    @builtins.property
    def allowed_origins(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#allowed_origins SignalrService#allowed_origins}.'''
        result = self._values.get("allowed_origins")
        assert result is not None, "Required property 'allowed_origins' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SignalrServiceCors(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SignalrServiceCorsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.signalrService.SignalrServiceCorsList",
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
            type_hints = typing.get_type_hints(SignalrServiceCorsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "SignalrServiceCorsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SignalrServiceCorsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SignalrServiceCorsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrServiceCorsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SignalrServiceCorsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SignalrServiceCorsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SignalrServiceCors]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SignalrServiceCors]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SignalrServiceCors]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrServiceCorsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SignalrServiceCorsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.signalrService.SignalrServiceCorsOutputReference",
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
            type_hints = typing.get_type_hints(SignalrServiceCorsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="allowedOriginsInput")
    def allowed_origins_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedOriginsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedOrigins")
    def allowed_origins(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedOrigins"))

    @allowed_origins.setter
    def allowed_origins(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrServiceCorsOutputReference, "allowed_origins").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedOrigins", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SignalrServiceCors, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SignalrServiceCors, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SignalrServiceCors, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrServiceCorsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.signalrService.SignalrServiceLiveTrace",
    jsii_struct_bases=[],
    name_mapping={
        "connectivity_logs_enabled": "connectivityLogsEnabled",
        "enabled": "enabled",
        "http_request_logs_enabled": "httpRequestLogsEnabled",
        "messaging_logs_enabled": "messagingLogsEnabled",
    },
)
class SignalrServiceLiveTrace:
    def __init__(
        self,
        *,
        connectivity_logs_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        http_request_logs_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        messaging_logs_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connectivity_logs_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#connectivity_logs_enabled SignalrService#connectivity_logs_enabled}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#enabled SignalrService#enabled}.
        :param http_request_logs_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#http_request_logs_enabled SignalrService#http_request_logs_enabled}.
        :param messaging_logs_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#messaging_logs_enabled SignalrService#messaging_logs_enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SignalrServiceLiveTrace.__init__)
            check_type(argname="argument connectivity_logs_enabled", value=connectivity_logs_enabled, expected_type=type_hints["connectivity_logs_enabled"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument http_request_logs_enabled", value=http_request_logs_enabled, expected_type=type_hints["http_request_logs_enabled"])
            check_type(argname="argument messaging_logs_enabled", value=messaging_logs_enabled, expected_type=type_hints["messaging_logs_enabled"])
        self._values: typing.Dict[str, typing.Any] = {}
        if connectivity_logs_enabled is not None:
            self._values["connectivity_logs_enabled"] = connectivity_logs_enabled
        if enabled is not None:
            self._values["enabled"] = enabled
        if http_request_logs_enabled is not None:
            self._values["http_request_logs_enabled"] = http_request_logs_enabled
        if messaging_logs_enabled is not None:
            self._values["messaging_logs_enabled"] = messaging_logs_enabled

    @builtins.property
    def connectivity_logs_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#connectivity_logs_enabled SignalrService#connectivity_logs_enabled}.'''
        result = self._values.get("connectivity_logs_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#enabled SignalrService#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def http_request_logs_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#http_request_logs_enabled SignalrService#http_request_logs_enabled}.'''
        result = self._values.get("http_request_logs_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def messaging_logs_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#messaging_logs_enabled SignalrService#messaging_logs_enabled}.'''
        result = self._values.get("messaging_logs_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SignalrServiceLiveTrace(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SignalrServiceLiveTraceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.signalrService.SignalrServiceLiveTraceOutputReference",
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
            type_hints = typing.get_type_hints(SignalrServiceLiveTraceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetConnectivityLogsEnabled")
    def reset_connectivity_logs_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectivityLogsEnabled", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetHttpRequestLogsEnabled")
    def reset_http_request_logs_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpRequestLogsEnabled", []))

    @jsii.member(jsii_name="resetMessagingLogsEnabled")
    def reset_messaging_logs_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessagingLogsEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="connectivityLogsEnabledInput")
    def connectivity_logs_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "connectivityLogsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="httpRequestLogsEnabledInput")
    def http_request_logs_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "httpRequestLogsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="messagingLogsEnabledInput")
    def messaging_logs_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "messagingLogsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="connectivityLogsEnabled")
    def connectivity_logs_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "connectivityLogsEnabled"))

    @connectivity_logs_enabled.setter
    def connectivity_logs_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrServiceLiveTraceOutputReference, "connectivity_logs_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectivityLogsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrServiceLiveTraceOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="httpRequestLogsEnabled")
    def http_request_logs_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "httpRequestLogsEnabled"))

    @http_request_logs_enabled.setter
    def http_request_logs_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrServiceLiveTraceOutputReference, "http_request_logs_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpRequestLogsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="messagingLogsEnabled")
    def messaging_logs_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "messagingLogsEnabled"))

    @messaging_logs_enabled.setter
    def messaging_logs_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrServiceLiveTraceOutputReference, "messaging_logs_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "messagingLogsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SignalrServiceLiveTrace]:
        return typing.cast(typing.Optional[SignalrServiceLiveTrace], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SignalrServiceLiveTrace]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrServiceLiveTraceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.signalrService.SignalrServiceSku",
    jsii_struct_bases=[],
    name_mapping={"capacity": "capacity", "name": "name"},
)
class SignalrServiceSku:
    def __init__(self, *, capacity: jsii.Number, name: builtins.str) -> None:
        '''
        :param capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#capacity SignalrService#capacity}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#name SignalrService#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SignalrServiceSku.__init__)
            check_type(argname="argument capacity", value=capacity, expected_type=type_hints["capacity"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "capacity": capacity,
            "name": name,
        }

    @builtins.property
    def capacity(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#capacity SignalrService#capacity}.'''
        result = self._values.get("capacity")
        assert result is not None, "Required property 'capacity' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#name SignalrService#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SignalrServiceSku(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SignalrServiceSkuOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.signalrService.SignalrServiceSkuOutputReference",
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
            type_hints = typing.get_type_hints(SignalrServiceSkuOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="capacityInput")
    def capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "capacityInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="capacity")
    def capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "capacity"))

    @capacity.setter
    def capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrServiceSkuOutputReference, "capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacity", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrServiceSkuOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SignalrServiceSku]:
        return typing.cast(typing.Optional[SignalrServiceSku], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SignalrServiceSku]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrServiceSkuOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.signalrService.SignalrServiceTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class SignalrServiceTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#create SignalrService#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#delete SignalrService#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#read SignalrService#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#update SignalrService#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SignalrServiceTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#create SignalrService#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#delete SignalrService#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#read SignalrService#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#update SignalrService#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SignalrServiceTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SignalrServiceTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.signalrService.SignalrServiceTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(SignalrServiceTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(SignalrServiceTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrServiceTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrServiceTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrServiceTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SignalrServiceTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SignalrServiceTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SignalrServiceTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrServiceTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.signalrService.SignalrServiceUpstreamEndpoint",
    jsii_struct_bases=[],
    name_mapping={
        "category_pattern": "categoryPattern",
        "event_pattern": "eventPattern",
        "hub_pattern": "hubPattern",
        "url_template": "urlTemplate",
    },
)
class SignalrServiceUpstreamEndpoint:
    def __init__(
        self,
        *,
        category_pattern: typing.Sequence[builtins.str],
        event_pattern: typing.Sequence[builtins.str],
        hub_pattern: typing.Sequence[builtins.str],
        url_template: builtins.str,
    ) -> None:
        '''
        :param category_pattern: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#category_pattern SignalrService#category_pattern}.
        :param event_pattern: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#event_pattern SignalrService#event_pattern}.
        :param hub_pattern: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#hub_pattern SignalrService#hub_pattern}.
        :param url_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#url_template SignalrService#url_template}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SignalrServiceUpstreamEndpoint.__init__)
            check_type(argname="argument category_pattern", value=category_pattern, expected_type=type_hints["category_pattern"])
            check_type(argname="argument event_pattern", value=event_pattern, expected_type=type_hints["event_pattern"])
            check_type(argname="argument hub_pattern", value=hub_pattern, expected_type=type_hints["hub_pattern"])
            check_type(argname="argument url_template", value=url_template, expected_type=type_hints["url_template"])
        self._values: typing.Dict[str, typing.Any] = {
            "category_pattern": category_pattern,
            "event_pattern": event_pattern,
            "hub_pattern": hub_pattern,
            "url_template": url_template,
        }

    @builtins.property
    def category_pattern(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#category_pattern SignalrService#category_pattern}.'''
        result = self._values.get("category_pattern")
        assert result is not None, "Required property 'category_pattern' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def event_pattern(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#event_pattern SignalrService#event_pattern}.'''
        result = self._values.get("event_pattern")
        assert result is not None, "Required property 'event_pattern' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def hub_pattern(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#hub_pattern SignalrService#hub_pattern}.'''
        result = self._values.get("hub_pattern")
        assert result is not None, "Required property 'hub_pattern' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def url_template(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/signalr_service#url_template SignalrService#url_template}.'''
        result = self._values.get("url_template")
        assert result is not None, "Required property 'url_template' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SignalrServiceUpstreamEndpoint(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SignalrServiceUpstreamEndpointList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.signalrService.SignalrServiceUpstreamEndpointList",
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
            type_hints = typing.get_type_hints(SignalrServiceUpstreamEndpointList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SignalrServiceUpstreamEndpointOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SignalrServiceUpstreamEndpointList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SignalrServiceUpstreamEndpointOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrServiceUpstreamEndpointList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SignalrServiceUpstreamEndpointList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SignalrServiceUpstreamEndpointList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SignalrServiceUpstreamEndpoint]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SignalrServiceUpstreamEndpoint]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SignalrServiceUpstreamEndpoint]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrServiceUpstreamEndpointList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SignalrServiceUpstreamEndpointOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.signalrService.SignalrServiceUpstreamEndpointOutputReference",
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
            type_hints = typing.get_type_hints(SignalrServiceUpstreamEndpointOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="categoryPatternInput")
    def category_pattern_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "categoryPatternInput"))

    @builtins.property
    @jsii.member(jsii_name="eventPatternInput")
    def event_pattern_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "eventPatternInput"))

    @builtins.property
    @jsii.member(jsii_name="hubPatternInput")
    def hub_pattern_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "hubPatternInput"))

    @builtins.property
    @jsii.member(jsii_name="urlTemplateInput")
    def url_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="categoryPattern")
    def category_pattern(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "categoryPattern"))

    @category_pattern.setter
    def category_pattern(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrServiceUpstreamEndpointOutputReference, "category_pattern").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "categoryPattern", value)

    @builtins.property
    @jsii.member(jsii_name="eventPattern")
    def event_pattern(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "eventPattern"))

    @event_pattern.setter
    def event_pattern(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrServiceUpstreamEndpointOutputReference, "event_pattern").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventPattern", value)

    @builtins.property
    @jsii.member(jsii_name="hubPattern")
    def hub_pattern(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "hubPattern"))

    @hub_pattern.setter
    def hub_pattern(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrServiceUpstreamEndpointOutputReference, "hub_pattern").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hubPattern", value)

    @builtins.property
    @jsii.member(jsii_name="urlTemplate")
    def url_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "urlTemplate"))

    @url_template.setter
    def url_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrServiceUpstreamEndpointOutputReference, "url_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "urlTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SignalrServiceUpstreamEndpoint, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SignalrServiceUpstreamEndpoint, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SignalrServiceUpstreamEndpoint, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SignalrServiceUpstreamEndpointOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SignalrService",
    "SignalrServiceConfig",
    "SignalrServiceCors",
    "SignalrServiceCorsList",
    "SignalrServiceCorsOutputReference",
    "SignalrServiceLiveTrace",
    "SignalrServiceLiveTraceOutputReference",
    "SignalrServiceSku",
    "SignalrServiceSkuOutputReference",
    "SignalrServiceTimeouts",
    "SignalrServiceTimeoutsOutputReference",
    "SignalrServiceUpstreamEndpoint",
    "SignalrServiceUpstreamEndpointList",
    "SignalrServiceUpstreamEndpointOutputReference",
]

publication.publish()
