'''
# `azurerm_api_management_custom_domain`

Refer to the Terraform Registory for docs: [`azurerm_api_management_custom_domain`](https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain).
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


class ApiManagementCustomDomain(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementCustomDomain.ApiManagementCustomDomain",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain azurerm_api_management_custom_domain}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        api_management_id: builtins.str,
        developer_portal: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementCustomDomainDeveloperPortal", typing.Dict[str, typing.Any]]]]] = None,
        gateway: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementCustomDomainGateway", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        management: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementCustomDomainManagement", typing.Dict[str, typing.Any]]]]] = None,
        portal: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementCustomDomainPortal", typing.Dict[str, typing.Any]]]]] = None,
        scm: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementCustomDomainScm", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["ApiManagementCustomDomainTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain azurerm_api_management_custom_domain} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param api_management_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#api_management_id ApiManagementCustomDomain#api_management_id}.
        :param developer_portal: developer_portal block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#developer_portal ApiManagementCustomDomain#developer_portal}
        :param gateway: gateway block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#gateway ApiManagementCustomDomain#gateway}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#id ApiManagementCustomDomain#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param management: management block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#management ApiManagementCustomDomain#management}
        :param portal: portal block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#portal ApiManagementCustomDomain#portal}
        :param scm: scm block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#scm ApiManagementCustomDomain#scm}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#timeouts ApiManagementCustomDomain#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementCustomDomain.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ApiManagementCustomDomainConfig(
            api_management_id=api_management_id,
            developer_portal=developer_portal,
            gateway=gateway,
            id=id,
            management=management,
            portal=portal,
            scm=scm,
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

    @jsii.member(jsii_name="putDeveloperPortal")
    def put_developer_portal(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementCustomDomainDeveloperPortal", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementCustomDomain.put_developer_portal)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDeveloperPortal", [value]))

    @jsii.member(jsii_name="putGateway")
    def put_gateway(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementCustomDomainGateway", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementCustomDomain.put_gateway)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGateway", [value]))

    @jsii.member(jsii_name="putManagement")
    def put_management(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementCustomDomainManagement", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementCustomDomain.put_management)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putManagement", [value]))

    @jsii.member(jsii_name="putPortal")
    def put_portal(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementCustomDomainPortal", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementCustomDomain.put_portal)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPortal", [value]))

    @jsii.member(jsii_name="putScm")
    def put_scm(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementCustomDomainScm", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementCustomDomain.put_scm)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putScm", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#create ApiManagementCustomDomain#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#delete ApiManagementCustomDomain#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#read ApiManagementCustomDomain#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#update ApiManagementCustomDomain#update}.
        '''
        value = ApiManagementCustomDomainTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDeveloperPortal")
    def reset_developer_portal(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeveloperPortal", []))

    @jsii.member(jsii_name="resetGateway")
    def reset_gateway(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGateway", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetManagement")
    def reset_management(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagement", []))

    @jsii.member(jsii_name="resetPortal")
    def reset_portal(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPortal", []))

    @jsii.member(jsii_name="resetScm")
    def reset_scm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScm", []))

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
    @jsii.member(jsii_name="developerPortal")
    def developer_portal(self) -> "ApiManagementCustomDomainDeveloperPortalList":
        return typing.cast("ApiManagementCustomDomainDeveloperPortalList", jsii.get(self, "developerPortal"))

    @builtins.property
    @jsii.member(jsii_name="gateway")
    def gateway(self) -> "ApiManagementCustomDomainGatewayList":
        return typing.cast("ApiManagementCustomDomainGatewayList", jsii.get(self, "gateway"))

    @builtins.property
    @jsii.member(jsii_name="management")
    def management(self) -> "ApiManagementCustomDomainManagementList":
        return typing.cast("ApiManagementCustomDomainManagementList", jsii.get(self, "management"))

    @builtins.property
    @jsii.member(jsii_name="portal")
    def portal(self) -> "ApiManagementCustomDomainPortalList":
        return typing.cast("ApiManagementCustomDomainPortalList", jsii.get(self, "portal"))

    @builtins.property
    @jsii.member(jsii_name="scm")
    def scm(self) -> "ApiManagementCustomDomainScmList":
        return typing.cast("ApiManagementCustomDomainScmList", jsii.get(self, "scm"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ApiManagementCustomDomainTimeoutsOutputReference":
        return typing.cast("ApiManagementCustomDomainTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="apiManagementIdInput")
    def api_management_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiManagementIdInput"))

    @builtins.property
    @jsii.member(jsii_name="developerPortalInput")
    def developer_portal_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementCustomDomainDeveloperPortal"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementCustomDomainDeveloperPortal"]]], jsii.get(self, "developerPortalInput"))

    @builtins.property
    @jsii.member(jsii_name="gatewayInput")
    def gateway_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementCustomDomainGateway"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementCustomDomainGateway"]]], jsii.get(self, "gatewayInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="managementInput")
    def management_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementCustomDomainManagement"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementCustomDomainManagement"]]], jsii.get(self, "managementInput"))

    @builtins.property
    @jsii.member(jsii_name="portalInput")
    def portal_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementCustomDomainPortal"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementCustomDomainPortal"]]], jsii.get(self, "portalInput"))

    @builtins.property
    @jsii.member(jsii_name="scmInput")
    def scm_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementCustomDomainScm"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementCustomDomainScm"]]], jsii.get(self, "scmInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ApiManagementCustomDomainTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ApiManagementCustomDomainTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="apiManagementId")
    def api_management_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiManagementId"))

    @api_management_id.setter
    def api_management_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomain, "api_management_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiManagementId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomain, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementCustomDomain.ApiManagementCustomDomainConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "api_management_id": "apiManagementId",
        "developer_portal": "developerPortal",
        "gateway": "gateway",
        "id": "id",
        "management": "management",
        "portal": "portal",
        "scm": "scm",
        "timeouts": "timeouts",
    },
)
class ApiManagementCustomDomainConfig(cdktf.TerraformMetaArguments):
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
        api_management_id: builtins.str,
        developer_portal: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementCustomDomainDeveloperPortal", typing.Dict[str, typing.Any]]]]] = None,
        gateway: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementCustomDomainGateway", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        management: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementCustomDomainManagement", typing.Dict[str, typing.Any]]]]] = None,
        portal: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementCustomDomainPortal", typing.Dict[str, typing.Any]]]]] = None,
        scm: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementCustomDomainScm", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["ApiManagementCustomDomainTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param api_management_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#api_management_id ApiManagementCustomDomain#api_management_id}.
        :param developer_portal: developer_portal block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#developer_portal ApiManagementCustomDomain#developer_portal}
        :param gateway: gateway block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#gateway ApiManagementCustomDomain#gateway}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#id ApiManagementCustomDomain#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param management: management block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#management ApiManagementCustomDomain#management}
        :param portal: portal block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#portal ApiManagementCustomDomain#portal}
        :param scm: scm block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#scm ApiManagementCustomDomain#scm}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#timeouts ApiManagementCustomDomain#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = ApiManagementCustomDomainTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementCustomDomainConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument api_management_id", value=api_management_id, expected_type=type_hints["api_management_id"])
            check_type(argname="argument developer_portal", value=developer_portal, expected_type=type_hints["developer_portal"])
            check_type(argname="argument gateway", value=gateway, expected_type=type_hints["gateway"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument management", value=management, expected_type=type_hints["management"])
            check_type(argname="argument portal", value=portal, expected_type=type_hints["portal"])
            check_type(argname="argument scm", value=scm, expected_type=type_hints["scm"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "api_management_id": api_management_id,
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
        if developer_portal is not None:
            self._values["developer_portal"] = developer_portal
        if gateway is not None:
            self._values["gateway"] = gateway
        if id is not None:
            self._values["id"] = id
        if management is not None:
            self._values["management"] = management
        if portal is not None:
            self._values["portal"] = portal
        if scm is not None:
            self._values["scm"] = scm
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
    def api_management_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#api_management_id ApiManagementCustomDomain#api_management_id}.'''
        result = self._values.get("api_management_id")
        assert result is not None, "Required property 'api_management_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def developer_portal(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementCustomDomainDeveloperPortal"]]]:
        '''developer_portal block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#developer_portal ApiManagementCustomDomain#developer_portal}
        '''
        result = self._values.get("developer_portal")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementCustomDomainDeveloperPortal"]]], result)

    @builtins.property
    def gateway(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementCustomDomainGateway"]]]:
        '''gateway block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#gateway ApiManagementCustomDomain#gateway}
        '''
        result = self._values.get("gateway")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementCustomDomainGateway"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#id ApiManagementCustomDomain#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def management(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementCustomDomainManagement"]]]:
        '''management block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#management ApiManagementCustomDomain#management}
        '''
        result = self._values.get("management")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementCustomDomainManagement"]]], result)

    @builtins.property
    def portal(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementCustomDomainPortal"]]]:
        '''portal block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#portal ApiManagementCustomDomain#portal}
        '''
        result = self._values.get("portal")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementCustomDomainPortal"]]], result)

    @builtins.property
    def scm(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementCustomDomainScm"]]]:
        '''scm block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#scm ApiManagementCustomDomain#scm}
        '''
        result = self._values.get("scm")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementCustomDomainScm"]]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ApiManagementCustomDomainTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#timeouts ApiManagementCustomDomain#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ApiManagementCustomDomainTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementCustomDomainConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementCustomDomain.ApiManagementCustomDomainDeveloperPortal",
    jsii_struct_bases=[],
    name_mapping={
        "host_name": "hostName",
        "certificate": "certificate",
        "certificate_password": "certificatePassword",
        "key_vault_id": "keyVaultId",
        "negotiate_client_certificate": "negotiateClientCertificate",
        "ssl_keyvault_identity_client_id": "sslKeyvaultIdentityClientId",
    },
)
class ApiManagementCustomDomainDeveloperPortal:
    def __init__(
        self,
        *,
        host_name: builtins.str,
        certificate: typing.Optional[builtins.str] = None,
        certificate_password: typing.Optional[builtins.str] = None,
        key_vault_id: typing.Optional[builtins.str] = None,
        negotiate_client_certificate: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ssl_keyvault_identity_client_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#host_name ApiManagementCustomDomain#host_name}.
        :param certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#certificate ApiManagementCustomDomain#certificate}.
        :param certificate_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#certificate_password ApiManagementCustomDomain#certificate_password}.
        :param key_vault_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#key_vault_id ApiManagementCustomDomain#key_vault_id}.
        :param negotiate_client_certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#negotiate_client_certificate ApiManagementCustomDomain#negotiate_client_certificate}.
        :param ssl_keyvault_identity_client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#ssl_keyvault_identity_client_id ApiManagementCustomDomain#ssl_keyvault_identity_client_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementCustomDomainDeveloperPortal.__init__)
            check_type(argname="argument host_name", value=host_name, expected_type=type_hints["host_name"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument certificate_password", value=certificate_password, expected_type=type_hints["certificate_password"])
            check_type(argname="argument key_vault_id", value=key_vault_id, expected_type=type_hints["key_vault_id"])
            check_type(argname="argument negotiate_client_certificate", value=negotiate_client_certificate, expected_type=type_hints["negotiate_client_certificate"])
            check_type(argname="argument ssl_keyvault_identity_client_id", value=ssl_keyvault_identity_client_id, expected_type=type_hints["ssl_keyvault_identity_client_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "host_name": host_name,
        }
        if certificate is not None:
            self._values["certificate"] = certificate
        if certificate_password is not None:
            self._values["certificate_password"] = certificate_password
        if key_vault_id is not None:
            self._values["key_vault_id"] = key_vault_id
        if negotiate_client_certificate is not None:
            self._values["negotiate_client_certificate"] = negotiate_client_certificate
        if ssl_keyvault_identity_client_id is not None:
            self._values["ssl_keyvault_identity_client_id"] = ssl_keyvault_identity_client_id

    @builtins.property
    def host_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#host_name ApiManagementCustomDomain#host_name}.'''
        result = self._values.get("host_name")
        assert result is not None, "Required property 'host_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#certificate ApiManagementCustomDomain#certificate}.'''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#certificate_password ApiManagementCustomDomain#certificate_password}.'''
        result = self._values.get("certificate_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_vault_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#key_vault_id ApiManagementCustomDomain#key_vault_id}.'''
        result = self._values.get("key_vault_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def negotiate_client_certificate(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#negotiate_client_certificate ApiManagementCustomDomain#negotiate_client_certificate}.'''
        result = self._values.get("negotiate_client_certificate")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def ssl_keyvault_identity_client_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#ssl_keyvault_identity_client_id ApiManagementCustomDomain#ssl_keyvault_identity_client_id}.'''
        result = self._values.get("ssl_keyvault_identity_client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementCustomDomainDeveloperPortal(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementCustomDomainDeveloperPortalList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementCustomDomain.ApiManagementCustomDomainDeveloperPortalList",
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
            type_hints = typing.get_type_hints(ApiManagementCustomDomainDeveloperPortalList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementCustomDomainDeveloperPortalOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementCustomDomainDeveloperPortalList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementCustomDomainDeveloperPortalOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainDeveloperPortalList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainDeveloperPortalList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainDeveloperPortalList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementCustomDomainDeveloperPortal]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementCustomDomainDeveloperPortal]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementCustomDomainDeveloperPortal]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainDeveloperPortalList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementCustomDomainDeveloperPortalOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementCustomDomain.ApiManagementCustomDomainDeveloperPortalOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementCustomDomainDeveloperPortalOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCertificate")
    def reset_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificate", []))

    @jsii.member(jsii_name="resetCertificatePassword")
    def reset_certificate_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificatePassword", []))

    @jsii.member(jsii_name="resetKeyVaultId")
    def reset_key_vault_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyVaultId", []))

    @jsii.member(jsii_name="resetNegotiateClientCertificate")
    def reset_negotiate_client_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegotiateClientCertificate", []))

    @jsii.member(jsii_name="resetSslKeyvaultIdentityClientId")
    def reset_ssl_keyvault_identity_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslKeyvaultIdentityClientId", []))

    @builtins.property
    @jsii.member(jsii_name="certificateSource")
    def certificate_source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateSource"))

    @builtins.property
    @jsii.member(jsii_name="certificateStatus")
    def certificate_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateStatus"))

    @builtins.property
    @jsii.member(jsii_name="expiry")
    def expiry(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expiry"))

    @builtins.property
    @jsii.member(jsii_name="subject")
    def subject(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subject"))

    @builtins.property
    @jsii.member(jsii_name="thumbprint")
    def thumbprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thumbprint"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateInput"))

    @builtins.property
    @jsii.member(jsii_name="certificatePasswordInput")
    def certificate_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificatePasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="hostNameInput")
    def host_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostNameInput"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultIdInput")
    def key_vault_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyVaultIdInput"))

    @builtins.property
    @jsii.member(jsii_name="negotiateClientCertificateInput")
    def negotiate_client_certificate_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negotiateClientCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="sslKeyvaultIdentityClientIdInput")
    def ssl_keyvault_identity_client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslKeyvaultIdentityClientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificate"))

    @certificate.setter
    def certificate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainDeveloperPortalOutputReference, "certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificate", value)

    @builtins.property
    @jsii.member(jsii_name="certificatePassword")
    def certificate_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificatePassword"))

    @certificate_password.setter
    def certificate_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainDeveloperPortalOutputReference, "certificate_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificatePassword", value)

    @builtins.property
    @jsii.member(jsii_name="hostName")
    def host_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostName"))

    @host_name.setter
    def host_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainDeveloperPortalOutputReference, "host_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostName", value)

    @builtins.property
    @jsii.member(jsii_name="keyVaultId")
    def key_vault_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyVaultId"))

    @key_vault_id.setter
    def key_vault_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainDeveloperPortalOutputReference, "key_vault_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyVaultId", value)

    @builtins.property
    @jsii.member(jsii_name="negotiateClientCertificate")
    def negotiate_client_certificate(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negotiateClientCertificate"))

    @negotiate_client_certificate.setter
    def negotiate_client_certificate(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainDeveloperPortalOutputReference, "negotiate_client_certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negotiateClientCertificate", value)

    @builtins.property
    @jsii.member(jsii_name="sslKeyvaultIdentityClientId")
    def ssl_keyvault_identity_client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslKeyvaultIdentityClientId"))

    @ssl_keyvault_identity_client_id.setter
    def ssl_keyvault_identity_client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainDeveloperPortalOutputReference, "ssl_keyvault_identity_client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslKeyvaultIdentityClientId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementCustomDomainDeveloperPortal, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementCustomDomainDeveloperPortal, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementCustomDomainDeveloperPortal, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainDeveloperPortalOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementCustomDomain.ApiManagementCustomDomainGateway",
    jsii_struct_bases=[],
    name_mapping={
        "host_name": "hostName",
        "certificate": "certificate",
        "certificate_password": "certificatePassword",
        "default_ssl_binding": "defaultSslBinding",
        "key_vault_id": "keyVaultId",
        "negotiate_client_certificate": "negotiateClientCertificate",
        "ssl_keyvault_identity_client_id": "sslKeyvaultIdentityClientId",
    },
)
class ApiManagementCustomDomainGateway:
    def __init__(
        self,
        *,
        host_name: builtins.str,
        certificate: typing.Optional[builtins.str] = None,
        certificate_password: typing.Optional[builtins.str] = None,
        default_ssl_binding: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        key_vault_id: typing.Optional[builtins.str] = None,
        negotiate_client_certificate: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ssl_keyvault_identity_client_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#host_name ApiManagementCustomDomain#host_name}.
        :param certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#certificate ApiManagementCustomDomain#certificate}.
        :param certificate_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#certificate_password ApiManagementCustomDomain#certificate_password}.
        :param default_ssl_binding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#default_ssl_binding ApiManagementCustomDomain#default_ssl_binding}.
        :param key_vault_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#key_vault_id ApiManagementCustomDomain#key_vault_id}.
        :param negotiate_client_certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#negotiate_client_certificate ApiManagementCustomDomain#negotiate_client_certificate}.
        :param ssl_keyvault_identity_client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#ssl_keyvault_identity_client_id ApiManagementCustomDomain#ssl_keyvault_identity_client_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementCustomDomainGateway.__init__)
            check_type(argname="argument host_name", value=host_name, expected_type=type_hints["host_name"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument certificate_password", value=certificate_password, expected_type=type_hints["certificate_password"])
            check_type(argname="argument default_ssl_binding", value=default_ssl_binding, expected_type=type_hints["default_ssl_binding"])
            check_type(argname="argument key_vault_id", value=key_vault_id, expected_type=type_hints["key_vault_id"])
            check_type(argname="argument negotiate_client_certificate", value=negotiate_client_certificate, expected_type=type_hints["negotiate_client_certificate"])
            check_type(argname="argument ssl_keyvault_identity_client_id", value=ssl_keyvault_identity_client_id, expected_type=type_hints["ssl_keyvault_identity_client_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "host_name": host_name,
        }
        if certificate is not None:
            self._values["certificate"] = certificate
        if certificate_password is not None:
            self._values["certificate_password"] = certificate_password
        if default_ssl_binding is not None:
            self._values["default_ssl_binding"] = default_ssl_binding
        if key_vault_id is not None:
            self._values["key_vault_id"] = key_vault_id
        if negotiate_client_certificate is not None:
            self._values["negotiate_client_certificate"] = negotiate_client_certificate
        if ssl_keyvault_identity_client_id is not None:
            self._values["ssl_keyvault_identity_client_id"] = ssl_keyvault_identity_client_id

    @builtins.property
    def host_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#host_name ApiManagementCustomDomain#host_name}.'''
        result = self._values.get("host_name")
        assert result is not None, "Required property 'host_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#certificate ApiManagementCustomDomain#certificate}.'''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#certificate_password ApiManagementCustomDomain#certificate_password}.'''
        result = self._values.get("certificate_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_ssl_binding(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#default_ssl_binding ApiManagementCustomDomain#default_ssl_binding}.'''
        result = self._values.get("default_ssl_binding")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def key_vault_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#key_vault_id ApiManagementCustomDomain#key_vault_id}.'''
        result = self._values.get("key_vault_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def negotiate_client_certificate(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#negotiate_client_certificate ApiManagementCustomDomain#negotiate_client_certificate}.'''
        result = self._values.get("negotiate_client_certificate")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def ssl_keyvault_identity_client_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#ssl_keyvault_identity_client_id ApiManagementCustomDomain#ssl_keyvault_identity_client_id}.'''
        result = self._values.get("ssl_keyvault_identity_client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementCustomDomainGateway(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementCustomDomainGatewayList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementCustomDomain.ApiManagementCustomDomainGatewayList",
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
            type_hints = typing.get_type_hints(ApiManagementCustomDomainGatewayList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementCustomDomainGatewayOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementCustomDomainGatewayList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementCustomDomainGatewayOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainGatewayList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainGatewayList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainGatewayList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementCustomDomainGateway]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementCustomDomainGateway]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementCustomDomainGateway]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainGatewayList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementCustomDomainGatewayOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementCustomDomain.ApiManagementCustomDomainGatewayOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementCustomDomainGatewayOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCertificate")
    def reset_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificate", []))

    @jsii.member(jsii_name="resetCertificatePassword")
    def reset_certificate_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificatePassword", []))

    @jsii.member(jsii_name="resetDefaultSslBinding")
    def reset_default_ssl_binding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultSslBinding", []))

    @jsii.member(jsii_name="resetKeyVaultId")
    def reset_key_vault_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyVaultId", []))

    @jsii.member(jsii_name="resetNegotiateClientCertificate")
    def reset_negotiate_client_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegotiateClientCertificate", []))

    @jsii.member(jsii_name="resetSslKeyvaultIdentityClientId")
    def reset_ssl_keyvault_identity_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslKeyvaultIdentityClientId", []))

    @builtins.property
    @jsii.member(jsii_name="certificateSource")
    def certificate_source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateSource"))

    @builtins.property
    @jsii.member(jsii_name="certificateStatus")
    def certificate_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateStatus"))

    @builtins.property
    @jsii.member(jsii_name="expiry")
    def expiry(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expiry"))

    @builtins.property
    @jsii.member(jsii_name="subject")
    def subject(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subject"))

    @builtins.property
    @jsii.member(jsii_name="thumbprint")
    def thumbprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thumbprint"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateInput"))

    @builtins.property
    @jsii.member(jsii_name="certificatePasswordInput")
    def certificate_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificatePasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultSslBindingInput")
    def default_ssl_binding_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "defaultSslBindingInput"))

    @builtins.property
    @jsii.member(jsii_name="hostNameInput")
    def host_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostNameInput"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultIdInput")
    def key_vault_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyVaultIdInput"))

    @builtins.property
    @jsii.member(jsii_name="negotiateClientCertificateInput")
    def negotiate_client_certificate_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negotiateClientCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="sslKeyvaultIdentityClientIdInput")
    def ssl_keyvault_identity_client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslKeyvaultIdentityClientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificate"))

    @certificate.setter
    def certificate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainGatewayOutputReference, "certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificate", value)

    @builtins.property
    @jsii.member(jsii_name="certificatePassword")
    def certificate_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificatePassword"))

    @certificate_password.setter
    def certificate_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainGatewayOutputReference, "certificate_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificatePassword", value)

    @builtins.property
    @jsii.member(jsii_name="defaultSslBinding")
    def default_ssl_binding(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "defaultSslBinding"))

    @default_ssl_binding.setter
    def default_ssl_binding(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainGatewayOutputReference, "default_ssl_binding").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultSslBinding", value)

    @builtins.property
    @jsii.member(jsii_name="hostName")
    def host_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostName"))

    @host_name.setter
    def host_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainGatewayOutputReference, "host_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostName", value)

    @builtins.property
    @jsii.member(jsii_name="keyVaultId")
    def key_vault_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyVaultId"))

    @key_vault_id.setter
    def key_vault_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainGatewayOutputReference, "key_vault_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyVaultId", value)

    @builtins.property
    @jsii.member(jsii_name="negotiateClientCertificate")
    def negotiate_client_certificate(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negotiateClientCertificate"))

    @negotiate_client_certificate.setter
    def negotiate_client_certificate(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainGatewayOutputReference, "negotiate_client_certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negotiateClientCertificate", value)

    @builtins.property
    @jsii.member(jsii_name="sslKeyvaultIdentityClientId")
    def ssl_keyvault_identity_client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslKeyvaultIdentityClientId"))

    @ssl_keyvault_identity_client_id.setter
    def ssl_keyvault_identity_client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainGatewayOutputReference, "ssl_keyvault_identity_client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslKeyvaultIdentityClientId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementCustomDomainGateway, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementCustomDomainGateway, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementCustomDomainGateway, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainGatewayOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementCustomDomain.ApiManagementCustomDomainManagement",
    jsii_struct_bases=[],
    name_mapping={
        "host_name": "hostName",
        "certificate": "certificate",
        "certificate_password": "certificatePassword",
        "key_vault_id": "keyVaultId",
        "negotiate_client_certificate": "negotiateClientCertificate",
        "ssl_keyvault_identity_client_id": "sslKeyvaultIdentityClientId",
    },
)
class ApiManagementCustomDomainManagement:
    def __init__(
        self,
        *,
        host_name: builtins.str,
        certificate: typing.Optional[builtins.str] = None,
        certificate_password: typing.Optional[builtins.str] = None,
        key_vault_id: typing.Optional[builtins.str] = None,
        negotiate_client_certificate: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ssl_keyvault_identity_client_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#host_name ApiManagementCustomDomain#host_name}.
        :param certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#certificate ApiManagementCustomDomain#certificate}.
        :param certificate_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#certificate_password ApiManagementCustomDomain#certificate_password}.
        :param key_vault_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#key_vault_id ApiManagementCustomDomain#key_vault_id}.
        :param negotiate_client_certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#negotiate_client_certificate ApiManagementCustomDomain#negotiate_client_certificate}.
        :param ssl_keyvault_identity_client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#ssl_keyvault_identity_client_id ApiManagementCustomDomain#ssl_keyvault_identity_client_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementCustomDomainManagement.__init__)
            check_type(argname="argument host_name", value=host_name, expected_type=type_hints["host_name"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument certificate_password", value=certificate_password, expected_type=type_hints["certificate_password"])
            check_type(argname="argument key_vault_id", value=key_vault_id, expected_type=type_hints["key_vault_id"])
            check_type(argname="argument negotiate_client_certificate", value=negotiate_client_certificate, expected_type=type_hints["negotiate_client_certificate"])
            check_type(argname="argument ssl_keyvault_identity_client_id", value=ssl_keyvault_identity_client_id, expected_type=type_hints["ssl_keyvault_identity_client_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "host_name": host_name,
        }
        if certificate is not None:
            self._values["certificate"] = certificate
        if certificate_password is not None:
            self._values["certificate_password"] = certificate_password
        if key_vault_id is not None:
            self._values["key_vault_id"] = key_vault_id
        if negotiate_client_certificate is not None:
            self._values["negotiate_client_certificate"] = negotiate_client_certificate
        if ssl_keyvault_identity_client_id is not None:
            self._values["ssl_keyvault_identity_client_id"] = ssl_keyvault_identity_client_id

    @builtins.property
    def host_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#host_name ApiManagementCustomDomain#host_name}.'''
        result = self._values.get("host_name")
        assert result is not None, "Required property 'host_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#certificate ApiManagementCustomDomain#certificate}.'''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#certificate_password ApiManagementCustomDomain#certificate_password}.'''
        result = self._values.get("certificate_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_vault_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#key_vault_id ApiManagementCustomDomain#key_vault_id}.'''
        result = self._values.get("key_vault_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def negotiate_client_certificate(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#negotiate_client_certificate ApiManagementCustomDomain#negotiate_client_certificate}.'''
        result = self._values.get("negotiate_client_certificate")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def ssl_keyvault_identity_client_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#ssl_keyvault_identity_client_id ApiManagementCustomDomain#ssl_keyvault_identity_client_id}.'''
        result = self._values.get("ssl_keyvault_identity_client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementCustomDomainManagement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementCustomDomainManagementList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementCustomDomain.ApiManagementCustomDomainManagementList",
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
            type_hints = typing.get_type_hints(ApiManagementCustomDomainManagementList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementCustomDomainManagementOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementCustomDomainManagementList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementCustomDomainManagementOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainManagementList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainManagementList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainManagementList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementCustomDomainManagement]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementCustomDomainManagement]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementCustomDomainManagement]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainManagementList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementCustomDomainManagementOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementCustomDomain.ApiManagementCustomDomainManagementOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementCustomDomainManagementOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCertificate")
    def reset_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificate", []))

    @jsii.member(jsii_name="resetCertificatePassword")
    def reset_certificate_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificatePassword", []))

    @jsii.member(jsii_name="resetKeyVaultId")
    def reset_key_vault_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyVaultId", []))

    @jsii.member(jsii_name="resetNegotiateClientCertificate")
    def reset_negotiate_client_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegotiateClientCertificate", []))

    @jsii.member(jsii_name="resetSslKeyvaultIdentityClientId")
    def reset_ssl_keyvault_identity_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslKeyvaultIdentityClientId", []))

    @builtins.property
    @jsii.member(jsii_name="certificateSource")
    def certificate_source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateSource"))

    @builtins.property
    @jsii.member(jsii_name="certificateStatus")
    def certificate_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateStatus"))

    @builtins.property
    @jsii.member(jsii_name="expiry")
    def expiry(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expiry"))

    @builtins.property
    @jsii.member(jsii_name="subject")
    def subject(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subject"))

    @builtins.property
    @jsii.member(jsii_name="thumbprint")
    def thumbprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thumbprint"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateInput"))

    @builtins.property
    @jsii.member(jsii_name="certificatePasswordInput")
    def certificate_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificatePasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="hostNameInput")
    def host_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostNameInput"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultIdInput")
    def key_vault_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyVaultIdInput"))

    @builtins.property
    @jsii.member(jsii_name="negotiateClientCertificateInput")
    def negotiate_client_certificate_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negotiateClientCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="sslKeyvaultIdentityClientIdInput")
    def ssl_keyvault_identity_client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslKeyvaultIdentityClientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificate"))

    @certificate.setter
    def certificate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainManagementOutputReference, "certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificate", value)

    @builtins.property
    @jsii.member(jsii_name="certificatePassword")
    def certificate_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificatePassword"))

    @certificate_password.setter
    def certificate_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainManagementOutputReference, "certificate_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificatePassword", value)

    @builtins.property
    @jsii.member(jsii_name="hostName")
    def host_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostName"))

    @host_name.setter
    def host_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainManagementOutputReference, "host_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostName", value)

    @builtins.property
    @jsii.member(jsii_name="keyVaultId")
    def key_vault_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyVaultId"))

    @key_vault_id.setter
    def key_vault_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainManagementOutputReference, "key_vault_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyVaultId", value)

    @builtins.property
    @jsii.member(jsii_name="negotiateClientCertificate")
    def negotiate_client_certificate(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negotiateClientCertificate"))

    @negotiate_client_certificate.setter
    def negotiate_client_certificate(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainManagementOutputReference, "negotiate_client_certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negotiateClientCertificate", value)

    @builtins.property
    @jsii.member(jsii_name="sslKeyvaultIdentityClientId")
    def ssl_keyvault_identity_client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslKeyvaultIdentityClientId"))

    @ssl_keyvault_identity_client_id.setter
    def ssl_keyvault_identity_client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainManagementOutputReference, "ssl_keyvault_identity_client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslKeyvaultIdentityClientId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementCustomDomainManagement, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementCustomDomainManagement, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementCustomDomainManagement, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainManagementOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementCustomDomain.ApiManagementCustomDomainPortal",
    jsii_struct_bases=[],
    name_mapping={
        "host_name": "hostName",
        "certificate": "certificate",
        "certificate_password": "certificatePassword",
        "key_vault_id": "keyVaultId",
        "negotiate_client_certificate": "negotiateClientCertificate",
        "ssl_keyvault_identity_client_id": "sslKeyvaultIdentityClientId",
    },
)
class ApiManagementCustomDomainPortal:
    def __init__(
        self,
        *,
        host_name: builtins.str,
        certificate: typing.Optional[builtins.str] = None,
        certificate_password: typing.Optional[builtins.str] = None,
        key_vault_id: typing.Optional[builtins.str] = None,
        negotiate_client_certificate: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ssl_keyvault_identity_client_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#host_name ApiManagementCustomDomain#host_name}.
        :param certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#certificate ApiManagementCustomDomain#certificate}.
        :param certificate_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#certificate_password ApiManagementCustomDomain#certificate_password}.
        :param key_vault_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#key_vault_id ApiManagementCustomDomain#key_vault_id}.
        :param negotiate_client_certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#negotiate_client_certificate ApiManagementCustomDomain#negotiate_client_certificate}.
        :param ssl_keyvault_identity_client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#ssl_keyvault_identity_client_id ApiManagementCustomDomain#ssl_keyvault_identity_client_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementCustomDomainPortal.__init__)
            check_type(argname="argument host_name", value=host_name, expected_type=type_hints["host_name"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument certificate_password", value=certificate_password, expected_type=type_hints["certificate_password"])
            check_type(argname="argument key_vault_id", value=key_vault_id, expected_type=type_hints["key_vault_id"])
            check_type(argname="argument negotiate_client_certificate", value=negotiate_client_certificate, expected_type=type_hints["negotiate_client_certificate"])
            check_type(argname="argument ssl_keyvault_identity_client_id", value=ssl_keyvault_identity_client_id, expected_type=type_hints["ssl_keyvault_identity_client_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "host_name": host_name,
        }
        if certificate is not None:
            self._values["certificate"] = certificate
        if certificate_password is not None:
            self._values["certificate_password"] = certificate_password
        if key_vault_id is not None:
            self._values["key_vault_id"] = key_vault_id
        if negotiate_client_certificate is not None:
            self._values["negotiate_client_certificate"] = negotiate_client_certificate
        if ssl_keyvault_identity_client_id is not None:
            self._values["ssl_keyvault_identity_client_id"] = ssl_keyvault_identity_client_id

    @builtins.property
    def host_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#host_name ApiManagementCustomDomain#host_name}.'''
        result = self._values.get("host_name")
        assert result is not None, "Required property 'host_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#certificate ApiManagementCustomDomain#certificate}.'''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#certificate_password ApiManagementCustomDomain#certificate_password}.'''
        result = self._values.get("certificate_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_vault_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#key_vault_id ApiManagementCustomDomain#key_vault_id}.'''
        result = self._values.get("key_vault_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def negotiate_client_certificate(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#negotiate_client_certificate ApiManagementCustomDomain#negotiate_client_certificate}.'''
        result = self._values.get("negotiate_client_certificate")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def ssl_keyvault_identity_client_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#ssl_keyvault_identity_client_id ApiManagementCustomDomain#ssl_keyvault_identity_client_id}.'''
        result = self._values.get("ssl_keyvault_identity_client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementCustomDomainPortal(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementCustomDomainPortalList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementCustomDomain.ApiManagementCustomDomainPortalList",
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
            type_hints = typing.get_type_hints(ApiManagementCustomDomainPortalList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementCustomDomainPortalOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementCustomDomainPortalList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementCustomDomainPortalOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainPortalList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainPortalList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainPortalList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementCustomDomainPortal]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementCustomDomainPortal]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementCustomDomainPortal]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainPortalList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementCustomDomainPortalOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementCustomDomain.ApiManagementCustomDomainPortalOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementCustomDomainPortalOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCertificate")
    def reset_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificate", []))

    @jsii.member(jsii_name="resetCertificatePassword")
    def reset_certificate_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificatePassword", []))

    @jsii.member(jsii_name="resetKeyVaultId")
    def reset_key_vault_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyVaultId", []))

    @jsii.member(jsii_name="resetNegotiateClientCertificate")
    def reset_negotiate_client_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegotiateClientCertificate", []))

    @jsii.member(jsii_name="resetSslKeyvaultIdentityClientId")
    def reset_ssl_keyvault_identity_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslKeyvaultIdentityClientId", []))

    @builtins.property
    @jsii.member(jsii_name="certificateSource")
    def certificate_source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateSource"))

    @builtins.property
    @jsii.member(jsii_name="certificateStatus")
    def certificate_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateStatus"))

    @builtins.property
    @jsii.member(jsii_name="expiry")
    def expiry(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expiry"))

    @builtins.property
    @jsii.member(jsii_name="subject")
    def subject(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subject"))

    @builtins.property
    @jsii.member(jsii_name="thumbprint")
    def thumbprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thumbprint"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateInput"))

    @builtins.property
    @jsii.member(jsii_name="certificatePasswordInput")
    def certificate_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificatePasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="hostNameInput")
    def host_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostNameInput"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultIdInput")
    def key_vault_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyVaultIdInput"))

    @builtins.property
    @jsii.member(jsii_name="negotiateClientCertificateInput")
    def negotiate_client_certificate_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negotiateClientCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="sslKeyvaultIdentityClientIdInput")
    def ssl_keyvault_identity_client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslKeyvaultIdentityClientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificate"))

    @certificate.setter
    def certificate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainPortalOutputReference, "certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificate", value)

    @builtins.property
    @jsii.member(jsii_name="certificatePassword")
    def certificate_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificatePassword"))

    @certificate_password.setter
    def certificate_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainPortalOutputReference, "certificate_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificatePassword", value)

    @builtins.property
    @jsii.member(jsii_name="hostName")
    def host_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostName"))

    @host_name.setter
    def host_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainPortalOutputReference, "host_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostName", value)

    @builtins.property
    @jsii.member(jsii_name="keyVaultId")
    def key_vault_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyVaultId"))

    @key_vault_id.setter
    def key_vault_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainPortalOutputReference, "key_vault_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyVaultId", value)

    @builtins.property
    @jsii.member(jsii_name="negotiateClientCertificate")
    def negotiate_client_certificate(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negotiateClientCertificate"))

    @negotiate_client_certificate.setter
    def negotiate_client_certificate(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainPortalOutputReference, "negotiate_client_certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negotiateClientCertificate", value)

    @builtins.property
    @jsii.member(jsii_name="sslKeyvaultIdentityClientId")
    def ssl_keyvault_identity_client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslKeyvaultIdentityClientId"))

    @ssl_keyvault_identity_client_id.setter
    def ssl_keyvault_identity_client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainPortalOutputReference, "ssl_keyvault_identity_client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslKeyvaultIdentityClientId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementCustomDomainPortal, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementCustomDomainPortal, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementCustomDomainPortal, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainPortalOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementCustomDomain.ApiManagementCustomDomainScm",
    jsii_struct_bases=[],
    name_mapping={
        "host_name": "hostName",
        "certificate": "certificate",
        "certificate_password": "certificatePassword",
        "key_vault_id": "keyVaultId",
        "negotiate_client_certificate": "negotiateClientCertificate",
        "ssl_keyvault_identity_client_id": "sslKeyvaultIdentityClientId",
    },
)
class ApiManagementCustomDomainScm:
    def __init__(
        self,
        *,
        host_name: builtins.str,
        certificate: typing.Optional[builtins.str] = None,
        certificate_password: typing.Optional[builtins.str] = None,
        key_vault_id: typing.Optional[builtins.str] = None,
        negotiate_client_certificate: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ssl_keyvault_identity_client_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#host_name ApiManagementCustomDomain#host_name}.
        :param certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#certificate ApiManagementCustomDomain#certificate}.
        :param certificate_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#certificate_password ApiManagementCustomDomain#certificate_password}.
        :param key_vault_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#key_vault_id ApiManagementCustomDomain#key_vault_id}.
        :param negotiate_client_certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#negotiate_client_certificate ApiManagementCustomDomain#negotiate_client_certificate}.
        :param ssl_keyvault_identity_client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#ssl_keyvault_identity_client_id ApiManagementCustomDomain#ssl_keyvault_identity_client_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementCustomDomainScm.__init__)
            check_type(argname="argument host_name", value=host_name, expected_type=type_hints["host_name"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument certificate_password", value=certificate_password, expected_type=type_hints["certificate_password"])
            check_type(argname="argument key_vault_id", value=key_vault_id, expected_type=type_hints["key_vault_id"])
            check_type(argname="argument negotiate_client_certificate", value=negotiate_client_certificate, expected_type=type_hints["negotiate_client_certificate"])
            check_type(argname="argument ssl_keyvault_identity_client_id", value=ssl_keyvault_identity_client_id, expected_type=type_hints["ssl_keyvault_identity_client_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "host_name": host_name,
        }
        if certificate is not None:
            self._values["certificate"] = certificate
        if certificate_password is not None:
            self._values["certificate_password"] = certificate_password
        if key_vault_id is not None:
            self._values["key_vault_id"] = key_vault_id
        if negotiate_client_certificate is not None:
            self._values["negotiate_client_certificate"] = negotiate_client_certificate
        if ssl_keyvault_identity_client_id is not None:
            self._values["ssl_keyvault_identity_client_id"] = ssl_keyvault_identity_client_id

    @builtins.property
    def host_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#host_name ApiManagementCustomDomain#host_name}.'''
        result = self._values.get("host_name")
        assert result is not None, "Required property 'host_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#certificate ApiManagementCustomDomain#certificate}.'''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#certificate_password ApiManagementCustomDomain#certificate_password}.'''
        result = self._values.get("certificate_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_vault_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#key_vault_id ApiManagementCustomDomain#key_vault_id}.'''
        result = self._values.get("key_vault_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def negotiate_client_certificate(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#negotiate_client_certificate ApiManagementCustomDomain#negotiate_client_certificate}.'''
        result = self._values.get("negotiate_client_certificate")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def ssl_keyvault_identity_client_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#ssl_keyvault_identity_client_id ApiManagementCustomDomain#ssl_keyvault_identity_client_id}.'''
        result = self._values.get("ssl_keyvault_identity_client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementCustomDomainScm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementCustomDomainScmList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementCustomDomain.ApiManagementCustomDomainScmList",
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
            type_hints = typing.get_type_hints(ApiManagementCustomDomainScmList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ApiManagementCustomDomainScmOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementCustomDomainScmList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementCustomDomainScmOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainScmList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainScmList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainScmList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementCustomDomainScm]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementCustomDomainScm]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementCustomDomainScm]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainScmList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementCustomDomainScmOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementCustomDomain.ApiManagementCustomDomainScmOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementCustomDomainScmOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCertificate")
    def reset_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificate", []))

    @jsii.member(jsii_name="resetCertificatePassword")
    def reset_certificate_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificatePassword", []))

    @jsii.member(jsii_name="resetKeyVaultId")
    def reset_key_vault_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyVaultId", []))

    @jsii.member(jsii_name="resetNegotiateClientCertificate")
    def reset_negotiate_client_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegotiateClientCertificate", []))

    @jsii.member(jsii_name="resetSslKeyvaultIdentityClientId")
    def reset_ssl_keyvault_identity_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslKeyvaultIdentityClientId", []))

    @builtins.property
    @jsii.member(jsii_name="certificateSource")
    def certificate_source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateSource"))

    @builtins.property
    @jsii.member(jsii_name="certificateStatus")
    def certificate_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateStatus"))

    @builtins.property
    @jsii.member(jsii_name="expiry")
    def expiry(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expiry"))

    @builtins.property
    @jsii.member(jsii_name="subject")
    def subject(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subject"))

    @builtins.property
    @jsii.member(jsii_name="thumbprint")
    def thumbprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thumbprint"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateInput"))

    @builtins.property
    @jsii.member(jsii_name="certificatePasswordInput")
    def certificate_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificatePasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="hostNameInput")
    def host_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostNameInput"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultIdInput")
    def key_vault_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyVaultIdInput"))

    @builtins.property
    @jsii.member(jsii_name="negotiateClientCertificateInput")
    def negotiate_client_certificate_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negotiateClientCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="sslKeyvaultIdentityClientIdInput")
    def ssl_keyvault_identity_client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslKeyvaultIdentityClientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificate"))

    @certificate.setter
    def certificate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainScmOutputReference, "certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificate", value)

    @builtins.property
    @jsii.member(jsii_name="certificatePassword")
    def certificate_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificatePassword"))

    @certificate_password.setter
    def certificate_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainScmOutputReference, "certificate_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificatePassword", value)

    @builtins.property
    @jsii.member(jsii_name="hostName")
    def host_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostName"))

    @host_name.setter
    def host_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainScmOutputReference, "host_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostName", value)

    @builtins.property
    @jsii.member(jsii_name="keyVaultId")
    def key_vault_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyVaultId"))

    @key_vault_id.setter
    def key_vault_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainScmOutputReference, "key_vault_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyVaultId", value)

    @builtins.property
    @jsii.member(jsii_name="negotiateClientCertificate")
    def negotiate_client_certificate(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negotiateClientCertificate"))

    @negotiate_client_certificate.setter
    def negotiate_client_certificate(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainScmOutputReference, "negotiate_client_certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negotiateClientCertificate", value)

    @builtins.property
    @jsii.member(jsii_name="sslKeyvaultIdentityClientId")
    def ssl_keyvault_identity_client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslKeyvaultIdentityClientId"))

    @ssl_keyvault_identity_client_id.setter
    def ssl_keyvault_identity_client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainScmOutputReference, "ssl_keyvault_identity_client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslKeyvaultIdentityClientId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementCustomDomainScm, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementCustomDomainScm, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementCustomDomainScm, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainScmOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementCustomDomain.ApiManagementCustomDomainTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class ApiManagementCustomDomainTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#create ApiManagementCustomDomain#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#delete ApiManagementCustomDomain#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#read ApiManagementCustomDomain#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#update ApiManagementCustomDomain#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementCustomDomainTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#create ApiManagementCustomDomain#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#delete ApiManagementCustomDomain#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#read ApiManagementCustomDomain#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_custom_domain#update ApiManagementCustomDomain#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementCustomDomainTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementCustomDomainTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementCustomDomain.ApiManagementCustomDomainTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementCustomDomainTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementCustomDomainTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementCustomDomainTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementCustomDomainTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCustomDomainTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ApiManagementCustomDomain",
    "ApiManagementCustomDomainConfig",
    "ApiManagementCustomDomainDeveloperPortal",
    "ApiManagementCustomDomainDeveloperPortalList",
    "ApiManagementCustomDomainDeveloperPortalOutputReference",
    "ApiManagementCustomDomainGateway",
    "ApiManagementCustomDomainGatewayList",
    "ApiManagementCustomDomainGatewayOutputReference",
    "ApiManagementCustomDomainManagement",
    "ApiManagementCustomDomainManagementList",
    "ApiManagementCustomDomainManagementOutputReference",
    "ApiManagementCustomDomainPortal",
    "ApiManagementCustomDomainPortalList",
    "ApiManagementCustomDomainPortalOutputReference",
    "ApiManagementCustomDomainScm",
    "ApiManagementCustomDomainScmList",
    "ApiManagementCustomDomainScmOutputReference",
    "ApiManagementCustomDomainTimeouts",
    "ApiManagementCustomDomainTimeoutsOutputReference",
]

publication.publish()
