'''
# `azurerm_datadog_monitor`

Refer to the Terraform Registory for docs: [`azurerm_datadog_monitor`](https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor).
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


class DatadogMonitor(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.datadogMonitor.DatadogMonitor",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor azurerm_datadog_monitor}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        datadog_organization: typing.Union["DatadogMonitorDatadogOrganization", typing.Dict[str, typing.Any]],
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        sku_name: builtins.str,
        user: typing.Union["DatadogMonitorUser", typing.Dict[str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["DatadogMonitorIdentity", typing.Dict[str, typing.Any]]] = None,
        monitoring_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["DatadogMonitorTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor azurerm_datadog_monitor} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param datadog_organization: datadog_organization block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#datadog_organization DatadogMonitor#datadog_organization}
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#location DatadogMonitor#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#name DatadogMonitor#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#resource_group_name DatadogMonitor#resource_group_name}.
        :param sku_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#sku_name DatadogMonitor#sku_name}.
        :param user: user block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#user DatadogMonitor#user}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#id DatadogMonitor#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#identity DatadogMonitor#identity}
        :param monitoring_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#monitoring_enabled DatadogMonitor#monitoring_enabled}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#tags DatadogMonitor#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#timeouts DatadogMonitor#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatadogMonitor.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DatadogMonitorConfig(
            datadog_organization=datadog_organization,
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            sku_name=sku_name,
            user=user,
            id=id,
            identity=identity,
            monitoring_enabled=monitoring_enabled,
            tags=tags,
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

    @jsii.member(jsii_name="putDatadogOrganization")
    def put_datadog_organization(
        self,
        *,
        api_key: builtins.str,
        application_key: builtins.str,
        enterprise_app_id: typing.Optional[builtins.str] = None,
        linking_auth_code: typing.Optional[builtins.str] = None,
        linking_client_id: typing.Optional[builtins.str] = None,
        redirect_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param api_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#api_key DatadogMonitor#api_key}.
        :param application_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#application_key DatadogMonitor#application_key}.
        :param enterprise_app_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#enterprise_app_id DatadogMonitor#enterprise_app_id}.
        :param linking_auth_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#linking_auth_code DatadogMonitor#linking_auth_code}.
        :param linking_client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#linking_client_id DatadogMonitor#linking_client_id}.
        :param redirect_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#redirect_uri DatadogMonitor#redirect_uri}.
        '''
        value = DatadogMonitorDatadogOrganization(
            api_key=api_key,
            application_key=application_key,
            enterprise_app_id=enterprise_app_id,
            linking_auth_code=linking_auth_code,
            linking_client_id=linking_client_id,
            redirect_uri=redirect_uri,
        )

        return typing.cast(None, jsii.invoke(self, "putDatadogOrganization", [value]))

    @jsii.member(jsii_name="putIdentity")
    def put_identity(self, *, type: builtins.str) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#type DatadogMonitor#type}.
        '''
        value = DatadogMonitorIdentity(type=type)

        return typing.cast(None, jsii.invoke(self, "putIdentity", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#create DatadogMonitor#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#delete DatadogMonitor#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#read DatadogMonitor#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#update DatadogMonitor#update}.
        '''
        value = DatadogMonitorTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putUser")
    def put_user(
        self,
        *,
        email: builtins.str,
        name: builtins.str,
        phone_number: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#email DatadogMonitor#email}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#name DatadogMonitor#name}.
        :param phone_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#phone_number DatadogMonitor#phone_number}.
        '''
        value = DatadogMonitorUser(email=email, name=name, phone_number=phone_number)

        return typing.cast(None, jsii.invoke(self, "putUser", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentity")
    def reset_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentity", []))

    @jsii.member(jsii_name="resetMonitoringEnabled")
    def reset_monitoring_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonitoringEnabled", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

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
    @jsii.member(jsii_name="datadogOrganization")
    def datadog_organization(
        self,
    ) -> "DatadogMonitorDatadogOrganizationOutputReference":
        return typing.cast("DatadogMonitorDatadogOrganizationOutputReference", jsii.get(self, "datadogOrganization"))

    @builtins.property
    @jsii.member(jsii_name="identity")
    def identity(self) -> "DatadogMonitorIdentityOutputReference":
        return typing.cast("DatadogMonitorIdentityOutputReference", jsii.get(self, "identity"))

    @builtins.property
    @jsii.member(jsii_name="marketplaceSubscriptionStatus")
    def marketplace_subscription_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "marketplaceSubscriptionStatus"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "DatadogMonitorTimeoutsOutputReference":
        return typing.cast("DatadogMonitorTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="user")
    def user(self) -> "DatadogMonitorUserOutputReference":
        return typing.cast("DatadogMonitorUserOutputReference", jsii.get(self, "user"))

    @builtins.property
    @jsii.member(jsii_name="datadogOrganizationInput")
    def datadog_organization_input(
        self,
    ) -> typing.Optional["DatadogMonitorDatadogOrganization"]:
        return typing.cast(typing.Optional["DatadogMonitorDatadogOrganization"], jsii.get(self, "datadogOrganizationInput"))

    @builtins.property
    @jsii.member(jsii_name="identityInput")
    def identity_input(self) -> typing.Optional["DatadogMonitorIdentity"]:
        return typing.cast(typing.Optional["DatadogMonitorIdentity"], jsii.get(self, "identityInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="monitoringEnabledInput")
    def monitoring_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "monitoringEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="skuNameInput")
    def sku_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "skuNameInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["DatadogMonitorTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DatadogMonitorTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="userInput")
    def user_input(self) -> typing.Optional["DatadogMonitorUser"]:
        return typing.cast(typing.Optional["DatadogMonitorUser"], jsii.get(self, "userInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatadogMonitor, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatadogMonitor, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="monitoringEnabled")
    def monitoring_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "monitoringEnabled"))

    @monitoring_enabled.setter
    def monitoring_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatadogMonitor, "monitoring_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monitoringEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatadogMonitor, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatadogMonitor, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="skuName")
    def sku_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "skuName"))

    @sku_name.setter
    def sku_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatadogMonitor, "sku_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skuName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatadogMonitor, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.datadogMonitor.DatadogMonitorConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "datadog_organization": "datadogOrganization",
        "location": "location",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "sku_name": "skuName",
        "user": "user",
        "id": "id",
        "identity": "identity",
        "monitoring_enabled": "monitoringEnabled",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class DatadogMonitorConfig(cdktf.TerraformMetaArguments):
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
        datadog_organization: typing.Union["DatadogMonitorDatadogOrganization", typing.Dict[str, typing.Any]],
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        sku_name: builtins.str,
        user: typing.Union["DatadogMonitorUser", typing.Dict[str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["DatadogMonitorIdentity", typing.Dict[str, typing.Any]]] = None,
        monitoring_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["DatadogMonitorTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param datadog_organization: datadog_organization block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#datadog_organization DatadogMonitor#datadog_organization}
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#location DatadogMonitor#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#name DatadogMonitor#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#resource_group_name DatadogMonitor#resource_group_name}.
        :param sku_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#sku_name DatadogMonitor#sku_name}.
        :param user: user block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#user DatadogMonitor#user}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#id DatadogMonitor#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#identity DatadogMonitor#identity}
        :param monitoring_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#monitoring_enabled DatadogMonitor#monitoring_enabled}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#tags DatadogMonitor#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#timeouts DatadogMonitor#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(datadog_organization, dict):
            datadog_organization = DatadogMonitorDatadogOrganization(**datadog_organization)
        if isinstance(user, dict):
            user = DatadogMonitorUser(**user)
        if isinstance(identity, dict):
            identity = DatadogMonitorIdentity(**identity)
        if isinstance(timeouts, dict):
            timeouts = DatadogMonitorTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(DatadogMonitorConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument datadog_organization", value=datadog_organization, expected_type=type_hints["datadog_organization"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument sku_name", value=sku_name, expected_type=type_hints["sku_name"])
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument monitoring_enabled", value=monitoring_enabled, expected_type=type_hints["monitoring_enabled"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "datadog_organization": datadog_organization,
            "location": location,
            "name": name,
            "resource_group_name": resource_group_name,
            "sku_name": sku_name,
            "user": user,
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
        if identity is not None:
            self._values["identity"] = identity
        if monitoring_enabled is not None:
            self._values["monitoring_enabled"] = monitoring_enabled
        if tags is not None:
            self._values["tags"] = tags
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
    def datadog_organization(self) -> "DatadogMonitorDatadogOrganization":
        '''datadog_organization block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#datadog_organization DatadogMonitor#datadog_organization}
        '''
        result = self._values.get("datadog_organization")
        assert result is not None, "Required property 'datadog_organization' is missing"
        return typing.cast("DatadogMonitorDatadogOrganization", result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#location DatadogMonitor#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#name DatadogMonitor#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#resource_group_name DatadogMonitor#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sku_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#sku_name DatadogMonitor#sku_name}.'''
        result = self._values.get("sku_name")
        assert result is not None, "Required property 'sku_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user(self) -> "DatadogMonitorUser":
        '''user block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#user DatadogMonitor#user}
        '''
        result = self._values.get("user")
        assert result is not None, "Required property 'user' is missing"
        return typing.cast("DatadogMonitorUser", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#id DatadogMonitor#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity(self) -> typing.Optional["DatadogMonitorIdentity"]:
        '''identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#identity DatadogMonitor#identity}
        '''
        result = self._values.get("identity")
        return typing.cast(typing.Optional["DatadogMonitorIdentity"], result)

    @builtins.property
    def monitoring_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#monitoring_enabled DatadogMonitor#monitoring_enabled}.'''
        result = self._values.get("monitoring_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#tags DatadogMonitor#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DatadogMonitorTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#timeouts DatadogMonitor#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DatadogMonitorTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatadogMonitorConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.datadogMonitor.DatadogMonitorDatadogOrganization",
    jsii_struct_bases=[],
    name_mapping={
        "api_key": "apiKey",
        "application_key": "applicationKey",
        "enterprise_app_id": "enterpriseAppId",
        "linking_auth_code": "linkingAuthCode",
        "linking_client_id": "linkingClientId",
        "redirect_uri": "redirectUri",
    },
)
class DatadogMonitorDatadogOrganization:
    def __init__(
        self,
        *,
        api_key: builtins.str,
        application_key: builtins.str,
        enterprise_app_id: typing.Optional[builtins.str] = None,
        linking_auth_code: typing.Optional[builtins.str] = None,
        linking_client_id: typing.Optional[builtins.str] = None,
        redirect_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param api_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#api_key DatadogMonitor#api_key}.
        :param application_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#application_key DatadogMonitor#application_key}.
        :param enterprise_app_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#enterprise_app_id DatadogMonitor#enterprise_app_id}.
        :param linking_auth_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#linking_auth_code DatadogMonitor#linking_auth_code}.
        :param linking_client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#linking_client_id DatadogMonitor#linking_client_id}.
        :param redirect_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#redirect_uri DatadogMonitor#redirect_uri}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatadogMonitorDatadogOrganization.__init__)
            check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
            check_type(argname="argument application_key", value=application_key, expected_type=type_hints["application_key"])
            check_type(argname="argument enterprise_app_id", value=enterprise_app_id, expected_type=type_hints["enterprise_app_id"])
            check_type(argname="argument linking_auth_code", value=linking_auth_code, expected_type=type_hints["linking_auth_code"])
            check_type(argname="argument linking_client_id", value=linking_client_id, expected_type=type_hints["linking_client_id"])
            check_type(argname="argument redirect_uri", value=redirect_uri, expected_type=type_hints["redirect_uri"])
        self._values: typing.Dict[str, typing.Any] = {
            "api_key": api_key,
            "application_key": application_key,
        }
        if enterprise_app_id is not None:
            self._values["enterprise_app_id"] = enterprise_app_id
        if linking_auth_code is not None:
            self._values["linking_auth_code"] = linking_auth_code
        if linking_client_id is not None:
            self._values["linking_client_id"] = linking_client_id
        if redirect_uri is not None:
            self._values["redirect_uri"] = redirect_uri

    @builtins.property
    def api_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#api_key DatadogMonitor#api_key}.'''
        result = self._values.get("api_key")
        assert result is not None, "Required property 'api_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def application_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#application_key DatadogMonitor#application_key}.'''
        result = self._values.get("application_key")
        assert result is not None, "Required property 'application_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enterprise_app_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#enterprise_app_id DatadogMonitor#enterprise_app_id}.'''
        result = self._values.get("enterprise_app_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def linking_auth_code(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#linking_auth_code DatadogMonitor#linking_auth_code}.'''
        result = self._values.get("linking_auth_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def linking_client_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#linking_client_id DatadogMonitor#linking_client_id}.'''
        result = self._values.get("linking_client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redirect_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#redirect_uri DatadogMonitor#redirect_uri}.'''
        result = self._values.get("redirect_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatadogMonitorDatadogOrganization(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatadogMonitorDatadogOrganizationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.datadogMonitor.DatadogMonitorDatadogOrganizationOutputReference",
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
            type_hints = typing.get_type_hints(DatadogMonitorDatadogOrganizationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnterpriseAppId")
    def reset_enterprise_app_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnterpriseAppId", []))

    @jsii.member(jsii_name="resetLinkingAuthCode")
    def reset_linking_auth_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinkingAuthCode", []))

    @jsii.member(jsii_name="resetLinkingClientId")
    def reset_linking_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinkingClientId", []))

    @jsii.member(jsii_name="resetRedirectUri")
    def reset_redirect_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectUri", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="apiKeyInput")
    def api_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationKeyInput")
    def application_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="enterpriseAppIdInput")
    def enterprise_app_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "enterpriseAppIdInput"))

    @builtins.property
    @jsii.member(jsii_name="linkingAuthCodeInput")
    def linking_auth_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "linkingAuthCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="linkingClientIdInput")
    def linking_client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "linkingClientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectUriInput")
    def redirect_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectUriInput"))

    @builtins.property
    @jsii.member(jsii_name="apiKey")
    def api_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiKey"))

    @api_key.setter
    def api_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatadogMonitorDatadogOrganizationOutputReference, "api_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiKey", value)

    @builtins.property
    @jsii.member(jsii_name="applicationKey")
    def application_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationKey"))

    @application_key.setter
    def application_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatadogMonitorDatadogOrganizationOutputReference, "application_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationKey", value)

    @builtins.property
    @jsii.member(jsii_name="enterpriseAppId")
    def enterprise_app_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enterpriseAppId"))

    @enterprise_app_id.setter
    def enterprise_app_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatadogMonitorDatadogOrganizationOutputReference, "enterprise_app_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enterpriseAppId", value)

    @builtins.property
    @jsii.member(jsii_name="linkingAuthCode")
    def linking_auth_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "linkingAuthCode"))

    @linking_auth_code.setter
    def linking_auth_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatadogMonitorDatadogOrganizationOutputReference, "linking_auth_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "linkingAuthCode", value)

    @builtins.property
    @jsii.member(jsii_name="linkingClientId")
    def linking_client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "linkingClientId"))

    @linking_client_id.setter
    def linking_client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatadogMonitorDatadogOrganizationOutputReference, "linking_client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "linkingClientId", value)

    @builtins.property
    @jsii.member(jsii_name="redirectUri")
    def redirect_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectUri"))

    @redirect_uri.setter
    def redirect_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatadogMonitorDatadogOrganizationOutputReference, "redirect_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectUri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DatadogMonitorDatadogOrganization]:
        return typing.cast(typing.Optional[DatadogMonitorDatadogOrganization], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatadogMonitorDatadogOrganization],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatadogMonitorDatadogOrganizationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.datadogMonitor.DatadogMonitorIdentity",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class DatadogMonitorIdentity:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#type DatadogMonitor#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatadogMonitorIdentity.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#type DatadogMonitor#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatadogMonitorIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatadogMonitorIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.datadogMonitor.DatadogMonitorIdentityOutputReference",
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
            type_hints = typing.get_type_hints(DatadogMonitorIdentityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="principalId")
    def principal_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "principalId"))

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatadogMonitorIdentityOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DatadogMonitorIdentity]:
        return typing.cast(typing.Optional[DatadogMonitorIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DatadogMonitorIdentity]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatadogMonitorIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.datadogMonitor.DatadogMonitorTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class DatadogMonitorTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#create DatadogMonitor#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#delete DatadogMonitor#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#read DatadogMonitor#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#update DatadogMonitor#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatadogMonitorTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#create DatadogMonitor#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#delete DatadogMonitor#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#read DatadogMonitor#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#update DatadogMonitor#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatadogMonitorTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatadogMonitorTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.datadogMonitor.DatadogMonitorTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(DatadogMonitorTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(DatadogMonitorTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatadogMonitorTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatadogMonitorTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatadogMonitorTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DatadogMonitorTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DatadogMonitorTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DatadogMonitorTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatadogMonitorTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.datadogMonitor.DatadogMonitorUser",
    jsii_struct_bases=[],
    name_mapping={"email": "email", "name": "name", "phone_number": "phoneNumber"},
)
class DatadogMonitorUser:
    def __init__(
        self,
        *,
        email: builtins.str,
        name: builtins.str,
        phone_number: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#email DatadogMonitor#email}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#name DatadogMonitor#name}.
        :param phone_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#phone_number DatadogMonitor#phone_number}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatadogMonitorUser.__init__)
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument phone_number", value=phone_number, expected_type=type_hints["phone_number"])
        self._values: typing.Dict[str, typing.Any] = {
            "email": email,
            "name": name,
        }
        if phone_number is not None:
            self._values["phone_number"] = phone_number

    @builtins.property
    def email(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#email DatadogMonitor#email}.'''
        result = self._values.get("email")
        assert result is not None, "Required property 'email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#name DatadogMonitor#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def phone_number(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/datadog_monitor#phone_number DatadogMonitor#phone_number}.'''
        result = self._values.get("phone_number")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatadogMonitorUser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatadogMonitorUserOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.datadogMonitor.DatadogMonitorUserOutputReference",
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
            type_hints = typing.get_type_hints(DatadogMonitorUserOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPhoneNumber")
    def reset_phone_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPhoneNumber", []))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="phoneNumberInput")
    def phone_number_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "phoneNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "email"))

    @email.setter
    def email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatadogMonitorUserOutputReference, "email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatadogMonitorUserOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="phoneNumber")
    def phone_number(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "phoneNumber"))

    @phone_number.setter
    def phone_number(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatadogMonitorUserOutputReference, "phone_number").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "phoneNumber", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DatadogMonitorUser]:
        return typing.cast(typing.Optional[DatadogMonitorUser], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DatadogMonitorUser]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatadogMonitorUserOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DatadogMonitor",
    "DatadogMonitorConfig",
    "DatadogMonitorDatadogOrganization",
    "DatadogMonitorDatadogOrganizationOutputReference",
    "DatadogMonitorIdentity",
    "DatadogMonitorIdentityOutputReference",
    "DatadogMonitorTimeouts",
    "DatadogMonitorTimeoutsOutputReference",
    "DatadogMonitorUser",
    "DatadogMonitorUserOutputReference",
]

publication.publish()
