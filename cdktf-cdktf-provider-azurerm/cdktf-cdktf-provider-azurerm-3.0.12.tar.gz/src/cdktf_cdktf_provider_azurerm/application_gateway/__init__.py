'''
# `azurerm_application_gateway`

Refer to the Terraform Registory for docs: [`azurerm_application_gateway`](https://www.terraform.io/docs/providers/azurerm/r/application_gateway).
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


class ApplicationGateway(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGateway",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway azurerm_application_gateway}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        backend_address_pool: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayBackendAddressPool", typing.Dict[str, typing.Any]]]],
        backend_http_settings: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayBackendHttpSettings", typing.Dict[str, typing.Any]]]],
        frontend_ip_configuration: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayFrontendIpConfiguration", typing.Dict[str, typing.Any]]]],
        frontend_port: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayFrontendPort", typing.Dict[str, typing.Any]]]],
        gateway_ip_configuration: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayGatewayIpConfiguration", typing.Dict[str, typing.Any]]]],
        http_listener: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayHttpListener", typing.Dict[str, typing.Any]]]],
        location: builtins.str,
        name: builtins.str,
        request_routing_rule: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayRequestRoutingRule", typing.Dict[str, typing.Any]]]],
        resource_group_name: builtins.str,
        sku: typing.Union["ApplicationGatewaySku", typing.Dict[str, typing.Any]],
        authentication_certificate: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayAuthenticationCertificate", typing.Dict[str, typing.Any]]]]] = None,
        autoscale_configuration: typing.Optional[typing.Union["ApplicationGatewayAutoscaleConfiguration", typing.Dict[str, typing.Any]]] = None,
        custom_error_configuration: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayCustomErrorConfiguration", typing.Dict[str, typing.Any]]]]] = None,
        enable_http2: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        fips_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        firewall_policy_id: typing.Optional[builtins.str] = None,
        force_firewall_policy_association: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        global_: typing.Optional[typing.Union["ApplicationGatewayGlobal", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["ApplicationGatewayIdentity", typing.Dict[str, typing.Any]]] = None,
        private_link_configuration: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayPrivateLinkConfiguration", typing.Dict[str, typing.Any]]]]] = None,
        probe: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayProbe", typing.Dict[str, typing.Any]]]]] = None,
        redirect_configuration: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayRedirectConfiguration", typing.Dict[str, typing.Any]]]]] = None,
        rewrite_rule_set: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayRewriteRuleSet", typing.Dict[str, typing.Any]]]]] = None,
        ssl_certificate: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewaySslCertificate", typing.Dict[str, typing.Any]]]]] = None,
        ssl_policy: typing.Optional[typing.Union["ApplicationGatewaySslPolicy", typing.Dict[str, typing.Any]]] = None,
        ssl_profile: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewaySslProfile", typing.Dict[str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ApplicationGatewayTimeouts", typing.Dict[str, typing.Any]]] = None,
        trusted_client_certificate: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayTrustedClientCertificate", typing.Dict[str, typing.Any]]]]] = None,
        trusted_root_certificate: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayTrustedRootCertificate", typing.Dict[str, typing.Any]]]]] = None,
        url_path_map: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayUrlPathMap", typing.Dict[str, typing.Any]]]]] = None,
        waf_configuration: typing.Optional[typing.Union["ApplicationGatewayWafConfiguration", typing.Dict[str, typing.Any]]] = None,
        zones: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway azurerm_application_gateway} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param backend_address_pool: backend_address_pool block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#backend_address_pool ApplicationGateway#backend_address_pool}
        :param backend_http_settings: backend_http_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#backend_http_settings ApplicationGateway#backend_http_settings}
        :param frontend_ip_configuration: frontend_ip_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#frontend_ip_configuration ApplicationGateway#frontend_ip_configuration}
        :param frontend_port: frontend_port block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#frontend_port ApplicationGateway#frontend_port}
        :param gateway_ip_configuration: gateway_ip_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#gateway_ip_configuration ApplicationGateway#gateway_ip_configuration}
        :param http_listener: http_listener block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#http_listener ApplicationGateway#http_listener}
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#location ApplicationGateway#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.
        :param request_routing_rule: request_routing_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#request_routing_rule ApplicationGateway#request_routing_rule}
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#resource_group_name ApplicationGateway#resource_group_name}.
        :param sku: sku block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#sku ApplicationGateway#sku}
        :param authentication_certificate: authentication_certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#authentication_certificate ApplicationGateway#authentication_certificate}
        :param autoscale_configuration: autoscale_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#autoscale_configuration ApplicationGateway#autoscale_configuration}
        :param custom_error_configuration: custom_error_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#custom_error_configuration ApplicationGateway#custom_error_configuration}
        :param enable_http2: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#enable_http2 ApplicationGateway#enable_http2}.
        :param fips_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#fips_enabled ApplicationGateway#fips_enabled}.
        :param firewall_policy_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#firewall_policy_id ApplicationGateway#firewall_policy_id}.
        :param force_firewall_policy_association: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#force_firewall_policy_association ApplicationGateway#force_firewall_policy_association}.
        :param global_: global block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#global ApplicationGateway#global}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#id ApplicationGateway#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#identity ApplicationGateway#identity}
        :param private_link_configuration: private_link_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#private_link_configuration ApplicationGateway#private_link_configuration}
        :param probe: probe block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#probe ApplicationGateway#probe}
        :param redirect_configuration: redirect_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#redirect_configuration ApplicationGateway#redirect_configuration}
        :param rewrite_rule_set: rewrite_rule_set block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#rewrite_rule_set ApplicationGateway#rewrite_rule_set}
        :param ssl_certificate: ssl_certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#ssl_certificate ApplicationGateway#ssl_certificate}
        :param ssl_policy: ssl_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#ssl_policy ApplicationGateway#ssl_policy}
        :param ssl_profile: ssl_profile block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#ssl_profile ApplicationGateway#ssl_profile}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#tags ApplicationGateway#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#timeouts ApplicationGateway#timeouts}
        :param trusted_client_certificate: trusted_client_certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#trusted_client_certificate ApplicationGateway#trusted_client_certificate}
        :param trusted_root_certificate: trusted_root_certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#trusted_root_certificate ApplicationGateway#trusted_root_certificate}
        :param url_path_map: url_path_map block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#url_path_map ApplicationGateway#url_path_map}
        :param waf_configuration: waf_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#waf_configuration ApplicationGateway#waf_configuration}
        :param zones: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#zones ApplicationGateway#zones}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGateway.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ApplicationGatewayConfig(
            backend_address_pool=backend_address_pool,
            backend_http_settings=backend_http_settings,
            frontend_ip_configuration=frontend_ip_configuration,
            frontend_port=frontend_port,
            gateway_ip_configuration=gateway_ip_configuration,
            http_listener=http_listener,
            location=location,
            name=name,
            request_routing_rule=request_routing_rule,
            resource_group_name=resource_group_name,
            sku=sku,
            authentication_certificate=authentication_certificate,
            autoscale_configuration=autoscale_configuration,
            custom_error_configuration=custom_error_configuration,
            enable_http2=enable_http2,
            fips_enabled=fips_enabled,
            firewall_policy_id=firewall_policy_id,
            force_firewall_policy_association=force_firewall_policy_association,
            global_=global_,
            id=id,
            identity=identity,
            private_link_configuration=private_link_configuration,
            probe=probe,
            redirect_configuration=redirect_configuration,
            rewrite_rule_set=rewrite_rule_set,
            ssl_certificate=ssl_certificate,
            ssl_policy=ssl_policy,
            ssl_profile=ssl_profile,
            tags=tags,
            timeouts=timeouts,
            trusted_client_certificate=trusted_client_certificate,
            trusted_root_certificate=trusted_root_certificate,
            url_path_map=url_path_map,
            waf_configuration=waf_configuration,
            zones=zones,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAuthenticationCertificate")
    def put_authentication_certificate(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayAuthenticationCertificate", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGateway.put_authentication_certificate)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAuthenticationCertificate", [value]))

    @jsii.member(jsii_name="putAutoscaleConfiguration")
    def put_autoscale_configuration(
        self,
        *,
        min_capacity: jsii.Number,
        max_capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param min_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#min_capacity ApplicationGateway#min_capacity}.
        :param max_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#max_capacity ApplicationGateway#max_capacity}.
        '''
        value = ApplicationGatewayAutoscaleConfiguration(
            min_capacity=min_capacity, max_capacity=max_capacity
        )

        return typing.cast(None, jsii.invoke(self, "putAutoscaleConfiguration", [value]))

    @jsii.member(jsii_name="putBackendAddressPool")
    def put_backend_address_pool(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayBackendAddressPool", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGateway.put_backend_address_pool)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBackendAddressPool", [value]))

    @jsii.member(jsii_name="putBackendHttpSettings")
    def put_backend_http_settings(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayBackendHttpSettings", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGateway.put_backend_http_settings)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBackendHttpSettings", [value]))

    @jsii.member(jsii_name="putCustomErrorConfiguration")
    def put_custom_error_configuration(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayCustomErrorConfiguration", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGateway.put_custom_error_configuration)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCustomErrorConfiguration", [value]))

    @jsii.member(jsii_name="putFrontendIpConfiguration")
    def put_frontend_ip_configuration(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayFrontendIpConfiguration", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGateway.put_frontend_ip_configuration)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFrontendIpConfiguration", [value]))

    @jsii.member(jsii_name="putFrontendPort")
    def put_frontend_port(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayFrontendPort", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGateway.put_frontend_port)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFrontendPort", [value]))

    @jsii.member(jsii_name="putGatewayIpConfiguration")
    def put_gateway_ip_configuration(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayGatewayIpConfiguration", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGateway.put_gateway_ip_configuration)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGatewayIpConfiguration", [value]))

    @jsii.member(jsii_name="putGlobal")
    def put_global(
        self,
        *,
        request_buffering_enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        response_buffering_enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param request_buffering_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#request_buffering_enabled ApplicationGateway#request_buffering_enabled}.
        :param response_buffering_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#response_buffering_enabled ApplicationGateway#response_buffering_enabled}.
        '''
        value = ApplicationGatewayGlobal(
            request_buffering_enabled=request_buffering_enabled,
            response_buffering_enabled=response_buffering_enabled,
        )

        return typing.cast(None, jsii.invoke(self, "putGlobal", [value]))

    @jsii.member(jsii_name="putHttpListener")
    def put_http_listener(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayHttpListener", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGateway.put_http_listener)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHttpListener", [value]))

    @jsii.member(jsii_name="putIdentity")
    def put_identity(
        self,
        *,
        identity_ids: typing.Sequence[builtins.str],
        type: builtins.str,
    ) -> None:
        '''
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#identity_ids ApplicationGateway#identity_ids}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#type ApplicationGateway#type}.
        '''
        value = ApplicationGatewayIdentity(identity_ids=identity_ids, type=type)

        return typing.cast(None, jsii.invoke(self, "putIdentity", [value]))

    @jsii.member(jsii_name="putPrivateLinkConfiguration")
    def put_private_link_configuration(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayPrivateLinkConfiguration", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGateway.put_private_link_configuration)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPrivateLinkConfiguration", [value]))

    @jsii.member(jsii_name="putProbe")
    def put_probe(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayProbe", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGateway.put_probe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putProbe", [value]))

    @jsii.member(jsii_name="putRedirectConfiguration")
    def put_redirect_configuration(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayRedirectConfiguration", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGateway.put_redirect_configuration)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRedirectConfiguration", [value]))

    @jsii.member(jsii_name="putRequestRoutingRule")
    def put_request_routing_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayRequestRoutingRule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGateway.put_request_routing_rule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRequestRoutingRule", [value]))

    @jsii.member(jsii_name="putRewriteRuleSet")
    def put_rewrite_rule_set(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayRewriteRuleSet", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGateway.put_rewrite_rule_set)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRewriteRuleSet", [value]))

    @jsii.member(jsii_name="putSku")
    def put_sku(
        self,
        *,
        name: builtins.str,
        tier: builtins.str,
        capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.
        :param tier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#tier ApplicationGateway#tier}.
        :param capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#capacity ApplicationGateway#capacity}.
        '''
        value = ApplicationGatewaySku(name=name, tier=tier, capacity=capacity)

        return typing.cast(None, jsii.invoke(self, "putSku", [value]))

    @jsii.member(jsii_name="putSslCertificate")
    def put_ssl_certificate(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewaySslCertificate", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGateway.put_ssl_certificate)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSslCertificate", [value]))

    @jsii.member(jsii_name="putSslPolicy")
    def put_ssl_policy(
        self,
        *,
        cipher_suites: typing.Optional[typing.Sequence[builtins.str]] = None,
        disabled_protocols: typing.Optional[typing.Sequence[builtins.str]] = None,
        min_protocol_version: typing.Optional[builtins.str] = None,
        policy_name: typing.Optional[builtins.str] = None,
        policy_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cipher_suites: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#cipher_suites ApplicationGateway#cipher_suites}.
        :param disabled_protocols: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#disabled_protocols ApplicationGateway#disabled_protocols}.
        :param min_protocol_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#min_protocol_version ApplicationGateway#min_protocol_version}.
        :param policy_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#policy_name ApplicationGateway#policy_name}.
        :param policy_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#policy_type ApplicationGateway#policy_type}.
        '''
        value = ApplicationGatewaySslPolicy(
            cipher_suites=cipher_suites,
            disabled_protocols=disabled_protocols,
            min_protocol_version=min_protocol_version,
            policy_name=policy_name,
            policy_type=policy_type,
        )

        return typing.cast(None, jsii.invoke(self, "putSslPolicy", [value]))

    @jsii.member(jsii_name="putSslProfile")
    def put_ssl_profile(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewaySslProfile", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGateway.put_ssl_profile)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSslProfile", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#create ApplicationGateway#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#delete ApplicationGateway#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#read ApplicationGateway#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#update ApplicationGateway#update}.
        '''
        value = ApplicationGatewayTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putTrustedClientCertificate")
    def put_trusted_client_certificate(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayTrustedClientCertificate", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGateway.put_trusted_client_certificate)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTrustedClientCertificate", [value]))

    @jsii.member(jsii_name="putTrustedRootCertificate")
    def put_trusted_root_certificate(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayTrustedRootCertificate", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGateway.put_trusted_root_certificate)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTrustedRootCertificate", [value]))

    @jsii.member(jsii_name="putUrlPathMap")
    def put_url_path_map(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayUrlPathMap", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGateway.put_url_path_map)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUrlPathMap", [value]))

    @jsii.member(jsii_name="putWafConfiguration")
    def put_waf_configuration(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        firewall_mode: builtins.str,
        rule_set_version: builtins.str,
        disabled_rule_group: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayWafConfigurationDisabledRuleGroup", typing.Dict[str, typing.Any]]]]] = None,
        exclusion: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayWafConfigurationExclusion", typing.Dict[str, typing.Any]]]]] = None,
        file_upload_limit_mb: typing.Optional[jsii.Number] = None,
        max_request_body_size_kb: typing.Optional[jsii.Number] = None,
        request_body_check: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        rule_set_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#enabled ApplicationGateway#enabled}.
        :param firewall_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#firewall_mode ApplicationGateway#firewall_mode}.
        :param rule_set_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#rule_set_version ApplicationGateway#rule_set_version}.
        :param disabled_rule_group: disabled_rule_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#disabled_rule_group ApplicationGateway#disabled_rule_group}
        :param exclusion: exclusion block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#exclusion ApplicationGateway#exclusion}
        :param file_upload_limit_mb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#file_upload_limit_mb ApplicationGateway#file_upload_limit_mb}.
        :param max_request_body_size_kb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#max_request_body_size_kb ApplicationGateway#max_request_body_size_kb}.
        :param request_body_check: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#request_body_check ApplicationGateway#request_body_check}.
        :param rule_set_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#rule_set_type ApplicationGateway#rule_set_type}.
        '''
        value = ApplicationGatewayWafConfiguration(
            enabled=enabled,
            firewall_mode=firewall_mode,
            rule_set_version=rule_set_version,
            disabled_rule_group=disabled_rule_group,
            exclusion=exclusion,
            file_upload_limit_mb=file_upload_limit_mb,
            max_request_body_size_kb=max_request_body_size_kb,
            request_body_check=request_body_check,
            rule_set_type=rule_set_type,
        )

        return typing.cast(None, jsii.invoke(self, "putWafConfiguration", [value]))

    @jsii.member(jsii_name="resetAuthenticationCertificate")
    def reset_authentication_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthenticationCertificate", []))

    @jsii.member(jsii_name="resetAutoscaleConfiguration")
    def reset_autoscale_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoscaleConfiguration", []))

    @jsii.member(jsii_name="resetCustomErrorConfiguration")
    def reset_custom_error_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomErrorConfiguration", []))

    @jsii.member(jsii_name="resetEnableHttp2")
    def reset_enable_http2(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableHttp2", []))

    @jsii.member(jsii_name="resetFipsEnabled")
    def reset_fips_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFipsEnabled", []))

    @jsii.member(jsii_name="resetFirewallPolicyId")
    def reset_firewall_policy_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFirewallPolicyId", []))

    @jsii.member(jsii_name="resetForceFirewallPolicyAssociation")
    def reset_force_firewall_policy_association(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceFirewallPolicyAssociation", []))

    @jsii.member(jsii_name="resetGlobal")
    def reset_global(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGlobal", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentity")
    def reset_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentity", []))

    @jsii.member(jsii_name="resetPrivateLinkConfiguration")
    def reset_private_link_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateLinkConfiguration", []))

    @jsii.member(jsii_name="resetProbe")
    def reset_probe(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProbe", []))

    @jsii.member(jsii_name="resetRedirectConfiguration")
    def reset_redirect_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectConfiguration", []))

    @jsii.member(jsii_name="resetRewriteRuleSet")
    def reset_rewrite_rule_set(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRewriteRuleSet", []))

    @jsii.member(jsii_name="resetSslCertificate")
    def reset_ssl_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslCertificate", []))

    @jsii.member(jsii_name="resetSslPolicy")
    def reset_ssl_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslPolicy", []))

    @jsii.member(jsii_name="resetSslProfile")
    def reset_ssl_profile(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslProfile", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTrustedClientCertificate")
    def reset_trusted_client_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrustedClientCertificate", []))

    @jsii.member(jsii_name="resetTrustedRootCertificate")
    def reset_trusted_root_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrustedRootCertificate", []))

    @jsii.member(jsii_name="resetUrlPathMap")
    def reset_url_path_map(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrlPathMap", []))

    @jsii.member(jsii_name="resetWafConfiguration")
    def reset_waf_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWafConfiguration", []))

    @jsii.member(jsii_name="resetZones")
    def reset_zones(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZones", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="authenticationCertificate")
    def authentication_certificate(
        self,
    ) -> "ApplicationGatewayAuthenticationCertificateList":
        return typing.cast("ApplicationGatewayAuthenticationCertificateList", jsii.get(self, "authenticationCertificate"))

    @builtins.property
    @jsii.member(jsii_name="autoscaleConfiguration")
    def autoscale_configuration(
        self,
    ) -> "ApplicationGatewayAutoscaleConfigurationOutputReference":
        return typing.cast("ApplicationGatewayAutoscaleConfigurationOutputReference", jsii.get(self, "autoscaleConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="backendAddressPool")
    def backend_address_pool(self) -> "ApplicationGatewayBackendAddressPoolList":
        return typing.cast("ApplicationGatewayBackendAddressPoolList", jsii.get(self, "backendAddressPool"))

    @builtins.property
    @jsii.member(jsii_name="backendHttpSettings")
    def backend_http_settings(self) -> "ApplicationGatewayBackendHttpSettingsList":
        return typing.cast("ApplicationGatewayBackendHttpSettingsList", jsii.get(self, "backendHttpSettings"))

    @builtins.property
    @jsii.member(jsii_name="customErrorConfiguration")
    def custom_error_configuration(
        self,
    ) -> "ApplicationGatewayCustomErrorConfigurationList":
        return typing.cast("ApplicationGatewayCustomErrorConfigurationList", jsii.get(self, "customErrorConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="frontendIpConfiguration")
    def frontend_ip_configuration(
        self,
    ) -> "ApplicationGatewayFrontendIpConfigurationList":
        return typing.cast("ApplicationGatewayFrontendIpConfigurationList", jsii.get(self, "frontendIpConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="frontendPort")
    def frontend_port(self) -> "ApplicationGatewayFrontendPortList":
        return typing.cast("ApplicationGatewayFrontendPortList", jsii.get(self, "frontendPort"))

    @builtins.property
    @jsii.member(jsii_name="gatewayIpConfiguration")
    def gateway_ip_configuration(
        self,
    ) -> "ApplicationGatewayGatewayIpConfigurationList":
        return typing.cast("ApplicationGatewayGatewayIpConfigurationList", jsii.get(self, "gatewayIpConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="global")
    def global_(self) -> "ApplicationGatewayGlobalOutputReference":
        return typing.cast("ApplicationGatewayGlobalOutputReference", jsii.get(self, "global"))

    @builtins.property
    @jsii.member(jsii_name="httpListener")
    def http_listener(self) -> "ApplicationGatewayHttpListenerList":
        return typing.cast("ApplicationGatewayHttpListenerList", jsii.get(self, "httpListener"))

    @builtins.property
    @jsii.member(jsii_name="identity")
    def identity(self) -> "ApplicationGatewayIdentityOutputReference":
        return typing.cast("ApplicationGatewayIdentityOutputReference", jsii.get(self, "identity"))

    @builtins.property
    @jsii.member(jsii_name="privateEndpointConnection")
    def private_endpoint_connection(
        self,
    ) -> "ApplicationGatewayPrivateEndpointConnectionList":
        return typing.cast("ApplicationGatewayPrivateEndpointConnectionList", jsii.get(self, "privateEndpointConnection"))

    @builtins.property
    @jsii.member(jsii_name="privateLinkConfiguration")
    def private_link_configuration(
        self,
    ) -> "ApplicationGatewayPrivateLinkConfigurationList":
        return typing.cast("ApplicationGatewayPrivateLinkConfigurationList", jsii.get(self, "privateLinkConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="probe")
    def probe(self) -> "ApplicationGatewayProbeList":
        return typing.cast("ApplicationGatewayProbeList", jsii.get(self, "probe"))

    @builtins.property
    @jsii.member(jsii_name="redirectConfiguration")
    def redirect_configuration(self) -> "ApplicationGatewayRedirectConfigurationList":
        return typing.cast("ApplicationGatewayRedirectConfigurationList", jsii.get(self, "redirectConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="requestRoutingRule")
    def request_routing_rule(self) -> "ApplicationGatewayRequestRoutingRuleList":
        return typing.cast("ApplicationGatewayRequestRoutingRuleList", jsii.get(self, "requestRoutingRule"))

    @builtins.property
    @jsii.member(jsii_name="rewriteRuleSet")
    def rewrite_rule_set(self) -> "ApplicationGatewayRewriteRuleSetList":
        return typing.cast("ApplicationGatewayRewriteRuleSetList", jsii.get(self, "rewriteRuleSet"))

    @builtins.property
    @jsii.member(jsii_name="sku")
    def sku(self) -> "ApplicationGatewaySkuOutputReference":
        return typing.cast("ApplicationGatewaySkuOutputReference", jsii.get(self, "sku"))

    @builtins.property
    @jsii.member(jsii_name="sslCertificate")
    def ssl_certificate(self) -> "ApplicationGatewaySslCertificateList":
        return typing.cast("ApplicationGatewaySslCertificateList", jsii.get(self, "sslCertificate"))

    @builtins.property
    @jsii.member(jsii_name="sslPolicy")
    def ssl_policy(self) -> "ApplicationGatewaySslPolicyOutputReference":
        return typing.cast("ApplicationGatewaySslPolicyOutputReference", jsii.get(self, "sslPolicy"))

    @builtins.property
    @jsii.member(jsii_name="sslProfile")
    def ssl_profile(self) -> "ApplicationGatewaySslProfileList":
        return typing.cast("ApplicationGatewaySslProfileList", jsii.get(self, "sslProfile"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ApplicationGatewayTimeoutsOutputReference":
        return typing.cast("ApplicationGatewayTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="trustedClientCertificate")
    def trusted_client_certificate(
        self,
    ) -> "ApplicationGatewayTrustedClientCertificateList":
        return typing.cast("ApplicationGatewayTrustedClientCertificateList", jsii.get(self, "trustedClientCertificate"))

    @builtins.property
    @jsii.member(jsii_name="trustedRootCertificate")
    def trusted_root_certificate(
        self,
    ) -> "ApplicationGatewayTrustedRootCertificateList":
        return typing.cast("ApplicationGatewayTrustedRootCertificateList", jsii.get(self, "trustedRootCertificate"))

    @builtins.property
    @jsii.member(jsii_name="urlPathMap")
    def url_path_map(self) -> "ApplicationGatewayUrlPathMapList":
        return typing.cast("ApplicationGatewayUrlPathMapList", jsii.get(self, "urlPathMap"))

    @builtins.property
    @jsii.member(jsii_name="wafConfiguration")
    def waf_configuration(self) -> "ApplicationGatewayWafConfigurationOutputReference":
        return typing.cast("ApplicationGatewayWafConfigurationOutputReference", jsii.get(self, "wafConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="authenticationCertificateInput")
    def authentication_certificate_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayAuthenticationCertificate"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayAuthenticationCertificate"]]], jsii.get(self, "authenticationCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="autoscaleConfigurationInput")
    def autoscale_configuration_input(
        self,
    ) -> typing.Optional["ApplicationGatewayAutoscaleConfiguration"]:
        return typing.cast(typing.Optional["ApplicationGatewayAutoscaleConfiguration"], jsii.get(self, "autoscaleConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="backendAddressPoolInput")
    def backend_address_pool_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayBackendAddressPool"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayBackendAddressPool"]]], jsii.get(self, "backendAddressPoolInput"))

    @builtins.property
    @jsii.member(jsii_name="backendHttpSettingsInput")
    def backend_http_settings_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayBackendHttpSettings"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayBackendHttpSettings"]]], jsii.get(self, "backendHttpSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="customErrorConfigurationInput")
    def custom_error_configuration_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayCustomErrorConfiguration"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayCustomErrorConfiguration"]]], jsii.get(self, "customErrorConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="enableHttp2Input")
    def enable_http2_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableHttp2Input"))

    @builtins.property
    @jsii.member(jsii_name="fipsEnabledInput")
    def fips_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "fipsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="firewallPolicyIdInput")
    def firewall_policy_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "firewallPolicyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="forceFirewallPolicyAssociationInput")
    def force_firewall_policy_association_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "forceFirewallPolicyAssociationInput"))

    @builtins.property
    @jsii.member(jsii_name="frontendIpConfigurationInput")
    def frontend_ip_configuration_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayFrontendIpConfiguration"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayFrontendIpConfiguration"]]], jsii.get(self, "frontendIpConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="frontendPortInput")
    def frontend_port_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayFrontendPort"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayFrontendPort"]]], jsii.get(self, "frontendPortInput"))

    @builtins.property
    @jsii.member(jsii_name="gatewayIpConfigurationInput")
    def gateway_ip_configuration_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayGatewayIpConfiguration"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayGatewayIpConfiguration"]]], jsii.get(self, "gatewayIpConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="globalInput")
    def global_input(self) -> typing.Optional["ApplicationGatewayGlobal"]:
        return typing.cast(typing.Optional["ApplicationGatewayGlobal"], jsii.get(self, "globalInput"))

    @builtins.property
    @jsii.member(jsii_name="httpListenerInput")
    def http_listener_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayHttpListener"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayHttpListener"]]], jsii.get(self, "httpListenerInput"))

    @builtins.property
    @jsii.member(jsii_name="identityInput")
    def identity_input(self) -> typing.Optional["ApplicationGatewayIdentity"]:
        return typing.cast(typing.Optional["ApplicationGatewayIdentity"], jsii.get(self, "identityInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="privateLinkConfigurationInput")
    def private_link_configuration_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayPrivateLinkConfiguration"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayPrivateLinkConfiguration"]]], jsii.get(self, "privateLinkConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="probeInput")
    def probe_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayProbe"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayProbe"]]], jsii.get(self, "probeInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectConfigurationInput")
    def redirect_configuration_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayRedirectConfiguration"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayRedirectConfiguration"]]], jsii.get(self, "redirectConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="requestRoutingRuleInput")
    def request_routing_rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayRequestRoutingRule"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayRequestRoutingRule"]]], jsii.get(self, "requestRoutingRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="rewriteRuleSetInput")
    def rewrite_rule_set_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayRewriteRuleSet"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayRewriteRuleSet"]]], jsii.get(self, "rewriteRuleSetInput"))

    @builtins.property
    @jsii.member(jsii_name="skuInput")
    def sku_input(self) -> typing.Optional["ApplicationGatewaySku"]:
        return typing.cast(typing.Optional["ApplicationGatewaySku"], jsii.get(self, "skuInput"))

    @builtins.property
    @jsii.member(jsii_name="sslCertificateInput")
    def ssl_certificate_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewaySslCertificate"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewaySslCertificate"]]], jsii.get(self, "sslCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="sslPolicyInput")
    def ssl_policy_input(self) -> typing.Optional["ApplicationGatewaySslPolicy"]:
        return typing.cast(typing.Optional["ApplicationGatewaySslPolicy"], jsii.get(self, "sslPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="sslProfileInput")
    def ssl_profile_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewaySslProfile"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewaySslProfile"]]], jsii.get(self, "sslProfileInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ApplicationGatewayTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ApplicationGatewayTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="trustedClientCertificateInput")
    def trusted_client_certificate_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayTrustedClientCertificate"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayTrustedClientCertificate"]]], jsii.get(self, "trustedClientCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="trustedRootCertificateInput")
    def trusted_root_certificate_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayTrustedRootCertificate"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayTrustedRootCertificate"]]], jsii.get(self, "trustedRootCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="urlPathMapInput")
    def url_path_map_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayUrlPathMap"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayUrlPathMap"]]], jsii.get(self, "urlPathMapInput"))

    @builtins.property
    @jsii.member(jsii_name="wafConfigurationInput")
    def waf_configuration_input(
        self,
    ) -> typing.Optional["ApplicationGatewayWafConfiguration"]:
        return typing.cast(typing.Optional["ApplicationGatewayWafConfiguration"], jsii.get(self, "wafConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="zonesInput")
    def zones_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "zonesInput"))

    @builtins.property
    @jsii.member(jsii_name="enableHttp2")
    def enable_http2(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableHttp2"))

    @enable_http2.setter
    def enable_http2(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGateway, "enable_http2").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableHttp2", value)

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
            type_hints = typing.get_type_hints(getattr(ApplicationGateway, "fips_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fipsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="firewallPolicyId")
    def firewall_policy_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "firewallPolicyId"))

    @firewall_policy_id.setter
    def firewall_policy_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGateway, "firewall_policy_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firewallPolicyId", value)

    @builtins.property
    @jsii.member(jsii_name="forceFirewallPolicyAssociation")
    def force_firewall_policy_association(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "forceFirewallPolicyAssociation"))

    @force_firewall_policy_association.setter
    def force_firewall_policy_association(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGateway, "force_firewall_policy_association").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceFirewallPolicyAssociation", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGateway, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGateway, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGateway, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGateway, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGateway, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="zones")
    def zones(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "zones"))

    @zones.setter
    def zones(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGateway, "zones").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zones", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayAuthenticationCertificate",
    jsii_struct_bases=[],
    name_mapping={"data": "data", "name": "name"},
)
class ApplicationGatewayAuthenticationCertificate:
    def __init__(self, *, data: builtins.str, name: builtins.str) -> None:
        '''
        :param data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#data ApplicationGateway#data}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayAuthenticationCertificate.__init__)
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "data": data,
            "name": name,
        }

    @builtins.property
    def data(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#data ApplicationGateway#data}.'''
        result = self._values.get("data")
        assert result is not None, "Required property 'data' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewayAuthenticationCertificate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationGatewayAuthenticationCertificateList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayAuthenticationCertificateList",
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
            type_hints = typing.get_type_hints(ApplicationGatewayAuthenticationCertificateList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationGatewayAuthenticationCertificateOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayAuthenticationCertificateList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationGatewayAuthenticationCertificateOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayAuthenticationCertificateList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayAuthenticationCertificateList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayAuthenticationCertificateList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayAuthenticationCertificate]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayAuthenticationCertificate]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayAuthenticationCertificate]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayAuthenticationCertificateList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationGatewayAuthenticationCertificateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayAuthenticationCertificateOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationGatewayAuthenticationCertificateOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="dataInput")
    def data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="data")
    def data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "data"))

    @data.setter
    def data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayAuthenticationCertificateOutputReference, "data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "data", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayAuthenticationCertificateOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationGatewayAuthenticationCertificate, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationGatewayAuthenticationCertificate, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationGatewayAuthenticationCertificate, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayAuthenticationCertificateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayAutoscaleConfiguration",
    jsii_struct_bases=[],
    name_mapping={"min_capacity": "minCapacity", "max_capacity": "maxCapacity"},
)
class ApplicationGatewayAutoscaleConfiguration:
    def __init__(
        self,
        *,
        min_capacity: jsii.Number,
        max_capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param min_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#min_capacity ApplicationGateway#min_capacity}.
        :param max_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#max_capacity ApplicationGateway#max_capacity}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayAutoscaleConfiguration.__init__)
            check_type(argname="argument min_capacity", value=min_capacity, expected_type=type_hints["min_capacity"])
            check_type(argname="argument max_capacity", value=max_capacity, expected_type=type_hints["max_capacity"])
        self._values: typing.Dict[str, typing.Any] = {
            "min_capacity": min_capacity,
        }
        if max_capacity is not None:
            self._values["max_capacity"] = max_capacity

    @builtins.property
    def min_capacity(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#min_capacity ApplicationGateway#min_capacity}.'''
        result = self._values.get("min_capacity")
        assert result is not None, "Required property 'min_capacity' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def max_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#max_capacity ApplicationGateway#max_capacity}.'''
        result = self._values.get("max_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewayAutoscaleConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationGatewayAutoscaleConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayAutoscaleConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationGatewayAutoscaleConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMaxCapacity")
    def reset_max_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxCapacity", []))

    @builtins.property
    @jsii.member(jsii_name="maxCapacityInput")
    def max_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="minCapacityInput")
    def min_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="maxCapacity")
    def max_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxCapacity"))

    @max_capacity.setter
    def max_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayAutoscaleConfigurationOutputReference, "max_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="minCapacity")
    def min_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minCapacity"))

    @min_capacity.setter
    def min_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayAutoscaleConfigurationOutputReference, "min_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ApplicationGatewayAutoscaleConfiguration]:
        return typing.cast(typing.Optional[ApplicationGatewayAutoscaleConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApplicationGatewayAutoscaleConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayAutoscaleConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayBackendAddressPool",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "fqdns": "fqdns", "ip_addresses": "ipAddresses"},
)
class ApplicationGatewayBackendAddressPool:
    def __init__(
        self,
        *,
        name: builtins.str,
        fqdns: typing.Optional[typing.Sequence[builtins.str]] = None,
        ip_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.
        :param fqdns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#fqdns ApplicationGateway#fqdns}.
        :param ip_addresses: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#ip_addresses ApplicationGateway#ip_addresses}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayBackendAddressPool.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument fqdns", value=fqdns, expected_type=type_hints["fqdns"])
            check_type(argname="argument ip_addresses", value=ip_addresses, expected_type=type_hints["ip_addresses"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if fqdns is not None:
            self._values["fqdns"] = fqdns
        if ip_addresses is not None:
            self._values["ip_addresses"] = ip_addresses

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fqdns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#fqdns ApplicationGateway#fqdns}.'''
        result = self._values.get("fqdns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ip_addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#ip_addresses ApplicationGateway#ip_addresses}.'''
        result = self._values.get("ip_addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewayBackendAddressPool(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationGatewayBackendAddressPoolList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayBackendAddressPoolList",
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
            type_hints = typing.get_type_hints(ApplicationGatewayBackendAddressPoolList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationGatewayBackendAddressPoolOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayBackendAddressPoolList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationGatewayBackendAddressPoolOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayBackendAddressPoolList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayBackendAddressPoolList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayBackendAddressPoolList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayBackendAddressPool]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayBackendAddressPool]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayBackendAddressPool]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayBackendAddressPoolList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationGatewayBackendAddressPoolOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayBackendAddressPoolOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationGatewayBackendAddressPoolOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetFqdns")
    def reset_fqdns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFqdns", []))

    @jsii.member(jsii_name="resetIpAddresses")
    def reset_ip_addresses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpAddresses", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="fqdnsInput")
    def fqdns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "fqdnsInput"))

    @builtins.property
    @jsii.member(jsii_name="ipAddressesInput")
    def ip_addresses_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ipAddressesInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="fqdns")
    def fqdns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "fqdns"))

    @fqdns.setter
    def fqdns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayBackendAddressPoolOutputReference, "fqdns").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fqdns", value)

    @builtins.property
    @jsii.member(jsii_name="ipAddresses")
    def ip_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ipAddresses"))

    @ip_addresses.setter
    def ip_addresses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayBackendAddressPoolOutputReference, "ip_addresses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipAddresses", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayBackendAddressPoolOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationGatewayBackendAddressPool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationGatewayBackendAddressPool, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationGatewayBackendAddressPool, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayBackendAddressPoolOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayBackendHttpSettings",
    jsii_struct_bases=[],
    name_mapping={
        "cookie_based_affinity": "cookieBasedAffinity",
        "name": "name",
        "port": "port",
        "protocol": "protocol",
        "affinity_cookie_name": "affinityCookieName",
        "authentication_certificate": "authenticationCertificate",
        "connection_draining": "connectionDraining",
        "host_name": "hostName",
        "path": "path",
        "pick_host_name_from_backend_address": "pickHostNameFromBackendAddress",
        "probe_name": "probeName",
        "request_timeout": "requestTimeout",
        "trusted_root_certificate_names": "trustedRootCertificateNames",
    },
)
class ApplicationGatewayBackendHttpSettings:
    def __init__(
        self,
        *,
        cookie_based_affinity: builtins.str,
        name: builtins.str,
        port: jsii.Number,
        protocol: builtins.str,
        affinity_cookie_name: typing.Optional[builtins.str] = None,
        authentication_certificate: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayBackendHttpSettingsAuthenticationCertificate", typing.Dict[str, typing.Any]]]]] = None,
        connection_draining: typing.Optional[typing.Union["ApplicationGatewayBackendHttpSettingsConnectionDraining", typing.Dict[str, typing.Any]]] = None,
        host_name: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        pick_host_name_from_backend_address: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        probe_name: typing.Optional[builtins.str] = None,
        request_timeout: typing.Optional[jsii.Number] = None,
        trusted_root_certificate_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param cookie_based_affinity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#cookie_based_affinity ApplicationGateway#cookie_based_affinity}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#port ApplicationGateway#port}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#protocol ApplicationGateway#protocol}.
        :param affinity_cookie_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#affinity_cookie_name ApplicationGateway#affinity_cookie_name}.
        :param authentication_certificate: authentication_certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#authentication_certificate ApplicationGateway#authentication_certificate}
        :param connection_draining: connection_draining block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#connection_draining ApplicationGateway#connection_draining}
        :param host_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#host_name ApplicationGateway#host_name}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#path ApplicationGateway#path}.
        :param pick_host_name_from_backend_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#pick_host_name_from_backend_address ApplicationGateway#pick_host_name_from_backend_address}.
        :param probe_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#probe_name ApplicationGateway#probe_name}.
        :param request_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#request_timeout ApplicationGateway#request_timeout}.
        :param trusted_root_certificate_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#trusted_root_certificate_names ApplicationGateway#trusted_root_certificate_names}.
        '''
        if isinstance(connection_draining, dict):
            connection_draining = ApplicationGatewayBackendHttpSettingsConnectionDraining(**connection_draining)
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayBackendHttpSettings.__init__)
            check_type(argname="argument cookie_based_affinity", value=cookie_based_affinity, expected_type=type_hints["cookie_based_affinity"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument affinity_cookie_name", value=affinity_cookie_name, expected_type=type_hints["affinity_cookie_name"])
            check_type(argname="argument authentication_certificate", value=authentication_certificate, expected_type=type_hints["authentication_certificate"])
            check_type(argname="argument connection_draining", value=connection_draining, expected_type=type_hints["connection_draining"])
            check_type(argname="argument host_name", value=host_name, expected_type=type_hints["host_name"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument pick_host_name_from_backend_address", value=pick_host_name_from_backend_address, expected_type=type_hints["pick_host_name_from_backend_address"])
            check_type(argname="argument probe_name", value=probe_name, expected_type=type_hints["probe_name"])
            check_type(argname="argument request_timeout", value=request_timeout, expected_type=type_hints["request_timeout"])
            check_type(argname="argument trusted_root_certificate_names", value=trusted_root_certificate_names, expected_type=type_hints["trusted_root_certificate_names"])
        self._values: typing.Dict[str, typing.Any] = {
            "cookie_based_affinity": cookie_based_affinity,
            "name": name,
            "port": port,
            "protocol": protocol,
        }
        if affinity_cookie_name is not None:
            self._values["affinity_cookie_name"] = affinity_cookie_name
        if authentication_certificate is not None:
            self._values["authentication_certificate"] = authentication_certificate
        if connection_draining is not None:
            self._values["connection_draining"] = connection_draining
        if host_name is not None:
            self._values["host_name"] = host_name
        if path is not None:
            self._values["path"] = path
        if pick_host_name_from_backend_address is not None:
            self._values["pick_host_name_from_backend_address"] = pick_host_name_from_backend_address
        if probe_name is not None:
            self._values["probe_name"] = probe_name
        if request_timeout is not None:
            self._values["request_timeout"] = request_timeout
        if trusted_root_certificate_names is not None:
            self._values["trusted_root_certificate_names"] = trusted_root_certificate_names

    @builtins.property
    def cookie_based_affinity(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#cookie_based_affinity ApplicationGateway#cookie_based_affinity}.'''
        result = self._values.get("cookie_based_affinity")
        assert result is not None, "Required property 'cookie_based_affinity' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#port ApplicationGateway#port}.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#protocol ApplicationGateway#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def affinity_cookie_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#affinity_cookie_name ApplicationGateway#affinity_cookie_name}.'''
        result = self._values.get("affinity_cookie_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def authentication_certificate(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayBackendHttpSettingsAuthenticationCertificate"]]]:
        '''authentication_certificate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#authentication_certificate ApplicationGateway#authentication_certificate}
        '''
        result = self._values.get("authentication_certificate")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayBackendHttpSettingsAuthenticationCertificate"]]], result)

    @builtins.property
    def connection_draining(
        self,
    ) -> typing.Optional["ApplicationGatewayBackendHttpSettingsConnectionDraining"]:
        '''connection_draining block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#connection_draining ApplicationGateway#connection_draining}
        '''
        result = self._values.get("connection_draining")
        return typing.cast(typing.Optional["ApplicationGatewayBackendHttpSettingsConnectionDraining"], result)

    @builtins.property
    def host_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#host_name ApplicationGateway#host_name}.'''
        result = self._values.get("host_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#path ApplicationGateway#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pick_host_name_from_backend_address(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#pick_host_name_from_backend_address ApplicationGateway#pick_host_name_from_backend_address}.'''
        result = self._values.get("pick_host_name_from_backend_address")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def probe_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#probe_name ApplicationGateway#probe_name}.'''
        result = self._values.get("probe_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#request_timeout ApplicationGateway#request_timeout}.'''
        result = self._values.get("request_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def trusted_root_certificate_names(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#trusted_root_certificate_names ApplicationGateway#trusted_root_certificate_names}.'''
        result = self._values.get("trusted_root_certificate_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewayBackendHttpSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayBackendHttpSettingsAuthenticationCertificate",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class ApplicationGatewayBackendHttpSettingsAuthenticationCertificate:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayBackendHttpSettingsAuthenticationCertificate.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewayBackendHttpSettingsAuthenticationCertificate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationGatewayBackendHttpSettingsAuthenticationCertificateList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayBackendHttpSettingsAuthenticationCertificateList",
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
            type_hints = typing.get_type_hints(ApplicationGatewayBackendHttpSettingsAuthenticationCertificateList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationGatewayBackendHttpSettingsAuthenticationCertificateOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayBackendHttpSettingsAuthenticationCertificateList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationGatewayBackendHttpSettingsAuthenticationCertificateOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayBackendHttpSettingsAuthenticationCertificateList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayBackendHttpSettingsAuthenticationCertificateList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayBackendHttpSettingsAuthenticationCertificateList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayBackendHttpSettingsAuthenticationCertificate]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayBackendHttpSettingsAuthenticationCertificate]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayBackendHttpSettingsAuthenticationCertificate]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayBackendHttpSettingsAuthenticationCertificateList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationGatewayBackendHttpSettingsAuthenticationCertificateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayBackendHttpSettingsAuthenticationCertificateOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationGatewayBackendHttpSettingsAuthenticationCertificateOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayBackendHttpSettingsAuthenticationCertificateOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationGatewayBackendHttpSettingsAuthenticationCertificate, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationGatewayBackendHttpSettingsAuthenticationCertificate, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationGatewayBackendHttpSettingsAuthenticationCertificate, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayBackendHttpSettingsAuthenticationCertificateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayBackendHttpSettingsConnectionDraining",
    jsii_struct_bases=[],
    name_mapping={"drain_timeout_sec": "drainTimeoutSec", "enabled": "enabled"},
)
class ApplicationGatewayBackendHttpSettingsConnectionDraining:
    def __init__(
        self,
        *,
        drain_timeout_sec: jsii.Number,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param drain_timeout_sec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#drain_timeout_sec ApplicationGateway#drain_timeout_sec}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#enabled ApplicationGateway#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayBackendHttpSettingsConnectionDraining.__init__)
            check_type(argname="argument drain_timeout_sec", value=drain_timeout_sec, expected_type=type_hints["drain_timeout_sec"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "drain_timeout_sec": drain_timeout_sec,
            "enabled": enabled,
        }

    @builtins.property
    def drain_timeout_sec(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#drain_timeout_sec ApplicationGateway#drain_timeout_sec}.'''
        result = self._values.get("drain_timeout_sec")
        assert result is not None, "Required property 'drain_timeout_sec' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#enabled ApplicationGateway#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewayBackendHttpSettingsConnectionDraining(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationGatewayBackendHttpSettingsConnectionDrainingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayBackendHttpSettingsConnectionDrainingOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationGatewayBackendHttpSettingsConnectionDrainingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="drainTimeoutSecInput")
    def drain_timeout_sec_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "drainTimeoutSecInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="drainTimeoutSec")
    def drain_timeout_sec(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "drainTimeoutSec"))

    @drain_timeout_sec.setter
    def drain_timeout_sec(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayBackendHttpSettingsConnectionDrainingOutputReference, "drain_timeout_sec").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "drainTimeoutSec", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayBackendHttpSettingsConnectionDrainingOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ApplicationGatewayBackendHttpSettingsConnectionDraining]:
        return typing.cast(typing.Optional[ApplicationGatewayBackendHttpSettingsConnectionDraining], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApplicationGatewayBackendHttpSettingsConnectionDraining],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayBackendHttpSettingsConnectionDrainingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationGatewayBackendHttpSettingsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayBackendHttpSettingsList",
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
            type_hints = typing.get_type_hints(ApplicationGatewayBackendHttpSettingsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationGatewayBackendHttpSettingsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayBackendHttpSettingsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationGatewayBackendHttpSettingsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayBackendHttpSettingsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayBackendHttpSettingsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayBackendHttpSettingsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayBackendHttpSettings]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayBackendHttpSettings]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayBackendHttpSettings]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayBackendHttpSettingsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationGatewayBackendHttpSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayBackendHttpSettingsOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationGatewayBackendHttpSettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAuthenticationCertificate")
    def put_authentication_certificate(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApplicationGatewayBackendHttpSettingsAuthenticationCertificate, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayBackendHttpSettingsOutputReference.put_authentication_certificate)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAuthenticationCertificate", [value]))

    @jsii.member(jsii_name="putConnectionDraining")
    def put_connection_draining(
        self,
        *,
        drain_timeout_sec: jsii.Number,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param drain_timeout_sec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#drain_timeout_sec ApplicationGateway#drain_timeout_sec}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#enabled ApplicationGateway#enabled}.
        '''
        value = ApplicationGatewayBackendHttpSettingsConnectionDraining(
            drain_timeout_sec=drain_timeout_sec, enabled=enabled
        )

        return typing.cast(None, jsii.invoke(self, "putConnectionDraining", [value]))

    @jsii.member(jsii_name="resetAffinityCookieName")
    def reset_affinity_cookie_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAffinityCookieName", []))

    @jsii.member(jsii_name="resetAuthenticationCertificate")
    def reset_authentication_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthenticationCertificate", []))

    @jsii.member(jsii_name="resetConnectionDraining")
    def reset_connection_draining(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionDraining", []))

    @jsii.member(jsii_name="resetHostName")
    def reset_host_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostName", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetPickHostNameFromBackendAddress")
    def reset_pick_host_name_from_backend_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPickHostNameFromBackendAddress", []))

    @jsii.member(jsii_name="resetProbeName")
    def reset_probe_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProbeName", []))

    @jsii.member(jsii_name="resetRequestTimeout")
    def reset_request_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestTimeout", []))

    @jsii.member(jsii_name="resetTrustedRootCertificateNames")
    def reset_trusted_root_certificate_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrustedRootCertificateNames", []))

    @builtins.property
    @jsii.member(jsii_name="authenticationCertificate")
    def authentication_certificate(
        self,
    ) -> ApplicationGatewayBackendHttpSettingsAuthenticationCertificateList:
        return typing.cast(ApplicationGatewayBackendHttpSettingsAuthenticationCertificateList, jsii.get(self, "authenticationCertificate"))

    @builtins.property
    @jsii.member(jsii_name="connectionDraining")
    def connection_draining(
        self,
    ) -> ApplicationGatewayBackendHttpSettingsConnectionDrainingOutputReference:
        return typing.cast(ApplicationGatewayBackendHttpSettingsConnectionDrainingOutputReference, jsii.get(self, "connectionDraining"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="probeId")
    def probe_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "probeId"))

    @builtins.property
    @jsii.member(jsii_name="affinityCookieNameInput")
    def affinity_cookie_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "affinityCookieNameInput"))

    @builtins.property
    @jsii.member(jsii_name="authenticationCertificateInput")
    def authentication_certificate_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayBackendHttpSettingsAuthenticationCertificate]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayBackendHttpSettingsAuthenticationCertificate]]], jsii.get(self, "authenticationCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionDrainingInput")
    def connection_draining_input(
        self,
    ) -> typing.Optional[ApplicationGatewayBackendHttpSettingsConnectionDraining]:
        return typing.cast(typing.Optional[ApplicationGatewayBackendHttpSettingsConnectionDraining], jsii.get(self, "connectionDrainingInput"))

    @builtins.property
    @jsii.member(jsii_name="cookieBasedAffinityInput")
    def cookie_based_affinity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cookieBasedAffinityInput"))

    @builtins.property
    @jsii.member(jsii_name="hostNameInput")
    def host_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostNameInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="pickHostNameFromBackendAddressInput")
    def pick_host_name_from_backend_address_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "pickHostNameFromBackendAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="probeNameInput")
    def probe_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "probeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="requestTimeoutInput")
    def request_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "requestTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="trustedRootCertificateNamesInput")
    def trusted_root_certificate_names_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "trustedRootCertificateNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="affinityCookieName")
    def affinity_cookie_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "affinityCookieName"))

    @affinity_cookie_name.setter
    def affinity_cookie_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayBackendHttpSettingsOutputReference, "affinity_cookie_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "affinityCookieName", value)

    @builtins.property
    @jsii.member(jsii_name="cookieBasedAffinity")
    def cookie_based_affinity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cookieBasedAffinity"))

    @cookie_based_affinity.setter
    def cookie_based_affinity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayBackendHttpSettingsOutputReference, "cookie_based_affinity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cookieBasedAffinity", value)

    @builtins.property
    @jsii.member(jsii_name="hostName")
    def host_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostName"))

    @host_name.setter
    def host_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayBackendHttpSettingsOutputReference, "host_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostName", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayBackendHttpSettingsOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayBackendHttpSettingsOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="pickHostNameFromBackendAddress")
    def pick_host_name_from_backend_address(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "pickHostNameFromBackendAddress"))

    @pick_host_name_from_backend_address.setter
    def pick_host_name_from_backend_address(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayBackendHttpSettingsOutputReference, "pick_host_name_from_backend_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pickHostNameFromBackendAddress", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayBackendHttpSettingsOutputReference, "port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="probeName")
    def probe_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "probeName"))

    @probe_name.setter
    def probe_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayBackendHttpSettingsOutputReference, "probe_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "probeName", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayBackendHttpSettingsOutputReference, "protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="requestTimeout")
    def request_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "requestTimeout"))

    @request_timeout.setter
    def request_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayBackendHttpSettingsOutputReference, "request_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="trustedRootCertificateNames")
    def trusted_root_certificate_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "trustedRootCertificateNames"))

    @trusted_root_certificate_names.setter
    def trusted_root_certificate_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayBackendHttpSettingsOutputReference, "trusted_root_certificate_names").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trustedRootCertificateNames", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationGatewayBackendHttpSettings, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationGatewayBackendHttpSettings, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationGatewayBackendHttpSettings, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayBackendHttpSettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "backend_address_pool": "backendAddressPool",
        "backend_http_settings": "backendHttpSettings",
        "frontend_ip_configuration": "frontendIpConfiguration",
        "frontend_port": "frontendPort",
        "gateway_ip_configuration": "gatewayIpConfiguration",
        "http_listener": "httpListener",
        "location": "location",
        "name": "name",
        "request_routing_rule": "requestRoutingRule",
        "resource_group_name": "resourceGroupName",
        "sku": "sku",
        "authentication_certificate": "authenticationCertificate",
        "autoscale_configuration": "autoscaleConfiguration",
        "custom_error_configuration": "customErrorConfiguration",
        "enable_http2": "enableHttp2",
        "fips_enabled": "fipsEnabled",
        "firewall_policy_id": "firewallPolicyId",
        "force_firewall_policy_association": "forceFirewallPolicyAssociation",
        "global_": "global",
        "id": "id",
        "identity": "identity",
        "private_link_configuration": "privateLinkConfiguration",
        "probe": "probe",
        "redirect_configuration": "redirectConfiguration",
        "rewrite_rule_set": "rewriteRuleSet",
        "ssl_certificate": "sslCertificate",
        "ssl_policy": "sslPolicy",
        "ssl_profile": "sslProfile",
        "tags": "tags",
        "timeouts": "timeouts",
        "trusted_client_certificate": "trustedClientCertificate",
        "trusted_root_certificate": "trustedRootCertificate",
        "url_path_map": "urlPathMap",
        "waf_configuration": "wafConfiguration",
        "zones": "zones",
    },
)
class ApplicationGatewayConfig(cdktf.TerraformMetaArguments):
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
        backend_address_pool: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApplicationGatewayBackendAddressPool, typing.Dict[str, typing.Any]]]],
        backend_http_settings: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApplicationGatewayBackendHttpSettings, typing.Dict[str, typing.Any]]]],
        frontend_ip_configuration: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayFrontendIpConfiguration", typing.Dict[str, typing.Any]]]],
        frontend_port: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayFrontendPort", typing.Dict[str, typing.Any]]]],
        gateway_ip_configuration: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayGatewayIpConfiguration", typing.Dict[str, typing.Any]]]],
        http_listener: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayHttpListener", typing.Dict[str, typing.Any]]]],
        location: builtins.str,
        name: builtins.str,
        request_routing_rule: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayRequestRoutingRule", typing.Dict[str, typing.Any]]]],
        resource_group_name: builtins.str,
        sku: typing.Union["ApplicationGatewaySku", typing.Dict[str, typing.Any]],
        authentication_certificate: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApplicationGatewayAuthenticationCertificate, typing.Dict[str, typing.Any]]]]] = None,
        autoscale_configuration: typing.Optional[typing.Union[ApplicationGatewayAutoscaleConfiguration, typing.Dict[str, typing.Any]]] = None,
        custom_error_configuration: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayCustomErrorConfiguration", typing.Dict[str, typing.Any]]]]] = None,
        enable_http2: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        fips_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        firewall_policy_id: typing.Optional[builtins.str] = None,
        force_firewall_policy_association: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        global_: typing.Optional[typing.Union["ApplicationGatewayGlobal", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["ApplicationGatewayIdentity", typing.Dict[str, typing.Any]]] = None,
        private_link_configuration: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayPrivateLinkConfiguration", typing.Dict[str, typing.Any]]]]] = None,
        probe: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayProbe", typing.Dict[str, typing.Any]]]]] = None,
        redirect_configuration: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayRedirectConfiguration", typing.Dict[str, typing.Any]]]]] = None,
        rewrite_rule_set: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayRewriteRuleSet", typing.Dict[str, typing.Any]]]]] = None,
        ssl_certificate: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewaySslCertificate", typing.Dict[str, typing.Any]]]]] = None,
        ssl_policy: typing.Optional[typing.Union["ApplicationGatewaySslPolicy", typing.Dict[str, typing.Any]]] = None,
        ssl_profile: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewaySslProfile", typing.Dict[str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ApplicationGatewayTimeouts", typing.Dict[str, typing.Any]]] = None,
        trusted_client_certificate: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayTrustedClientCertificate", typing.Dict[str, typing.Any]]]]] = None,
        trusted_root_certificate: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayTrustedRootCertificate", typing.Dict[str, typing.Any]]]]] = None,
        url_path_map: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayUrlPathMap", typing.Dict[str, typing.Any]]]]] = None,
        waf_configuration: typing.Optional[typing.Union["ApplicationGatewayWafConfiguration", typing.Dict[str, typing.Any]]] = None,
        zones: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param backend_address_pool: backend_address_pool block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#backend_address_pool ApplicationGateway#backend_address_pool}
        :param backend_http_settings: backend_http_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#backend_http_settings ApplicationGateway#backend_http_settings}
        :param frontend_ip_configuration: frontend_ip_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#frontend_ip_configuration ApplicationGateway#frontend_ip_configuration}
        :param frontend_port: frontend_port block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#frontend_port ApplicationGateway#frontend_port}
        :param gateway_ip_configuration: gateway_ip_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#gateway_ip_configuration ApplicationGateway#gateway_ip_configuration}
        :param http_listener: http_listener block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#http_listener ApplicationGateway#http_listener}
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#location ApplicationGateway#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.
        :param request_routing_rule: request_routing_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#request_routing_rule ApplicationGateway#request_routing_rule}
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#resource_group_name ApplicationGateway#resource_group_name}.
        :param sku: sku block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#sku ApplicationGateway#sku}
        :param authentication_certificate: authentication_certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#authentication_certificate ApplicationGateway#authentication_certificate}
        :param autoscale_configuration: autoscale_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#autoscale_configuration ApplicationGateway#autoscale_configuration}
        :param custom_error_configuration: custom_error_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#custom_error_configuration ApplicationGateway#custom_error_configuration}
        :param enable_http2: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#enable_http2 ApplicationGateway#enable_http2}.
        :param fips_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#fips_enabled ApplicationGateway#fips_enabled}.
        :param firewall_policy_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#firewall_policy_id ApplicationGateway#firewall_policy_id}.
        :param force_firewall_policy_association: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#force_firewall_policy_association ApplicationGateway#force_firewall_policy_association}.
        :param global_: global block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#global ApplicationGateway#global}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#id ApplicationGateway#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#identity ApplicationGateway#identity}
        :param private_link_configuration: private_link_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#private_link_configuration ApplicationGateway#private_link_configuration}
        :param probe: probe block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#probe ApplicationGateway#probe}
        :param redirect_configuration: redirect_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#redirect_configuration ApplicationGateway#redirect_configuration}
        :param rewrite_rule_set: rewrite_rule_set block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#rewrite_rule_set ApplicationGateway#rewrite_rule_set}
        :param ssl_certificate: ssl_certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#ssl_certificate ApplicationGateway#ssl_certificate}
        :param ssl_policy: ssl_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#ssl_policy ApplicationGateway#ssl_policy}
        :param ssl_profile: ssl_profile block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#ssl_profile ApplicationGateway#ssl_profile}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#tags ApplicationGateway#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#timeouts ApplicationGateway#timeouts}
        :param trusted_client_certificate: trusted_client_certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#trusted_client_certificate ApplicationGateway#trusted_client_certificate}
        :param trusted_root_certificate: trusted_root_certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#trusted_root_certificate ApplicationGateway#trusted_root_certificate}
        :param url_path_map: url_path_map block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#url_path_map ApplicationGateway#url_path_map}
        :param waf_configuration: waf_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#waf_configuration ApplicationGateway#waf_configuration}
        :param zones: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#zones ApplicationGateway#zones}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(sku, dict):
            sku = ApplicationGatewaySku(**sku)
        if isinstance(autoscale_configuration, dict):
            autoscale_configuration = ApplicationGatewayAutoscaleConfiguration(**autoscale_configuration)
        if isinstance(global_, dict):
            global_ = ApplicationGatewayGlobal(**global_)
        if isinstance(identity, dict):
            identity = ApplicationGatewayIdentity(**identity)
        if isinstance(ssl_policy, dict):
            ssl_policy = ApplicationGatewaySslPolicy(**ssl_policy)
        if isinstance(timeouts, dict):
            timeouts = ApplicationGatewayTimeouts(**timeouts)
        if isinstance(waf_configuration, dict):
            waf_configuration = ApplicationGatewayWafConfiguration(**waf_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument backend_address_pool", value=backend_address_pool, expected_type=type_hints["backend_address_pool"])
            check_type(argname="argument backend_http_settings", value=backend_http_settings, expected_type=type_hints["backend_http_settings"])
            check_type(argname="argument frontend_ip_configuration", value=frontend_ip_configuration, expected_type=type_hints["frontend_ip_configuration"])
            check_type(argname="argument frontend_port", value=frontend_port, expected_type=type_hints["frontend_port"])
            check_type(argname="argument gateway_ip_configuration", value=gateway_ip_configuration, expected_type=type_hints["gateway_ip_configuration"])
            check_type(argname="argument http_listener", value=http_listener, expected_type=type_hints["http_listener"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument request_routing_rule", value=request_routing_rule, expected_type=type_hints["request_routing_rule"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument sku", value=sku, expected_type=type_hints["sku"])
            check_type(argname="argument authentication_certificate", value=authentication_certificate, expected_type=type_hints["authentication_certificate"])
            check_type(argname="argument autoscale_configuration", value=autoscale_configuration, expected_type=type_hints["autoscale_configuration"])
            check_type(argname="argument custom_error_configuration", value=custom_error_configuration, expected_type=type_hints["custom_error_configuration"])
            check_type(argname="argument enable_http2", value=enable_http2, expected_type=type_hints["enable_http2"])
            check_type(argname="argument fips_enabled", value=fips_enabled, expected_type=type_hints["fips_enabled"])
            check_type(argname="argument firewall_policy_id", value=firewall_policy_id, expected_type=type_hints["firewall_policy_id"])
            check_type(argname="argument force_firewall_policy_association", value=force_firewall_policy_association, expected_type=type_hints["force_firewall_policy_association"])
            check_type(argname="argument global_", value=global_, expected_type=type_hints["global_"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument private_link_configuration", value=private_link_configuration, expected_type=type_hints["private_link_configuration"])
            check_type(argname="argument probe", value=probe, expected_type=type_hints["probe"])
            check_type(argname="argument redirect_configuration", value=redirect_configuration, expected_type=type_hints["redirect_configuration"])
            check_type(argname="argument rewrite_rule_set", value=rewrite_rule_set, expected_type=type_hints["rewrite_rule_set"])
            check_type(argname="argument ssl_certificate", value=ssl_certificate, expected_type=type_hints["ssl_certificate"])
            check_type(argname="argument ssl_policy", value=ssl_policy, expected_type=type_hints["ssl_policy"])
            check_type(argname="argument ssl_profile", value=ssl_profile, expected_type=type_hints["ssl_profile"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument trusted_client_certificate", value=trusted_client_certificate, expected_type=type_hints["trusted_client_certificate"])
            check_type(argname="argument trusted_root_certificate", value=trusted_root_certificate, expected_type=type_hints["trusted_root_certificate"])
            check_type(argname="argument url_path_map", value=url_path_map, expected_type=type_hints["url_path_map"])
            check_type(argname="argument waf_configuration", value=waf_configuration, expected_type=type_hints["waf_configuration"])
            check_type(argname="argument zones", value=zones, expected_type=type_hints["zones"])
        self._values: typing.Dict[str, typing.Any] = {
            "backend_address_pool": backend_address_pool,
            "backend_http_settings": backend_http_settings,
            "frontend_ip_configuration": frontend_ip_configuration,
            "frontend_port": frontend_port,
            "gateway_ip_configuration": gateway_ip_configuration,
            "http_listener": http_listener,
            "location": location,
            "name": name,
            "request_routing_rule": request_routing_rule,
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
        if authentication_certificate is not None:
            self._values["authentication_certificate"] = authentication_certificate
        if autoscale_configuration is not None:
            self._values["autoscale_configuration"] = autoscale_configuration
        if custom_error_configuration is not None:
            self._values["custom_error_configuration"] = custom_error_configuration
        if enable_http2 is not None:
            self._values["enable_http2"] = enable_http2
        if fips_enabled is not None:
            self._values["fips_enabled"] = fips_enabled
        if firewall_policy_id is not None:
            self._values["firewall_policy_id"] = firewall_policy_id
        if force_firewall_policy_association is not None:
            self._values["force_firewall_policy_association"] = force_firewall_policy_association
        if global_ is not None:
            self._values["global_"] = global_
        if id is not None:
            self._values["id"] = id
        if identity is not None:
            self._values["identity"] = identity
        if private_link_configuration is not None:
            self._values["private_link_configuration"] = private_link_configuration
        if probe is not None:
            self._values["probe"] = probe
        if redirect_configuration is not None:
            self._values["redirect_configuration"] = redirect_configuration
        if rewrite_rule_set is not None:
            self._values["rewrite_rule_set"] = rewrite_rule_set
        if ssl_certificate is not None:
            self._values["ssl_certificate"] = ssl_certificate
        if ssl_policy is not None:
            self._values["ssl_policy"] = ssl_policy
        if ssl_profile is not None:
            self._values["ssl_profile"] = ssl_profile
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if trusted_client_certificate is not None:
            self._values["trusted_client_certificate"] = trusted_client_certificate
        if trusted_root_certificate is not None:
            self._values["trusted_root_certificate"] = trusted_root_certificate
        if url_path_map is not None:
            self._values["url_path_map"] = url_path_map
        if waf_configuration is not None:
            self._values["waf_configuration"] = waf_configuration
        if zones is not None:
            self._values["zones"] = zones

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
    def backend_address_pool(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayBackendAddressPool]]:
        '''backend_address_pool block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#backend_address_pool ApplicationGateway#backend_address_pool}
        '''
        result = self._values.get("backend_address_pool")
        assert result is not None, "Required property 'backend_address_pool' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayBackendAddressPool]], result)

    @builtins.property
    def backend_http_settings(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayBackendHttpSettings]]:
        '''backend_http_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#backend_http_settings ApplicationGateway#backend_http_settings}
        '''
        result = self._values.get("backend_http_settings")
        assert result is not None, "Required property 'backend_http_settings' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayBackendHttpSettings]], result)

    @builtins.property
    def frontend_ip_configuration(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayFrontendIpConfiguration"]]:
        '''frontend_ip_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#frontend_ip_configuration ApplicationGateway#frontend_ip_configuration}
        '''
        result = self._values.get("frontend_ip_configuration")
        assert result is not None, "Required property 'frontend_ip_configuration' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayFrontendIpConfiguration"]], result)

    @builtins.property
    def frontend_port(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayFrontendPort"]]:
        '''frontend_port block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#frontend_port ApplicationGateway#frontend_port}
        '''
        result = self._values.get("frontend_port")
        assert result is not None, "Required property 'frontend_port' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayFrontendPort"]], result)

    @builtins.property
    def gateway_ip_configuration(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayGatewayIpConfiguration"]]:
        '''gateway_ip_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#gateway_ip_configuration ApplicationGateway#gateway_ip_configuration}
        '''
        result = self._values.get("gateway_ip_configuration")
        assert result is not None, "Required property 'gateway_ip_configuration' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayGatewayIpConfiguration"]], result)

    @builtins.property
    def http_listener(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayHttpListener"]]:
        '''http_listener block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#http_listener ApplicationGateway#http_listener}
        '''
        result = self._values.get("http_listener")
        assert result is not None, "Required property 'http_listener' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayHttpListener"]], result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#location ApplicationGateway#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def request_routing_rule(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayRequestRoutingRule"]]:
        '''request_routing_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#request_routing_rule ApplicationGateway#request_routing_rule}
        '''
        result = self._values.get("request_routing_rule")
        assert result is not None, "Required property 'request_routing_rule' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayRequestRoutingRule"]], result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#resource_group_name ApplicationGateway#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sku(self) -> "ApplicationGatewaySku":
        '''sku block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#sku ApplicationGateway#sku}
        '''
        result = self._values.get("sku")
        assert result is not None, "Required property 'sku' is missing"
        return typing.cast("ApplicationGatewaySku", result)

    @builtins.property
    def authentication_certificate(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayAuthenticationCertificate]]]:
        '''authentication_certificate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#authentication_certificate ApplicationGateway#authentication_certificate}
        '''
        result = self._values.get("authentication_certificate")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayAuthenticationCertificate]]], result)

    @builtins.property
    def autoscale_configuration(
        self,
    ) -> typing.Optional[ApplicationGatewayAutoscaleConfiguration]:
        '''autoscale_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#autoscale_configuration ApplicationGateway#autoscale_configuration}
        '''
        result = self._values.get("autoscale_configuration")
        return typing.cast(typing.Optional[ApplicationGatewayAutoscaleConfiguration], result)

    @builtins.property
    def custom_error_configuration(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayCustomErrorConfiguration"]]]:
        '''custom_error_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#custom_error_configuration ApplicationGateway#custom_error_configuration}
        '''
        result = self._values.get("custom_error_configuration")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayCustomErrorConfiguration"]]], result)

    @builtins.property
    def enable_http2(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#enable_http2 ApplicationGateway#enable_http2}.'''
        result = self._values.get("enable_http2")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def fips_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#fips_enabled ApplicationGateway#fips_enabled}.'''
        result = self._values.get("fips_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def firewall_policy_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#firewall_policy_id ApplicationGateway#firewall_policy_id}.'''
        result = self._values.get("firewall_policy_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def force_firewall_policy_association(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#force_firewall_policy_association ApplicationGateway#force_firewall_policy_association}.'''
        result = self._values.get("force_firewall_policy_association")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def global_(self) -> typing.Optional["ApplicationGatewayGlobal"]:
        '''global block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#global ApplicationGateway#global}
        '''
        result = self._values.get("global_")
        return typing.cast(typing.Optional["ApplicationGatewayGlobal"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#id ApplicationGateway#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity(self) -> typing.Optional["ApplicationGatewayIdentity"]:
        '''identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#identity ApplicationGateway#identity}
        '''
        result = self._values.get("identity")
        return typing.cast(typing.Optional["ApplicationGatewayIdentity"], result)

    @builtins.property
    def private_link_configuration(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayPrivateLinkConfiguration"]]]:
        '''private_link_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#private_link_configuration ApplicationGateway#private_link_configuration}
        '''
        result = self._values.get("private_link_configuration")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayPrivateLinkConfiguration"]]], result)

    @builtins.property
    def probe(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayProbe"]]]:
        '''probe block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#probe ApplicationGateway#probe}
        '''
        result = self._values.get("probe")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayProbe"]]], result)

    @builtins.property
    def redirect_configuration(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayRedirectConfiguration"]]]:
        '''redirect_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#redirect_configuration ApplicationGateway#redirect_configuration}
        '''
        result = self._values.get("redirect_configuration")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayRedirectConfiguration"]]], result)

    @builtins.property
    def rewrite_rule_set(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayRewriteRuleSet"]]]:
        '''rewrite_rule_set block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#rewrite_rule_set ApplicationGateway#rewrite_rule_set}
        '''
        result = self._values.get("rewrite_rule_set")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayRewriteRuleSet"]]], result)

    @builtins.property
    def ssl_certificate(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewaySslCertificate"]]]:
        '''ssl_certificate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#ssl_certificate ApplicationGateway#ssl_certificate}
        '''
        result = self._values.get("ssl_certificate")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewaySslCertificate"]]], result)

    @builtins.property
    def ssl_policy(self) -> typing.Optional["ApplicationGatewaySslPolicy"]:
        '''ssl_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#ssl_policy ApplicationGateway#ssl_policy}
        '''
        result = self._values.get("ssl_policy")
        return typing.cast(typing.Optional["ApplicationGatewaySslPolicy"], result)

    @builtins.property
    def ssl_profile(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewaySslProfile"]]]:
        '''ssl_profile block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#ssl_profile ApplicationGateway#ssl_profile}
        '''
        result = self._values.get("ssl_profile")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewaySslProfile"]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#tags ApplicationGateway#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ApplicationGatewayTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#timeouts ApplicationGateway#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ApplicationGatewayTimeouts"], result)

    @builtins.property
    def trusted_client_certificate(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayTrustedClientCertificate"]]]:
        '''trusted_client_certificate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#trusted_client_certificate ApplicationGateway#trusted_client_certificate}
        '''
        result = self._values.get("trusted_client_certificate")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayTrustedClientCertificate"]]], result)

    @builtins.property
    def trusted_root_certificate(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayTrustedRootCertificate"]]]:
        '''trusted_root_certificate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#trusted_root_certificate ApplicationGateway#trusted_root_certificate}
        '''
        result = self._values.get("trusted_root_certificate")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayTrustedRootCertificate"]]], result)

    @builtins.property
    def url_path_map(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayUrlPathMap"]]]:
        '''url_path_map block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#url_path_map ApplicationGateway#url_path_map}
        '''
        result = self._values.get("url_path_map")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayUrlPathMap"]]], result)

    @builtins.property
    def waf_configuration(
        self,
    ) -> typing.Optional["ApplicationGatewayWafConfiguration"]:
        '''waf_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#waf_configuration ApplicationGateway#waf_configuration}
        '''
        result = self._values.get("waf_configuration")
        return typing.cast(typing.Optional["ApplicationGatewayWafConfiguration"], result)

    @builtins.property
    def zones(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#zones ApplicationGateway#zones}.'''
        result = self._values.get("zones")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewayConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayCustomErrorConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "custom_error_page_url": "customErrorPageUrl",
        "status_code": "statusCode",
    },
)
class ApplicationGatewayCustomErrorConfiguration:
    def __init__(
        self,
        *,
        custom_error_page_url: builtins.str,
        status_code: builtins.str,
    ) -> None:
        '''
        :param custom_error_page_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#custom_error_page_url ApplicationGateway#custom_error_page_url}.
        :param status_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#status_code ApplicationGateway#status_code}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayCustomErrorConfiguration.__init__)
            check_type(argname="argument custom_error_page_url", value=custom_error_page_url, expected_type=type_hints["custom_error_page_url"])
            check_type(argname="argument status_code", value=status_code, expected_type=type_hints["status_code"])
        self._values: typing.Dict[str, typing.Any] = {
            "custom_error_page_url": custom_error_page_url,
            "status_code": status_code,
        }

    @builtins.property
    def custom_error_page_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#custom_error_page_url ApplicationGateway#custom_error_page_url}.'''
        result = self._values.get("custom_error_page_url")
        assert result is not None, "Required property 'custom_error_page_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def status_code(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#status_code ApplicationGateway#status_code}.'''
        result = self._values.get("status_code")
        assert result is not None, "Required property 'status_code' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewayCustomErrorConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationGatewayCustomErrorConfigurationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayCustomErrorConfigurationList",
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
            type_hints = typing.get_type_hints(ApplicationGatewayCustomErrorConfigurationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationGatewayCustomErrorConfigurationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayCustomErrorConfigurationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationGatewayCustomErrorConfigurationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayCustomErrorConfigurationList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayCustomErrorConfigurationList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayCustomErrorConfigurationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayCustomErrorConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayCustomErrorConfiguration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayCustomErrorConfiguration]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayCustomErrorConfigurationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationGatewayCustomErrorConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayCustomErrorConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationGatewayCustomErrorConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="customErrorPageUrlInput")
    def custom_error_page_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customErrorPageUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="statusCodeInput")
    def status_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="customErrorPageUrl")
    def custom_error_page_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customErrorPageUrl"))

    @custom_error_page_url.setter
    def custom_error_page_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayCustomErrorConfigurationOutputReference, "custom_error_page_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customErrorPageUrl", value)

    @builtins.property
    @jsii.member(jsii_name="statusCode")
    def status_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statusCode"))

    @status_code.setter
    def status_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayCustomErrorConfigurationOutputReference, "status_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statusCode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationGatewayCustomErrorConfiguration, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationGatewayCustomErrorConfiguration, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationGatewayCustomErrorConfiguration, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayCustomErrorConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayFrontendIpConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "private_ip_address": "privateIpAddress",
        "private_ip_address_allocation": "privateIpAddressAllocation",
        "private_link_configuration_name": "privateLinkConfigurationName",
        "public_ip_address_id": "publicIpAddressId",
        "subnet_id": "subnetId",
    },
)
class ApplicationGatewayFrontendIpConfiguration:
    def __init__(
        self,
        *,
        name: builtins.str,
        private_ip_address: typing.Optional[builtins.str] = None,
        private_ip_address_allocation: typing.Optional[builtins.str] = None,
        private_link_configuration_name: typing.Optional[builtins.str] = None,
        public_ip_address_id: typing.Optional[builtins.str] = None,
        subnet_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.
        :param private_ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#private_ip_address ApplicationGateway#private_ip_address}.
        :param private_ip_address_allocation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#private_ip_address_allocation ApplicationGateway#private_ip_address_allocation}.
        :param private_link_configuration_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#private_link_configuration_name ApplicationGateway#private_link_configuration_name}.
        :param public_ip_address_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#public_ip_address_id ApplicationGateway#public_ip_address_id}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#subnet_id ApplicationGateway#subnet_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayFrontendIpConfiguration.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument private_ip_address", value=private_ip_address, expected_type=type_hints["private_ip_address"])
            check_type(argname="argument private_ip_address_allocation", value=private_ip_address_allocation, expected_type=type_hints["private_ip_address_allocation"])
            check_type(argname="argument private_link_configuration_name", value=private_link_configuration_name, expected_type=type_hints["private_link_configuration_name"])
            check_type(argname="argument public_ip_address_id", value=public_ip_address_id, expected_type=type_hints["public_ip_address_id"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if private_ip_address is not None:
            self._values["private_ip_address"] = private_ip_address
        if private_ip_address_allocation is not None:
            self._values["private_ip_address_allocation"] = private_ip_address_allocation
        if private_link_configuration_name is not None:
            self._values["private_link_configuration_name"] = private_link_configuration_name
        if public_ip_address_id is not None:
            self._values["public_ip_address_id"] = public_ip_address_id
        if subnet_id is not None:
            self._values["subnet_id"] = subnet_id

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def private_ip_address(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#private_ip_address ApplicationGateway#private_ip_address}.'''
        result = self._values.get("private_ip_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_ip_address_allocation(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#private_ip_address_allocation ApplicationGateway#private_ip_address_allocation}.'''
        result = self._values.get("private_ip_address_allocation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_link_configuration_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#private_link_configuration_name ApplicationGateway#private_link_configuration_name}.'''
        result = self._values.get("private_link_configuration_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_ip_address_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#public_ip_address_id ApplicationGateway#public_ip_address_id}.'''
        result = self._values.get("public_ip_address_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnet_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#subnet_id ApplicationGateway#subnet_id}.'''
        result = self._values.get("subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewayFrontendIpConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationGatewayFrontendIpConfigurationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayFrontendIpConfigurationList",
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
            type_hints = typing.get_type_hints(ApplicationGatewayFrontendIpConfigurationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationGatewayFrontendIpConfigurationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayFrontendIpConfigurationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationGatewayFrontendIpConfigurationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayFrontendIpConfigurationList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayFrontendIpConfigurationList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayFrontendIpConfigurationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayFrontendIpConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayFrontendIpConfiguration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayFrontendIpConfiguration]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayFrontendIpConfigurationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationGatewayFrontendIpConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayFrontendIpConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationGatewayFrontendIpConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetPrivateIpAddress")
    def reset_private_ip_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateIpAddress", []))

    @jsii.member(jsii_name="resetPrivateIpAddressAllocation")
    def reset_private_ip_address_allocation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateIpAddressAllocation", []))

    @jsii.member(jsii_name="resetPrivateLinkConfigurationName")
    def reset_private_link_configuration_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateLinkConfigurationName", []))

    @jsii.member(jsii_name="resetPublicIpAddressId")
    def reset_public_ip_address_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicIpAddressId", []))

    @jsii.member(jsii_name="resetSubnetId")
    def reset_subnet_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetId", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="privateLinkConfigurationId")
    def private_link_configuration_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateLinkConfigurationId"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="privateIpAddressAllocationInput")
    def private_ip_address_allocation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateIpAddressAllocationInput"))

    @builtins.property
    @jsii.member(jsii_name="privateIpAddressInput")
    def private_ip_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateIpAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="privateLinkConfigurationNameInput")
    def private_link_configuration_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateLinkConfigurationNameInput"))

    @builtins.property
    @jsii.member(jsii_name="publicIpAddressIdInput")
    def public_ip_address_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicIpAddressIdInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdInput")
    def subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayFrontendIpConfigurationOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="privateIpAddress")
    def private_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateIpAddress"))

    @private_ip_address.setter
    def private_ip_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayFrontendIpConfigurationOutputReference, "private_ip_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateIpAddress", value)

    @builtins.property
    @jsii.member(jsii_name="privateIpAddressAllocation")
    def private_ip_address_allocation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateIpAddressAllocation"))

    @private_ip_address_allocation.setter
    def private_ip_address_allocation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayFrontendIpConfigurationOutputReference, "private_ip_address_allocation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateIpAddressAllocation", value)

    @builtins.property
    @jsii.member(jsii_name="privateLinkConfigurationName")
    def private_link_configuration_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateLinkConfigurationName"))

    @private_link_configuration_name.setter
    def private_link_configuration_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayFrontendIpConfigurationOutputReference, "private_link_configuration_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateLinkConfigurationName", value)

    @builtins.property
    @jsii.member(jsii_name="publicIpAddressId")
    def public_ip_address_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicIpAddressId"))

    @public_ip_address_id.setter
    def public_ip_address_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayFrontendIpConfigurationOutputReference, "public_ip_address_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicIpAddressId", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayFrontendIpConfigurationOutputReference, "subnet_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationGatewayFrontendIpConfiguration, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationGatewayFrontendIpConfiguration, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationGatewayFrontendIpConfiguration, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayFrontendIpConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayFrontendPort",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "port": "port"},
)
class ApplicationGatewayFrontendPort:
    def __init__(self, *, name: builtins.str, port: jsii.Number) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#port ApplicationGateway#port}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayFrontendPort.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "port": port,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#port ApplicationGateway#port}.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewayFrontendPort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationGatewayFrontendPortList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayFrontendPortList",
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
            type_hints = typing.get_type_hints(ApplicationGatewayFrontendPortList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationGatewayFrontendPortOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayFrontendPortList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationGatewayFrontendPortOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayFrontendPortList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayFrontendPortList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayFrontendPortList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayFrontendPort]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayFrontendPort]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayFrontendPort]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayFrontendPortList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationGatewayFrontendPortOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayFrontendPortOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationGatewayFrontendPortOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayFrontendPortOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayFrontendPortOutputReference, "port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationGatewayFrontendPort, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationGatewayFrontendPort, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationGatewayFrontendPort, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayFrontendPortOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayGatewayIpConfiguration",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "subnet_id": "subnetId"},
)
class ApplicationGatewayGatewayIpConfiguration:
    def __init__(self, *, name: builtins.str, subnet_id: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#subnet_id ApplicationGateway#subnet_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayGatewayIpConfiguration.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "subnet_id": subnet_id,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#subnet_id ApplicationGateway#subnet_id}.'''
        result = self._values.get("subnet_id")
        assert result is not None, "Required property 'subnet_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewayGatewayIpConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationGatewayGatewayIpConfigurationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayGatewayIpConfigurationList",
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
            type_hints = typing.get_type_hints(ApplicationGatewayGatewayIpConfigurationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationGatewayGatewayIpConfigurationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayGatewayIpConfigurationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationGatewayGatewayIpConfigurationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayGatewayIpConfigurationList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayGatewayIpConfigurationList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayGatewayIpConfigurationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayGatewayIpConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayGatewayIpConfiguration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayGatewayIpConfiguration]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayGatewayIpConfigurationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationGatewayGatewayIpConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayGatewayIpConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationGatewayGatewayIpConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdInput")
    def subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayGatewayIpConfigurationOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayGatewayIpConfigurationOutputReference, "subnet_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationGatewayGatewayIpConfiguration, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationGatewayGatewayIpConfiguration, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationGatewayGatewayIpConfiguration, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayGatewayIpConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayGlobal",
    jsii_struct_bases=[],
    name_mapping={
        "request_buffering_enabled": "requestBufferingEnabled",
        "response_buffering_enabled": "responseBufferingEnabled",
    },
)
class ApplicationGatewayGlobal:
    def __init__(
        self,
        *,
        request_buffering_enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        response_buffering_enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param request_buffering_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#request_buffering_enabled ApplicationGateway#request_buffering_enabled}.
        :param response_buffering_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#response_buffering_enabled ApplicationGateway#response_buffering_enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayGlobal.__init__)
            check_type(argname="argument request_buffering_enabled", value=request_buffering_enabled, expected_type=type_hints["request_buffering_enabled"])
            check_type(argname="argument response_buffering_enabled", value=response_buffering_enabled, expected_type=type_hints["response_buffering_enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "request_buffering_enabled": request_buffering_enabled,
            "response_buffering_enabled": response_buffering_enabled,
        }

    @builtins.property
    def request_buffering_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#request_buffering_enabled ApplicationGateway#request_buffering_enabled}.'''
        result = self._values.get("request_buffering_enabled")
        assert result is not None, "Required property 'request_buffering_enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def response_buffering_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#response_buffering_enabled ApplicationGateway#response_buffering_enabled}.'''
        result = self._values.get("response_buffering_enabled")
        assert result is not None, "Required property 'response_buffering_enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewayGlobal(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationGatewayGlobalOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayGlobalOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationGatewayGlobalOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="requestBufferingEnabledInput")
    def request_buffering_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requestBufferingEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="responseBufferingEnabledInput")
    def response_buffering_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "responseBufferingEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="requestBufferingEnabled")
    def request_buffering_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "requestBufferingEnabled"))

    @request_buffering_enabled.setter
    def request_buffering_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayGlobalOutputReference, "request_buffering_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestBufferingEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="responseBufferingEnabled")
    def response_buffering_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "responseBufferingEnabled"))

    @response_buffering_enabled.setter
    def response_buffering_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayGlobalOutputReference, "response_buffering_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseBufferingEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApplicationGatewayGlobal]:
        return typing.cast(typing.Optional[ApplicationGatewayGlobal], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ApplicationGatewayGlobal]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayGlobalOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayHttpListener",
    jsii_struct_bases=[],
    name_mapping={
        "frontend_ip_configuration_name": "frontendIpConfigurationName",
        "frontend_port_name": "frontendPortName",
        "name": "name",
        "protocol": "protocol",
        "custom_error_configuration": "customErrorConfiguration",
        "firewall_policy_id": "firewallPolicyId",
        "host_name": "hostName",
        "host_names": "hostNames",
        "require_sni": "requireSni",
        "ssl_certificate_name": "sslCertificateName",
        "ssl_profile_name": "sslProfileName",
    },
)
class ApplicationGatewayHttpListener:
    def __init__(
        self,
        *,
        frontend_ip_configuration_name: builtins.str,
        frontend_port_name: builtins.str,
        name: builtins.str,
        protocol: builtins.str,
        custom_error_configuration: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayHttpListenerCustomErrorConfiguration", typing.Dict[str, typing.Any]]]]] = None,
        firewall_policy_id: typing.Optional[builtins.str] = None,
        host_name: typing.Optional[builtins.str] = None,
        host_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        require_sni: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ssl_certificate_name: typing.Optional[builtins.str] = None,
        ssl_profile_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param frontend_ip_configuration_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#frontend_ip_configuration_name ApplicationGateway#frontend_ip_configuration_name}.
        :param frontend_port_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#frontend_port_name ApplicationGateway#frontend_port_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#protocol ApplicationGateway#protocol}.
        :param custom_error_configuration: custom_error_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#custom_error_configuration ApplicationGateway#custom_error_configuration}
        :param firewall_policy_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#firewall_policy_id ApplicationGateway#firewall_policy_id}.
        :param host_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#host_name ApplicationGateway#host_name}.
        :param host_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#host_names ApplicationGateway#host_names}.
        :param require_sni: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#require_sni ApplicationGateway#require_sni}.
        :param ssl_certificate_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#ssl_certificate_name ApplicationGateway#ssl_certificate_name}.
        :param ssl_profile_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#ssl_profile_name ApplicationGateway#ssl_profile_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayHttpListener.__init__)
            check_type(argname="argument frontend_ip_configuration_name", value=frontend_ip_configuration_name, expected_type=type_hints["frontend_ip_configuration_name"])
            check_type(argname="argument frontend_port_name", value=frontend_port_name, expected_type=type_hints["frontend_port_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument custom_error_configuration", value=custom_error_configuration, expected_type=type_hints["custom_error_configuration"])
            check_type(argname="argument firewall_policy_id", value=firewall_policy_id, expected_type=type_hints["firewall_policy_id"])
            check_type(argname="argument host_name", value=host_name, expected_type=type_hints["host_name"])
            check_type(argname="argument host_names", value=host_names, expected_type=type_hints["host_names"])
            check_type(argname="argument require_sni", value=require_sni, expected_type=type_hints["require_sni"])
            check_type(argname="argument ssl_certificate_name", value=ssl_certificate_name, expected_type=type_hints["ssl_certificate_name"])
            check_type(argname="argument ssl_profile_name", value=ssl_profile_name, expected_type=type_hints["ssl_profile_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "frontend_ip_configuration_name": frontend_ip_configuration_name,
            "frontend_port_name": frontend_port_name,
            "name": name,
            "protocol": protocol,
        }
        if custom_error_configuration is not None:
            self._values["custom_error_configuration"] = custom_error_configuration
        if firewall_policy_id is not None:
            self._values["firewall_policy_id"] = firewall_policy_id
        if host_name is not None:
            self._values["host_name"] = host_name
        if host_names is not None:
            self._values["host_names"] = host_names
        if require_sni is not None:
            self._values["require_sni"] = require_sni
        if ssl_certificate_name is not None:
            self._values["ssl_certificate_name"] = ssl_certificate_name
        if ssl_profile_name is not None:
            self._values["ssl_profile_name"] = ssl_profile_name

    @builtins.property
    def frontend_ip_configuration_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#frontend_ip_configuration_name ApplicationGateway#frontend_ip_configuration_name}.'''
        result = self._values.get("frontend_ip_configuration_name")
        assert result is not None, "Required property 'frontend_ip_configuration_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def frontend_port_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#frontend_port_name ApplicationGateway#frontend_port_name}.'''
        result = self._values.get("frontend_port_name")
        assert result is not None, "Required property 'frontend_port_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#protocol ApplicationGateway#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_error_configuration(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayHttpListenerCustomErrorConfiguration"]]]:
        '''custom_error_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#custom_error_configuration ApplicationGateway#custom_error_configuration}
        '''
        result = self._values.get("custom_error_configuration")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayHttpListenerCustomErrorConfiguration"]]], result)

    @builtins.property
    def firewall_policy_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#firewall_policy_id ApplicationGateway#firewall_policy_id}.'''
        result = self._values.get("firewall_policy_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def host_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#host_name ApplicationGateway#host_name}.'''
        result = self._values.get("host_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def host_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#host_names ApplicationGateway#host_names}.'''
        result = self._values.get("host_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def require_sni(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#require_sni ApplicationGateway#require_sni}.'''
        result = self._values.get("require_sni")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def ssl_certificate_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#ssl_certificate_name ApplicationGateway#ssl_certificate_name}.'''
        result = self._values.get("ssl_certificate_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssl_profile_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#ssl_profile_name ApplicationGateway#ssl_profile_name}.'''
        result = self._values.get("ssl_profile_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewayHttpListener(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayHttpListenerCustomErrorConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "custom_error_page_url": "customErrorPageUrl",
        "status_code": "statusCode",
    },
)
class ApplicationGatewayHttpListenerCustomErrorConfiguration:
    def __init__(
        self,
        *,
        custom_error_page_url: builtins.str,
        status_code: builtins.str,
    ) -> None:
        '''
        :param custom_error_page_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#custom_error_page_url ApplicationGateway#custom_error_page_url}.
        :param status_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#status_code ApplicationGateway#status_code}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayHttpListenerCustomErrorConfiguration.__init__)
            check_type(argname="argument custom_error_page_url", value=custom_error_page_url, expected_type=type_hints["custom_error_page_url"])
            check_type(argname="argument status_code", value=status_code, expected_type=type_hints["status_code"])
        self._values: typing.Dict[str, typing.Any] = {
            "custom_error_page_url": custom_error_page_url,
            "status_code": status_code,
        }

    @builtins.property
    def custom_error_page_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#custom_error_page_url ApplicationGateway#custom_error_page_url}.'''
        result = self._values.get("custom_error_page_url")
        assert result is not None, "Required property 'custom_error_page_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def status_code(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#status_code ApplicationGateway#status_code}.'''
        result = self._values.get("status_code")
        assert result is not None, "Required property 'status_code' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewayHttpListenerCustomErrorConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationGatewayHttpListenerCustomErrorConfigurationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayHttpListenerCustomErrorConfigurationList",
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
            type_hints = typing.get_type_hints(ApplicationGatewayHttpListenerCustomErrorConfigurationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationGatewayHttpListenerCustomErrorConfigurationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayHttpListenerCustomErrorConfigurationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationGatewayHttpListenerCustomErrorConfigurationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayHttpListenerCustomErrorConfigurationList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayHttpListenerCustomErrorConfigurationList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayHttpListenerCustomErrorConfigurationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayHttpListenerCustomErrorConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayHttpListenerCustomErrorConfiguration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayHttpListenerCustomErrorConfiguration]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayHttpListenerCustomErrorConfigurationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationGatewayHttpListenerCustomErrorConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayHttpListenerCustomErrorConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationGatewayHttpListenerCustomErrorConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="customErrorPageUrlInput")
    def custom_error_page_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customErrorPageUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="statusCodeInput")
    def status_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="customErrorPageUrl")
    def custom_error_page_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customErrorPageUrl"))

    @custom_error_page_url.setter
    def custom_error_page_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayHttpListenerCustomErrorConfigurationOutputReference, "custom_error_page_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customErrorPageUrl", value)

    @builtins.property
    @jsii.member(jsii_name="statusCode")
    def status_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statusCode"))

    @status_code.setter
    def status_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayHttpListenerCustomErrorConfigurationOutputReference, "status_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statusCode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationGatewayHttpListenerCustomErrorConfiguration, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationGatewayHttpListenerCustomErrorConfiguration, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationGatewayHttpListenerCustomErrorConfiguration, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayHttpListenerCustomErrorConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationGatewayHttpListenerList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayHttpListenerList",
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
            type_hints = typing.get_type_hints(ApplicationGatewayHttpListenerList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationGatewayHttpListenerOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayHttpListenerList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationGatewayHttpListenerOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayHttpListenerList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayHttpListenerList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayHttpListenerList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayHttpListener]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayHttpListener]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayHttpListener]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayHttpListenerList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationGatewayHttpListenerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayHttpListenerOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationGatewayHttpListenerOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCustomErrorConfiguration")
    def put_custom_error_configuration(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApplicationGatewayHttpListenerCustomErrorConfiguration, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayHttpListenerOutputReference.put_custom_error_configuration)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCustomErrorConfiguration", [value]))

    @jsii.member(jsii_name="resetCustomErrorConfiguration")
    def reset_custom_error_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomErrorConfiguration", []))

    @jsii.member(jsii_name="resetFirewallPolicyId")
    def reset_firewall_policy_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFirewallPolicyId", []))

    @jsii.member(jsii_name="resetHostName")
    def reset_host_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostName", []))

    @jsii.member(jsii_name="resetHostNames")
    def reset_host_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostNames", []))

    @jsii.member(jsii_name="resetRequireSni")
    def reset_require_sni(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequireSni", []))

    @jsii.member(jsii_name="resetSslCertificateName")
    def reset_ssl_certificate_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslCertificateName", []))

    @jsii.member(jsii_name="resetSslProfileName")
    def reset_ssl_profile_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslProfileName", []))

    @builtins.property
    @jsii.member(jsii_name="customErrorConfiguration")
    def custom_error_configuration(
        self,
    ) -> ApplicationGatewayHttpListenerCustomErrorConfigurationList:
        return typing.cast(ApplicationGatewayHttpListenerCustomErrorConfigurationList, jsii.get(self, "customErrorConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="frontendIpConfigurationId")
    def frontend_ip_configuration_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "frontendIpConfigurationId"))

    @builtins.property
    @jsii.member(jsii_name="frontendPortId")
    def frontend_port_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "frontendPortId"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="sslCertificateId")
    def ssl_certificate_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslCertificateId"))

    @builtins.property
    @jsii.member(jsii_name="sslProfileId")
    def ssl_profile_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslProfileId"))

    @builtins.property
    @jsii.member(jsii_name="customErrorConfigurationInput")
    def custom_error_configuration_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayHttpListenerCustomErrorConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayHttpListenerCustomErrorConfiguration]]], jsii.get(self, "customErrorConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="firewallPolicyIdInput")
    def firewall_policy_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "firewallPolicyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="frontendIpConfigurationNameInput")
    def frontend_ip_configuration_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "frontendIpConfigurationNameInput"))

    @builtins.property
    @jsii.member(jsii_name="frontendPortNameInput")
    def frontend_port_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "frontendPortNameInput"))

    @builtins.property
    @jsii.member(jsii_name="hostNameInput")
    def host_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostNameInput"))

    @builtins.property
    @jsii.member(jsii_name="hostNamesInput")
    def host_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "hostNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="requireSniInput")
    def require_sni_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requireSniInput"))

    @builtins.property
    @jsii.member(jsii_name="sslCertificateNameInput")
    def ssl_certificate_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslCertificateNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sslProfileNameInput")
    def ssl_profile_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslProfileNameInput"))

    @builtins.property
    @jsii.member(jsii_name="firewallPolicyId")
    def firewall_policy_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "firewallPolicyId"))

    @firewall_policy_id.setter
    def firewall_policy_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayHttpListenerOutputReference, "firewall_policy_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firewallPolicyId", value)

    @builtins.property
    @jsii.member(jsii_name="frontendIpConfigurationName")
    def frontend_ip_configuration_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "frontendIpConfigurationName"))

    @frontend_ip_configuration_name.setter
    def frontend_ip_configuration_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayHttpListenerOutputReference, "frontend_ip_configuration_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frontendIpConfigurationName", value)

    @builtins.property
    @jsii.member(jsii_name="frontendPortName")
    def frontend_port_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "frontendPortName"))

    @frontend_port_name.setter
    def frontend_port_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayHttpListenerOutputReference, "frontend_port_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frontendPortName", value)

    @builtins.property
    @jsii.member(jsii_name="hostName")
    def host_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostName"))

    @host_name.setter
    def host_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayHttpListenerOutputReference, "host_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostName", value)

    @builtins.property
    @jsii.member(jsii_name="hostNames")
    def host_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "hostNames"))

    @host_names.setter
    def host_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayHttpListenerOutputReference, "host_names").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostNames", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayHttpListenerOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayHttpListenerOutputReference, "protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="requireSni")
    def require_sni(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "requireSni"))

    @require_sni.setter
    def require_sni(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayHttpListenerOutputReference, "require_sni").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requireSni", value)

    @builtins.property
    @jsii.member(jsii_name="sslCertificateName")
    def ssl_certificate_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslCertificateName"))

    @ssl_certificate_name.setter
    def ssl_certificate_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayHttpListenerOutputReference, "ssl_certificate_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslCertificateName", value)

    @builtins.property
    @jsii.member(jsii_name="sslProfileName")
    def ssl_profile_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslProfileName"))

    @ssl_profile_name.setter
    def ssl_profile_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayHttpListenerOutputReference, "ssl_profile_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslProfileName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationGatewayHttpListener, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationGatewayHttpListener, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationGatewayHttpListener, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayHttpListenerOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayIdentity",
    jsii_struct_bases=[],
    name_mapping={"identity_ids": "identityIds", "type": "type"},
)
class ApplicationGatewayIdentity:
    def __init__(
        self,
        *,
        identity_ids: typing.Sequence[builtins.str],
        type: builtins.str,
    ) -> None:
        '''
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#identity_ids ApplicationGateway#identity_ids}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#type ApplicationGateway#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayIdentity.__init__)
            check_type(argname="argument identity_ids", value=identity_ids, expected_type=type_hints["identity_ids"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "identity_ids": identity_ids,
            "type": type,
        }

    @builtins.property
    def identity_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#identity_ids ApplicationGateway#identity_ids}.'''
        result = self._values.get("identity_ids")
        assert result is not None, "Required property 'identity_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#type ApplicationGateway#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewayIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationGatewayIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayIdentityOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationGatewayIdentityOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayIdentityOutputReference, "identity_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityIds", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayIdentityOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApplicationGatewayIdentity]:
        return typing.cast(typing.Optional[ApplicationGatewayIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApplicationGatewayIdentity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayPrivateEndpointConnection",
    jsii_struct_bases=[],
    name_mapping={},
)
class ApplicationGatewayPrivateEndpointConnection:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewayPrivateEndpointConnection(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationGatewayPrivateEndpointConnectionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayPrivateEndpointConnectionList",
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
            type_hints = typing.get_type_hints(ApplicationGatewayPrivateEndpointConnectionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationGatewayPrivateEndpointConnectionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayPrivateEndpointConnectionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationGatewayPrivateEndpointConnectionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayPrivateEndpointConnectionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayPrivateEndpointConnectionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayPrivateEndpointConnectionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class ApplicationGatewayPrivateEndpointConnectionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayPrivateEndpointConnectionOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationGatewayPrivateEndpointConnectionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ApplicationGatewayPrivateEndpointConnection]:
        return typing.cast(typing.Optional[ApplicationGatewayPrivateEndpointConnection], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApplicationGatewayPrivateEndpointConnection],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayPrivateEndpointConnectionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayPrivateLinkConfiguration",
    jsii_struct_bases=[],
    name_mapping={"ip_configuration": "ipConfiguration", "name": "name"},
)
class ApplicationGatewayPrivateLinkConfiguration:
    def __init__(
        self,
        *,
        ip_configuration: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayPrivateLinkConfigurationIpConfiguration", typing.Dict[str, typing.Any]]]],
        name: builtins.str,
    ) -> None:
        '''
        :param ip_configuration: ip_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#ip_configuration ApplicationGateway#ip_configuration}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayPrivateLinkConfiguration.__init__)
            check_type(argname="argument ip_configuration", value=ip_configuration, expected_type=type_hints["ip_configuration"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "ip_configuration": ip_configuration,
            "name": name,
        }

    @builtins.property
    def ip_configuration(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayPrivateLinkConfigurationIpConfiguration"]]:
        '''ip_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#ip_configuration ApplicationGateway#ip_configuration}
        '''
        result = self._values.get("ip_configuration")
        assert result is not None, "Required property 'ip_configuration' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayPrivateLinkConfigurationIpConfiguration"]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewayPrivateLinkConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayPrivateLinkConfigurationIpConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "primary": "primary",
        "private_ip_address_allocation": "privateIpAddressAllocation",
        "subnet_id": "subnetId",
        "private_ip_address": "privateIpAddress",
    },
)
class ApplicationGatewayPrivateLinkConfigurationIpConfiguration:
    def __init__(
        self,
        *,
        name: builtins.str,
        primary: typing.Union[builtins.bool, cdktf.IResolvable],
        private_ip_address_allocation: builtins.str,
        subnet_id: builtins.str,
        private_ip_address: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.
        :param primary: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#primary ApplicationGateway#primary}.
        :param private_ip_address_allocation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#private_ip_address_allocation ApplicationGateway#private_ip_address_allocation}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#subnet_id ApplicationGateway#subnet_id}.
        :param private_ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#private_ip_address ApplicationGateway#private_ip_address}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayPrivateLinkConfigurationIpConfiguration.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument primary", value=primary, expected_type=type_hints["primary"])
            check_type(argname="argument private_ip_address_allocation", value=private_ip_address_allocation, expected_type=type_hints["private_ip_address_allocation"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
            check_type(argname="argument private_ip_address", value=private_ip_address, expected_type=type_hints["private_ip_address"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "primary": primary,
            "private_ip_address_allocation": private_ip_address_allocation,
            "subnet_id": subnet_id,
        }
        if private_ip_address is not None:
            self._values["private_ip_address"] = private_ip_address

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def primary(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#primary ApplicationGateway#primary}.'''
        result = self._values.get("primary")
        assert result is not None, "Required property 'primary' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def private_ip_address_allocation(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#private_ip_address_allocation ApplicationGateway#private_ip_address_allocation}.'''
        result = self._values.get("private_ip_address_allocation")
        assert result is not None, "Required property 'private_ip_address_allocation' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#subnet_id ApplicationGateway#subnet_id}.'''
        result = self._values.get("subnet_id")
        assert result is not None, "Required property 'subnet_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def private_ip_address(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#private_ip_address ApplicationGateway#private_ip_address}.'''
        result = self._values.get("private_ip_address")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewayPrivateLinkConfigurationIpConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationGatewayPrivateLinkConfigurationIpConfigurationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayPrivateLinkConfigurationIpConfigurationList",
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
            type_hints = typing.get_type_hints(ApplicationGatewayPrivateLinkConfigurationIpConfigurationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationGatewayPrivateLinkConfigurationIpConfigurationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayPrivateLinkConfigurationIpConfigurationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationGatewayPrivateLinkConfigurationIpConfigurationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayPrivateLinkConfigurationIpConfigurationList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayPrivateLinkConfigurationIpConfigurationList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayPrivateLinkConfigurationIpConfigurationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayPrivateLinkConfigurationIpConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayPrivateLinkConfigurationIpConfiguration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayPrivateLinkConfigurationIpConfiguration]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayPrivateLinkConfigurationIpConfigurationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationGatewayPrivateLinkConfigurationIpConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayPrivateLinkConfigurationIpConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationGatewayPrivateLinkConfigurationIpConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetPrivateIpAddress")
    def reset_private_ip_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateIpAddress", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryInput")
    def primary_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "primaryInput"))

    @builtins.property
    @jsii.member(jsii_name="privateIpAddressAllocationInput")
    def private_ip_address_allocation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateIpAddressAllocationInput"))

    @builtins.property
    @jsii.member(jsii_name="privateIpAddressInput")
    def private_ip_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateIpAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdInput")
    def subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayPrivateLinkConfigurationIpConfigurationOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="primary")
    def primary(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "primary"))

    @primary.setter
    def primary(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayPrivateLinkConfigurationIpConfigurationOutputReference, "primary").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primary", value)

    @builtins.property
    @jsii.member(jsii_name="privateIpAddress")
    def private_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateIpAddress"))

    @private_ip_address.setter
    def private_ip_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayPrivateLinkConfigurationIpConfigurationOutputReference, "private_ip_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateIpAddress", value)

    @builtins.property
    @jsii.member(jsii_name="privateIpAddressAllocation")
    def private_ip_address_allocation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateIpAddressAllocation"))

    @private_ip_address_allocation.setter
    def private_ip_address_allocation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayPrivateLinkConfigurationIpConfigurationOutputReference, "private_ip_address_allocation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateIpAddressAllocation", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayPrivateLinkConfigurationIpConfigurationOutputReference, "subnet_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationGatewayPrivateLinkConfigurationIpConfiguration, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationGatewayPrivateLinkConfigurationIpConfiguration, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationGatewayPrivateLinkConfigurationIpConfiguration, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayPrivateLinkConfigurationIpConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationGatewayPrivateLinkConfigurationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayPrivateLinkConfigurationList",
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
            type_hints = typing.get_type_hints(ApplicationGatewayPrivateLinkConfigurationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationGatewayPrivateLinkConfigurationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayPrivateLinkConfigurationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationGatewayPrivateLinkConfigurationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayPrivateLinkConfigurationList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayPrivateLinkConfigurationList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayPrivateLinkConfigurationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayPrivateLinkConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayPrivateLinkConfiguration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayPrivateLinkConfiguration]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayPrivateLinkConfigurationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationGatewayPrivateLinkConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayPrivateLinkConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationGatewayPrivateLinkConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putIpConfiguration")
    def put_ip_configuration(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApplicationGatewayPrivateLinkConfigurationIpConfiguration, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayPrivateLinkConfigurationOutputReference.put_ip_configuration)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIpConfiguration", [value]))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="ipConfiguration")
    def ip_configuration(
        self,
    ) -> ApplicationGatewayPrivateLinkConfigurationIpConfigurationList:
        return typing.cast(ApplicationGatewayPrivateLinkConfigurationIpConfigurationList, jsii.get(self, "ipConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="ipConfigurationInput")
    def ip_configuration_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayPrivateLinkConfigurationIpConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayPrivateLinkConfigurationIpConfiguration]]], jsii.get(self, "ipConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayPrivateLinkConfigurationOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationGatewayPrivateLinkConfiguration, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationGatewayPrivateLinkConfiguration, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationGatewayPrivateLinkConfiguration, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayPrivateLinkConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayProbe",
    jsii_struct_bases=[],
    name_mapping={
        "interval": "interval",
        "name": "name",
        "path": "path",
        "protocol": "protocol",
        "timeout": "timeout",
        "unhealthy_threshold": "unhealthyThreshold",
        "host": "host",
        "match": "match",
        "minimum_servers": "minimumServers",
        "pick_host_name_from_backend_http_settings": "pickHostNameFromBackendHttpSettings",
        "port": "port",
    },
)
class ApplicationGatewayProbe:
    def __init__(
        self,
        *,
        interval: jsii.Number,
        name: builtins.str,
        path: builtins.str,
        protocol: builtins.str,
        timeout: jsii.Number,
        unhealthy_threshold: jsii.Number,
        host: typing.Optional[builtins.str] = None,
        match: typing.Optional[typing.Union["ApplicationGatewayProbeMatch", typing.Dict[str, typing.Any]]] = None,
        minimum_servers: typing.Optional[jsii.Number] = None,
        pick_host_name_from_backend_http_settings: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#interval ApplicationGateway#interval}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#path ApplicationGateway#path}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#protocol ApplicationGateway#protocol}.
        :param timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#timeout ApplicationGateway#timeout}.
        :param unhealthy_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#unhealthy_threshold ApplicationGateway#unhealthy_threshold}.
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#host ApplicationGateway#host}.
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#match ApplicationGateway#match}
        :param minimum_servers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#minimum_servers ApplicationGateway#minimum_servers}.
        :param pick_host_name_from_backend_http_settings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#pick_host_name_from_backend_http_settings ApplicationGateway#pick_host_name_from_backend_http_settings}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#port ApplicationGateway#port}.
        '''
        if isinstance(match, dict):
            match = ApplicationGatewayProbeMatch(**match)
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayProbe.__init__)
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument unhealthy_threshold", value=unhealthy_threshold, expected_type=type_hints["unhealthy_threshold"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument match", value=match, expected_type=type_hints["match"])
            check_type(argname="argument minimum_servers", value=minimum_servers, expected_type=type_hints["minimum_servers"])
            check_type(argname="argument pick_host_name_from_backend_http_settings", value=pick_host_name_from_backend_http_settings, expected_type=type_hints["pick_host_name_from_backend_http_settings"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[str, typing.Any] = {
            "interval": interval,
            "name": name,
            "path": path,
            "protocol": protocol,
            "timeout": timeout,
            "unhealthy_threshold": unhealthy_threshold,
        }
        if host is not None:
            self._values["host"] = host
        if match is not None:
            self._values["match"] = match
        if minimum_servers is not None:
            self._values["minimum_servers"] = minimum_servers
        if pick_host_name_from_backend_http_settings is not None:
            self._values["pick_host_name_from_backend_http_settings"] = pick_host_name_from_backend_http_settings
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def interval(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#interval ApplicationGateway#interval}.'''
        result = self._values.get("interval")
        assert result is not None, "Required property 'interval' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#path ApplicationGateway#path}.'''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#protocol ApplicationGateway#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def timeout(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#timeout ApplicationGateway#timeout}.'''
        result = self._values.get("timeout")
        assert result is not None, "Required property 'timeout' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def unhealthy_threshold(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#unhealthy_threshold ApplicationGateway#unhealthy_threshold}.'''
        result = self._values.get("unhealthy_threshold")
        assert result is not None, "Required property 'unhealthy_threshold' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#host ApplicationGateway#host}.'''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match(self) -> typing.Optional["ApplicationGatewayProbeMatch"]:
        '''match block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#match ApplicationGateway#match}
        '''
        result = self._values.get("match")
        return typing.cast(typing.Optional["ApplicationGatewayProbeMatch"], result)

    @builtins.property
    def minimum_servers(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#minimum_servers ApplicationGateway#minimum_servers}.'''
        result = self._values.get("minimum_servers")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def pick_host_name_from_backend_http_settings(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#pick_host_name_from_backend_http_settings ApplicationGateway#pick_host_name_from_backend_http_settings}.'''
        result = self._values.get("pick_host_name_from_backend_http_settings")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#port ApplicationGateway#port}.'''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewayProbe(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationGatewayProbeList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayProbeList",
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
            type_hints = typing.get_type_hints(ApplicationGatewayProbeList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ApplicationGatewayProbeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayProbeList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationGatewayProbeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayProbeList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayProbeList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayProbeList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayProbe]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayProbe]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayProbe]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayProbeList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayProbeMatch",
    jsii_struct_bases=[],
    name_mapping={"status_code": "statusCode", "body": "body"},
)
class ApplicationGatewayProbeMatch:
    def __init__(
        self,
        *,
        status_code: typing.Sequence[builtins.str],
        body: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param status_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#status_code ApplicationGateway#status_code}.
        :param body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#body ApplicationGateway#body}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayProbeMatch.__init__)
            check_type(argname="argument status_code", value=status_code, expected_type=type_hints["status_code"])
            check_type(argname="argument body", value=body, expected_type=type_hints["body"])
        self._values: typing.Dict[str, typing.Any] = {
            "status_code": status_code,
        }
        if body is not None:
            self._values["body"] = body

    @builtins.property
    def status_code(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#status_code ApplicationGateway#status_code}.'''
        result = self._values.get("status_code")
        assert result is not None, "Required property 'status_code' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def body(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#body ApplicationGateway#body}.'''
        result = self._values.get("body")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewayProbeMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationGatewayProbeMatchOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayProbeMatchOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationGatewayProbeMatchOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBody")
    def reset_body(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBody", []))

    @builtins.property
    @jsii.member(jsii_name="bodyInput")
    def body_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bodyInput"))

    @builtins.property
    @jsii.member(jsii_name="statusCodeInput")
    def status_code_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "statusCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="body")
    def body(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "body"))

    @body.setter
    def body(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayProbeMatchOutputReference, "body").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "body", value)

    @builtins.property
    @jsii.member(jsii_name="statusCode")
    def status_code(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "statusCode"))

    @status_code.setter
    def status_code(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayProbeMatchOutputReference, "status_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statusCode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApplicationGatewayProbeMatch]:
        return typing.cast(typing.Optional[ApplicationGatewayProbeMatch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApplicationGatewayProbeMatch],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayProbeMatchOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationGatewayProbeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayProbeOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationGatewayProbeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMatch")
    def put_match(
        self,
        *,
        status_code: typing.Sequence[builtins.str],
        body: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param status_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#status_code ApplicationGateway#status_code}.
        :param body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#body ApplicationGateway#body}.
        '''
        value = ApplicationGatewayProbeMatch(status_code=status_code, body=body)

        return typing.cast(None, jsii.invoke(self, "putMatch", [value]))

    @jsii.member(jsii_name="resetHost")
    def reset_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHost", []))

    @jsii.member(jsii_name="resetMatch")
    def reset_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatch", []))

    @jsii.member(jsii_name="resetMinimumServers")
    def reset_minimum_servers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinimumServers", []))

    @jsii.member(jsii_name="resetPickHostNameFromBackendHttpSettings")
    def reset_pick_host_name_from_backend_http_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPickHostNameFromBackendHttpSettings", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="match")
    def match(self) -> ApplicationGatewayProbeMatchOutputReference:
        return typing.cast(ApplicationGatewayProbeMatchOutputReference, jsii.get(self, "match"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="matchInput")
    def match_input(self) -> typing.Optional[ApplicationGatewayProbeMatch]:
        return typing.cast(typing.Optional[ApplicationGatewayProbeMatch], jsii.get(self, "matchInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumServersInput")
    def minimum_servers_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minimumServersInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="pickHostNameFromBackendHttpSettingsInput")
    def pick_host_name_from_backend_http_settings_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "pickHostNameFromBackendHttpSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInput")
    def timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="unhealthyThresholdInput")
    def unhealthy_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "unhealthyThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayProbeOutputReference, "host").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayProbeOutputReference, "interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value)

    @builtins.property
    @jsii.member(jsii_name="minimumServers")
    def minimum_servers(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minimumServers"))

    @minimum_servers.setter
    def minimum_servers(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayProbeOutputReference, "minimum_servers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumServers", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayProbeOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayProbeOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="pickHostNameFromBackendHttpSettings")
    def pick_host_name_from_backend_http_settings(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "pickHostNameFromBackendHttpSettings"))

    @pick_host_name_from_backend_http_settings.setter
    def pick_host_name_from_backend_http_settings(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayProbeOutputReference, "pick_host_name_from_backend_http_settings").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pickHostNameFromBackendHttpSettings", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayProbeOutputReference, "port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayProbeOutputReference, "protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeout"))

    @timeout.setter
    def timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayProbeOutputReference, "timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeout", value)

    @builtins.property
    @jsii.member(jsii_name="unhealthyThreshold")
    def unhealthy_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "unhealthyThreshold"))

    @unhealthy_threshold.setter
    def unhealthy_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayProbeOutputReference, "unhealthy_threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unhealthyThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationGatewayProbe, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationGatewayProbe, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationGatewayProbe, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayProbeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayRedirectConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "redirect_type": "redirectType",
        "include_path": "includePath",
        "include_query_string": "includeQueryString",
        "target_listener_name": "targetListenerName",
        "target_url": "targetUrl",
    },
)
class ApplicationGatewayRedirectConfiguration:
    def __init__(
        self,
        *,
        name: builtins.str,
        redirect_type: builtins.str,
        include_path: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        include_query_string: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        target_listener_name: typing.Optional[builtins.str] = None,
        target_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.
        :param redirect_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#redirect_type ApplicationGateway#redirect_type}.
        :param include_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#include_path ApplicationGateway#include_path}.
        :param include_query_string: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#include_query_string ApplicationGateway#include_query_string}.
        :param target_listener_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#target_listener_name ApplicationGateway#target_listener_name}.
        :param target_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#target_url ApplicationGateway#target_url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayRedirectConfiguration.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument redirect_type", value=redirect_type, expected_type=type_hints["redirect_type"])
            check_type(argname="argument include_path", value=include_path, expected_type=type_hints["include_path"])
            check_type(argname="argument include_query_string", value=include_query_string, expected_type=type_hints["include_query_string"])
            check_type(argname="argument target_listener_name", value=target_listener_name, expected_type=type_hints["target_listener_name"])
            check_type(argname="argument target_url", value=target_url, expected_type=type_hints["target_url"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "redirect_type": redirect_type,
        }
        if include_path is not None:
            self._values["include_path"] = include_path
        if include_query_string is not None:
            self._values["include_query_string"] = include_query_string
        if target_listener_name is not None:
            self._values["target_listener_name"] = target_listener_name
        if target_url is not None:
            self._values["target_url"] = target_url

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def redirect_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#redirect_type ApplicationGateway#redirect_type}.'''
        result = self._values.get("redirect_type")
        assert result is not None, "Required property 'redirect_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def include_path(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#include_path ApplicationGateway#include_path}.'''
        result = self._values.get("include_path")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def include_query_string(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#include_query_string ApplicationGateway#include_query_string}.'''
        result = self._values.get("include_query_string")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def target_listener_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#target_listener_name ApplicationGateway#target_listener_name}.'''
        result = self._values.get("target_listener_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#target_url ApplicationGateway#target_url}.'''
        result = self._values.get("target_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewayRedirectConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationGatewayRedirectConfigurationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayRedirectConfigurationList",
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
            type_hints = typing.get_type_hints(ApplicationGatewayRedirectConfigurationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationGatewayRedirectConfigurationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayRedirectConfigurationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationGatewayRedirectConfigurationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRedirectConfigurationList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRedirectConfigurationList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRedirectConfigurationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayRedirectConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayRedirectConfiguration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayRedirectConfiguration]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRedirectConfigurationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationGatewayRedirectConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayRedirectConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationGatewayRedirectConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIncludePath")
    def reset_include_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludePath", []))

    @jsii.member(jsii_name="resetIncludeQueryString")
    def reset_include_query_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeQueryString", []))

    @jsii.member(jsii_name="resetTargetListenerName")
    def reset_target_listener_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetListenerName", []))

    @jsii.member(jsii_name="resetTargetUrl")
    def reset_target_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetUrl", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="targetListenerId")
    def target_listener_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetListenerId"))

    @builtins.property
    @jsii.member(jsii_name="includePathInput")
    def include_path_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "includePathInput"))

    @builtins.property
    @jsii.member(jsii_name="includeQueryStringInput")
    def include_query_string_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "includeQueryStringInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectTypeInput")
    def redirect_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="targetListenerNameInput")
    def target_listener_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetListenerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="targetUrlInput")
    def target_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="includePath")
    def include_path(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "includePath"))

    @include_path.setter
    def include_path(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRedirectConfigurationOutputReference, "include_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includePath", value)

    @builtins.property
    @jsii.member(jsii_name="includeQueryString")
    def include_query_string(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "includeQueryString"))

    @include_query_string.setter
    def include_query_string(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRedirectConfigurationOutputReference, "include_query_string").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeQueryString", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRedirectConfigurationOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="redirectType")
    def redirect_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectType"))

    @redirect_type.setter
    def redirect_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRedirectConfigurationOutputReference, "redirect_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectType", value)

    @builtins.property
    @jsii.member(jsii_name="targetListenerName")
    def target_listener_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetListenerName"))

    @target_listener_name.setter
    def target_listener_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRedirectConfigurationOutputReference, "target_listener_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetListenerName", value)

    @builtins.property
    @jsii.member(jsii_name="targetUrl")
    def target_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetUrl"))

    @target_url.setter
    def target_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRedirectConfigurationOutputReference, "target_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationGatewayRedirectConfiguration, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationGatewayRedirectConfiguration, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationGatewayRedirectConfiguration, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRedirectConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayRequestRoutingRule",
    jsii_struct_bases=[],
    name_mapping={
        "http_listener_name": "httpListenerName",
        "name": "name",
        "rule_type": "ruleType",
        "backend_address_pool_name": "backendAddressPoolName",
        "backend_http_settings_name": "backendHttpSettingsName",
        "priority": "priority",
        "redirect_configuration_name": "redirectConfigurationName",
        "rewrite_rule_set_name": "rewriteRuleSetName",
        "url_path_map_name": "urlPathMapName",
    },
)
class ApplicationGatewayRequestRoutingRule:
    def __init__(
        self,
        *,
        http_listener_name: builtins.str,
        name: builtins.str,
        rule_type: builtins.str,
        backend_address_pool_name: typing.Optional[builtins.str] = None,
        backend_http_settings_name: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
        redirect_configuration_name: typing.Optional[builtins.str] = None,
        rewrite_rule_set_name: typing.Optional[builtins.str] = None,
        url_path_map_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param http_listener_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#http_listener_name ApplicationGateway#http_listener_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.
        :param rule_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#rule_type ApplicationGateway#rule_type}.
        :param backend_address_pool_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#backend_address_pool_name ApplicationGateway#backend_address_pool_name}.
        :param backend_http_settings_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#backend_http_settings_name ApplicationGateway#backend_http_settings_name}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#priority ApplicationGateway#priority}.
        :param redirect_configuration_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#redirect_configuration_name ApplicationGateway#redirect_configuration_name}.
        :param rewrite_rule_set_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#rewrite_rule_set_name ApplicationGateway#rewrite_rule_set_name}.
        :param url_path_map_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#url_path_map_name ApplicationGateway#url_path_map_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayRequestRoutingRule.__init__)
            check_type(argname="argument http_listener_name", value=http_listener_name, expected_type=type_hints["http_listener_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument rule_type", value=rule_type, expected_type=type_hints["rule_type"])
            check_type(argname="argument backend_address_pool_name", value=backend_address_pool_name, expected_type=type_hints["backend_address_pool_name"])
            check_type(argname="argument backend_http_settings_name", value=backend_http_settings_name, expected_type=type_hints["backend_http_settings_name"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument redirect_configuration_name", value=redirect_configuration_name, expected_type=type_hints["redirect_configuration_name"])
            check_type(argname="argument rewrite_rule_set_name", value=rewrite_rule_set_name, expected_type=type_hints["rewrite_rule_set_name"])
            check_type(argname="argument url_path_map_name", value=url_path_map_name, expected_type=type_hints["url_path_map_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "http_listener_name": http_listener_name,
            "name": name,
            "rule_type": rule_type,
        }
        if backend_address_pool_name is not None:
            self._values["backend_address_pool_name"] = backend_address_pool_name
        if backend_http_settings_name is not None:
            self._values["backend_http_settings_name"] = backend_http_settings_name
        if priority is not None:
            self._values["priority"] = priority
        if redirect_configuration_name is not None:
            self._values["redirect_configuration_name"] = redirect_configuration_name
        if rewrite_rule_set_name is not None:
            self._values["rewrite_rule_set_name"] = rewrite_rule_set_name
        if url_path_map_name is not None:
            self._values["url_path_map_name"] = url_path_map_name

    @builtins.property
    def http_listener_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#http_listener_name ApplicationGateway#http_listener_name}.'''
        result = self._values.get("http_listener_name")
        assert result is not None, "Required property 'http_listener_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#rule_type ApplicationGateway#rule_type}.'''
        result = self._values.get("rule_type")
        assert result is not None, "Required property 'rule_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def backend_address_pool_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#backend_address_pool_name ApplicationGateway#backend_address_pool_name}.'''
        result = self._values.get("backend_address_pool_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def backend_http_settings_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#backend_http_settings_name ApplicationGateway#backend_http_settings_name}.'''
        result = self._values.get("backend_http_settings_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#priority ApplicationGateway#priority}.'''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def redirect_configuration_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#redirect_configuration_name ApplicationGateway#redirect_configuration_name}.'''
        result = self._values.get("redirect_configuration_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rewrite_rule_set_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#rewrite_rule_set_name ApplicationGateway#rewrite_rule_set_name}.'''
        result = self._values.get("rewrite_rule_set_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def url_path_map_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#url_path_map_name ApplicationGateway#url_path_map_name}.'''
        result = self._values.get("url_path_map_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewayRequestRoutingRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationGatewayRequestRoutingRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayRequestRoutingRuleList",
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
            type_hints = typing.get_type_hints(ApplicationGatewayRequestRoutingRuleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationGatewayRequestRoutingRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayRequestRoutingRuleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationGatewayRequestRoutingRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRequestRoutingRuleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRequestRoutingRuleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRequestRoutingRuleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayRequestRoutingRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayRequestRoutingRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayRequestRoutingRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRequestRoutingRuleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationGatewayRequestRoutingRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayRequestRoutingRuleOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationGatewayRequestRoutingRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetBackendAddressPoolName")
    def reset_backend_address_pool_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackendAddressPoolName", []))

    @jsii.member(jsii_name="resetBackendHttpSettingsName")
    def reset_backend_http_settings_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackendHttpSettingsName", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @jsii.member(jsii_name="resetRedirectConfigurationName")
    def reset_redirect_configuration_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectConfigurationName", []))

    @jsii.member(jsii_name="resetRewriteRuleSetName")
    def reset_rewrite_rule_set_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRewriteRuleSetName", []))

    @jsii.member(jsii_name="resetUrlPathMapName")
    def reset_url_path_map_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrlPathMapName", []))

    @builtins.property
    @jsii.member(jsii_name="backendAddressPoolId")
    def backend_address_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backendAddressPoolId"))

    @builtins.property
    @jsii.member(jsii_name="backendHttpSettingsId")
    def backend_http_settings_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backendHttpSettingsId"))

    @builtins.property
    @jsii.member(jsii_name="httpListenerId")
    def http_listener_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpListenerId"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="redirectConfigurationId")
    def redirect_configuration_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectConfigurationId"))

    @builtins.property
    @jsii.member(jsii_name="rewriteRuleSetId")
    def rewrite_rule_set_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rewriteRuleSetId"))

    @builtins.property
    @jsii.member(jsii_name="urlPathMapId")
    def url_path_map_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "urlPathMapId"))

    @builtins.property
    @jsii.member(jsii_name="backendAddressPoolNameInput")
    def backend_address_pool_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backendAddressPoolNameInput"))

    @builtins.property
    @jsii.member(jsii_name="backendHttpSettingsNameInput")
    def backend_http_settings_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backendHttpSettingsNameInput"))

    @builtins.property
    @jsii.member(jsii_name="httpListenerNameInput")
    def http_listener_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpListenerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectConfigurationNameInput")
    def redirect_configuration_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectConfigurationNameInput"))

    @builtins.property
    @jsii.member(jsii_name="rewriteRuleSetNameInput")
    def rewrite_rule_set_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rewriteRuleSetNameInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleTypeInput")
    def rule_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="urlPathMapNameInput")
    def url_path_map_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlPathMapNameInput"))

    @builtins.property
    @jsii.member(jsii_name="backendAddressPoolName")
    def backend_address_pool_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backendAddressPoolName"))

    @backend_address_pool_name.setter
    def backend_address_pool_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRequestRoutingRuleOutputReference, "backend_address_pool_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backendAddressPoolName", value)

    @builtins.property
    @jsii.member(jsii_name="backendHttpSettingsName")
    def backend_http_settings_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backendHttpSettingsName"))

    @backend_http_settings_name.setter
    def backend_http_settings_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRequestRoutingRuleOutputReference, "backend_http_settings_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backendHttpSettingsName", value)

    @builtins.property
    @jsii.member(jsii_name="httpListenerName")
    def http_listener_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpListenerName"))

    @http_listener_name.setter
    def http_listener_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRequestRoutingRuleOutputReference, "http_listener_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpListenerName", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRequestRoutingRuleOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRequestRoutingRuleOutputReference, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="redirectConfigurationName")
    def redirect_configuration_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectConfigurationName"))

    @redirect_configuration_name.setter
    def redirect_configuration_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRequestRoutingRuleOutputReference, "redirect_configuration_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectConfigurationName", value)

    @builtins.property
    @jsii.member(jsii_name="rewriteRuleSetName")
    def rewrite_rule_set_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rewriteRuleSetName"))

    @rewrite_rule_set_name.setter
    def rewrite_rule_set_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRequestRoutingRuleOutputReference, "rewrite_rule_set_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rewriteRuleSetName", value)

    @builtins.property
    @jsii.member(jsii_name="ruleType")
    def rule_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ruleType"))

    @rule_type.setter
    def rule_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRequestRoutingRuleOutputReference, "rule_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleType", value)

    @builtins.property
    @jsii.member(jsii_name="urlPathMapName")
    def url_path_map_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "urlPathMapName"))

    @url_path_map_name.setter
    def url_path_map_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRequestRoutingRuleOutputReference, "url_path_map_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "urlPathMapName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationGatewayRequestRoutingRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationGatewayRequestRoutingRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationGatewayRequestRoutingRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRequestRoutingRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayRewriteRuleSet",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "rewrite_rule": "rewriteRule"},
)
class ApplicationGatewayRewriteRuleSet:
    def __init__(
        self,
        *,
        name: builtins.str,
        rewrite_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayRewriteRuleSetRewriteRule", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.
        :param rewrite_rule: rewrite_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#rewrite_rule ApplicationGateway#rewrite_rule}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayRewriteRuleSet.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument rewrite_rule", value=rewrite_rule, expected_type=type_hints["rewrite_rule"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if rewrite_rule is not None:
            self._values["rewrite_rule"] = rewrite_rule

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rewrite_rule(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayRewriteRuleSetRewriteRule"]]]:
        '''rewrite_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#rewrite_rule ApplicationGateway#rewrite_rule}
        '''
        result = self._values.get("rewrite_rule")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayRewriteRuleSetRewriteRule"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewayRewriteRuleSet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationGatewayRewriteRuleSetList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayRewriteRuleSetList",
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
            type_hints = typing.get_type_hints(ApplicationGatewayRewriteRuleSetList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationGatewayRewriteRuleSetOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayRewriteRuleSetList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationGatewayRewriteRuleSetOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayRewriteRuleSet]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayRewriteRuleSet]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayRewriteRuleSet]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationGatewayRewriteRuleSetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayRewriteRuleSetOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationGatewayRewriteRuleSetOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putRewriteRule")
    def put_rewrite_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayRewriteRuleSetRewriteRule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayRewriteRuleSetOutputReference.put_rewrite_rule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRewriteRule", [value]))

    @jsii.member(jsii_name="resetRewriteRule")
    def reset_rewrite_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRewriteRule", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="rewriteRule")
    def rewrite_rule(self) -> "ApplicationGatewayRewriteRuleSetRewriteRuleList":
        return typing.cast("ApplicationGatewayRewriteRuleSetRewriteRuleList", jsii.get(self, "rewriteRule"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="rewriteRuleInput")
    def rewrite_rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayRewriteRuleSetRewriteRule"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayRewriteRuleSetRewriteRule"]]], jsii.get(self, "rewriteRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationGatewayRewriteRuleSet, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationGatewayRewriteRuleSet, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationGatewayRewriteRuleSet, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayRewriteRuleSetRewriteRule",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "rule_sequence": "ruleSequence",
        "condition": "condition",
        "request_header_configuration": "requestHeaderConfiguration",
        "response_header_configuration": "responseHeaderConfiguration",
        "url": "url",
    },
)
class ApplicationGatewayRewriteRuleSetRewriteRule:
    def __init__(
        self,
        *,
        name: builtins.str,
        rule_sequence: jsii.Number,
        condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayRewriteRuleSetRewriteRuleCondition", typing.Dict[str, typing.Any]]]]] = None,
        request_header_configuration: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayRewriteRuleSetRewriteRuleRequestHeaderConfiguration", typing.Dict[str, typing.Any]]]]] = None,
        response_header_configuration: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayRewriteRuleSetRewriteRuleResponseHeaderConfiguration", typing.Dict[str, typing.Any]]]]] = None,
        url: typing.Optional[typing.Union["ApplicationGatewayRewriteRuleSetRewriteRuleUrl", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.
        :param rule_sequence: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#rule_sequence ApplicationGateway#rule_sequence}.
        :param condition: condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#condition ApplicationGateway#condition}
        :param request_header_configuration: request_header_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#request_header_configuration ApplicationGateway#request_header_configuration}
        :param response_header_configuration: response_header_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#response_header_configuration ApplicationGateway#response_header_configuration}
        :param url: url block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#url ApplicationGateway#url}
        '''
        if isinstance(url, dict):
            url = ApplicationGatewayRewriteRuleSetRewriteRuleUrl(**url)
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayRewriteRuleSetRewriteRule.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument rule_sequence", value=rule_sequence, expected_type=type_hints["rule_sequence"])
            check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
            check_type(argname="argument request_header_configuration", value=request_header_configuration, expected_type=type_hints["request_header_configuration"])
            check_type(argname="argument response_header_configuration", value=response_header_configuration, expected_type=type_hints["response_header_configuration"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "rule_sequence": rule_sequence,
        }
        if condition is not None:
            self._values["condition"] = condition
        if request_header_configuration is not None:
            self._values["request_header_configuration"] = request_header_configuration
        if response_header_configuration is not None:
            self._values["response_header_configuration"] = response_header_configuration
        if url is not None:
            self._values["url"] = url

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_sequence(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#rule_sequence ApplicationGateway#rule_sequence}.'''
        result = self._values.get("rule_sequence")
        assert result is not None, "Required property 'rule_sequence' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def condition(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayRewriteRuleSetRewriteRuleCondition"]]]:
        '''condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#condition ApplicationGateway#condition}
        '''
        result = self._values.get("condition")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayRewriteRuleSetRewriteRuleCondition"]]], result)

    @builtins.property
    def request_header_configuration(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayRewriteRuleSetRewriteRuleRequestHeaderConfiguration"]]]:
        '''request_header_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#request_header_configuration ApplicationGateway#request_header_configuration}
        '''
        result = self._values.get("request_header_configuration")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayRewriteRuleSetRewriteRuleRequestHeaderConfiguration"]]], result)

    @builtins.property
    def response_header_configuration(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayRewriteRuleSetRewriteRuleResponseHeaderConfiguration"]]]:
        '''response_header_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#response_header_configuration ApplicationGateway#response_header_configuration}
        '''
        result = self._values.get("response_header_configuration")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayRewriteRuleSetRewriteRuleResponseHeaderConfiguration"]]], result)

    @builtins.property
    def url(self) -> typing.Optional["ApplicationGatewayRewriteRuleSetRewriteRuleUrl"]:
        '''url block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#url ApplicationGateway#url}
        '''
        result = self._values.get("url")
        return typing.cast(typing.Optional["ApplicationGatewayRewriteRuleSetRewriteRuleUrl"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewayRewriteRuleSetRewriteRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayRewriteRuleSetRewriteRuleCondition",
    jsii_struct_bases=[],
    name_mapping={
        "pattern": "pattern",
        "variable": "variable",
        "ignore_case": "ignoreCase",
        "negate": "negate",
    },
)
class ApplicationGatewayRewriteRuleSetRewriteRuleCondition:
    def __init__(
        self,
        *,
        pattern: builtins.str,
        variable: builtins.str,
        ignore_case: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        negate: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param pattern: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#pattern ApplicationGateway#pattern}.
        :param variable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#variable ApplicationGateway#variable}.
        :param ignore_case: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#ignore_case ApplicationGateway#ignore_case}.
        :param negate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#negate ApplicationGateway#negate}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayRewriteRuleSetRewriteRuleCondition.__init__)
            check_type(argname="argument pattern", value=pattern, expected_type=type_hints["pattern"])
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
            check_type(argname="argument ignore_case", value=ignore_case, expected_type=type_hints["ignore_case"])
            check_type(argname="argument negate", value=negate, expected_type=type_hints["negate"])
        self._values: typing.Dict[str, typing.Any] = {
            "pattern": pattern,
            "variable": variable,
        }
        if ignore_case is not None:
            self._values["ignore_case"] = ignore_case
        if negate is not None:
            self._values["negate"] = negate

    @builtins.property
    def pattern(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#pattern ApplicationGateway#pattern}.'''
        result = self._values.get("pattern")
        assert result is not None, "Required property 'pattern' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def variable(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#variable ApplicationGateway#variable}.'''
        result = self._values.get("variable")
        assert result is not None, "Required property 'variable' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ignore_case(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#ignore_case ApplicationGateway#ignore_case}.'''
        result = self._values.get("ignore_case")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def negate(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#negate ApplicationGateway#negate}.'''
        result = self._values.get("negate")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewayRewriteRuleSetRewriteRuleCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationGatewayRewriteRuleSetRewriteRuleConditionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayRewriteRuleSetRewriteRuleConditionList",
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
            type_hints = typing.get_type_hints(ApplicationGatewayRewriteRuleSetRewriteRuleConditionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationGatewayRewriteRuleSetRewriteRuleConditionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayRewriteRuleSetRewriteRuleConditionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationGatewayRewriteRuleSetRewriteRuleConditionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetRewriteRuleConditionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetRewriteRuleConditionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetRewriteRuleConditionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayRewriteRuleSetRewriteRuleCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayRewriteRuleSetRewriteRuleCondition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayRewriteRuleSetRewriteRuleCondition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetRewriteRuleConditionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationGatewayRewriteRuleSetRewriteRuleConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayRewriteRuleSetRewriteRuleConditionOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationGatewayRewriteRuleSetRewriteRuleConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIgnoreCase")
    def reset_ignore_case(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreCase", []))

    @jsii.member(jsii_name="resetNegate")
    def reset_negate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegate", []))

    @builtins.property
    @jsii.member(jsii_name="ignoreCaseInput")
    def ignore_case_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ignoreCaseInput"))

    @builtins.property
    @jsii.member(jsii_name="negateInput")
    def negate_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negateInput"))

    @builtins.property
    @jsii.member(jsii_name="patternInput")
    def pattern_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "patternInput"))

    @builtins.property
    @jsii.member(jsii_name="variableInput")
    def variable_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "variableInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreCase")
    def ignore_case(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ignoreCase"))

    @ignore_case.setter
    def ignore_case(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetRewriteRuleConditionOutputReference, "ignore_case").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreCase", value)

    @builtins.property
    @jsii.member(jsii_name="negate")
    def negate(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negate"))

    @negate.setter
    def negate(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetRewriteRuleConditionOutputReference, "negate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negate", value)

    @builtins.property
    @jsii.member(jsii_name="pattern")
    def pattern(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pattern"))

    @pattern.setter
    def pattern(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetRewriteRuleConditionOutputReference, "pattern").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pattern", value)

    @builtins.property
    @jsii.member(jsii_name="variable")
    def variable(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "variable"))

    @variable.setter
    def variable(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetRewriteRuleConditionOutputReference, "variable").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "variable", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationGatewayRewriteRuleSetRewriteRuleCondition, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationGatewayRewriteRuleSetRewriteRuleCondition, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationGatewayRewriteRuleSetRewriteRuleCondition, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetRewriteRuleConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationGatewayRewriteRuleSetRewriteRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayRewriteRuleSetRewriteRuleList",
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
            type_hints = typing.get_type_hints(ApplicationGatewayRewriteRuleSetRewriteRuleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationGatewayRewriteRuleSetRewriteRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayRewriteRuleSetRewriteRuleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationGatewayRewriteRuleSetRewriteRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetRewriteRuleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetRewriteRuleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetRewriteRuleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayRewriteRuleSetRewriteRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayRewriteRuleSetRewriteRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayRewriteRuleSetRewriteRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetRewriteRuleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationGatewayRewriteRuleSetRewriteRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayRewriteRuleSetRewriteRuleOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationGatewayRewriteRuleSetRewriteRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCondition")
    def put_condition(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApplicationGatewayRewriteRuleSetRewriteRuleCondition, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayRewriteRuleSetRewriteRuleOutputReference.put_condition)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCondition", [value]))

    @jsii.member(jsii_name="putRequestHeaderConfiguration")
    def put_request_header_configuration(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayRewriteRuleSetRewriteRuleRequestHeaderConfiguration", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayRewriteRuleSetRewriteRuleOutputReference.put_request_header_configuration)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRequestHeaderConfiguration", [value]))

    @jsii.member(jsii_name="putResponseHeaderConfiguration")
    def put_response_header_configuration(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayRewriteRuleSetRewriteRuleResponseHeaderConfiguration", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayRewriteRuleSetRewriteRuleOutputReference.put_response_header_configuration)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putResponseHeaderConfiguration", [value]))

    @jsii.member(jsii_name="putUrl")
    def put_url(
        self,
        *,
        components: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        query_string: typing.Optional[builtins.str] = None,
        reroute: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param components: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#components ApplicationGateway#components}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#path ApplicationGateway#path}.
        :param query_string: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#query_string ApplicationGateway#query_string}.
        :param reroute: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#reroute ApplicationGateway#reroute}.
        '''
        value = ApplicationGatewayRewriteRuleSetRewriteRuleUrl(
            components=components,
            path=path,
            query_string=query_string,
            reroute=reroute,
        )

        return typing.cast(None, jsii.invoke(self, "putUrl", [value]))

    @jsii.member(jsii_name="resetCondition")
    def reset_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCondition", []))

    @jsii.member(jsii_name="resetRequestHeaderConfiguration")
    def reset_request_header_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestHeaderConfiguration", []))

    @jsii.member(jsii_name="resetResponseHeaderConfiguration")
    def reset_response_header_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseHeaderConfiguration", []))

    @jsii.member(jsii_name="resetUrl")
    def reset_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrl", []))

    @builtins.property
    @jsii.member(jsii_name="condition")
    def condition(self) -> ApplicationGatewayRewriteRuleSetRewriteRuleConditionList:
        return typing.cast(ApplicationGatewayRewriteRuleSetRewriteRuleConditionList, jsii.get(self, "condition"))

    @builtins.property
    @jsii.member(jsii_name="requestHeaderConfiguration")
    def request_header_configuration(
        self,
    ) -> "ApplicationGatewayRewriteRuleSetRewriteRuleRequestHeaderConfigurationList":
        return typing.cast("ApplicationGatewayRewriteRuleSetRewriteRuleRequestHeaderConfigurationList", jsii.get(self, "requestHeaderConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="responseHeaderConfiguration")
    def response_header_configuration(
        self,
    ) -> "ApplicationGatewayRewriteRuleSetRewriteRuleResponseHeaderConfigurationList":
        return typing.cast("ApplicationGatewayRewriteRuleSetRewriteRuleResponseHeaderConfigurationList", jsii.get(self, "responseHeaderConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> "ApplicationGatewayRewriteRuleSetRewriteRuleUrlOutputReference":
        return typing.cast("ApplicationGatewayRewriteRuleSetRewriteRuleUrlOutputReference", jsii.get(self, "url"))

    @builtins.property
    @jsii.member(jsii_name="conditionInput")
    def condition_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayRewriteRuleSetRewriteRuleCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayRewriteRuleSetRewriteRuleCondition]]], jsii.get(self, "conditionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="requestHeaderConfigurationInput")
    def request_header_configuration_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayRewriteRuleSetRewriteRuleRequestHeaderConfiguration"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayRewriteRuleSetRewriteRuleRequestHeaderConfiguration"]]], jsii.get(self, "requestHeaderConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="responseHeaderConfigurationInput")
    def response_header_configuration_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayRewriteRuleSetRewriteRuleResponseHeaderConfiguration"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayRewriteRuleSetRewriteRuleResponseHeaderConfiguration"]]], jsii.get(self, "responseHeaderConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleSequenceInput")
    def rule_sequence_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ruleSequenceInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(
        self,
    ) -> typing.Optional["ApplicationGatewayRewriteRuleSetRewriteRuleUrl"]:
        return typing.cast(typing.Optional["ApplicationGatewayRewriteRuleSetRewriteRuleUrl"], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetRewriteRuleOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="ruleSequence")
    def rule_sequence(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ruleSequence"))

    @rule_sequence.setter
    def rule_sequence(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetRewriteRuleOutputReference, "rule_sequence").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleSequence", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationGatewayRewriteRuleSetRewriteRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationGatewayRewriteRuleSetRewriteRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationGatewayRewriteRuleSetRewriteRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetRewriteRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayRewriteRuleSetRewriteRuleRequestHeaderConfiguration",
    jsii_struct_bases=[],
    name_mapping={"header_name": "headerName", "header_value": "headerValue"},
)
class ApplicationGatewayRewriteRuleSetRewriteRuleRequestHeaderConfiguration:
    def __init__(
        self,
        *,
        header_name: builtins.str,
        header_value: builtins.str,
    ) -> None:
        '''
        :param header_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#header_name ApplicationGateway#header_name}.
        :param header_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#header_value ApplicationGateway#header_value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayRewriteRuleSetRewriteRuleRequestHeaderConfiguration.__init__)
            check_type(argname="argument header_name", value=header_name, expected_type=type_hints["header_name"])
            check_type(argname="argument header_value", value=header_value, expected_type=type_hints["header_value"])
        self._values: typing.Dict[str, typing.Any] = {
            "header_name": header_name,
            "header_value": header_value,
        }

    @builtins.property
    def header_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#header_name ApplicationGateway#header_name}.'''
        result = self._values.get("header_name")
        assert result is not None, "Required property 'header_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def header_value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#header_value ApplicationGateway#header_value}.'''
        result = self._values.get("header_value")
        assert result is not None, "Required property 'header_value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewayRewriteRuleSetRewriteRuleRequestHeaderConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationGatewayRewriteRuleSetRewriteRuleRequestHeaderConfigurationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayRewriteRuleSetRewriteRuleRequestHeaderConfigurationList",
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
            type_hints = typing.get_type_hints(ApplicationGatewayRewriteRuleSetRewriteRuleRequestHeaderConfigurationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationGatewayRewriteRuleSetRewriteRuleRequestHeaderConfigurationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayRewriteRuleSetRewriteRuleRequestHeaderConfigurationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationGatewayRewriteRuleSetRewriteRuleRequestHeaderConfigurationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetRewriteRuleRequestHeaderConfigurationList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetRewriteRuleRequestHeaderConfigurationList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetRewriteRuleRequestHeaderConfigurationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayRewriteRuleSetRewriteRuleRequestHeaderConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayRewriteRuleSetRewriteRuleRequestHeaderConfiguration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayRewriteRuleSetRewriteRuleRequestHeaderConfiguration]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetRewriteRuleRequestHeaderConfigurationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationGatewayRewriteRuleSetRewriteRuleRequestHeaderConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayRewriteRuleSetRewriteRuleRequestHeaderConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationGatewayRewriteRuleSetRewriteRuleRequestHeaderConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="headerNameInput")
    def header_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="headerValueInput")
    def header_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerValueInput"))

    @builtins.property
    @jsii.member(jsii_name="headerName")
    def header_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerName"))

    @header_name.setter
    def header_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetRewriteRuleRequestHeaderConfigurationOutputReference, "header_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerName", value)

    @builtins.property
    @jsii.member(jsii_name="headerValue")
    def header_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerValue"))

    @header_value.setter
    def header_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetRewriteRuleRequestHeaderConfigurationOutputReference, "header_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationGatewayRewriteRuleSetRewriteRuleRequestHeaderConfiguration, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationGatewayRewriteRuleSetRewriteRuleRequestHeaderConfiguration, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationGatewayRewriteRuleSetRewriteRuleRequestHeaderConfiguration, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetRewriteRuleRequestHeaderConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayRewriteRuleSetRewriteRuleResponseHeaderConfiguration",
    jsii_struct_bases=[],
    name_mapping={"header_name": "headerName", "header_value": "headerValue"},
)
class ApplicationGatewayRewriteRuleSetRewriteRuleResponseHeaderConfiguration:
    def __init__(
        self,
        *,
        header_name: builtins.str,
        header_value: builtins.str,
    ) -> None:
        '''
        :param header_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#header_name ApplicationGateway#header_name}.
        :param header_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#header_value ApplicationGateway#header_value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayRewriteRuleSetRewriteRuleResponseHeaderConfiguration.__init__)
            check_type(argname="argument header_name", value=header_name, expected_type=type_hints["header_name"])
            check_type(argname="argument header_value", value=header_value, expected_type=type_hints["header_value"])
        self._values: typing.Dict[str, typing.Any] = {
            "header_name": header_name,
            "header_value": header_value,
        }

    @builtins.property
    def header_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#header_name ApplicationGateway#header_name}.'''
        result = self._values.get("header_name")
        assert result is not None, "Required property 'header_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def header_value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#header_value ApplicationGateway#header_value}.'''
        result = self._values.get("header_value")
        assert result is not None, "Required property 'header_value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewayRewriteRuleSetRewriteRuleResponseHeaderConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationGatewayRewriteRuleSetRewriteRuleResponseHeaderConfigurationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayRewriteRuleSetRewriteRuleResponseHeaderConfigurationList",
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
            type_hints = typing.get_type_hints(ApplicationGatewayRewriteRuleSetRewriteRuleResponseHeaderConfigurationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationGatewayRewriteRuleSetRewriteRuleResponseHeaderConfigurationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayRewriteRuleSetRewriteRuleResponseHeaderConfigurationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationGatewayRewriteRuleSetRewriteRuleResponseHeaderConfigurationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetRewriteRuleResponseHeaderConfigurationList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetRewriteRuleResponseHeaderConfigurationList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetRewriteRuleResponseHeaderConfigurationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayRewriteRuleSetRewriteRuleResponseHeaderConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayRewriteRuleSetRewriteRuleResponseHeaderConfiguration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayRewriteRuleSetRewriteRuleResponseHeaderConfiguration]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetRewriteRuleResponseHeaderConfigurationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationGatewayRewriteRuleSetRewriteRuleResponseHeaderConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayRewriteRuleSetRewriteRuleResponseHeaderConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationGatewayRewriteRuleSetRewriteRuleResponseHeaderConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="headerNameInput")
    def header_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="headerValueInput")
    def header_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerValueInput"))

    @builtins.property
    @jsii.member(jsii_name="headerName")
    def header_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerName"))

    @header_name.setter
    def header_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetRewriteRuleResponseHeaderConfigurationOutputReference, "header_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerName", value)

    @builtins.property
    @jsii.member(jsii_name="headerValue")
    def header_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerValue"))

    @header_value.setter
    def header_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetRewriteRuleResponseHeaderConfigurationOutputReference, "header_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationGatewayRewriteRuleSetRewriteRuleResponseHeaderConfiguration, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationGatewayRewriteRuleSetRewriteRuleResponseHeaderConfiguration, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationGatewayRewriteRuleSetRewriteRuleResponseHeaderConfiguration, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetRewriteRuleResponseHeaderConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayRewriteRuleSetRewriteRuleUrl",
    jsii_struct_bases=[],
    name_mapping={
        "components": "components",
        "path": "path",
        "query_string": "queryString",
        "reroute": "reroute",
    },
)
class ApplicationGatewayRewriteRuleSetRewriteRuleUrl:
    def __init__(
        self,
        *,
        components: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        query_string: typing.Optional[builtins.str] = None,
        reroute: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param components: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#components ApplicationGateway#components}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#path ApplicationGateway#path}.
        :param query_string: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#query_string ApplicationGateway#query_string}.
        :param reroute: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#reroute ApplicationGateway#reroute}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayRewriteRuleSetRewriteRuleUrl.__init__)
            check_type(argname="argument components", value=components, expected_type=type_hints["components"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument query_string", value=query_string, expected_type=type_hints["query_string"])
            check_type(argname="argument reroute", value=reroute, expected_type=type_hints["reroute"])
        self._values: typing.Dict[str, typing.Any] = {}
        if components is not None:
            self._values["components"] = components
        if path is not None:
            self._values["path"] = path
        if query_string is not None:
            self._values["query_string"] = query_string
        if reroute is not None:
            self._values["reroute"] = reroute

    @builtins.property
    def components(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#components ApplicationGateway#components}.'''
        result = self._values.get("components")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#path ApplicationGateway#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def query_string(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#query_string ApplicationGateway#query_string}.'''
        result = self._values.get("query_string")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def reroute(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#reroute ApplicationGateway#reroute}.'''
        result = self._values.get("reroute")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewayRewriteRuleSetRewriteRuleUrl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationGatewayRewriteRuleSetRewriteRuleUrlOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayRewriteRuleSetRewriteRuleUrlOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationGatewayRewriteRuleSetRewriteRuleUrlOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetComponents")
    def reset_components(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComponents", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetQueryString")
    def reset_query_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryString", []))

    @jsii.member(jsii_name="resetReroute")
    def reset_reroute(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReroute", []))

    @builtins.property
    @jsii.member(jsii_name="componentsInput")
    def components_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "componentsInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="queryStringInput")
    def query_string_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryStringInput"))

    @builtins.property
    @jsii.member(jsii_name="rerouteInput")
    def reroute_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "rerouteInput"))

    @builtins.property
    @jsii.member(jsii_name="components")
    def components(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "components"))

    @components.setter
    def components(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetRewriteRuleUrlOutputReference, "components").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "components", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetRewriteRuleUrlOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="queryString")
    def query_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "queryString"))

    @query_string.setter
    def query_string(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetRewriteRuleUrlOutputReference, "query_string").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryString", value)

    @builtins.property
    @jsii.member(jsii_name="reroute")
    def reroute(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "reroute"))

    @reroute.setter
    def reroute(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetRewriteRuleUrlOutputReference, "reroute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reroute", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ApplicationGatewayRewriteRuleSetRewriteRuleUrl]:
        return typing.cast(typing.Optional[ApplicationGatewayRewriteRuleSetRewriteRuleUrl], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApplicationGatewayRewriteRuleSetRewriteRuleUrl],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayRewriteRuleSetRewriteRuleUrlOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewaySku",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "tier": "tier", "capacity": "capacity"},
)
class ApplicationGatewaySku:
    def __init__(
        self,
        *,
        name: builtins.str,
        tier: builtins.str,
        capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.
        :param tier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#tier ApplicationGateway#tier}.
        :param capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#capacity ApplicationGateway#capacity}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewaySku.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tier", value=tier, expected_type=type_hints["tier"])
            check_type(argname="argument capacity", value=capacity, expected_type=type_hints["capacity"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "tier": tier,
        }
        if capacity is not None:
            self._values["capacity"] = capacity

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tier(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#tier ApplicationGateway#tier}.'''
        result = self._values.get("tier")
        assert result is not None, "Required property 'tier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#capacity ApplicationGateway#capacity}.'''
        result = self._values.get("capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewaySku(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationGatewaySkuOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewaySkuOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationGatewaySkuOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCapacity")
    def reset_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapacity", []))

    @builtins.property
    @jsii.member(jsii_name="capacityInput")
    def capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "capacityInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="tierInput")
    def tier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tierInput"))

    @builtins.property
    @jsii.member(jsii_name="capacity")
    def capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "capacity"))

    @capacity.setter
    def capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewaySkuOutputReference, "capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacity", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewaySkuOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tier")
    def tier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tier"))

    @tier.setter
    def tier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewaySkuOutputReference, "tier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tier", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApplicationGatewaySku]:
        return typing.cast(typing.Optional[ApplicationGatewaySku], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ApplicationGatewaySku]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewaySkuOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewaySslCertificate",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "data": "data",
        "key_vault_secret_id": "keyVaultSecretId",
        "password": "password",
    },
)
class ApplicationGatewaySslCertificate:
    def __init__(
        self,
        *,
        name: builtins.str,
        data: typing.Optional[builtins.str] = None,
        key_vault_secret_id: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.
        :param data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#data ApplicationGateway#data}.
        :param key_vault_secret_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#key_vault_secret_id ApplicationGateway#key_vault_secret_id}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#password ApplicationGateway#password}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewaySslCertificate.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            check_type(argname="argument key_vault_secret_id", value=key_vault_secret_id, expected_type=type_hints["key_vault_secret_id"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if data is not None:
            self._values["data"] = data
        if key_vault_secret_id is not None:
            self._values["key_vault_secret_id"] = key_vault_secret_id
        if password is not None:
            self._values["password"] = password

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#data ApplicationGateway#data}.'''
        result = self._values.get("data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_vault_secret_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#key_vault_secret_id ApplicationGateway#key_vault_secret_id}.'''
        result = self._values.get("key_vault_secret_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#password ApplicationGateway#password}.'''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewaySslCertificate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationGatewaySslCertificateList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewaySslCertificateList",
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
            type_hints = typing.get_type_hints(ApplicationGatewaySslCertificateList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationGatewaySslCertificateOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewaySslCertificateList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationGatewaySslCertificateOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewaySslCertificateList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewaySslCertificateList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewaySslCertificateList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewaySslCertificate]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewaySslCertificate]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewaySslCertificate]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewaySslCertificateList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationGatewaySslCertificateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewaySslCertificateOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationGatewaySslCertificateOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetData")
    def reset_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetData", []))

    @jsii.member(jsii_name="resetKeyVaultSecretId")
    def reset_key_vault_secret_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyVaultSecretId", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="publicCertData")
    def public_cert_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicCertData"))

    @builtins.property
    @jsii.member(jsii_name="dataInput")
    def data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataInput"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultSecretIdInput")
    def key_vault_secret_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyVaultSecretIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="data")
    def data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "data"))

    @data.setter
    def data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewaySslCertificateOutputReference, "data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "data", value)

    @builtins.property
    @jsii.member(jsii_name="keyVaultSecretId")
    def key_vault_secret_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyVaultSecretId"))

    @key_vault_secret_id.setter
    def key_vault_secret_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewaySslCertificateOutputReference, "key_vault_secret_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyVaultSecretId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewaySslCertificateOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewaySslCertificateOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationGatewaySslCertificate, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationGatewaySslCertificate, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationGatewaySslCertificate, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewaySslCertificateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewaySslPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "cipher_suites": "cipherSuites",
        "disabled_protocols": "disabledProtocols",
        "min_protocol_version": "minProtocolVersion",
        "policy_name": "policyName",
        "policy_type": "policyType",
    },
)
class ApplicationGatewaySslPolicy:
    def __init__(
        self,
        *,
        cipher_suites: typing.Optional[typing.Sequence[builtins.str]] = None,
        disabled_protocols: typing.Optional[typing.Sequence[builtins.str]] = None,
        min_protocol_version: typing.Optional[builtins.str] = None,
        policy_name: typing.Optional[builtins.str] = None,
        policy_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cipher_suites: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#cipher_suites ApplicationGateway#cipher_suites}.
        :param disabled_protocols: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#disabled_protocols ApplicationGateway#disabled_protocols}.
        :param min_protocol_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#min_protocol_version ApplicationGateway#min_protocol_version}.
        :param policy_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#policy_name ApplicationGateway#policy_name}.
        :param policy_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#policy_type ApplicationGateway#policy_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewaySslPolicy.__init__)
            check_type(argname="argument cipher_suites", value=cipher_suites, expected_type=type_hints["cipher_suites"])
            check_type(argname="argument disabled_protocols", value=disabled_protocols, expected_type=type_hints["disabled_protocols"])
            check_type(argname="argument min_protocol_version", value=min_protocol_version, expected_type=type_hints["min_protocol_version"])
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
            check_type(argname="argument policy_type", value=policy_type, expected_type=type_hints["policy_type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cipher_suites is not None:
            self._values["cipher_suites"] = cipher_suites
        if disabled_protocols is not None:
            self._values["disabled_protocols"] = disabled_protocols
        if min_protocol_version is not None:
            self._values["min_protocol_version"] = min_protocol_version
        if policy_name is not None:
            self._values["policy_name"] = policy_name
        if policy_type is not None:
            self._values["policy_type"] = policy_type

    @builtins.property
    def cipher_suites(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#cipher_suites ApplicationGateway#cipher_suites}.'''
        result = self._values.get("cipher_suites")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def disabled_protocols(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#disabled_protocols ApplicationGateway#disabled_protocols}.'''
        result = self._values.get("disabled_protocols")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def min_protocol_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#min_protocol_version ApplicationGateway#min_protocol_version}.'''
        result = self._values.get("min_protocol_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policy_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#policy_name ApplicationGateway#policy_name}.'''
        result = self._values.get("policy_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policy_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#policy_type ApplicationGateway#policy_type}.'''
        result = self._values.get("policy_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewaySslPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationGatewaySslPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewaySslPolicyOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationGatewaySslPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCipherSuites")
    def reset_cipher_suites(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCipherSuites", []))

    @jsii.member(jsii_name="resetDisabledProtocols")
    def reset_disabled_protocols(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisabledProtocols", []))

    @jsii.member(jsii_name="resetMinProtocolVersion")
    def reset_min_protocol_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinProtocolVersion", []))

    @jsii.member(jsii_name="resetPolicyName")
    def reset_policy_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicyName", []))

    @jsii.member(jsii_name="resetPolicyType")
    def reset_policy_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicyType", []))

    @builtins.property
    @jsii.member(jsii_name="cipherSuitesInput")
    def cipher_suites_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "cipherSuitesInput"))

    @builtins.property
    @jsii.member(jsii_name="disabledProtocolsInput")
    def disabled_protocols_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "disabledProtocolsInput"))

    @builtins.property
    @jsii.member(jsii_name="minProtocolVersionInput")
    def min_protocol_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minProtocolVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="policyNameInput")
    def policy_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="policyTypeInput")
    def policy_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="cipherSuites")
    def cipher_suites(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "cipherSuites"))

    @cipher_suites.setter
    def cipher_suites(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewaySslPolicyOutputReference, "cipher_suites").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cipherSuites", value)

    @builtins.property
    @jsii.member(jsii_name="disabledProtocols")
    def disabled_protocols(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "disabledProtocols"))

    @disabled_protocols.setter
    def disabled_protocols(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewaySslPolicyOutputReference, "disabled_protocols").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabledProtocols", value)

    @builtins.property
    @jsii.member(jsii_name="minProtocolVersion")
    def min_protocol_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minProtocolVersion"))

    @min_protocol_version.setter
    def min_protocol_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewaySslPolicyOutputReference, "min_protocol_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minProtocolVersion", value)

    @builtins.property
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policyName"))

    @policy_name.setter
    def policy_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewaySslPolicyOutputReference, "policy_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyName", value)

    @builtins.property
    @jsii.member(jsii_name="policyType")
    def policy_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policyType"))

    @policy_type.setter
    def policy_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewaySslPolicyOutputReference, "policy_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApplicationGatewaySslPolicy]:
        return typing.cast(typing.Optional[ApplicationGatewaySslPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApplicationGatewaySslPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewaySslPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewaySslProfile",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "ssl_policy": "sslPolicy",
        "trusted_client_certificate_names": "trustedClientCertificateNames",
        "verify_client_cert_issuer_dn": "verifyClientCertIssuerDn",
    },
)
class ApplicationGatewaySslProfile:
    def __init__(
        self,
        *,
        name: builtins.str,
        ssl_policy: typing.Optional[typing.Union["ApplicationGatewaySslProfileSslPolicy", typing.Dict[str, typing.Any]]] = None,
        trusted_client_certificate_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        verify_client_cert_issuer_dn: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.
        :param ssl_policy: ssl_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#ssl_policy ApplicationGateway#ssl_policy}
        :param trusted_client_certificate_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#trusted_client_certificate_names ApplicationGateway#trusted_client_certificate_names}.
        :param verify_client_cert_issuer_dn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#verify_client_cert_issuer_dn ApplicationGateway#verify_client_cert_issuer_dn}.
        '''
        if isinstance(ssl_policy, dict):
            ssl_policy = ApplicationGatewaySslProfileSslPolicy(**ssl_policy)
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewaySslProfile.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument ssl_policy", value=ssl_policy, expected_type=type_hints["ssl_policy"])
            check_type(argname="argument trusted_client_certificate_names", value=trusted_client_certificate_names, expected_type=type_hints["trusted_client_certificate_names"])
            check_type(argname="argument verify_client_cert_issuer_dn", value=verify_client_cert_issuer_dn, expected_type=type_hints["verify_client_cert_issuer_dn"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if ssl_policy is not None:
            self._values["ssl_policy"] = ssl_policy
        if trusted_client_certificate_names is not None:
            self._values["trusted_client_certificate_names"] = trusted_client_certificate_names
        if verify_client_cert_issuer_dn is not None:
            self._values["verify_client_cert_issuer_dn"] = verify_client_cert_issuer_dn

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ssl_policy(self) -> typing.Optional["ApplicationGatewaySslProfileSslPolicy"]:
        '''ssl_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#ssl_policy ApplicationGateway#ssl_policy}
        '''
        result = self._values.get("ssl_policy")
        return typing.cast(typing.Optional["ApplicationGatewaySslProfileSslPolicy"], result)

    @builtins.property
    def trusted_client_certificate_names(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#trusted_client_certificate_names ApplicationGateway#trusted_client_certificate_names}.'''
        result = self._values.get("trusted_client_certificate_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def verify_client_cert_issuer_dn(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#verify_client_cert_issuer_dn ApplicationGateway#verify_client_cert_issuer_dn}.'''
        result = self._values.get("verify_client_cert_issuer_dn")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewaySslProfile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationGatewaySslProfileList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewaySslProfileList",
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
            type_hints = typing.get_type_hints(ApplicationGatewaySslProfileList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ApplicationGatewaySslProfileOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewaySslProfileList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationGatewaySslProfileOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewaySslProfileList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewaySslProfileList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewaySslProfileList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewaySslProfile]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewaySslProfile]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewaySslProfile]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewaySslProfileList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationGatewaySslProfileOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewaySslProfileOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationGatewaySslProfileOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putSslPolicy")
    def put_ssl_policy(
        self,
        *,
        cipher_suites: typing.Optional[typing.Sequence[builtins.str]] = None,
        disabled_protocols: typing.Optional[typing.Sequence[builtins.str]] = None,
        min_protocol_version: typing.Optional[builtins.str] = None,
        policy_name: typing.Optional[builtins.str] = None,
        policy_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cipher_suites: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#cipher_suites ApplicationGateway#cipher_suites}.
        :param disabled_protocols: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#disabled_protocols ApplicationGateway#disabled_protocols}.
        :param min_protocol_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#min_protocol_version ApplicationGateway#min_protocol_version}.
        :param policy_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#policy_name ApplicationGateway#policy_name}.
        :param policy_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#policy_type ApplicationGateway#policy_type}.
        '''
        value = ApplicationGatewaySslProfileSslPolicy(
            cipher_suites=cipher_suites,
            disabled_protocols=disabled_protocols,
            min_protocol_version=min_protocol_version,
            policy_name=policy_name,
            policy_type=policy_type,
        )

        return typing.cast(None, jsii.invoke(self, "putSslPolicy", [value]))

    @jsii.member(jsii_name="resetSslPolicy")
    def reset_ssl_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslPolicy", []))

    @jsii.member(jsii_name="resetTrustedClientCertificateNames")
    def reset_trusted_client_certificate_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrustedClientCertificateNames", []))

    @jsii.member(jsii_name="resetVerifyClientCertIssuerDn")
    def reset_verify_client_cert_issuer_dn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVerifyClientCertIssuerDn", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="sslPolicy")
    def ssl_policy(self) -> "ApplicationGatewaySslProfileSslPolicyOutputReference":
        return typing.cast("ApplicationGatewaySslProfileSslPolicyOutputReference", jsii.get(self, "sslPolicy"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sslPolicyInput")
    def ssl_policy_input(
        self,
    ) -> typing.Optional["ApplicationGatewaySslProfileSslPolicy"]:
        return typing.cast(typing.Optional["ApplicationGatewaySslProfileSslPolicy"], jsii.get(self, "sslPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="trustedClientCertificateNamesInput")
    def trusted_client_certificate_names_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "trustedClientCertificateNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="verifyClientCertIssuerDnInput")
    def verify_client_cert_issuer_dn_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "verifyClientCertIssuerDnInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewaySslProfileOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="trustedClientCertificateNames")
    def trusted_client_certificate_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "trustedClientCertificateNames"))

    @trusted_client_certificate_names.setter
    def trusted_client_certificate_names(
        self,
        value: typing.List[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewaySslProfileOutputReference, "trusted_client_certificate_names").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trustedClientCertificateNames", value)

    @builtins.property
    @jsii.member(jsii_name="verifyClientCertIssuerDn")
    def verify_client_cert_issuer_dn(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "verifyClientCertIssuerDn"))

    @verify_client_cert_issuer_dn.setter
    def verify_client_cert_issuer_dn(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewaySslProfileOutputReference, "verify_client_cert_issuer_dn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "verifyClientCertIssuerDn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationGatewaySslProfile, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationGatewaySslProfile, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationGatewaySslProfile, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewaySslProfileOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewaySslProfileSslPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "cipher_suites": "cipherSuites",
        "disabled_protocols": "disabledProtocols",
        "min_protocol_version": "minProtocolVersion",
        "policy_name": "policyName",
        "policy_type": "policyType",
    },
)
class ApplicationGatewaySslProfileSslPolicy:
    def __init__(
        self,
        *,
        cipher_suites: typing.Optional[typing.Sequence[builtins.str]] = None,
        disabled_protocols: typing.Optional[typing.Sequence[builtins.str]] = None,
        min_protocol_version: typing.Optional[builtins.str] = None,
        policy_name: typing.Optional[builtins.str] = None,
        policy_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cipher_suites: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#cipher_suites ApplicationGateway#cipher_suites}.
        :param disabled_protocols: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#disabled_protocols ApplicationGateway#disabled_protocols}.
        :param min_protocol_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#min_protocol_version ApplicationGateway#min_protocol_version}.
        :param policy_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#policy_name ApplicationGateway#policy_name}.
        :param policy_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#policy_type ApplicationGateway#policy_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewaySslProfileSslPolicy.__init__)
            check_type(argname="argument cipher_suites", value=cipher_suites, expected_type=type_hints["cipher_suites"])
            check_type(argname="argument disabled_protocols", value=disabled_protocols, expected_type=type_hints["disabled_protocols"])
            check_type(argname="argument min_protocol_version", value=min_protocol_version, expected_type=type_hints["min_protocol_version"])
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
            check_type(argname="argument policy_type", value=policy_type, expected_type=type_hints["policy_type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cipher_suites is not None:
            self._values["cipher_suites"] = cipher_suites
        if disabled_protocols is not None:
            self._values["disabled_protocols"] = disabled_protocols
        if min_protocol_version is not None:
            self._values["min_protocol_version"] = min_protocol_version
        if policy_name is not None:
            self._values["policy_name"] = policy_name
        if policy_type is not None:
            self._values["policy_type"] = policy_type

    @builtins.property
    def cipher_suites(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#cipher_suites ApplicationGateway#cipher_suites}.'''
        result = self._values.get("cipher_suites")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def disabled_protocols(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#disabled_protocols ApplicationGateway#disabled_protocols}.'''
        result = self._values.get("disabled_protocols")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def min_protocol_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#min_protocol_version ApplicationGateway#min_protocol_version}.'''
        result = self._values.get("min_protocol_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policy_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#policy_name ApplicationGateway#policy_name}.'''
        result = self._values.get("policy_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policy_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#policy_type ApplicationGateway#policy_type}.'''
        result = self._values.get("policy_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewaySslProfileSslPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationGatewaySslProfileSslPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewaySslProfileSslPolicyOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationGatewaySslProfileSslPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCipherSuites")
    def reset_cipher_suites(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCipherSuites", []))

    @jsii.member(jsii_name="resetDisabledProtocols")
    def reset_disabled_protocols(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisabledProtocols", []))

    @jsii.member(jsii_name="resetMinProtocolVersion")
    def reset_min_protocol_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinProtocolVersion", []))

    @jsii.member(jsii_name="resetPolicyName")
    def reset_policy_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicyName", []))

    @jsii.member(jsii_name="resetPolicyType")
    def reset_policy_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicyType", []))

    @builtins.property
    @jsii.member(jsii_name="cipherSuitesInput")
    def cipher_suites_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "cipherSuitesInput"))

    @builtins.property
    @jsii.member(jsii_name="disabledProtocolsInput")
    def disabled_protocols_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "disabledProtocolsInput"))

    @builtins.property
    @jsii.member(jsii_name="minProtocolVersionInput")
    def min_protocol_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minProtocolVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="policyNameInput")
    def policy_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="policyTypeInput")
    def policy_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="cipherSuites")
    def cipher_suites(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "cipherSuites"))

    @cipher_suites.setter
    def cipher_suites(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewaySslProfileSslPolicyOutputReference, "cipher_suites").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cipherSuites", value)

    @builtins.property
    @jsii.member(jsii_name="disabledProtocols")
    def disabled_protocols(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "disabledProtocols"))

    @disabled_protocols.setter
    def disabled_protocols(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewaySslProfileSslPolicyOutputReference, "disabled_protocols").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabledProtocols", value)

    @builtins.property
    @jsii.member(jsii_name="minProtocolVersion")
    def min_protocol_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minProtocolVersion"))

    @min_protocol_version.setter
    def min_protocol_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewaySslProfileSslPolicyOutputReference, "min_protocol_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minProtocolVersion", value)

    @builtins.property
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policyName"))

    @policy_name.setter
    def policy_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewaySslProfileSslPolicyOutputReference, "policy_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyName", value)

    @builtins.property
    @jsii.member(jsii_name="policyType")
    def policy_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policyType"))

    @policy_type.setter
    def policy_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewaySslProfileSslPolicyOutputReference, "policy_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApplicationGatewaySslProfileSslPolicy]:
        return typing.cast(typing.Optional[ApplicationGatewaySslProfileSslPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApplicationGatewaySslProfileSslPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewaySslProfileSslPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class ApplicationGatewayTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#create ApplicationGateway#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#delete ApplicationGateway#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#read ApplicationGateway#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#update ApplicationGateway#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#create ApplicationGateway#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#delete ApplicationGateway#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#read ApplicationGateway#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#update ApplicationGateway#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewayTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationGatewayTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationGatewayTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationGatewayTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationGatewayTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationGatewayTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayTrustedClientCertificate",
    jsii_struct_bases=[],
    name_mapping={"data": "data", "name": "name"},
)
class ApplicationGatewayTrustedClientCertificate:
    def __init__(self, *, data: builtins.str, name: builtins.str) -> None:
        '''
        :param data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#data ApplicationGateway#data}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayTrustedClientCertificate.__init__)
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "data": data,
            "name": name,
        }

    @builtins.property
    def data(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#data ApplicationGateway#data}.'''
        result = self._values.get("data")
        assert result is not None, "Required property 'data' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewayTrustedClientCertificate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationGatewayTrustedClientCertificateList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayTrustedClientCertificateList",
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
            type_hints = typing.get_type_hints(ApplicationGatewayTrustedClientCertificateList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationGatewayTrustedClientCertificateOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayTrustedClientCertificateList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationGatewayTrustedClientCertificateOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayTrustedClientCertificateList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayTrustedClientCertificateList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayTrustedClientCertificateList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayTrustedClientCertificate]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayTrustedClientCertificate]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayTrustedClientCertificate]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayTrustedClientCertificateList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationGatewayTrustedClientCertificateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayTrustedClientCertificateOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationGatewayTrustedClientCertificateOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="dataInput")
    def data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="data")
    def data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "data"))

    @data.setter
    def data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayTrustedClientCertificateOutputReference, "data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "data", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayTrustedClientCertificateOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationGatewayTrustedClientCertificate, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationGatewayTrustedClientCertificate, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationGatewayTrustedClientCertificate, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayTrustedClientCertificateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayTrustedRootCertificate",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "data": "data",
        "key_vault_secret_id": "keyVaultSecretId",
    },
)
class ApplicationGatewayTrustedRootCertificate:
    def __init__(
        self,
        *,
        name: builtins.str,
        data: typing.Optional[builtins.str] = None,
        key_vault_secret_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.
        :param data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#data ApplicationGateway#data}.
        :param key_vault_secret_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#key_vault_secret_id ApplicationGateway#key_vault_secret_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayTrustedRootCertificate.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            check_type(argname="argument key_vault_secret_id", value=key_vault_secret_id, expected_type=type_hints["key_vault_secret_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if data is not None:
            self._values["data"] = data
        if key_vault_secret_id is not None:
            self._values["key_vault_secret_id"] = key_vault_secret_id

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#data ApplicationGateway#data}.'''
        result = self._values.get("data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_vault_secret_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#key_vault_secret_id ApplicationGateway#key_vault_secret_id}.'''
        result = self._values.get("key_vault_secret_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewayTrustedRootCertificate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationGatewayTrustedRootCertificateList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayTrustedRootCertificateList",
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
            type_hints = typing.get_type_hints(ApplicationGatewayTrustedRootCertificateList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationGatewayTrustedRootCertificateOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayTrustedRootCertificateList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationGatewayTrustedRootCertificateOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayTrustedRootCertificateList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayTrustedRootCertificateList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayTrustedRootCertificateList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayTrustedRootCertificate]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayTrustedRootCertificate]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayTrustedRootCertificate]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayTrustedRootCertificateList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationGatewayTrustedRootCertificateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayTrustedRootCertificateOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationGatewayTrustedRootCertificateOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetData")
    def reset_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetData", []))

    @jsii.member(jsii_name="resetKeyVaultSecretId")
    def reset_key_vault_secret_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyVaultSecretId", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="dataInput")
    def data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataInput"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultSecretIdInput")
    def key_vault_secret_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyVaultSecretIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="data")
    def data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "data"))

    @data.setter
    def data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayTrustedRootCertificateOutputReference, "data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "data", value)

    @builtins.property
    @jsii.member(jsii_name="keyVaultSecretId")
    def key_vault_secret_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyVaultSecretId"))

    @key_vault_secret_id.setter
    def key_vault_secret_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayTrustedRootCertificateOutputReference, "key_vault_secret_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyVaultSecretId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayTrustedRootCertificateOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationGatewayTrustedRootCertificate, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationGatewayTrustedRootCertificate, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationGatewayTrustedRootCertificate, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayTrustedRootCertificateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayUrlPathMap",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "path_rule": "pathRule",
        "default_backend_address_pool_name": "defaultBackendAddressPoolName",
        "default_backend_http_settings_name": "defaultBackendHttpSettingsName",
        "default_redirect_configuration_name": "defaultRedirectConfigurationName",
        "default_rewrite_rule_set_name": "defaultRewriteRuleSetName",
    },
)
class ApplicationGatewayUrlPathMap:
    def __init__(
        self,
        *,
        name: builtins.str,
        path_rule: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayUrlPathMapPathRule", typing.Dict[str, typing.Any]]]],
        default_backend_address_pool_name: typing.Optional[builtins.str] = None,
        default_backend_http_settings_name: typing.Optional[builtins.str] = None,
        default_redirect_configuration_name: typing.Optional[builtins.str] = None,
        default_rewrite_rule_set_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.
        :param path_rule: path_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#path_rule ApplicationGateway#path_rule}
        :param default_backend_address_pool_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#default_backend_address_pool_name ApplicationGateway#default_backend_address_pool_name}.
        :param default_backend_http_settings_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#default_backend_http_settings_name ApplicationGateway#default_backend_http_settings_name}.
        :param default_redirect_configuration_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#default_redirect_configuration_name ApplicationGateway#default_redirect_configuration_name}.
        :param default_rewrite_rule_set_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#default_rewrite_rule_set_name ApplicationGateway#default_rewrite_rule_set_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayUrlPathMap.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument path_rule", value=path_rule, expected_type=type_hints["path_rule"])
            check_type(argname="argument default_backend_address_pool_name", value=default_backend_address_pool_name, expected_type=type_hints["default_backend_address_pool_name"])
            check_type(argname="argument default_backend_http_settings_name", value=default_backend_http_settings_name, expected_type=type_hints["default_backend_http_settings_name"])
            check_type(argname="argument default_redirect_configuration_name", value=default_redirect_configuration_name, expected_type=type_hints["default_redirect_configuration_name"])
            check_type(argname="argument default_rewrite_rule_set_name", value=default_rewrite_rule_set_name, expected_type=type_hints["default_rewrite_rule_set_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "path_rule": path_rule,
        }
        if default_backend_address_pool_name is not None:
            self._values["default_backend_address_pool_name"] = default_backend_address_pool_name
        if default_backend_http_settings_name is not None:
            self._values["default_backend_http_settings_name"] = default_backend_http_settings_name
        if default_redirect_configuration_name is not None:
            self._values["default_redirect_configuration_name"] = default_redirect_configuration_name
        if default_rewrite_rule_set_name is not None:
            self._values["default_rewrite_rule_set_name"] = default_rewrite_rule_set_name

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path_rule(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayUrlPathMapPathRule"]]:
        '''path_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#path_rule ApplicationGateway#path_rule}
        '''
        result = self._values.get("path_rule")
        assert result is not None, "Required property 'path_rule' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayUrlPathMapPathRule"]], result)

    @builtins.property
    def default_backend_address_pool_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#default_backend_address_pool_name ApplicationGateway#default_backend_address_pool_name}.'''
        result = self._values.get("default_backend_address_pool_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_backend_http_settings_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#default_backend_http_settings_name ApplicationGateway#default_backend_http_settings_name}.'''
        result = self._values.get("default_backend_http_settings_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_redirect_configuration_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#default_redirect_configuration_name ApplicationGateway#default_redirect_configuration_name}.'''
        result = self._values.get("default_redirect_configuration_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_rewrite_rule_set_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#default_rewrite_rule_set_name ApplicationGateway#default_rewrite_rule_set_name}.'''
        result = self._values.get("default_rewrite_rule_set_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewayUrlPathMap(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationGatewayUrlPathMapList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayUrlPathMapList",
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
            type_hints = typing.get_type_hints(ApplicationGatewayUrlPathMapList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ApplicationGatewayUrlPathMapOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayUrlPathMapList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationGatewayUrlPathMapOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayUrlPathMapList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayUrlPathMapList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayUrlPathMapList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayUrlPathMap]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayUrlPathMap]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayUrlPathMap]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayUrlPathMapList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationGatewayUrlPathMapOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayUrlPathMapOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationGatewayUrlPathMapOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putPathRule")
    def put_path_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayUrlPathMapPathRule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayUrlPathMapOutputReference.put_path_rule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPathRule", [value]))

    @jsii.member(jsii_name="resetDefaultBackendAddressPoolName")
    def reset_default_backend_address_pool_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultBackendAddressPoolName", []))

    @jsii.member(jsii_name="resetDefaultBackendHttpSettingsName")
    def reset_default_backend_http_settings_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultBackendHttpSettingsName", []))

    @jsii.member(jsii_name="resetDefaultRedirectConfigurationName")
    def reset_default_redirect_configuration_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultRedirectConfigurationName", []))

    @jsii.member(jsii_name="resetDefaultRewriteRuleSetName")
    def reset_default_rewrite_rule_set_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultRewriteRuleSetName", []))

    @builtins.property
    @jsii.member(jsii_name="defaultBackendAddressPoolId")
    def default_backend_address_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultBackendAddressPoolId"))

    @builtins.property
    @jsii.member(jsii_name="defaultBackendHttpSettingsId")
    def default_backend_http_settings_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultBackendHttpSettingsId"))

    @builtins.property
    @jsii.member(jsii_name="defaultRedirectConfigurationId")
    def default_redirect_configuration_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultRedirectConfigurationId"))

    @builtins.property
    @jsii.member(jsii_name="defaultRewriteRuleSetId")
    def default_rewrite_rule_set_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultRewriteRuleSetId"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="pathRule")
    def path_rule(self) -> "ApplicationGatewayUrlPathMapPathRuleList":
        return typing.cast("ApplicationGatewayUrlPathMapPathRuleList", jsii.get(self, "pathRule"))

    @builtins.property
    @jsii.member(jsii_name="defaultBackendAddressPoolNameInput")
    def default_backend_address_pool_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultBackendAddressPoolNameInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultBackendHttpSettingsNameInput")
    def default_backend_http_settings_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultBackendHttpSettingsNameInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultRedirectConfigurationNameInput")
    def default_redirect_configuration_name_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultRedirectConfigurationNameInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultRewriteRuleSetNameInput")
    def default_rewrite_rule_set_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultRewriteRuleSetNameInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="pathRuleInput")
    def path_rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayUrlPathMapPathRule"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayUrlPathMapPathRule"]]], jsii.get(self, "pathRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultBackendAddressPoolName")
    def default_backend_address_pool_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultBackendAddressPoolName"))

    @default_backend_address_pool_name.setter
    def default_backend_address_pool_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayUrlPathMapOutputReference, "default_backend_address_pool_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultBackendAddressPoolName", value)

    @builtins.property
    @jsii.member(jsii_name="defaultBackendHttpSettingsName")
    def default_backend_http_settings_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultBackendHttpSettingsName"))

    @default_backend_http_settings_name.setter
    def default_backend_http_settings_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayUrlPathMapOutputReference, "default_backend_http_settings_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultBackendHttpSettingsName", value)

    @builtins.property
    @jsii.member(jsii_name="defaultRedirectConfigurationName")
    def default_redirect_configuration_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultRedirectConfigurationName"))

    @default_redirect_configuration_name.setter
    def default_redirect_configuration_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayUrlPathMapOutputReference, "default_redirect_configuration_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultRedirectConfigurationName", value)

    @builtins.property
    @jsii.member(jsii_name="defaultRewriteRuleSetName")
    def default_rewrite_rule_set_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultRewriteRuleSetName"))

    @default_rewrite_rule_set_name.setter
    def default_rewrite_rule_set_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayUrlPathMapOutputReference, "default_rewrite_rule_set_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultRewriteRuleSetName", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayUrlPathMapOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationGatewayUrlPathMap, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationGatewayUrlPathMap, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationGatewayUrlPathMap, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayUrlPathMapOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayUrlPathMapPathRule",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "paths": "paths",
        "backend_address_pool_name": "backendAddressPoolName",
        "backend_http_settings_name": "backendHttpSettingsName",
        "firewall_policy_id": "firewallPolicyId",
        "redirect_configuration_name": "redirectConfigurationName",
        "rewrite_rule_set_name": "rewriteRuleSetName",
    },
)
class ApplicationGatewayUrlPathMapPathRule:
    def __init__(
        self,
        *,
        name: builtins.str,
        paths: typing.Sequence[builtins.str],
        backend_address_pool_name: typing.Optional[builtins.str] = None,
        backend_http_settings_name: typing.Optional[builtins.str] = None,
        firewall_policy_id: typing.Optional[builtins.str] = None,
        redirect_configuration_name: typing.Optional[builtins.str] = None,
        rewrite_rule_set_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.
        :param paths: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#paths ApplicationGateway#paths}.
        :param backend_address_pool_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#backend_address_pool_name ApplicationGateway#backend_address_pool_name}.
        :param backend_http_settings_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#backend_http_settings_name ApplicationGateway#backend_http_settings_name}.
        :param firewall_policy_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#firewall_policy_id ApplicationGateway#firewall_policy_id}.
        :param redirect_configuration_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#redirect_configuration_name ApplicationGateway#redirect_configuration_name}.
        :param rewrite_rule_set_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#rewrite_rule_set_name ApplicationGateway#rewrite_rule_set_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayUrlPathMapPathRule.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument paths", value=paths, expected_type=type_hints["paths"])
            check_type(argname="argument backend_address_pool_name", value=backend_address_pool_name, expected_type=type_hints["backend_address_pool_name"])
            check_type(argname="argument backend_http_settings_name", value=backend_http_settings_name, expected_type=type_hints["backend_http_settings_name"])
            check_type(argname="argument firewall_policy_id", value=firewall_policy_id, expected_type=type_hints["firewall_policy_id"])
            check_type(argname="argument redirect_configuration_name", value=redirect_configuration_name, expected_type=type_hints["redirect_configuration_name"])
            check_type(argname="argument rewrite_rule_set_name", value=rewrite_rule_set_name, expected_type=type_hints["rewrite_rule_set_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "paths": paths,
        }
        if backend_address_pool_name is not None:
            self._values["backend_address_pool_name"] = backend_address_pool_name
        if backend_http_settings_name is not None:
            self._values["backend_http_settings_name"] = backend_http_settings_name
        if firewall_policy_id is not None:
            self._values["firewall_policy_id"] = firewall_policy_id
        if redirect_configuration_name is not None:
            self._values["redirect_configuration_name"] = redirect_configuration_name
        if rewrite_rule_set_name is not None:
            self._values["rewrite_rule_set_name"] = rewrite_rule_set_name

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#name ApplicationGateway#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def paths(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#paths ApplicationGateway#paths}.'''
        result = self._values.get("paths")
        assert result is not None, "Required property 'paths' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def backend_address_pool_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#backend_address_pool_name ApplicationGateway#backend_address_pool_name}.'''
        result = self._values.get("backend_address_pool_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def backend_http_settings_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#backend_http_settings_name ApplicationGateway#backend_http_settings_name}.'''
        result = self._values.get("backend_http_settings_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def firewall_policy_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#firewall_policy_id ApplicationGateway#firewall_policy_id}.'''
        result = self._values.get("firewall_policy_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redirect_configuration_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#redirect_configuration_name ApplicationGateway#redirect_configuration_name}.'''
        result = self._values.get("redirect_configuration_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rewrite_rule_set_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#rewrite_rule_set_name ApplicationGateway#rewrite_rule_set_name}.'''
        result = self._values.get("rewrite_rule_set_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewayUrlPathMapPathRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationGatewayUrlPathMapPathRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayUrlPathMapPathRuleList",
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
            type_hints = typing.get_type_hints(ApplicationGatewayUrlPathMapPathRuleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationGatewayUrlPathMapPathRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayUrlPathMapPathRuleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationGatewayUrlPathMapPathRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayUrlPathMapPathRuleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayUrlPathMapPathRuleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayUrlPathMapPathRuleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayUrlPathMapPathRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayUrlPathMapPathRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayUrlPathMapPathRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayUrlPathMapPathRuleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationGatewayUrlPathMapPathRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayUrlPathMapPathRuleOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationGatewayUrlPathMapPathRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetBackendAddressPoolName")
    def reset_backend_address_pool_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackendAddressPoolName", []))

    @jsii.member(jsii_name="resetBackendHttpSettingsName")
    def reset_backend_http_settings_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackendHttpSettingsName", []))

    @jsii.member(jsii_name="resetFirewallPolicyId")
    def reset_firewall_policy_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFirewallPolicyId", []))

    @jsii.member(jsii_name="resetRedirectConfigurationName")
    def reset_redirect_configuration_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectConfigurationName", []))

    @jsii.member(jsii_name="resetRewriteRuleSetName")
    def reset_rewrite_rule_set_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRewriteRuleSetName", []))

    @builtins.property
    @jsii.member(jsii_name="backendAddressPoolId")
    def backend_address_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backendAddressPoolId"))

    @builtins.property
    @jsii.member(jsii_name="backendHttpSettingsId")
    def backend_http_settings_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backendHttpSettingsId"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="redirectConfigurationId")
    def redirect_configuration_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectConfigurationId"))

    @builtins.property
    @jsii.member(jsii_name="rewriteRuleSetId")
    def rewrite_rule_set_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rewriteRuleSetId"))

    @builtins.property
    @jsii.member(jsii_name="backendAddressPoolNameInput")
    def backend_address_pool_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backendAddressPoolNameInput"))

    @builtins.property
    @jsii.member(jsii_name="backendHttpSettingsNameInput")
    def backend_http_settings_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backendHttpSettingsNameInput"))

    @builtins.property
    @jsii.member(jsii_name="firewallPolicyIdInput")
    def firewall_policy_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "firewallPolicyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="pathsInput")
    def paths_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "pathsInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectConfigurationNameInput")
    def redirect_configuration_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectConfigurationNameInput"))

    @builtins.property
    @jsii.member(jsii_name="rewriteRuleSetNameInput")
    def rewrite_rule_set_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rewriteRuleSetNameInput"))

    @builtins.property
    @jsii.member(jsii_name="backendAddressPoolName")
    def backend_address_pool_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backendAddressPoolName"))

    @backend_address_pool_name.setter
    def backend_address_pool_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayUrlPathMapPathRuleOutputReference, "backend_address_pool_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backendAddressPoolName", value)

    @builtins.property
    @jsii.member(jsii_name="backendHttpSettingsName")
    def backend_http_settings_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backendHttpSettingsName"))

    @backend_http_settings_name.setter
    def backend_http_settings_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayUrlPathMapPathRuleOutputReference, "backend_http_settings_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backendHttpSettingsName", value)

    @builtins.property
    @jsii.member(jsii_name="firewallPolicyId")
    def firewall_policy_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "firewallPolicyId"))

    @firewall_policy_id.setter
    def firewall_policy_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayUrlPathMapPathRuleOutputReference, "firewall_policy_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firewallPolicyId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayUrlPathMapPathRuleOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="paths")
    def paths(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "paths"))

    @paths.setter
    def paths(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayUrlPathMapPathRuleOutputReference, "paths").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "paths", value)

    @builtins.property
    @jsii.member(jsii_name="redirectConfigurationName")
    def redirect_configuration_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectConfigurationName"))

    @redirect_configuration_name.setter
    def redirect_configuration_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayUrlPathMapPathRuleOutputReference, "redirect_configuration_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectConfigurationName", value)

    @builtins.property
    @jsii.member(jsii_name="rewriteRuleSetName")
    def rewrite_rule_set_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rewriteRuleSetName"))

    @rewrite_rule_set_name.setter
    def rewrite_rule_set_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayUrlPathMapPathRuleOutputReference, "rewrite_rule_set_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rewriteRuleSetName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationGatewayUrlPathMapPathRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationGatewayUrlPathMapPathRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationGatewayUrlPathMapPathRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayUrlPathMapPathRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayWafConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "firewall_mode": "firewallMode",
        "rule_set_version": "ruleSetVersion",
        "disabled_rule_group": "disabledRuleGroup",
        "exclusion": "exclusion",
        "file_upload_limit_mb": "fileUploadLimitMb",
        "max_request_body_size_kb": "maxRequestBodySizeKb",
        "request_body_check": "requestBodyCheck",
        "rule_set_type": "ruleSetType",
    },
)
class ApplicationGatewayWafConfiguration:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        firewall_mode: builtins.str,
        rule_set_version: builtins.str,
        disabled_rule_group: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayWafConfigurationDisabledRuleGroup", typing.Dict[str, typing.Any]]]]] = None,
        exclusion: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApplicationGatewayWafConfigurationExclusion", typing.Dict[str, typing.Any]]]]] = None,
        file_upload_limit_mb: typing.Optional[jsii.Number] = None,
        max_request_body_size_kb: typing.Optional[jsii.Number] = None,
        request_body_check: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        rule_set_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#enabled ApplicationGateway#enabled}.
        :param firewall_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#firewall_mode ApplicationGateway#firewall_mode}.
        :param rule_set_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#rule_set_version ApplicationGateway#rule_set_version}.
        :param disabled_rule_group: disabled_rule_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#disabled_rule_group ApplicationGateway#disabled_rule_group}
        :param exclusion: exclusion block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#exclusion ApplicationGateway#exclusion}
        :param file_upload_limit_mb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#file_upload_limit_mb ApplicationGateway#file_upload_limit_mb}.
        :param max_request_body_size_kb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#max_request_body_size_kb ApplicationGateway#max_request_body_size_kb}.
        :param request_body_check: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#request_body_check ApplicationGateway#request_body_check}.
        :param rule_set_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#rule_set_type ApplicationGateway#rule_set_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayWafConfiguration.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument firewall_mode", value=firewall_mode, expected_type=type_hints["firewall_mode"])
            check_type(argname="argument rule_set_version", value=rule_set_version, expected_type=type_hints["rule_set_version"])
            check_type(argname="argument disabled_rule_group", value=disabled_rule_group, expected_type=type_hints["disabled_rule_group"])
            check_type(argname="argument exclusion", value=exclusion, expected_type=type_hints["exclusion"])
            check_type(argname="argument file_upload_limit_mb", value=file_upload_limit_mb, expected_type=type_hints["file_upload_limit_mb"])
            check_type(argname="argument max_request_body_size_kb", value=max_request_body_size_kb, expected_type=type_hints["max_request_body_size_kb"])
            check_type(argname="argument request_body_check", value=request_body_check, expected_type=type_hints["request_body_check"])
            check_type(argname="argument rule_set_type", value=rule_set_type, expected_type=type_hints["rule_set_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
            "firewall_mode": firewall_mode,
            "rule_set_version": rule_set_version,
        }
        if disabled_rule_group is not None:
            self._values["disabled_rule_group"] = disabled_rule_group
        if exclusion is not None:
            self._values["exclusion"] = exclusion
        if file_upload_limit_mb is not None:
            self._values["file_upload_limit_mb"] = file_upload_limit_mb
        if max_request_body_size_kb is not None:
            self._values["max_request_body_size_kb"] = max_request_body_size_kb
        if request_body_check is not None:
            self._values["request_body_check"] = request_body_check
        if rule_set_type is not None:
            self._values["rule_set_type"] = rule_set_type

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#enabled ApplicationGateway#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def firewall_mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#firewall_mode ApplicationGateway#firewall_mode}.'''
        result = self._values.get("firewall_mode")
        assert result is not None, "Required property 'firewall_mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_set_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#rule_set_version ApplicationGateway#rule_set_version}.'''
        result = self._values.get("rule_set_version")
        assert result is not None, "Required property 'rule_set_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disabled_rule_group(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayWafConfigurationDisabledRuleGroup"]]]:
        '''disabled_rule_group block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#disabled_rule_group ApplicationGateway#disabled_rule_group}
        '''
        result = self._values.get("disabled_rule_group")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayWafConfigurationDisabledRuleGroup"]]], result)

    @builtins.property
    def exclusion(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayWafConfigurationExclusion"]]]:
        '''exclusion block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#exclusion ApplicationGateway#exclusion}
        '''
        result = self._values.get("exclusion")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApplicationGatewayWafConfigurationExclusion"]]], result)

    @builtins.property
    def file_upload_limit_mb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#file_upload_limit_mb ApplicationGateway#file_upload_limit_mb}.'''
        result = self._values.get("file_upload_limit_mb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_request_body_size_kb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#max_request_body_size_kb ApplicationGateway#max_request_body_size_kb}.'''
        result = self._values.get("max_request_body_size_kb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def request_body_check(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#request_body_check ApplicationGateway#request_body_check}.'''
        result = self._values.get("request_body_check")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def rule_set_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#rule_set_type ApplicationGateway#rule_set_type}.'''
        result = self._values.get("rule_set_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewayWafConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayWafConfigurationDisabledRuleGroup",
    jsii_struct_bases=[],
    name_mapping={"rule_group_name": "ruleGroupName", "rules": "rules"},
)
class ApplicationGatewayWafConfigurationDisabledRuleGroup:
    def __init__(
        self,
        *,
        rule_group_name: builtins.str,
        rules: typing.Optional[typing.Sequence[jsii.Number]] = None,
    ) -> None:
        '''
        :param rule_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#rule_group_name ApplicationGateway#rule_group_name}.
        :param rules: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#rules ApplicationGateway#rules}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayWafConfigurationDisabledRuleGroup.__init__)
            check_type(argname="argument rule_group_name", value=rule_group_name, expected_type=type_hints["rule_group_name"])
            check_type(argname="argument rules", value=rules, expected_type=type_hints["rules"])
        self._values: typing.Dict[str, typing.Any] = {
            "rule_group_name": rule_group_name,
        }
        if rules is not None:
            self._values["rules"] = rules

    @builtins.property
    def rule_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#rule_group_name ApplicationGateway#rule_group_name}.'''
        result = self._values.get("rule_group_name")
        assert result is not None, "Required property 'rule_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rules(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#rules ApplicationGateway#rules}.'''
        result = self._values.get("rules")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewayWafConfigurationDisabledRuleGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationGatewayWafConfigurationDisabledRuleGroupList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayWafConfigurationDisabledRuleGroupList",
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
            type_hints = typing.get_type_hints(ApplicationGatewayWafConfigurationDisabledRuleGroupList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationGatewayWafConfigurationDisabledRuleGroupOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayWafConfigurationDisabledRuleGroupList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationGatewayWafConfigurationDisabledRuleGroupOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayWafConfigurationDisabledRuleGroupList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayWafConfigurationDisabledRuleGroupList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayWafConfigurationDisabledRuleGroupList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayWafConfigurationDisabledRuleGroup]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayWafConfigurationDisabledRuleGroup]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayWafConfigurationDisabledRuleGroup]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayWafConfigurationDisabledRuleGroupList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationGatewayWafConfigurationDisabledRuleGroupOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayWafConfigurationDisabledRuleGroupOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationGatewayWafConfigurationDisabledRuleGroupOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetRules")
    def reset_rules(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRules", []))

    @builtins.property
    @jsii.member(jsii_name="ruleGroupNameInput")
    def rule_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="rulesInput")
    def rules_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "rulesInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleGroupName")
    def rule_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ruleGroupName"))

    @rule_group_name.setter
    def rule_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayWafConfigurationDisabledRuleGroupOutputReference, "rule_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="rules")
    def rules(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "rules"))

    @rules.setter
    def rules(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayWafConfigurationDisabledRuleGroupOutputReference, "rules").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rules", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationGatewayWafConfigurationDisabledRuleGroup, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationGatewayWafConfigurationDisabledRuleGroup, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationGatewayWafConfigurationDisabledRuleGroup, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayWafConfigurationDisabledRuleGroupOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayWafConfigurationExclusion",
    jsii_struct_bases=[],
    name_mapping={
        "match_variable": "matchVariable",
        "selector": "selector",
        "selector_match_operator": "selectorMatchOperator",
    },
)
class ApplicationGatewayWafConfigurationExclusion:
    def __init__(
        self,
        *,
        match_variable: builtins.str,
        selector: typing.Optional[builtins.str] = None,
        selector_match_operator: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param match_variable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#match_variable ApplicationGateway#match_variable}.
        :param selector: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#selector ApplicationGateway#selector}.
        :param selector_match_operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#selector_match_operator ApplicationGateway#selector_match_operator}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayWafConfigurationExclusion.__init__)
            check_type(argname="argument match_variable", value=match_variable, expected_type=type_hints["match_variable"])
            check_type(argname="argument selector", value=selector, expected_type=type_hints["selector"])
            check_type(argname="argument selector_match_operator", value=selector_match_operator, expected_type=type_hints["selector_match_operator"])
        self._values: typing.Dict[str, typing.Any] = {
            "match_variable": match_variable,
        }
        if selector is not None:
            self._values["selector"] = selector
        if selector_match_operator is not None:
            self._values["selector_match_operator"] = selector_match_operator

    @builtins.property
    def match_variable(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#match_variable ApplicationGateway#match_variable}.'''
        result = self._values.get("match_variable")
        assert result is not None, "Required property 'match_variable' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def selector(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#selector ApplicationGateway#selector}.'''
        result = self._values.get("selector")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def selector_match_operator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_gateway#selector_match_operator ApplicationGateway#selector_match_operator}.'''
        result = self._values.get("selector_match_operator")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationGatewayWafConfigurationExclusion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationGatewayWafConfigurationExclusionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayWafConfigurationExclusionList",
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
            type_hints = typing.get_type_hints(ApplicationGatewayWafConfigurationExclusionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationGatewayWafConfigurationExclusionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayWafConfigurationExclusionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationGatewayWafConfigurationExclusionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayWafConfigurationExclusionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayWafConfigurationExclusionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayWafConfigurationExclusionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayWafConfigurationExclusion]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayWafConfigurationExclusion]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayWafConfigurationExclusion]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayWafConfigurationExclusionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationGatewayWafConfigurationExclusionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayWafConfigurationExclusionOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationGatewayWafConfigurationExclusionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetSelector")
    def reset_selector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSelector", []))

    @jsii.member(jsii_name="resetSelectorMatchOperator")
    def reset_selector_match_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSelectorMatchOperator", []))

    @builtins.property
    @jsii.member(jsii_name="matchVariableInput")
    def match_variable_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "matchVariableInput"))

    @builtins.property
    @jsii.member(jsii_name="selectorInput")
    def selector_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "selectorInput"))

    @builtins.property
    @jsii.member(jsii_name="selectorMatchOperatorInput")
    def selector_match_operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "selectorMatchOperatorInput"))

    @builtins.property
    @jsii.member(jsii_name="matchVariable")
    def match_variable(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchVariable"))

    @match_variable.setter
    def match_variable(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayWafConfigurationExclusionOutputReference, "match_variable").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchVariable", value)

    @builtins.property
    @jsii.member(jsii_name="selector")
    def selector(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selector"))

    @selector.setter
    def selector(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayWafConfigurationExclusionOutputReference, "selector").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "selector", value)

    @builtins.property
    @jsii.member(jsii_name="selectorMatchOperator")
    def selector_match_operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selectorMatchOperator"))

    @selector_match_operator.setter
    def selector_match_operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayWafConfigurationExclusionOutputReference, "selector_match_operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "selectorMatchOperator", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationGatewayWafConfigurationExclusion, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationGatewayWafConfigurationExclusion, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationGatewayWafConfigurationExclusion, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayWafConfigurationExclusionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationGatewayWafConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationGateway.ApplicationGatewayWafConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationGatewayWafConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDisabledRuleGroup")
    def put_disabled_rule_group(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApplicationGatewayWafConfigurationDisabledRuleGroup, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayWafConfigurationOutputReference.put_disabled_rule_group)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDisabledRuleGroup", [value]))

    @jsii.member(jsii_name="putExclusion")
    def put_exclusion(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApplicationGatewayWafConfigurationExclusion, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationGatewayWafConfigurationOutputReference.put_exclusion)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExclusion", [value]))

    @jsii.member(jsii_name="resetDisabledRuleGroup")
    def reset_disabled_rule_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisabledRuleGroup", []))

    @jsii.member(jsii_name="resetExclusion")
    def reset_exclusion(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExclusion", []))

    @jsii.member(jsii_name="resetFileUploadLimitMb")
    def reset_file_upload_limit_mb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileUploadLimitMb", []))

    @jsii.member(jsii_name="resetMaxRequestBodySizeKb")
    def reset_max_request_body_size_kb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxRequestBodySizeKb", []))

    @jsii.member(jsii_name="resetRequestBodyCheck")
    def reset_request_body_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestBodyCheck", []))

    @jsii.member(jsii_name="resetRuleSetType")
    def reset_rule_set_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuleSetType", []))

    @builtins.property
    @jsii.member(jsii_name="disabledRuleGroup")
    def disabled_rule_group(
        self,
    ) -> ApplicationGatewayWafConfigurationDisabledRuleGroupList:
        return typing.cast(ApplicationGatewayWafConfigurationDisabledRuleGroupList, jsii.get(self, "disabledRuleGroup"))

    @builtins.property
    @jsii.member(jsii_name="exclusion")
    def exclusion(self) -> ApplicationGatewayWafConfigurationExclusionList:
        return typing.cast(ApplicationGatewayWafConfigurationExclusionList, jsii.get(self, "exclusion"))

    @builtins.property
    @jsii.member(jsii_name="disabledRuleGroupInput")
    def disabled_rule_group_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayWafConfigurationDisabledRuleGroup]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayWafConfigurationDisabledRuleGroup]]], jsii.get(self, "disabledRuleGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="exclusionInput")
    def exclusion_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayWafConfigurationExclusion]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApplicationGatewayWafConfigurationExclusion]]], jsii.get(self, "exclusionInput"))

    @builtins.property
    @jsii.member(jsii_name="fileUploadLimitMbInput")
    def file_upload_limit_mb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "fileUploadLimitMbInput"))

    @builtins.property
    @jsii.member(jsii_name="firewallModeInput")
    def firewall_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "firewallModeInput"))

    @builtins.property
    @jsii.member(jsii_name="maxRequestBodySizeKbInput")
    def max_request_body_size_kb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxRequestBodySizeKbInput"))

    @builtins.property
    @jsii.member(jsii_name="requestBodyCheckInput")
    def request_body_check_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requestBodyCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleSetTypeInput")
    def rule_set_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleSetTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleSetVersionInput")
    def rule_set_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleSetVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayWafConfigurationOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="fileUploadLimitMb")
    def file_upload_limit_mb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "fileUploadLimitMb"))

    @file_upload_limit_mb.setter
    def file_upload_limit_mb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayWafConfigurationOutputReference, "file_upload_limit_mb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileUploadLimitMb", value)

    @builtins.property
    @jsii.member(jsii_name="firewallMode")
    def firewall_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "firewallMode"))

    @firewall_mode.setter
    def firewall_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayWafConfigurationOutputReference, "firewall_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firewallMode", value)

    @builtins.property
    @jsii.member(jsii_name="maxRequestBodySizeKb")
    def max_request_body_size_kb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxRequestBodySizeKb"))

    @max_request_body_size_kb.setter
    def max_request_body_size_kb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayWafConfigurationOutputReference, "max_request_body_size_kb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxRequestBodySizeKb", value)

    @builtins.property
    @jsii.member(jsii_name="requestBodyCheck")
    def request_body_check(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "requestBodyCheck"))

    @request_body_check.setter
    def request_body_check(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayWafConfigurationOutputReference, "request_body_check").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestBodyCheck", value)

    @builtins.property
    @jsii.member(jsii_name="ruleSetType")
    def rule_set_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ruleSetType"))

    @rule_set_type.setter
    def rule_set_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayWafConfigurationOutputReference, "rule_set_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleSetType", value)

    @builtins.property
    @jsii.member(jsii_name="ruleSetVersion")
    def rule_set_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ruleSetVersion"))

    @rule_set_version.setter
    def rule_set_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayWafConfigurationOutputReference, "rule_set_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleSetVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApplicationGatewayWafConfiguration]:
        return typing.cast(typing.Optional[ApplicationGatewayWafConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApplicationGatewayWafConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationGatewayWafConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ApplicationGateway",
    "ApplicationGatewayAuthenticationCertificate",
    "ApplicationGatewayAuthenticationCertificateList",
    "ApplicationGatewayAuthenticationCertificateOutputReference",
    "ApplicationGatewayAutoscaleConfiguration",
    "ApplicationGatewayAutoscaleConfigurationOutputReference",
    "ApplicationGatewayBackendAddressPool",
    "ApplicationGatewayBackendAddressPoolList",
    "ApplicationGatewayBackendAddressPoolOutputReference",
    "ApplicationGatewayBackendHttpSettings",
    "ApplicationGatewayBackendHttpSettingsAuthenticationCertificate",
    "ApplicationGatewayBackendHttpSettingsAuthenticationCertificateList",
    "ApplicationGatewayBackendHttpSettingsAuthenticationCertificateOutputReference",
    "ApplicationGatewayBackendHttpSettingsConnectionDraining",
    "ApplicationGatewayBackendHttpSettingsConnectionDrainingOutputReference",
    "ApplicationGatewayBackendHttpSettingsList",
    "ApplicationGatewayBackendHttpSettingsOutputReference",
    "ApplicationGatewayConfig",
    "ApplicationGatewayCustomErrorConfiguration",
    "ApplicationGatewayCustomErrorConfigurationList",
    "ApplicationGatewayCustomErrorConfigurationOutputReference",
    "ApplicationGatewayFrontendIpConfiguration",
    "ApplicationGatewayFrontendIpConfigurationList",
    "ApplicationGatewayFrontendIpConfigurationOutputReference",
    "ApplicationGatewayFrontendPort",
    "ApplicationGatewayFrontendPortList",
    "ApplicationGatewayFrontendPortOutputReference",
    "ApplicationGatewayGatewayIpConfiguration",
    "ApplicationGatewayGatewayIpConfigurationList",
    "ApplicationGatewayGatewayIpConfigurationOutputReference",
    "ApplicationGatewayGlobal",
    "ApplicationGatewayGlobalOutputReference",
    "ApplicationGatewayHttpListener",
    "ApplicationGatewayHttpListenerCustomErrorConfiguration",
    "ApplicationGatewayHttpListenerCustomErrorConfigurationList",
    "ApplicationGatewayHttpListenerCustomErrorConfigurationOutputReference",
    "ApplicationGatewayHttpListenerList",
    "ApplicationGatewayHttpListenerOutputReference",
    "ApplicationGatewayIdentity",
    "ApplicationGatewayIdentityOutputReference",
    "ApplicationGatewayPrivateEndpointConnection",
    "ApplicationGatewayPrivateEndpointConnectionList",
    "ApplicationGatewayPrivateEndpointConnectionOutputReference",
    "ApplicationGatewayPrivateLinkConfiguration",
    "ApplicationGatewayPrivateLinkConfigurationIpConfiguration",
    "ApplicationGatewayPrivateLinkConfigurationIpConfigurationList",
    "ApplicationGatewayPrivateLinkConfigurationIpConfigurationOutputReference",
    "ApplicationGatewayPrivateLinkConfigurationList",
    "ApplicationGatewayPrivateLinkConfigurationOutputReference",
    "ApplicationGatewayProbe",
    "ApplicationGatewayProbeList",
    "ApplicationGatewayProbeMatch",
    "ApplicationGatewayProbeMatchOutputReference",
    "ApplicationGatewayProbeOutputReference",
    "ApplicationGatewayRedirectConfiguration",
    "ApplicationGatewayRedirectConfigurationList",
    "ApplicationGatewayRedirectConfigurationOutputReference",
    "ApplicationGatewayRequestRoutingRule",
    "ApplicationGatewayRequestRoutingRuleList",
    "ApplicationGatewayRequestRoutingRuleOutputReference",
    "ApplicationGatewayRewriteRuleSet",
    "ApplicationGatewayRewriteRuleSetList",
    "ApplicationGatewayRewriteRuleSetOutputReference",
    "ApplicationGatewayRewriteRuleSetRewriteRule",
    "ApplicationGatewayRewriteRuleSetRewriteRuleCondition",
    "ApplicationGatewayRewriteRuleSetRewriteRuleConditionList",
    "ApplicationGatewayRewriteRuleSetRewriteRuleConditionOutputReference",
    "ApplicationGatewayRewriteRuleSetRewriteRuleList",
    "ApplicationGatewayRewriteRuleSetRewriteRuleOutputReference",
    "ApplicationGatewayRewriteRuleSetRewriteRuleRequestHeaderConfiguration",
    "ApplicationGatewayRewriteRuleSetRewriteRuleRequestHeaderConfigurationList",
    "ApplicationGatewayRewriteRuleSetRewriteRuleRequestHeaderConfigurationOutputReference",
    "ApplicationGatewayRewriteRuleSetRewriteRuleResponseHeaderConfiguration",
    "ApplicationGatewayRewriteRuleSetRewriteRuleResponseHeaderConfigurationList",
    "ApplicationGatewayRewriteRuleSetRewriteRuleResponseHeaderConfigurationOutputReference",
    "ApplicationGatewayRewriteRuleSetRewriteRuleUrl",
    "ApplicationGatewayRewriteRuleSetRewriteRuleUrlOutputReference",
    "ApplicationGatewaySku",
    "ApplicationGatewaySkuOutputReference",
    "ApplicationGatewaySslCertificate",
    "ApplicationGatewaySslCertificateList",
    "ApplicationGatewaySslCertificateOutputReference",
    "ApplicationGatewaySslPolicy",
    "ApplicationGatewaySslPolicyOutputReference",
    "ApplicationGatewaySslProfile",
    "ApplicationGatewaySslProfileList",
    "ApplicationGatewaySslProfileOutputReference",
    "ApplicationGatewaySslProfileSslPolicy",
    "ApplicationGatewaySslProfileSslPolicyOutputReference",
    "ApplicationGatewayTimeouts",
    "ApplicationGatewayTimeoutsOutputReference",
    "ApplicationGatewayTrustedClientCertificate",
    "ApplicationGatewayTrustedClientCertificateList",
    "ApplicationGatewayTrustedClientCertificateOutputReference",
    "ApplicationGatewayTrustedRootCertificate",
    "ApplicationGatewayTrustedRootCertificateList",
    "ApplicationGatewayTrustedRootCertificateOutputReference",
    "ApplicationGatewayUrlPathMap",
    "ApplicationGatewayUrlPathMapList",
    "ApplicationGatewayUrlPathMapOutputReference",
    "ApplicationGatewayUrlPathMapPathRule",
    "ApplicationGatewayUrlPathMapPathRuleList",
    "ApplicationGatewayUrlPathMapPathRuleOutputReference",
    "ApplicationGatewayWafConfiguration",
    "ApplicationGatewayWafConfigurationDisabledRuleGroup",
    "ApplicationGatewayWafConfigurationDisabledRuleGroupList",
    "ApplicationGatewayWafConfigurationDisabledRuleGroupOutputReference",
    "ApplicationGatewayWafConfigurationExclusion",
    "ApplicationGatewayWafConfigurationExclusionList",
    "ApplicationGatewayWafConfigurationExclusionOutputReference",
    "ApplicationGatewayWafConfigurationOutputReference",
]

publication.publish()
