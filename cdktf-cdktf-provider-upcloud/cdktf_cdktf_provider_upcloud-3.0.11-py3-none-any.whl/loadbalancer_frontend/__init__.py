'''
# `upcloud_loadbalancer_frontend`

Refer to the Terraform Registory for docs: [`upcloud_loadbalancer_frontend`](https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend).
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


class LoadbalancerFrontend(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontend.LoadbalancerFrontend",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend upcloud_loadbalancer_frontend}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        default_backend_name: builtins.str,
        loadbalancer: builtins.str,
        mode: builtins.str,
        name: builtins.str,
        port: jsii.Number,
        id: typing.Optional[builtins.str] = None,
        properties: typing.Optional[typing.Union["LoadbalancerFrontendProperties", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend upcloud_loadbalancer_frontend} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param default_backend_name: The name of the default backend where traffic will be routed. Note, default backend can be overwritten in frontend rules. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend#default_backend_name LoadbalancerFrontend#default_backend_name}
        :param loadbalancer: ID of the load balancer to which the frontend is connected. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend#loadbalancer LoadbalancerFrontend#loadbalancer}
        :param mode: When load balancer operating in ``tcp`` mode it acts as a layer 4 proxy. In ``http`` mode it acts as a layer 7 proxy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend#mode LoadbalancerFrontend#mode}
        :param name: The name of the frontend must be unique within the load balancer service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend#name LoadbalancerFrontend#name}
        :param port: Port to listen incoming requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend#port LoadbalancerFrontend#port}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend#id LoadbalancerFrontend#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param properties: properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend#properties LoadbalancerFrontend#properties}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontend.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LoadbalancerFrontendConfig(
            default_backend_name=default_backend_name,
            loadbalancer=loadbalancer,
            mode=mode,
            name=name,
            port=port,
            id=id,
            properties=properties,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putProperties")
    def put_properties(
        self,
        *,
        inbound_proxy_protocol: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        timeout_client: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param inbound_proxy_protocol: Enable or disable inbound proxy protocol support. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend#inbound_proxy_protocol LoadbalancerFrontend#inbound_proxy_protocol}
        :param timeout_client: Client request timeout in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend#timeout_client LoadbalancerFrontend#timeout_client}
        '''
        value = LoadbalancerFrontendProperties(
            inbound_proxy_protocol=inbound_proxy_protocol,
            timeout_client=timeout_client,
        )

        return typing.cast(None, jsii.invoke(self, "putProperties", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetProperties")
    def reset_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProperties", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="properties")
    def properties(self) -> "LoadbalancerFrontendPropertiesOutputReference":
        return typing.cast("LoadbalancerFrontendPropertiesOutputReference", jsii.get(self, "properties"))

    @builtins.property
    @jsii.member(jsii_name="rules")
    def rules(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "rules"))

    @builtins.property
    @jsii.member(jsii_name="tlsConfigs")
    def tls_configs(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tlsConfigs"))

    @builtins.property
    @jsii.member(jsii_name="defaultBackendNameInput")
    def default_backend_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultBackendNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="loadbalancerInput")
    def loadbalancer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loadbalancerInput"))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="propertiesInput")
    def properties_input(self) -> typing.Optional["LoadbalancerFrontendProperties"]:
        return typing.cast(typing.Optional["LoadbalancerFrontendProperties"], jsii.get(self, "propertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultBackendName")
    def default_backend_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultBackendName"))

    @default_backend_name.setter
    def default_backend_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontend, "default_backend_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultBackendName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontend, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="loadbalancer")
    def loadbalancer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loadbalancer"))

    @loadbalancer.setter
    def loadbalancer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontend, "loadbalancer").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadbalancer", value)

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontend, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontend, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontend, "port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontend.LoadbalancerFrontendConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "default_backend_name": "defaultBackendName",
        "loadbalancer": "loadbalancer",
        "mode": "mode",
        "name": "name",
        "port": "port",
        "id": "id",
        "properties": "properties",
    },
)
class LoadbalancerFrontendConfig(cdktf.TerraformMetaArguments):
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
        default_backend_name: builtins.str,
        loadbalancer: builtins.str,
        mode: builtins.str,
        name: builtins.str,
        port: jsii.Number,
        id: typing.Optional[builtins.str] = None,
        properties: typing.Optional[typing.Union["LoadbalancerFrontendProperties", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param default_backend_name: The name of the default backend where traffic will be routed. Note, default backend can be overwritten in frontend rules. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend#default_backend_name LoadbalancerFrontend#default_backend_name}
        :param loadbalancer: ID of the load balancer to which the frontend is connected. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend#loadbalancer LoadbalancerFrontend#loadbalancer}
        :param mode: When load balancer operating in ``tcp`` mode it acts as a layer 4 proxy. In ``http`` mode it acts as a layer 7 proxy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend#mode LoadbalancerFrontend#mode}
        :param name: The name of the frontend must be unique within the load balancer service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend#name LoadbalancerFrontend#name}
        :param port: Port to listen incoming requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend#port LoadbalancerFrontend#port}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend#id LoadbalancerFrontend#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param properties: properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend#properties LoadbalancerFrontend#properties}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(properties, dict):
            properties = LoadbalancerFrontendProperties(**properties)
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument default_backend_name", value=default_backend_name, expected_type=type_hints["default_backend_name"])
            check_type(argname="argument loadbalancer", value=loadbalancer, expected_type=type_hints["loadbalancer"])
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
        self._values: typing.Dict[str, typing.Any] = {
            "default_backend_name": default_backend_name,
            "loadbalancer": loadbalancer,
            "mode": mode,
            "name": name,
            "port": port,
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
        if id is not None:
            self._values["id"] = id
        if properties is not None:
            self._values["properties"] = properties

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
    def default_backend_name(self) -> builtins.str:
        '''The name of the default backend where traffic will be routed.

        Note, default backend can be overwritten in frontend rules.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend#default_backend_name LoadbalancerFrontend#default_backend_name}
        '''
        result = self._values.get("default_backend_name")
        assert result is not None, "Required property 'default_backend_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def loadbalancer(self) -> builtins.str:
        '''ID of the load balancer to which the frontend is connected.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend#loadbalancer LoadbalancerFrontend#loadbalancer}
        '''
        result = self._values.get("loadbalancer")
        assert result is not None, "Required property 'loadbalancer' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mode(self) -> builtins.str:
        '''When load balancer operating in ``tcp`` mode it acts as a layer 4 proxy.

        In ``http`` mode it acts as a layer 7 proxy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend#mode LoadbalancerFrontend#mode}
        '''
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the frontend must be unique within the load balancer service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend#name LoadbalancerFrontend#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''Port to listen incoming requests.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend#port LoadbalancerFrontend#port}
        '''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend#id LoadbalancerFrontend#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def properties(self) -> typing.Optional["LoadbalancerFrontendProperties"]:
        '''properties block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend#properties LoadbalancerFrontend#properties}
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Optional["LoadbalancerFrontendProperties"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadbalancerFrontendConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontend.LoadbalancerFrontendProperties",
    jsii_struct_bases=[],
    name_mapping={
        "inbound_proxy_protocol": "inboundProxyProtocol",
        "timeout_client": "timeoutClient",
    },
)
class LoadbalancerFrontendProperties:
    def __init__(
        self,
        *,
        inbound_proxy_protocol: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        timeout_client: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param inbound_proxy_protocol: Enable or disable inbound proxy protocol support. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend#inbound_proxy_protocol LoadbalancerFrontend#inbound_proxy_protocol}
        :param timeout_client: Client request timeout in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend#timeout_client LoadbalancerFrontend#timeout_client}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendProperties.__init__)
            check_type(argname="argument inbound_proxy_protocol", value=inbound_proxy_protocol, expected_type=type_hints["inbound_proxy_protocol"])
            check_type(argname="argument timeout_client", value=timeout_client, expected_type=type_hints["timeout_client"])
        self._values: typing.Dict[str, typing.Any] = {}
        if inbound_proxy_protocol is not None:
            self._values["inbound_proxy_protocol"] = inbound_proxy_protocol
        if timeout_client is not None:
            self._values["timeout_client"] = timeout_client

    @builtins.property
    def inbound_proxy_protocol(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable or disable inbound proxy protocol support.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend#inbound_proxy_protocol LoadbalancerFrontend#inbound_proxy_protocol}
        '''
        result = self._values.get("inbound_proxy_protocol")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def timeout_client(self) -> typing.Optional[jsii.Number]:
        '''Client request timeout in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend#timeout_client LoadbalancerFrontend#timeout_client}
        '''
        result = self._values.get("timeout_client")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadbalancerFrontendProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadbalancerFrontendPropertiesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontend.LoadbalancerFrontendPropertiesOutputReference",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendPropertiesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetInboundProxyProtocol")
    def reset_inbound_proxy_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInboundProxyProtocol", []))

    @jsii.member(jsii_name="resetTimeoutClient")
    def reset_timeout_client(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeoutClient", []))

    @builtins.property
    @jsii.member(jsii_name="inboundProxyProtocolInput")
    def inbound_proxy_protocol_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "inboundProxyProtocolInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutClientInput")
    def timeout_client_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutClientInput"))

    @builtins.property
    @jsii.member(jsii_name="inboundProxyProtocol")
    def inbound_proxy_protocol(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "inboundProxyProtocol"))

    @inbound_proxy_protocol.setter
    def inbound_proxy_protocol(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendPropertiesOutputReference, "inbound_proxy_protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inboundProxyProtocol", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutClient")
    def timeout_client(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeoutClient"))

    @timeout_client.setter
    def timeout_client(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendPropertiesOutputReference, "timeout_client").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutClient", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LoadbalancerFrontendProperties]:
        return typing.cast(typing.Optional[LoadbalancerFrontendProperties], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LoadbalancerFrontendProperties],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendPropertiesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "LoadbalancerFrontend",
    "LoadbalancerFrontendConfig",
    "LoadbalancerFrontendProperties",
    "LoadbalancerFrontendPropertiesOutputReference",
]

publication.publish()
