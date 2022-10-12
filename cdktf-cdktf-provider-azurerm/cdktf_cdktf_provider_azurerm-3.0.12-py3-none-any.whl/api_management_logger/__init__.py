'''
# `azurerm_api_management_logger`

Refer to the Terraform Registory for docs: [`azurerm_api_management_logger`](https://www.terraform.io/docs/providers/azurerm/r/api_management_logger).
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


class ApiManagementLogger(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementLogger.ApiManagementLogger",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger azurerm_api_management_logger}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        api_management_name: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        application_insights: typing.Optional[typing.Union["ApiManagementLoggerApplicationInsights", typing.Dict[str, typing.Any]]] = None,
        buffered: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        eventhub: typing.Optional[typing.Union["ApiManagementLoggerEventhub", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        resource_id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["ApiManagementLoggerTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger azurerm_api_management_logger} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param api_management_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#api_management_name ApiManagementLogger#api_management_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#name ApiManagementLogger#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#resource_group_name ApiManagementLogger#resource_group_name}.
        :param application_insights: application_insights block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#application_insights ApiManagementLogger#application_insights}
        :param buffered: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#buffered ApiManagementLogger#buffered}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#description ApiManagementLogger#description}.
        :param eventhub: eventhub block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#eventhub ApiManagementLogger#eventhub}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#id ApiManagementLogger#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#resource_id ApiManagementLogger#resource_id}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#timeouts ApiManagementLogger#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementLogger.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ApiManagementLoggerConfig(
            api_management_name=api_management_name,
            name=name,
            resource_group_name=resource_group_name,
            application_insights=application_insights,
            buffered=buffered,
            description=description,
            eventhub=eventhub,
            id=id,
            resource_id=resource_id,
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

    @jsii.member(jsii_name="putApplicationInsights")
    def put_application_insights(self, *, instrumentation_key: builtins.str) -> None:
        '''
        :param instrumentation_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#instrumentation_key ApiManagementLogger#instrumentation_key}.
        '''
        value = ApiManagementLoggerApplicationInsights(
            instrumentation_key=instrumentation_key
        )

        return typing.cast(None, jsii.invoke(self, "putApplicationInsights", [value]))

    @jsii.member(jsii_name="putEventhub")
    def put_eventhub(
        self,
        *,
        connection_string: builtins.str,
        name: builtins.str,
    ) -> None:
        '''
        :param connection_string: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#connection_string ApiManagementLogger#connection_string}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#name ApiManagementLogger#name}.
        '''
        value = ApiManagementLoggerEventhub(
            connection_string=connection_string, name=name
        )

        return typing.cast(None, jsii.invoke(self, "putEventhub", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#create ApiManagementLogger#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#delete ApiManagementLogger#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#read ApiManagementLogger#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#update ApiManagementLogger#update}.
        '''
        value = ApiManagementLoggerTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetApplicationInsights")
    def reset_application_insights(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplicationInsights", []))

    @jsii.member(jsii_name="resetBuffered")
    def reset_buffered(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuffered", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEventhub")
    def reset_eventhub(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventhub", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetResourceId")
    def reset_resource_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceId", []))

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
    @jsii.member(jsii_name="applicationInsights")
    def application_insights(
        self,
    ) -> "ApiManagementLoggerApplicationInsightsOutputReference":
        return typing.cast("ApiManagementLoggerApplicationInsightsOutputReference", jsii.get(self, "applicationInsights"))

    @builtins.property
    @jsii.member(jsii_name="eventhub")
    def eventhub(self) -> "ApiManagementLoggerEventhubOutputReference":
        return typing.cast("ApiManagementLoggerEventhubOutputReference", jsii.get(self, "eventhub"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ApiManagementLoggerTimeoutsOutputReference":
        return typing.cast("ApiManagementLoggerTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="apiManagementNameInput")
    def api_management_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiManagementNameInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationInsightsInput")
    def application_insights_input(
        self,
    ) -> typing.Optional["ApiManagementLoggerApplicationInsights"]:
        return typing.cast(typing.Optional["ApiManagementLoggerApplicationInsights"], jsii.get(self, "applicationInsightsInput"))

    @builtins.property
    @jsii.member(jsii_name="bufferedInput")
    def buffered_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "bufferedInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="eventhubInput")
    def eventhub_input(self) -> typing.Optional["ApiManagementLoggerEventhub"]:
        return typing.cast(typing.Optional["ApiManagementLoggerEventhub"], jsii.get(self, "eventhubInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceIdInput")
    def resource_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ApiManagementLoggerTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ApiManagementLoggerTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="apiManagementName")
    def api_management_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiManagementName"))

    @api_management_name.setter
    def api_management_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementLogger, "api_management_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiManagementName", value)

    @builtins.property
    @jsii.member(jsii_name="buffered")
    def buffered(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "buffered"))

    @buffered.setter
    def buffered(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementLogger, "buffered").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "buffered", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementLogger, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementLogger, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementLogger, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementLogger, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="resourceId")
    def resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceId"))

    @resource_id.setter
    def resource_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementLogger, "resource_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementLogger.ApiManagementLoggerApplicationInsights",
    jsii_struct_bases=[],
    name_mapping={"instrumentation_key": "instrumentationKey"},
)
class ApiManagementLoggerApplicationInsights:
    def __init__(self, *, instrumentation_key: builtins.str) -> None:
        '''
        :param instrumentation_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#instrumentation_key ApiManagementLogger#instrumentation_key}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementLoggerApplicationInsights.__init__)
            check_type(argname="argument instrumentation_key", value=instrumentation_key, expected_type=type_hints["instrumentation_key"])
        self._values: typing.Dict[str, typing.Any] = {
            "instrumentation_key": instrumentation_key,
        }

    @builtins.property
    def instrumentation_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#instrumentation_key ApiManagementLogger#instrumentation_key}.'''
        result = self._values.get("instrumentation_key")
        assert result is not None, "Required property 'instrumentation_key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementLoggerApplicationInsights(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementLoggerApplicationInsightsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementLogger.ApiManagementLoggerApplicationInsightsOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementLoggerApplicationInsightsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="instrumentationKeyInput")
    def instrumentation_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instrumentationKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="instrumentationKey")
    def instrumentation_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instrumentationKey"))

    @instrumentation_key.setter
    def instrumentation_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementLoggerApplicationInsightsOutputReference, "instrumentation_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instrumentationKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApiManagementLoggerApplicationInsights]:
        return typing.cast(typing.Optional[ApiManagementLoggerApplicationInsights], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApiManagementLoggerApplicationInsights],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementLoggerApplicationInsightsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementLogger.ApiManagementLoggerConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "api_management_name": "apiManagementName",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "application_insights": "applicationInsights",
        "buffered": "buffered",
        "description": "description",
        "eventhub": "eventhub",
        "id": "id",
        "resource_id": "resourceId",
        "timeouts": "timeouts",
    },
)
class ApiManagementLoggerConfig(cdktf.TerraformMetaArguments):
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
        api_management_name: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        application_insights: typing.Optional[typing.Union[ApiManagementLoggerApplicationInsights, typing.Dict[str, typing.Any]]] = None,
        buffered: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        eventhub: typing.Optional[typing.Union["ApiManagementLoggerEventhub", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        resource_id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["ApiManagementLoggerTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param api_management_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#api_management_name ApiManagementLogger#api_management_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#name ApiManagementLogger#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#resource_group_name ApiManagementLogger#resource_group_name}.
        :param application_insights: application_insights block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#application_insights ApiManagementLogger#application_insights}
        :param buffered: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#buffered ApiManagementLogger#buffered}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#description ApiManagementLogger#description}.
        :param eventhub: eventhub block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#eventhub ApiManagementLogger#eventhub}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#id ApiManagementLogger#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#resource_id ApiManagementLogger#resource_id}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#timeouts ApiManagementLogger#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(application_insights, dict):
            application_insights = ApiManagementLoggerApplicationInsights(**application_insights)
        if isinstance(eventhub, dict):
            eventhub = ApiManagementLoggerEventhub(**eventhub)
        if isinstance(timeouts, dict):
            timeouts = ApiManagementLoggerTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementLoggerConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument api_management_name", value=api_management_name, expected_type=type_hints["api_management_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument application_insights", value=application_insights, expected_type=type_hints["application_insights"])
            check_type(argname="argument buffered", value=buffered, expected_type=type_hints["buffered"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument eventhub", value=eventhub, expected_type=type_hints["eventhub"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "api_management_name": api_management_name,
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
        if application_insights is not None:
            self._values["application_insights"] = application_insights
        if buffered is not None:
            self._values["buffered"] = buffered
        if description is not None:
            self._values["description"] = description
        if eventhub is not None:
            self._values["eventhub"] = eventhub
        if id is not None:
            self._values["id"] = id
        if resource_id is not None:
            self._values["resource_id"] = resource_id
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
    def api_management_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#api_management_name ApiManagementLogger#api_management_name}.'''
        result = self._values.get("api_management_name")
        assert result is not None, "Required property 'api_management_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#name ApiManagementLogger#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#resource_group_name ApiManagementLogger#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def application_insights(
        self,
    ) -> typing.Optional[ApiManagementLoggerApplicationInsights]:
        '''application_insights block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#application_insights ApiManagementLogger#application_insights}
        '''
        result = self._values.get("application_insights")
        return typing.cast(typing.Optional[ApiManagementLoggerApplicationInsights], result)

    @builtins.property
    def buffered(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#buffered ApiManagementLogger#buffered}.'''
        result = self._values.get("buffered")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#description ApiManagementLogger#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def eventhub(self) -> typing.Optional["ApiManagementLoggerEventhub"]:
        '''eventhub block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#eventhub ApiManagementLogger#eventhub}
        '''
        result = self._values.get("eventhub")
        return typing.cast(typing.Optional["ApiManagementLoggerEventhub"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#id ApiManagementLogger#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#resource_id ApiManagementLogger#resource_id}.'''
        result = self._values.get("resource_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ApiManagementLoggerTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#timeouts ApiManagementLogger#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ApiManagementLoggerTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementLoggerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementLogger.ApiManagementLoggerEventhub",
    jsii_struct_bases=[],
    name_mapping={"connection_string": "connectionString", "name": "name"},
)
class ApiManagementLoggerEventhub:
    def __init__(self, *, connection_string: builtins.str, name: builtins.str) -> None:
        '''
        :param connection_string: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#connection_string ApiManagementLogger#connection_string}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#name ApiManagementLogger#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementLoggerEventhub.__init__)
            check_type(argname="argument connection_string", value=connection_string, expected_type=type_hints["connection_string"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "connection_string": connection_string,
            "name": name,
        }

    @builtins.property
    def connection_string(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#connection_string ApiManagementLogger#connection_string}.'''
        result = self._values.get("connection_string")
        assert result is not None, "Required property 'connection_string' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#name ApiManagementLogger#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementLoggerEventhub(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementLoggerEventhubOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementLogger.ApiManagementLoggerEventhubOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementLoggerEventhubOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="connectionStringInput")
    def connection_string_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionStringInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionString")
    def connection_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionString"))

    @connection_string.setter
    def connection_string(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementLoggerEventhubOutputReference, "connection_string").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionString", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementLoggerEventhubOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApiManagementLoggerEventhub]:
        return typing.cast(typing.Optional[ApiManagementLoggerEventhub], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApiManagementLoggerEventhub],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementLoggerEventhubOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementLogger.ApiManagementLoggerTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class ApiManagementLoggerTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#create ApiManagementLogger#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#delete ApiManagementLogger#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#read ApiManagementLogger#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#update ApiManagementLogger#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementLoggerTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#create ApiManagementLogger#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#delete ApiManagementLogger#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#read ApiManagementLogger#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_logger#update ApiManagementLogger#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementLoggerTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementLoggerTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementLogger.ApiManagementLoggerTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementLoggerTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementLoggerTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementLoggerTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementLoggerTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementLoggerTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementLoggerTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementLoggerTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementLoggerTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementLoggerTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ApiManagementLogger",
    "ApiManagementLoggerApplicationInsights",
    "ApiManagementLoggerApplicationInsightsOutputReference",
    "ApiManagementLoggerConfig",
    "ApiManagementLoggerEventhub",
    "ApiManagementLoggerEventhubOutputReference",
    "ApiManagementLoggerTimeouts",
    "ApiManagementLoggerTimeoutsOutputReference",
]

publication.publish()
