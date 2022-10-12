'''
# `azurerm_subscription_cost_management_export`

Refer to the Terraform Registory for docs: [`azurerm_subscription_cost_management_export`](https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export).
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


class SubscriptionCostManagementExport(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.subscriptionCostManagementExport.SubscriptionCostManagementExport",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export azurerm_subscription_cost_management_export}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        export_data_options: typing.Union["SubscriptionCostManagementExportExportDataOptions", typing.Dict[str, typing.Any]],
        export_data_storage_location: typing.Union["SubscriptionCostManagementExportExportDataStorageLocation", typing.Dict[str, typing.Any]],
        name: builtins.str,
        recurrence_period_end_date: builtins.str,
        recurrence_period_start_date: builtins.str,
        recurrence_type: builtins.str,
        subscription_id: builtins.str,
        active: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["SubscriptionCostManagementExportTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export azurerm_subscription_cost_management_export} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param export_data_options: export_data_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#export_data_options SubscriptionCostManagementExport#export_data_options}
        :param export_data_storage_location: export_data_storage_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#export_data_storage_location SubscriptionCostManagementExport#export_data_storage_location}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#name SubscriptionCostManagementExport#name}.
        :param recurrence_period_end_date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#recurrence_period_end_date SubscriptionCostManagementExport#recurrence_period_end_date}.
        :param recurrence_period_start_date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#recurrence_period_start_date SubscriptionCostManagementExport#recurrence_period_start_date}.
        :param recurrence_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#recurrence_type SubscriptionCostManagementExport#recurrence_type}.
        :param subscription_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#subscription_id SubscriptionCostManagementExport#subscription_id}.
        :param active: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#active SubscriptionCostManagementExport#active}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#id SubscriptionCostManagementExport#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#timeouts SubscriptionCostManagementExport#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SubscriptionCostManagementExport.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SubscriptionCostManagementExportConfig(
            export_data_options=export_data_options,
            export_data_storage_location=export_data_storage_location,
            name=name,
            recurrence_period_end_date=recurrence_period_end_date,
            recurrence_period_start_date=recurrence_period_start_date,
            recurrence_type=recurrence_type,
            subscription_id=subscription_id,
            active=active,
            id=id,
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

    @jsii.member(jsii_name="putExportDataOptions")
    def put_export_data_options(
        self,
        *,
        time_frame: builtins.str,
        type: builtins.str,
    ) -> None:
        '''
        :param time_frame: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#time_frame SubscriptionCostManagementExport#time_frame}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#type SubscriptionCostManagementExport#type}.
        '''
        value = SubscriptionCostManagementExportExportDataOptions(
            time_frame=time_frame, type=type
        )

        return typing.cast(None, jsii.invoke(self, "putExportDataOptions", [value]))

    @jsii.member(jsii_name="putExportDataStorageLocation")
    def put_export_data_storage_location(
        self,
        *,
        container_id: builtins.str,
        root_folder_path: builtins.str,
    ) -> None:
        '''
        :param container_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#container_id SubscriptionCostManagementExport#container_id}.
        :param root_folder_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#root_folder_path SubscriptionCostManagementExport#root_folder_path}.
        '''
        value = SubscriptionCostManagementExportExportDataStorageLocation(
            container_id=container_id, root_folder_path=root_folder_path
        )

        return typing.cast(None, jsii.invoke(self, "putExportDataStorageLocation", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#create SubscriptionCostManagementExport#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#delete SubscriptionCostManagementExport#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#read SubscriptionCostManagementExport#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#update SubscriptionCostManagementExport#update}.
        '''
        value = SubscriptionCostManagementExportTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetActive")
    def reset_active(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActive", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    @jsii.member(jsii_name="exportDataOptions")
    def export_data_options(
        self,
    ) -> "SubscriptionCostManagementExportExportDataOptionsOutputReference":
        return typing.cast("SubscriptionCostManagementExportExportDataOptionsOutputReference", jsii.get(self, "exportDataOptions"))

    @builtins.property
    @jsii.member(jsii_name="exportDataStorageLocation")
    def export_data_storage_location(
        self,
    ) -> "SubscriptionCostManagementExportExportDataStorageLocationOutputReference":
        return typing.cast("SubscriptionCostManagementExportExportDataStorageLocationOutputReference", jsii.get(self, "exportDataStorageLocation"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "SubscriptionCostManagementExportTimeoutsOutputReference":
        return typing.cast("SubscriptionCostManagementExportTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="activeInput")
    def active_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "activeInput"))

    @builtins.property
    @jsii.member(jsii_name="exportDataOptionsInput")
    def export_data_options_input(
        self,
    ) -> typing.Optional["SubscriptionCostManagementExportExportDataOptions"]:
        return typing.cast(typing.Optional["SubscriptionCostManagementExportExportDataOptions"], jsii.get(self, "exportDataOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="exportDataStorageLocationInput")
    def export_data_storage_location_input(
        self,
    ) -> typing.Optional["SubscriptionCostManagementExportExportDataStorageLocation"]:
        return typing.cast(typing.Optional["SubscriptionCostManagementExportExportDataStorageLocation"], jsii.get(self, "exportDataStorageLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="recurrencePeriodEndDateInput")
    def recurrence_period_end_date_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recurrencePeriodEndDateInput"))

    @builtins.property
    @jsii.member(jsii_name="recurrencePeriodStartDateInput")
    def recurrence_period_start_date_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recurrencePeriodStartDateInput"))

    @builtins.property
    @jsii.member(jsii_name="recurrenceTypeInput")
    def recurrence_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recurrenceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="subscriptionIdInput")
    def subscription_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subscriptionIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["SubscriptionCostManagementExportTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["SubscriptionCostManagementExportTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="active")
    def active(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "active"))

    @active.setter
    def active(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SubscriptionCostManagementExport, "active").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "active", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SubscriptionCostManagementExport, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SubscriptionCostManagementExport, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="recurrencePeriodEndDate")
    def recurrence_period_end_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recurrencePeriodEndDate"))

    @recurrence_period_end_date.setter
    def recurrence_period_end_date(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SubscriptionCostManagementExport, "recurrence_period_end_date").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recurrencePeriodEndDate", value)

    @builtins.property
    @jsii.member(jsii_name="recurrencePeriodStartDate")
    def recurrence_period_start_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recurrencePeriodStartDate"))

    @recurrence_period_start_date.setter
    def recurrence_period_start_date(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SubscriptionCostManagementExport, "recurrence_period_start_date").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recurrencePeriodStartDate", value)

    @builtins.property
    @jsii.member(jsii_name="recurrenceType")
    def recurrence_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recurrenceType"))

    @recurrence_type.setter
    def recurrence_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SubscriptionCostManagementExport, "recurrence_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recurrenceType", value)

    @builtins.property
    @jsii.member(jsii_name="subscriptionId")
    def subscription_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subscriptionId"))

    @subscription_id.setter
    def subscription_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SubscriptionCostManagementExport, "subscription_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subscriptionId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.subscriptionCostManagementExport.SubscriptionCostManagementExportConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "export_data_options": "exportDataOptions",
        "export_data_storage_location": "exportDataStorageLocation",
        "name": "name",
        "recurrence_period_end_date": "recurrencePeriodEndDate",
        "recurrence_period_start_date": "recurrencePeriodStartDate",
        "recurrence_type": "recurrenceType",
        "subscription_id": "subscriptionId",
        "active": "active",
        "id": "id",
        "timeouts": "timeouts",
    },
)
class SubscriptionCostManagementExportConfig(cdktf.TerraformMetaArguments):
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
        export_data_options: typing.Union["SubscriptionCostManagementExportExportDataOptions", typing.Dict[str, typing.Any]],
        export_data_storage_location: typing.Union["SubscriptionCostManagementExportExportDataStorageLocation", typing.Dict[str, typing.Any]],
        name: builtins.str,
        recurrence_period_end_date: builtins.str,
        recurrence_period_start_date: builtins.str,
        recurrence_type: builtins.str,
        subscription_id: builtins.str,
        active: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["SubscriptionCostManagementExportTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param export_data_options: export_data_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#export_data_options SubscriptionCostManagementExport#export_data_options}
        :param export_data_storage_location: export_data_storage_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#export_data_storage_location SubscriptionCostManagementExport#export_data_storage_location}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#name SubscriptionCostManagementExport#name}.
        :param recurrence_period_end_date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#recurrence_period_end_date SubscriptionCostManagementExport#recurrence_period_end_date}.
        :param recurrence_period_start_date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#recurrence_period_start_date SubscriptionCostManagementExport#recurrence_period_start_date}.
        :param recurrence_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#recurrence_type SubscriptionCostManagementExport#recurrence_type}.
        :param subscription_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#subscription_id SubscriptionCostManagementExport#subscription_id}.
        :param active: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#active SubscriptionCostManagementExport#active}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#id SubscriptionCostManagementExport#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#timeouts SubscriptionCostManagementExport#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(export_data_options, dict):
            export_data_options = SubscriptionCostManagementExportExportDataOptions(**export_data_options)
        if isinstance(export_data_storage_location, dict):
            export_data_storage_location = SubscriptionCostManagementExportExportDataStorageLocation(**export_data_storage_location)
        if isinstance(timeouts, dict):
            timeouts = SubscriptionCostManagementExportTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(SubscriptionCostManagementExportConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument export_data_options", value=export_data_options, expected_type=type_hints["export_data_options"])
            check_type(argname="argument export_data_storage_location", value=export_data_storage_location, expected_type=type_hints["export_data_storage_location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument recurrence_period_end_date", value=recurrence_period_end_date, expected_type=type_hints["recurrence_period_end_date"])
            check_type(argname="argument recurrence_period_start_date", value=recurrence_period_start_date, expected_type=type_hints["recurrence_period_start_date"])
            check_type(argname="argument recurrence_type", value=recurrence_type, expected_type=type_hints["recurrence_type"])
            check_type(argname="argument subscription_id", value=subscription_id, expected_type=type_hints["subscription_id"])
            check_type(argname="argument active", value=active, expected_type=type_hints["active"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "export_data_options": export_data_options,
            "export_data_storage_location": export_data_storage_location,
            "name": name,
            "recurrence_period_end_date": recurrence_period_end_date,
            "recurrence_period_start_date": recurrence_period_start_date,
            "recurrence_type": recurrence_type,
            "subscription_id": subscription_id,
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
        if active is not None:
            self._values["active"] = active
        if id is not None:
            self._values["id"] = id
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
    def export_data_options(
        self,
    ) -> "SubscriptionCostManagementExportExportDataOptions":
        '''export_data_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#export_data_options SubscriptionCostManagementExport#export_data_options}
        '''
        result = self._values.get("export_data_options")
        assert result is not None, "Required property 'export_data_options' is missing"
        return typing.cast("SubscriptionCostManagementExportExportDataOptions", result)

    @builtins.property
    def export_data_storage_location(
        self,
    ) -> "SubscriptionCostManagementExportExportDataStorageLocation":
        '''export_data_storage_location block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#export_data_storage_location SubscriptionCostManagementExport#export_data_storage_location}
        '''
        result = self._values.get("export_data_storage_location")
        assert result is not None, "Required property 'export_data_storage_location' is missing"
        return typing.cast("SubscriptionCostManagementExportExportDataStorageLocation", result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#name SubscriptionCostManagementExport#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def recurrence_period_end_date(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#recurrence_period_end_date SubscriptionCostManagementExport#recurrence_period_end_date}.'''
        result = self._values.get("recurrence_period_end_date")
        assert result is not None, "Required property 'recurrence_period_end_date' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def recurrence_period_start_date(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#recurrence_period_start_date SubscriptionCostManagementExport#recurrence_period_start_date}.'''
        result = self._values.get("recurrence_period_start_date")
        assert result is not None, "Required property 'recurrence_period_start_date' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def recurrence_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#recurrence_type SubscriptionCostManagementExport#recurrence_type}.'''
        result = self._values.get("recurrence_type")
        assert result is not None, "Required property 'recurrence_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subscription_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#subscription_id SubscriptionCostManagementExport#subscription_id}.'''
        result = self._values.get("subscription_id")
        assert result is not None, "Required property 'subscription_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def active(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#active SubscriptionCostManagementExport#active}.'''
        result = self._values.get("active")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#id SubscriptionCostManagementExport#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["SubscriptionCostManagementExportTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#timeouts SubscriptionCostManagementExport#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["SubscriptionCostManagementExportTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubscriptionCostManagementExportConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.subscriptionCostManagementExport.SubscriptionCostManagementExportExportDataOptions",
    jsii_struct_bases=[],
    name_mapping={"time_frame": "timeFrame", "type": "type"},
)
class SubscriptionCostManagementExportExportDataOptions:
    def __init__(self, *, time_frame: builtins.str, type: builtins.str) -> None:
        '''
        :param time_frame: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#time_frame SubscriptionCostManagementExport#time_frame}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#type SubscriptionCostManagementExport#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SubscriptionCostManagementExportExportDataOptions.__init__)
            check_type(argname="argument time_frame", value=time_frame, expected_type=type_hints["time_frame"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "time_frame": time_frame,
            "type": type,
        }

    @builtins.property
    def time_frame(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#time_frame SubscriptionCostManagementExport#time_frame}.'''
        result = self._values.get("time_frame")
        assert result is not None, "Required property 'time_frame' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#type SubscriptionCostManagementExport#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubscriptionCostManagementExportExportDataOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SubscriptionCostManagementExportExportDataOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.subscriptionCostManagementExport.SubscriptionCostManagementExportExportDataOptionsOutputReference",
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
            type_hints = typing.get_type_hints(SubscriptionCostManagementExportExportDataOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="timeFrameInput")
    def time_frame_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeFrameInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="timeFrame")
    def time_frame(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeFrame"))

    @time_frame.setter
    def time_frame(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SubscriptionCostManagementExportExportDataOptionsOutputReference, "time_frame").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeFrame", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SubscriptionCostManagementExportExportDataOptionsOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SubscriptionCostManagementExportExportDataOptions]:
        return typing.cast(typing.Optional[SubscriptionCostManagementExportExportDataOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SubscriptionCostManagementExportExportDataOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SubscriptionCostManagementExportExportDataOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.subscriptionCostManagementExport.SubscriptionCostManagementExportExportDataStorageLocation",
    jsii_struct_bases=[],
    name_mapping={"container_id": "containerId", "root_folder_path": "rootFolderPath"},
)
class SubscriptionCostManagementExportExportDataStorageLocation:
    def __init__(
        self,
        *,
        container_id: builtins.str,
        root_folder_path: builtins.str,
    ) -> None:
        '''
        :param container_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#container_id SubscriptionCostManagementExport#container_id}.
        :param root_folder_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#root_folder_path SubscriptionCostManagementExport#root_folder_path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SubscriptionCostManagementExportExportDataStorageLocation.__init__)
            check_type(argname="argument container_id", value=container_id, expected_type=type_hints["container_id"])
            check_type(argname="argument root_folder_path", value=root_folder_path, expected_type=type_hints["root_folder_path"])
        self._values: typing.Dict[str, typing.Any] = {
            "container_id": container_id,
            "root_folder_path": root_folder_path,
        }

    @builtins.property
    def container_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#container_id SubscriptionCostManagementExport#container_id}.'''
        result = self._values.get("container_id")
        assert result is not None, "Required property 'container_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def root_folder_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#root_folder_path SubscriptionCostManagementExport#root_folder_path}.'''
        result = self._values.get("root_folder_path")
        assert result is not None, "Required property 'root_folder_path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubscriptionCostManagementExportExportDataStorageLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SubscriptionCostManagementExportExportDataStorageLocationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.subscriptionCostManagementExport.SubscriptionCostManagementExportExportDataStorageLocationOutputReference",
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
            type_hints = typing.get_type_hints(SubscriptionCostManagementExportExportDataStorageLocationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="containerIdInput")
    def container_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerIdInput"))

    @builtins.property
    @jsii.member(jsii_name="rootFolderPathInput")
    def root_folder_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rootFolderPathInput"))

    @builtins.property
    @jsii.member(jsii_name="containerId")
    def container_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerId"))

    @container_id.setter
    def container_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SubscriptionCostManagementExportExportDataStorageLocationOutputReference, "container_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerId", value)

    @builtins.property
    @jsii.member(jsii_name="rootFolderPath")
    def root_folder_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rootFolderPath"))

    @root_folder_path.setter
    def root_folder_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SubscriptionCostManagementExportExportDataStorageLocationOutputReference, "root_folder_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootFolderPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SubscriptionCostManagementExportExportDataStorageLocation]:
        return typing.cast(typing.Optional[SubscriptionCostManagementExportExportDataStorageLocation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SubscriptionCostManagementExportExportDataStorageLocation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SubscriptionCostManagementExportExportDataStorageLocationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.subscriptionCostManagementExport.SubscriptionCostManagementExportTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class SubscriptionCostManagementExportTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#create SubscriptionCostManagementExport#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#delete SubscriptionCostManagementExport#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#read SubscriptionCostManagementExport#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#update SubscriptionCostManagementExport#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SubscriptionCostManagementExportTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#create SubscriptionCostManagementExport#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#delete SubscriptionCostManagementExport#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#read SubscriptionCostManagementExport#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subscription_cost_management_export#update SubscriptionCostManagementExport#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubscriptionCostManagementExportTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SubscriptionCostManagementExportTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.subscriptionCostManagementExport.SubscriptionCostManagementExportTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(SubscriptionCostManagementExportTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(SubscriptionCostManagementExportTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SubscriptionCostManagementExportTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SubscriptionCostManagementExportTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SubscriptionCostManagementExportTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SubscriptionCostManagementExportTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SubscriptionCostManagementExportTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SubscriptionCostManagementExportTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SubscriptionCostManagementExportTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SubscriptionCostManagementExport",
    "SubscriptionCostManagementExportConfig",
    "SubscriptionCostManagementExportExportDataOptions",
    "SubscriptionCostManagementExportExportDataOptionsOutputReference",
    "SubscriptionCostManagementExportExportDataStorageLocation",
    "SubscriptionCostManagementExportExportDataStorageLocationOutputReference",
    "SubscriptionCostManagementExportTimeouts",
    "SubscriptionCostManagementExportTimeoutsOutputReference",
]

publication.publish()
