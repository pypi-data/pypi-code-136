'''
# `azurerm_spring_cloud_gateway`

Refer to the Terraform Registory for docs: [`azurerm_spring_cloud_gateway`](https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway).
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


class SpringCloudGateway(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.springCloudGateway.SpringCloudGateway",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway azurerm_spring_cloud_gateway}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        spring_cloud_service_id: builtins.str,
        api_metadata: typing.Optional[typing.Union["SpringCloudGatewayApiMetadata", typing.Dict[str, typing.Any]]] = None,
        cors: typing.Optional[typing.Union["SpringCloudGatewayCors", typing.Dict[str, typing.Any]]] = None,
        https_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        instance_count: typing.Optional[jsii.Number] = None,
        public_network_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        quota: typing.Optional[typing.Union["SpringCloudGatewayQuota", typing.Dict[str, typing.Any]]] = None,
        sso: typing.Optional[typing.Union["SpringCloudGatewaySso", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["SpringCloudGatewayTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway azurerm_spring_cloud_gateway} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#name SpringCloudGateway#name}.
        :param spring_cloud_service_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#spring_cloud_service_id SpringCloudGateway#spring_cloud_service_id}.
        :param api_metadata: api_metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#api_metadata SpringCloudGateway#api_metadata}
        :param cors: cors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#cors SpringCloudGateway#cors}
        :param https_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#https_only SpringCloudGateway#https_only}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#id SpringCloudGateway#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#instance_count SpringCloudGateway#instance_count}.
        :param public_network_access_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#public_network_access_enabled SpringCloudGateway#public_network_access_enabled}.
        :param quota: quota block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#quota SpringCloudGateway#quota}
        :param sso: sso block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#sso SpringCloudGateway#sso}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#timeouts SpringCloudGateway#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SpringCloudGateway.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SpringCloudGatewayConfig(
            name=name,
            spring_cloud_service_id=spring_cloud_service_id,
            api_metadata=api_metadata,
            cors=cors,
            https_only=https_only,
            id=id,
            instance_count=instance_count,
            public_network_access_enabled=public_network_access_enabled,
            quota=quota,
            sso=sso,
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

    @jsii.member(jsii_name="putApiMetadata")
    def put_api_metadata(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        documentation_url: typing.Optional[builtins.str] = None,
        server_url: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#description SpringCloudGateway#description}.
        :param documentation_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#documentation_url SpringCloudGateway#documentation_url}.
        :param server_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#server_url SpringCloudGateway#server_url}.
        :param title: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#title SpringCloudGateway#title}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#version SpringCloudGateway#version}.
        '''
        value = SpringCloudGatewayApiMetadata(
            description=description,
            documentation_url=documentation_url,
            server_url=server_url,
            title=title,
            version=version,
        )

        return typing.cast(None, jsii.invoke(self, "putApiMetadata", [value]))

    @jsii.member(jsii_name="putCors")
    def put_cors(
        self,
        *,
        allowed_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        allowed_methods: typing.Optional[typing.Sequence[builtins.str]] = None,
        allowed_origins: typing.Optional[typing.Sequence[builtins.str]] = None,
        credentials_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        exposed_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        max_age_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param allowed_headers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#allowed_headers SpringCloudGateway#allowed_headers}.
        :param allowed_methods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#allowed_methods SpringCloudGateway#allowed_methods}.
        :param allowed_origins: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#allowed_origins SpringCloudGateway#allowed_origins}.
        :param credentials_allowed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#credentials_allowed SpringCloudGateway#credentials_allowed}.
        :param exposed_headers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#exposed_headers SpringCloudGateway#exposed_headers}.
        :param max_age_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#max_age_seconds SpringCloudGateway#max_age_seconds}.
        '''
        value = SpringCloudGatewayCors(
            allowed_headers=allowed_headers,
            allowed_methods=allowed_methods,
            allowed_origins=allowed_origins,
            credentials_allowed=credentials_allowed,
            exposed_headers=exposed_headers,
            max_age_seconds=max_age_seconds,
        )

        return typing.cast(None, jsii.invoke(self, "putCors", [value]))

    @jsii.member(jsii_name="putQuota")
    def put_quota(
        self,
        *,
        cpu: typing.Optional[builtins.str] = None,
        memory: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cpu: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#cpu SpringCloudGateway#cpu}.
        :param memory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#memory SpringCloudGateway#memory}.
        '''
        value = SpringCloudGatewayQuota(cpu=cpu, memory=memory)

        return typing.cast(None, jsii.invoke(self, "putQuota", [value]))

    @jsii.member(jsii_name="putSso")
    def put_sso(
        self,
        *,
        client_id: typing.Optional[builtins.str] = None,
        client_secret: typing.Optional[builtins.str] = None,
        issuer_uri: typing.Optional[builtins.str] = None,
        scope: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#client_id SpringCloudGateway#client_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#client_secret SpringCloudGateway#client_secret}.
        :param issuer_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#issuer_uri SpringCloudGateway#issuer_uri}.
        :param scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#scope SpringCloudGateway#scope}.
        '''
        value = SpringCloudGatewaySso(
            client_id=client_id,
            client_secret=client_secret,
            issuer_uri=issuer_uri,
            scope=scope,
        )

        return typing.cast(None, jsii.invoke(self, "putSso", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#create SpringCloudGateway#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#delete SpringCloudGateway#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#read SpringCloudGateway#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#update SpringCloudGateway#update}.
        '''
        value = SpringCloudGatewayTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetApiMetadata")
    def reset_api_metadata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiMetadata", []))

    @jsii.member(jsii_name="resetCors")
    def reset_cors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCors", []))

    @jsii.member(jsii_name="resetHttpsOnly")
    def reset_https_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpsOnly", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInstanceCount")
    def reset_instance_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceCount", []))

    @jsii.member(jsii_name="resetPublicNetworkAccessEnabled")
    def reset_public_network_access_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicNetworkAccessEnabled", []))

    @jsii.member(jsii_name="resetQuota")
    def reset_quota(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQuota", []))

    @jsii.member(jsii_name="resetSso")
    def reset_sso(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSso", []))

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
    @jsii.member(jsii_name="apiMetadata")
    def api_metadata(self) -> "SpringCloudGatewayApiMetadataOutputReference":
        return typing.cast("SpringCloudGatewayApiMetadataOutputReference", jsii.get(self, "apiMetadata"))

    @builtins.property
    @jsii.member(jsii_name="cors")
    def cors(self) -> "SpringCloudGatewayCorsOutputReference":
        return typing.cast("SpringCloudGatewayCorsOutputReference", jsii.get(self, "cors"))

    @builtins.property
    @jsii.member(jsii_name="quota")
    def quota(self) -> "SpringCloudGatewayQuotaOutputReference":
        return typing.cast("SpringCloudGatewayQuotaOutputReference", jsii.get(self, "quota"))

    @builtins.property
    @jsii.member(jsii_name="sso")
    def sso(self) -> "SpringCloudGatewaySsoOutputReference":
        return typing.cast("SpringCloudGatewaySsoOutputReference", jsii.get(self, "sso"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "SpringCloudGatewayTimeoutsOutputReference":
        return typing.cast("SpringCloudGatewayTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @builtins.property
    @jsii.member(jsii_name="apiMetadataInput")
    def api_metadata_input(self) -> typing.Optional["SpringCloudGatewayApiMetadata"]:
        return typing.cast(typing.Optional["SpringCloudGatewayApiMetadata"], jsii.get(self, "apiMetadataInput"))

    @builtins.property
    @jsii.member(jsii_name="corsInput")
    def cors_input(self) -> typing.Optional["SpringCloudGatewayCors"]:
        return typing.cast(typing.Optional["SpringCloudGatewayCors"], jsii.get(self, "corsInput"))

    @builtins.property
    @jsii.member(jsii_name="httpsOnlyInput")
    def https_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "httpsOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceCountInput")
    def instance_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "instanceCountInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="publicNetworkAccessEnabledInput")
    def public_network_access_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "publicNetworkAccessEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="quotaInput")
    def quota_input(self) -> typing.Optional["SpringCloudGatewayQuota"]:
        return typing.cast(typing.Optional["SpringCloudGatewayQuota"], jsii.get(self, "quotaInput"))

    @builtins.property
    @jsii.member(jsii_name="springCloudServiceIdInput")
    def spring_cloud_service_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "springCloudServiceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="ssoInput")
    def sso_input(self) -> typing.Optional["SpringCloudGatewaySso"]:
        return typing.cast(typing.Optional["SpringCloudGatewaySso"], jsii.get(self, "ssoInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["SpringCloudGatewayTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["SpringCloudGatewayTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="httpsOnly")
    def https_only(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "httpsOnly"))

    @https_only.setter
    def https_only(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudGateway, "https_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpsOnly", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudGateway, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="instanceCount")
    def instance_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instanceCount"))

    @instance_count.setter
    def instance_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudGateway, "instance_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceCount", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudGateway, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

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
            type_hints = typing.get_type_hints(getattr(SpringCloudGateway, "public_network_access_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicNetworkAccessEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="springCloudServiceId")
    def spring_cloud_service_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "springCloudServiceId"))

    @spring_cloud_service_id.setter
    def spring_cloud_service_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudGateway, "spring_cloud_service_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "springCloudServiceId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.springCloudGateway.SpringCloudGatewayApiMetadata",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "documentation_url": "documentationUrl",
        "server_url": "serverUrl",
        "title": "title",
        "version": "version",
    },
)
class SpringCloudGatewayApiMetadata:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        documentation_url: typing.Optional[builtins.str] = None,
        server_url: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#description SpringCloudGateway#description}.
        :param documentation_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#documentation_url SpringCloudGateway#documentation_url}.
        :param server_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#server_url SpringCloudGateway#server_url}.
        :param title: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#title SpringCloudGateway#title}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#version SpringCloudGateway#version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SpringCloudGatewayApiMetadata.__init__)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument documentation_url", value=documentation_url, expected_type=type_hints["documentation_url"])
            check_type(argname="argument server_url", value=server_url, expected_type=type_hints["server_url"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if documentation_url is not None:
            self._values["documentation_url"] = documentation_url
        if server_url is not None:
            self._values["server_url"] = server_url
        if title is not None:
            self._values["title"] = title
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#description SpringCloudGateway#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def documentation_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#documentation_url SpringCloudGateway#documentation_url}.'''
        result = self._values.get("documentation_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#server_url SpringCloudGateway#server_url}.'''
        result = self._values.get("server_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#title SpringCloudGateway#title}.'''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#version SpringCloudGateway#version}.'''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpringCloudGatewayApiMetadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SpringCloudGatewayApiMetadataOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.springCloudGateway.SpringCloudGatewayApiMetadataOutputReference",
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
            type_hints = typing.get_type_hints(SpringCloudGatewayApiMetadataOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDocumentationUrl")
    def reset_documentation_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDocumentationUrl", []))

    @jsii.member(jsii_name="resetServerUrl")
    def reset_server_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerUrl", []))

    @jsii.member(jsii_name="resetTitle")
    def reset_title(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTitle", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="documentationUrlInput")
    def documentation_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "documentationUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="serverUrlInput")
    def server_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudGatewayApiMetadataOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="documentationUrl")
    def documentation_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "documentationUrl"))

    @documentation_url.setter
    def documentation_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudGatewayApiMetadataOutputReference, "documentation_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "documentationUrl", value)

    @builtins.property
    @jsii.member(jsii_name="serverUrl")
    def server_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverUrl"))

    @server_url.setter
    def server_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudGatewayApiMetadataOutputReference, "server_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverUrl", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudGatewayApiMetadataOutputReference, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudGatewayApiMetadataOutputReference, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SpringCloudGatewayApiMetadata]:
        return typing.cast(typing.Optional[SpringCloudGatewayApiMetadata], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SpringCloudGatewayApiMetadata],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudGatewayApiMetadataOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.springCloudGateway.SpringCloudGatewayConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "spring_cloud_service_id": "springCloudServiceId",
        "api_metadata": "apiMetadata",
        "cors": "cors",
        "https_only": "httpsOnly",
        "id": "id",
        "instance_count": "instanceCount",
        "public_network_access_enabled": "publicNetworkAccessEnabled",
        "quota": "quota",
        "sso": "sso",
        "timeouts": "timeouts",
    },
)
class SpringCloudGatewayConfig(cdktf.TerraformMetaArguments):
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
        name: builtins.str,
        spring_cloud_service_id: builtins.str,
        api_metadata: typing.Optional[typing.Union[SpringCloudGatewayApiMetadata, typing.Dict[str, typing.Any]]] = None,
        cors: typing.Optional[typing.Union["SpringCloudGatewayCors", typing.Dict[str, typing.Any]]] = None,
        https_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        instance_count: typing.Optional[jsii.Number] = None,
        public_network_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        quota: typing.Optional[typing.Union["SpringCloudGatewayQuota", typing.Dict[str, typing.Any]]] = None,
        sso: typing.Optional[typing.Union["SpringCloudGatewaySso", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["SpringCloudGatewayTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#name SpringCloudGateway#name}.
        :param spring_cloud_service_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#spring_cloud_service_id SpringCloudGateway#spring_cloud_service_id}.
        :param api_metadata: api_metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#api_metadata SpringCloudGateway#api_metadata}
        :param cors: cors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#cors SpringCloudGateway#cors}
        :param https_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#https_only SpringCloudGateway#https_only}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#id SpringCloudGateway#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#instance_count SpringCloudGateway#instance_count}.
        :param public_network_access_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#public_network_access_enabled SpringCloudGateway#public_network_access_enabled}.
        :param quota: quota block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#quota SpringCloudGateway#quota}
        :param sso: sso block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#sso SpringCloudGateway#sso}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#timeouts SpringCloudGateway#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(api_metadata, dict):
            api_metadata = SpringCloudGatewayApiMetadata(**api_metadata)
        if isinstance(cors, dict):
            cors = SpringCloudGatewayCors(**cors)
        if isinstance(quota, dict):
            quota = SpringCloudGatewayQuota(**quota)
        if isinstance(sso, dict):
            sso = SpringCloudGatewaySso(**sso)
        if isinstance(timeouts, dict):
            timeouts = SpringCloudGatewayTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(SpringCloudGatewayConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument spring_cloud_service_id", value=spring_cloud_service_id, expected_type=type_hints["spring_cloud_service_id"])
            check_type(argname="argument api_metadata", value=api_metadata, expected_type=type_hints["api_metadata"])
            check_type(argname="argument cors", value=cors, expected_type=type_hints["cors"])
            check_type(argname="argument https_only", value=https_only, expected_type=type_hints["https_only"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument instance_count", value=instance_count, expected_type=type_hints["instance_count"])
            check_type(argname="argument public_network_access_enabled", value=public_network_access_enabled, expected_type=type_hints["public_network_access_enabled"])
            check_type(argname="argument quota", value=quota, expected_type=type_hints["quota"])
            check_type(argname="argument sso", value=sso, expected_type=type_hints["sso"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "spring_cloud_service_id": spring_cloud_service_id,
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
        if api_metadata is not None:
            self._values["api_metadata"] = api_metadata
        if cors is not None:
            self._values["cors"] = cors
        if https_only is not None:
            self._values["https_only"] = https_only
        if id is not None:
            self._values["id"] = id
        if instance_count is not None:
            self._values["instance_count"] = instance_count
        if public_network_access_enabled is not None:
            self._values["public_network_access_enabled"] = public_network_access_enabled
        if quota is not None:
            self._values["quota"] = quota
        if sso is not None:
            self._values["sso"] = sso
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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#name SpringCloudGateway#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def spring_cloud_service_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#spring_cloud_service_id SpringCloudGateway#spring_cloud_service_id}.'''
        result = self._values.get("spring_cloud_service_id")
        assert result is not None, "Required property 'spring_cloud_service_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_metadata(self) -> typing.Optional[SpringCloudGatewayApiMetadata]:
        '''api_metadata block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#api_metadata SpringCloudGateway#api_metadata}
        '''
        result = self._values.get("api_metadata")
        return typing.cast(typing.Optional[SpringCloudGatewayApiMetadata], result)

    @builtins.property
    def cors(self) -> typing.Optional["SpringCloudGatewayCors"]:
        '''cors block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#cors SpringCloudGateway#cors}
        '''
        result = self._values.get("cors")
        return typing.cast(typing.Optional["SpringCloudGatewayCors"], result)

    @builtins.property
    def https_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#https_only SpringCloudGateway#https_only}.'''
        result = self._values.get("https_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#id SpringCloudGateway#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#instance_count SpringCloudGateway#instance_count}.'''
        result = self._values.get("instance_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def public_network_access_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#public_network_access_enabled SpringCloudGateway#public_network_access_enabled}.'''
        result = self._values.get("public_network_access_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def quota(self) -> typing.Optional["SpringCloudGatewayQuota"]:
        '''quota block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#quota SpringCloudGateway#quota}
        '''
        result = self._values.get("quota")
        return typing.cast(typing.Optional["SpringCloudGatewayQuota"], result)

    @builtins.property
    def sso(self) -> typing.Optional["SpringCloudGatewaySso"]:
        '''sso block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#sso SpringCloudGateway#sso}
        '''
        result = self._values.get("sso")
        return typing.cast(typing.Optional["SpringCloudGatewaySso"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["SpringCloudGatewayTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#timeouts SpringCloudGateway#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["SpringCloudGatewayTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpringCloudGatewayConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.springCloudGateway.SpringCloudGatewayCors",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_headers": "allowedHeaders",
        "allowed_methods": "allowedMethods",
        "allowed_origins": "allowedOrigins",
        "credentials_allowed": "credentialsAllowed",
        "exposed_headers": "exposedHeaders",
        "max_age_seconds": "maxAgeSeconds",
    },
)
class SpringCloudGatewayCors:
    def __init__(
        self,
        *,
        allowed_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        allowed_methods: typing.Optional[typing.Sequence[builtins.str]] = None,
        allowed_origins: typing.Optional[typing.Sequence[builtins.str]] = None,
        credentials_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        exposed_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        max_age_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param allowed_headers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#allowed_headers SpringCloudGateway#allowed_headers}.
        :param allowed_methods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#allowed_methods SpringCloudGateway#allowed_methods}.
        :param allowed_origins: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#allowed_origins SpringCloudGateway#allowed_origins}.
        :param credentials_allowed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#credentials_allowed SpringCloudGateway#credentials_allowed}.
        :param exposed_headers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#exposed_headers SpringCloudGateway#exposed_headers}.
        :param max_age_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#max_age_seconds SpringCloudGateway#max_age_seconds}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SpringCloudGatewayCors.__init__)
            check_type(argname="argument allowed_headers", value=allowed_headers, expected_type=type_hints["allowed_headers"])
            check_type(argname="argument allowed_methods", value=allowed_methods, expected_type=type_hints["allowed_methods"])
            check_type(argname="argument allowed_origins", value=allowed_origins, expected_type=type_hints["allowed_origins"])
            check_type(argname="argument credentials_allowed", value=credentials_allowed, expected_type=type_hints["credentials_allowed"])
            check_type(argname="argument exposed_headers", value=exposed_headers, expected_type=type_hints["exposed_headers"])
            check_type(argname="argument max_age_seconds", value=max_age_seconds, expected_type=type_hints["max_age_seconds"])
        self._values: typing.Dict[str, typing.Any] = {}
        if allowed_headers is not None:
            self._values["allowed_headers"] = allowed_headers
        if allowed_methods is not None:
            self._values["allowed_methods"] = allowed_methods
        if allowed_origins is not None:
            self._values["allowed_origins"] = allowed_origins
        if credentials_allowed is not None:
            self._values["credentials_allowed"] = credentials_allowed
        if exposed_headers is not None:
            self._values["exposed_headers"] = exposed_headers
        if max_age_seconds is not None:
            self._values["max_age_seconds"] = max_age_seconds

    @builtins.property
    def allowed_headers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#allowed_headers SpringCloudGateway#allowed_headers}.'''
        result = self._values.get("allowed_headers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allowed_methods(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#allowed_methods SpringCloudGateway#allowed_methods}.'''
        result = self._values.get("allowed_methods")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allowed_origins(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#allowed_origins SpringCloudGateway#allowed_origins}.'''
        result = self._values.get("allowed_origins")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def credentials_allowed(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#credentials_allowed SpringCloudGateway#credentials_allowed}.'''
        result = self._values.get("credentials_allowed")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def exposed_headers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#exposed_headers SpringCloudGateway#exposed_headers}.'''
        result = self._values.get("exposed_headers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def max_age_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#max_age_seconds SpringCloudGateway#max_age_seconds}.'''
        result = self._values.get("max_age_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpringCloudGatewayCors(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SpringCloudGatewayCorsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.springCloudGateway.SpringCloudGatewayCorsOutputReference",
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
            type_hints = typing.get_type_hints(SpringCloudGatewayCorsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowedHeaders")
    def reset_allowed_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedHeaders", []))

    @jsii.member(jsii_name="resetAllowedMethods")
    def reset_allowed_methods(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedMethods", []))

    @jsii.member(jsii_name="resetAllowedOrigins")
    def reset_allowed_origins(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedOrigins", []))

    @jsii.member(jsii_name="resetCredentialsAllowed")
    def reset_credentials_allowed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCredentialsAllowed", []))

    @jsii.member(jsii_name="resetExposedHeaders")
    def reset_exposed_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExposedHeaders", []))

    @jsii.member(jsii_name="resetMaxAgeSeconds")
    def reset_max_age_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxAgeSeconds", []))

    @builtins.property
    @jsii.member(jsii_name="allowedHeadersInput")
    def allowed_headers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedMethodsInput")
    def allowed_methods_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedMethodsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedOriginsInput")
    def allowed_origins_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedOriginsInput"))

    @builtins.property
    @jsii.member(jsii_name="credentialsAllowedInput")
    def credentials_allowed_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "credentialsAllowedInput"))

    @builtins.property
    @jsii.member(jsii_name="exposedHeadersInput")
    def exposed_headers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "exposedHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="maxAgeSecondsInput")
    def max_age_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxAgeSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedHeaders")
    def allowed_headers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedHeaders"))

    @allowed_headers.setter
    def allowed_headers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudGatewayCorsOutputReference, "allowed_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="allowedMethods")
    def allowed_methods(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedMethods"))

    @allowed_methods.setter
    def allowed_methods(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudGatewayCorsOutputReference, "allowed_methods").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedMethods", value)

    @builtins.property
    @jsii.member(jsii_name="allowedOrigins")
    def allowed_origins(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedOrigins"))

    @allowed_origins.setter
    def allowed_origins(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudGatewayCorsOutputReference, "allowed_origins").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedOrigins", value)

    @builtins.property
    @jsii.member(jsii_name="credentialsAllowed")
    def credentials_allowed(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "credentialsAllowed"))

    @credentials_allowed.setter
    def credentials_allowed(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudGatewayCorsOutputReference, "credentials_allowed").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "credentialsAllowed", value)

    @builtins.property
    @jsii.member(jsii_name="exposedHeaders")
    def exposed_headers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exposedHeaders"))

    @exposed_headers.setter
    def exposed_headers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudGatewayCorsOutputReference, "exposed_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exposedHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="maxAgeSeconds")
    def max_age_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxAgeSeconds"))

    @max_age_seconds.setter
    def max_age_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudGatewayCorsOutputReference, "max_age_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxAgeSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SpringCloudGatewayCors]:
        return typing.cast(typing.Optional[SpringCloudGatewayCors], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SpringCloudGatewayCors]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudGatewayCorsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.springCloudGateway.SpringCloudGatewayQuota",
    jsii_struct_bases=[],
    name_mapping={"cpu": "cpu", "memory": "memory"},
)
class SpringCloudGatewayQuota:
    def __init__(
        self,
        *,
        cpu: typing.Optional[builtins.str] = None,
        memory: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cpu: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#cpu SpringCloudGateway#cpu}.
        :param memory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#memory SpringCloudGateway#memory}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SpringCloudGatewayQuota.__init__)
            check_type(argname="argument cpu", value=cpu, expected_type=type_hints["cpu"])
            check_type(argname="argument memory", value=memory, expected_type=type_hints["memory"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cpu is not None:
            self._values["cpu"] = cpu
        if memory is not None:
            self._values["memory"] = memory

    @builtins.property
    def cpu(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#cpu SpringCloudGateway#cpu}.'''
        result = self._values.get("cpu")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def memory(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#memory SpringCloudGateway#memory}.'''
        result = self._values.get("memory")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpringCloudGatewayQuota(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SpringCloudGatewayQuotaOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.springCloudGateway.SpringCloudGatewayQuotaOutputReference",
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
            type_hints = typing.get_type_hints(SpringCloudGatewayQuotaOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCpu")
    def reset_cpu(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpu", []))

    @jsii.member(jsii_name="resetMemory")
    def reset_memory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemory", []))

    @builtins.property
    @jsii.member(jsii_name="cpuInput")
    def cpu_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cpuInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryInput")
    def memory_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "memoryInput"))

    @builtins.property
    @jsii.member(jsii_name="cpu")
    def cpu(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cpu"))

    @cpu.setter
    def cpu(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudGatewayQuotaOutputReference, "cpu").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpu", value)

    @builtins.property
    @jsii.member(jsii_name="memory")
    def memory(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "memory"))

    @memory.setter
    def memory(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudGatewayQuotaOutputReference, "memory").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memory", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SpringCloudGatewayQuota]:
        return typing.cast(typing.Optional[SpringCloudGatewayQuota], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SpringCloudGatewayQuota]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudGatewayQuotaOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.springCloudGateway.SpringCloudGatewaySso",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "issuer_uri": "issuerUri",
        "scope": "scope",
    },
)
class SpringCloudGatewaySso:
    def __init__(
        self,
        *,
        client_id: typing.Optional[builtins.str] = None,
        client_secret: typing.Optional[builtins.str] = None,
        issuer_uri: typing.Optional[builtins.str] = None,
        scope: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#client_id SpringCloudGateway#client_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#client_secret SpringCloudGateway#client_secret}.
        :param issuer_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#issuer_uri SpringCloudGateway#issuer_uri}.
        :param scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#scope SpringCloudGateway#scope}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SpringCloudGatewaySso.__init__)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
            check_type(argname="argument issuer_uri", value=issuer_uri, expected_type=type_hints["issuer_uri"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        self._values: typing.Dict[str, typing.Any] = {}
        if client_id is not None:
            self._values["client_id"] = client_id
        if client_secret is not None:
            self._values["client_secret"] = client_secret
        if issuer_uri is not None:
            self._values["issuer_uri"] = issuer_uri
        if scope is not None:
            self._values["scope"] = scope

    @builtins.property
    def client_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#client_id SpringCloudGateway#client_id}.'''
        result = self._values.get("client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_secret(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#client_secret SpringCloudGateway#client_secret}.'''
        result = self._values.get("client_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def issuer_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#issuer_uri SpringCloudGateway#issuer_uri}.'''
        result = self._values.get("issuer_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scope(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#scope SpringCloudGateway#scope}.'''
        result = self._values.get("scope")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpringCloudGatewaySso(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SpringCloudGatewaySsoOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.springCloudGateway.SpringCloudGatewaySsoOutputReference",
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
            type_hints = typing.get_type_hints(SpringCloudGatewaySsoOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetClientId")
    def reset_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientId", []))

    @jsii.member(jsii_name="resetClientSecret")
    def reset_client_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientSecret", []))

    @jsii.member(jsii_name="resetIssuerUri")
    def reset_issuer_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIssuerUri", []))

    @jsii.member(jsii_name="resetScope")
    def reset_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScope", []))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretInput")
    def client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="issuerUriInput")
    def issuer_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "issuerUriInput"))

    @builtins.property
    @jsii.member(jsii_name="scopeInput")
    def scope_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "scopeInput"))

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudGatewaySsoOutputReference, "client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudGatewaySsoOutputReference, "client_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="issuerUri")
    def issuer_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "issuerUri"))

    @issuer_uri.setter
    def issuer_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudGatewaySsoOutputReference, "issuer_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "issuerUri", value)

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "scope"))

    @scope.setter
    def scope(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudGatewaySsoOutputReference, "scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scope", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SpringCloudGatewaySso]:
        return typing.cast(typing.Optional[SpringCloudGatewaySso], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SpringCloudGatewaySso]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudGatewaySsoOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.springCloudGateway.SpringCloudGatewayTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class SpringCloudGatewayTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#create SpringCloudGateway#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#delete SpringCloudGateway#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#read SpringCloudGateway#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#update SpringCloudGateway#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SpringCloudGatewayTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#create SpringCloudGateway#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#delete SpringCloudGateway#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#read SpringCloudGateway#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_gateway#update SpringCloudGateway#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpringCloudGatewayTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SpringCloudGatewayTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.springCloudGateway.SpringCloudGatewayTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(SpringCloudGatewayTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(SpringCloudGatewayTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudGatewayTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudGatewayTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudGatewayTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SpringCloudGatewayTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SpringCloudGatewayTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SpringCloudGatewayTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudGatewayTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SpringCloudGateway",
    "SpringCloudGatewayApiMetadata",
    "SpringCloudGatewayApiMetadataOutputReference",
    "SpringCloudGatewayConfig",
    "SpringCloudGatewayCors",
    "SpringCloudGatewayCorsOutputReference",
    "SpringCloudGatewayQuota",
    "SpringCloudGatewayQuotaOutputReference",
    "SpringCloudGatewaySso",
    "SpringCloudGatewaySsoOutputReference",
    "SpringCloudGatewayTimeouts",
    "SpringCloudGatewayTimeoutsOutputReference",
]

publication.publish()
