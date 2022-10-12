'''
# `azurerm_databox_edge_order`

Refer to the Terraform Registory for docs: [`azurerm_databox_edge_order`](https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order).
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


class DataboxEdgeOrder(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.databoxEdgeOrder.DataboxEdgeOrder",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order azurerm_databox_edge_order}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        contact: typing.Union["DataboxEdgeOrderContact", typing.Dict[str, typing.Any]],
        device_name: builtins.str,
        resource_group_name: builtins.str,
        shipment_address: typing.Union["DataboxEdgeOrderShipmentAddress", typing.Dict[str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DataboxEdgeOrderTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order azurerm_databox_edge_order} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param contact: contact block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#contact DataboxEdgeOrder#contact}
        :param device_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#device_name DataboxEdgeOrder#device_name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#resource_group_name DataboxEdgeOrder#resource_group_name}.
        :param shipment_address: shipment_address block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#shipment_address DataboxEdgeOrder#shipment_address}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#id DataboxEdgeOrder#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#timeouts DataboxEdgeOrder#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataboxEdgeOrder.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataboxEdgeOrderConfig(
            contact=contact,
            device_name=device_name,
            resource_group_name=resource_group_name,
            shipment_address=shipment_address,
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

    @jsii.member(jsii_name="putContact")
    def put_contact(
        self,
        *,
        company_name: builtins.str,
        emails: typing.Sequence[builtins.str],
        name: builtins.str,
        phone_number: builtins.str,
    ) -> None:
        '''
        :param company_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#company_name DataboxEdgeOrder#company_name}.
        :param emails: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#emails DataboxEdgeOrder#emails}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#name DataboxEdgeOrder#name}.
        :param phone_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#phone_number DataboxEdgeOrder#phone_number}.
        '''
        value = DataboxEdgeOrderContact(
            company_name=company_name,
            emails=emails,
            name=name,
            phone_number=phone_number,
        )

        return typing.cast(None, jsii.invoke(self, "putContact", [value]))

    @jsii.member(jsii_name="putShipmentAddress")
    def put_shipment_address(
        self,
        *,
        address: typing.Sequence[builtins.str],
        city: builtins.str,
        country: builtins.str,
        postal_code: builtins.str,
        state: builtins.str,
    ) -> None:
        '''
        :param address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#address DataboxEdgeOrder#address}.
        :param city: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#city DataboxEdgeOrder#city}.
        :param country: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#country DataboxEdgeOrder#country}.
        :param postal_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#postal_code DataboxEdgeOrder#postal_code}.
        :param state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#state DataboxEdgeOrder#state}.
        '''
        value = DataboxEdgeOrderShipmentAddress(
            address=address,
            city=city,
            country=country,
            postal_code=postal_code,
            state=state,
        )

        return typing.cast(None, jsii.invoke(self, "putShipmentAddress", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#create DataboxEdgeOrder#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#delete DataboxEdgeOrder#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#read DataboxEdgeOrder#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#update DataboxEdgeOrder#update}.
        '''
        value = DataboxEdgeOrderTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

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
    @jsii.member(jsii_name="contact")
    def contact(self) -> "DataboxEdgeOrderContactOutputReference":
        return typing.cast("DataboxEdgeOrderContactOutputReference", jsii.get(self, "contact"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="returnTracking")
    def return_tracking(self) -> "DataboxEdgeOrderReturnTrackingList":
        return typing.cast("DataboxEdgeOrderReturnTrackingList", jsii.get(self, "returnTracking"))

    @builtins.property
    @jsii.member(jsii_name="serialNumber")
    def serial_number(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serialNumber"))

    @builtins.property
    @jsii.member(jsii_name="shipmentAddress")
    def shipment_address(self) -> "DataboxEdgeOrderShipmentAddressOutputReference":
        return typing.cast("DataboxEdgeOrderShipmentAddressOutputReference", jsii.get(self, "shipmentAddress"))

    @builtins.property
    @jsii.member(jsii_name="shipmentHistory")
    def shipment_history(self) -> "DataboxEdgeOrderShipmentHistoryList":
        return typing.cast("DataboxEdgeOrderShipmentHistoryList", jsii.get(self, "shipmentHistory"))

    @builtins.property
    @jsii.member(jsii_name="shipmentTracking")
    def shipment_tracking(self) -> "DataboxEdgeOrderShipmentTrackingList":
        return typing.cast("DataboxEdgeOrderShipmentTrackingList", jsii.get(self, "shipmentTracking"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> "DataboxEdgeOrderStatusList":
        return typing.cast("DataboxEdgeOrderStatusList", jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "DataboxEdgeOrderTimeoutsOutputReference":
        return typing.cast("DataboxEdgeOrderTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="contactInput")
    def contact_input(self) -> typing.Optional["DataboxEdgeOrderContact"]:
        return typing.cast(typing.Optional["DataboxEdgeOrderContact"], jsii.get(self, "contactInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceNameInput")
    def device_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="shipmentAddressInput")
    def shipment_address_input(
        self,
    ) -> typing.Optional["DataboxEdgeOrderShipmentAddress"]:
        return typing.cast(typing.Optional["DataboxEdgeOrderShipmentAddress"], jsii.get(self, "shipmentAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["DataboxEdgeOrderTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DataboxEdgeOrderTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceName")
    def device_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deviceName"))

    @device_name.setter
    def device_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataboxEdgeOrder, "device_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataboxEdgeOrder, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataboxEdgeOrder, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.databoxEdgeOrder.DataboxEdgeOrderConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "contact": "contact",
        "device_name": "deviceName",
        "resource_group_name": "resourceGroupName",
        "shipment_address": "shipmentAddress",
        "id": "id",
        "timeouts": "timeouts",
    },
)
class DataboxEdgeOrderConfig(cdktf.TerraformMetaArguments):
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
        contact: typing.Union["DataboxEdgeOrderContact", typing.Dict[str, typing.Any]],
        device_name: builtins.str,
        resource_group_name: builtins.str,
        shipment_address: typing.Union["DataboxEdgeOrderShipmentAddress", typing.Dict[str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DataboxEdgeOrderTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param contact: contact block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#contact DataboxEdgeOrder#contact}
        :param device_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#device_name DataboxEdgeOrder#device_name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#resource_group_name DataboxEdgeOrder#resource_group_name}.
        :param shipment_address: shipment_address block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#shipment_address DataboxEdgeOrder#shipment_address}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#id DataboxEdgeOrder#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#timeouts DataboxEdgeOrder#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(contact, dict):
            contact = DataboxEdgeOrderContact(**contact)
        if isinstance(shipment_address, dict):
            shipment_address = DataboxEdgeOrderShipmentAddress(**shipment_address)
        if isinstance(timeouts, dict):
            timeouts = DataboxEdgeOrderTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(DataboxEdgeOrderConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument contact", value=contact, expected_type=type_hints["contact"])
            check_type(argname="argument device_name", value=device_name, expected_type=type_hints["device_name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument shipment_address", value=shipment_address, expected_type=type_hints["shipment_address"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "contact": contact,
            "device_name": device_name,
            "resource_group_name": resource_group_name,
            "shipment_address": shipment_address,
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
    def contact(self) -> "DataboxEdgeOrderContact":
        '''contact block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#contact DataboxEdgeOrder#contact}
        '''
        result = self._values.get("contact")
        assert result is not None, "Required property 'contact' is missing"
        return typing.cast("DataboxEdgeOrderContact", result)

    @builtins.property
    def device_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#device_name DataboxEdgeOrder#device_name}.'''
        result = self._values.get("device_name")
        assert result is not None, "Required property 'device_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#resource_group_name DataboxEdgeOrder#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def shipment_address(self) -> "DataboxEdgeOrderShipmentAddress":
        '''shipment_address block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#shipment_address DataboxEdgeOrder#shipment_address}
        '''
        result = self._values.get("shipment_address")
        assert result is not None, "Required property 'shipment_address' is missing"
        return typing.cast("DataboxEdgeOrderShipmentAddress", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#id DataboxEdgeOrder#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DataboxEdgeOrderTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#timeouts DataboxEdgeOrder#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DataboxEdgeOrderTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataboxEdgeOrderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.databoxEdgeOrder.DataboxEdgeOrderContact",
    jsii_struct_bases=[],
    name_mapping={
        "company_name": "companyName",
        "emails": "emails",
        "name": "name",
        "phone_number": "phoneNumber",
    },
)
class DataboxEdgeOrderContact:
    def __init__(
        self,
        *,
        company_name: builtins.str,
        emails: typing.Sequence[builtins.str],
        name: builtins.str,
        phone_number: builtins.str,
    ) -> None:
        '''
        :param company_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#company_name DataboxEdgeOrder#company_name}.
        :param emails: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#emails DataboxEdgeOrder#emails}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#name DataboxEdgeOrder#name}.
        :param phone_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#phone_number DataboxEdgeOrder#phone_number}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataboxEdgeOrderContact.__init__)
            check_type(argname="argument company_name", value=company_name, expected_type=type_hints["company_name"])
            check_type(argname="argument emails", value=emails, expected_type=type_hints["emails"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument phone_number", value=phone_number, expected_type=type_hints["phone_number"])
        self._values: typing.Dict[str, typing.Any] = {
            "company_name": company_name,
            "emails": emails,
            "name": name,
            "phone_number": phone_number,
        }

    @builtins.property
    def company_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#company_name DataboxEdgeOrder#company_name}.'''
        result = self._values.get("company_name")
        assert result is not None, "Required property 'company_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def emails(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#emails DataboxEdgeOrder#emails}.'''
        result = self._values.get("emails")
        assert result is not None, "Required property 'emails' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#name DataboxEdgeOrder#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def phone_number(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#phone_number DataboxEdgeOrder#phone_number}.'''
        result = self._values.get("phone_number")
        assert result is not None, "Required property 'phone_number' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataboxEdgeOrderContact(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataboxEdgeOrderContactOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.databoxEdgeOrder.DataboxEdgeOrderContactOutputReference",
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
            type_hints = typing.get_type_hints(DataboxEdgeOrderContactOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="companyNameInput")
    def company_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "companyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="emailsInput")
    def emails_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "emailsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="phoneNumberInput")
    def phone_number_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "phoneNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="companyName")
    def company_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "companyName"))

    @company_name.setter
    def company_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataboxEdgeOrderContactOutputReference, "company_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "companyName", value)

    @builtins.property
    @jsii.member(jsii_name="emails")
    def emails(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "emails"))

    @emails.setter
    def emails(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataboxEdgeOrderContactOutputReference, "emails").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emails", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataboxEdgeOrderContactOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="phoneNumber")
    def phone_number(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "phoneNumber"))

    @phone_number.setter
    def phone_number(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataboxEdgeOrderContactOutputReference, "phone_number").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "phoneNumber", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataboxEdgeOrderContact]:
        return typing.cast(typing.Optional[DataboxEdgeOrderContact], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DataboxEdgeOrderContact]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataboxEdgeOrderContactOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.databoxEdgeOrder.DataboxEdgeOrderReturnTracking",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataboxEdgeOrderReturnTracking:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataboxEdgeOrderReturnTracking(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataboxEdgeOrderReturnTrackingList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.databoxEdgeOrder.DataboxEdgeOrderReturnTrackingList",
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
            type_hints = typing.get_type_hints(DataboxEdgeOrderReturnTrackingList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataboxEdgeOrderReturnTrackingOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataboxEdgeOrderReturnTrackingList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataboxEdgeOrderReturnTrackingOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataboxEdgeOrderReturnTrackingList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataboxEdgeOrderReturnTrackingList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataboxEdgeOrderReturnTrackingList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataboxEdgeOrderReturnTrackingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.databoxEdgeOrder.DataboxEdgeOrderReturnTrackingOutputReference",
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
            type_hints = typing.get_type_hints(DataboxEdgeOrderReturnTrackingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="carrierName")
    def carrier_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "carrierName"))

    @builtins.property
    @jsii.member(jsii_name="serialNumber")
    def serial_number(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serialNumber"))

    @builtins.property
    @jsii.member(jsii_name="trackingId")
    def tracking_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "trackingId"))

    @builtins.property
    @jsii.member(jsii_name="trackingUrl")
    def tracking_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "trackingUrl"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataboxEdgeOrderReturnTracking]:
        return typing.cast(typing.Optional[DataboxEdgeOrderReturnTracking], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataboxEdgeOrderReturnTracking],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataboxEdgeOrderReturnTrackingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.databoxEdgeOrder.DataboxEdgeOrderShipmentAddress",
    jsii_struct_bases=[],
    name_mapping={
        "address": "address",
        "city": "city",
        "country": "country",
        "postal_code": "postalCode",
        "state": "state",
    },
)
class DataboxEdgeOrderShipmentAddress:
    def __init__(
        self,
        *,
        address: typing.Sequence[builtins.str],
        city: builtins.str,
        country: builtins.str,
        postal_code: builtins.str,
        state: builtins.str,
    ) -> None:
        '''
        :param address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#address DataboxEdgeOrder#address}.
        :param city: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#city DataboxEdgeOrder#city}.
        :param country: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#country DataboxEdgeOrder#country}.
        :param postal_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#postal_code DataboxEdgeOrder#postal_code}.
        :param state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#state DataboxEdgeOrder#state}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataboxEdgeOrderShipmentAddress.__init__)
            check_type(argname="argument address", value=address, expected_type=type_hints["address"])
            check_type(argname="argument city", value=city, expected_type=type_hints["city"])
            check_type(argname="argument country", value=country, expected_type=type_hints["country"])
            check_type(argname="argument postal_code", value=postal_code, expected_type=type_hints["postal_code"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
        self._values: typing.Dict[str, typing.Any] = {
            "address": address,
            "city": city,
            "country": country,
            "postal_code": postal_code,
            "state": state,
        }

    @builtins.property
    def address(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#address DataboxEdgeOrder#address}.'''
        result = self._values.get("address")
        assert result is not None, "Required property 'address' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def city(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#city DataboxEdgeOrder#city}.'''
        result = self._values.get("city")
        assert result is not None, "Required property 'city' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def country(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#country DataboxEdgeOrder#country}.'''
        result = self._values.get("country")
        assert result is not None, "Required property 'country' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def postal_code(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#postal_code DataboxEdgeOrder#postal_code}.'''
        result = self._values.get("postal_code")
        assert result is not None, "Required property 'postal_code' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def state(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#state DataboxEdgeOrder#state}.'''
        result = self._values.get("state")
        assert result is not None, "Required property 'state' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataboxEdgeOrderShipmentAddress(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataboxEdgeOrderShipmentAddressOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.databoxEdgeOrder.DataboxEdgeOrderShipmentAddressOutputReference",
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
            type_hints = typing.get_type_hints(DataboxEdgeOrderShipmentAddressOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="addressInput")
    def address_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "addressInput"))

    @builtins.property
    @jsii.member(jsii_name="cityInput")
    def city_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cityInput"))

    @builtins.property
    @jsii.member(jsii_name="countryInput")
    def country_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "countryInput"))

    @builtins.property
    @jsii.member(jsii_name="postalCodeInput")
    def postal_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "postalCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="stateInput")
    def state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateInput"))

    @builtins.property
    @jsii.member(jsii_name="address")
    def address(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "address"))

    @address.setter
    def address(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataboxEdgeOrderShipmentAddressOutputReference, "address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "address", value)

    @builtins.property
    @jsii.member(jsii_name="city")
    def city(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "city"))

    @city.setter
    def city(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataboxEdgeOrderShipmentAddressOutputReference, "city").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "city", value)

    @builtins.property
    @jsii.member(jsii_name="country")
    def country(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "country"))

    @country.setter
    def country(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataboxEdgeOrderShipmentAddressOutputReference, "country").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "country", value)

    @builtins.property
    @jsii.member(jsii_name="postalCode")
    def postal_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "postalCode"))

    @postal_code.setter
    def postal_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataboxEdgeOrderShipmentAddressOutputReference, "postal_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "postalCode", value)

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @state.setter
    def state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataboxEdgeOrderShipmentAddressOutputReference, "state").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataboxEdgeOrderShipmentAddress]:
        return typing.cast(typing.Optional[DataboxEdgeOrderShipmentAddress], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataboxEdgeOrderShipmentAddress],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataboxEdgeOrderShipmentAddressOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.databoxEdgeOrder.DataboxEdgeOrderShipmentHistory",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataboxEdgeOrderShipmentHistory:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataboxEdgeOrderShipmentHistory(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataboxEdgeOrderShipmentHistoryList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.databoxEdgeOrder.DataboxEdgeOrderShipmentHistoryList",
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
            type_hints = typing.get_type_hints(DataboxEdgeOrderShipmentHistoryList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataboxEdgeOrderShipmentHistoryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataboxEdgeOrderShipmentHistoryList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataboxEdgeOrderShipmentHistoryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataboxEdgeOrderShipmentHistoryList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataboxEdgeOrderShipmentHistoryList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataboxEdgeOrderShipmentHistoryList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataboxEdgeOrderShipmentHistoryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.databoxEdgeOrder.DataboxEdgeOrderShipmentHistoryOutputReference",
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
            type_hints = typing.get_type_hints(DataboxEdgeOrderShipmentHistoryOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="additionalDetails")
    def additional_details(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "additionalDetails"))

    @builtins.property
    @jsii.member(jsii_name="comments")
    def comments(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comments"))

    @builtins.property
    @jsii.member(jsii_name="lastUpdate")
    def last_update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastUpdate"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataboxEdgeOrderShipmentHistory]:
        return typing.cast(typing.Optional[DataboxEdgeOrderShipmentHistory], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataboxEdgeOrderShipmentHistory],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataboxEdgeOrderShipmentHistoryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.databoxEdgeOrder.DataboxEdgeOrderShipmentTracking",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataboxEdgeOrderShipmentTracking:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataboxEdgeOrderShipmentTracking(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataboxEdgeOrderShipmentTrackingList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.databoxEdgeOrder.DataboxEdgeOrderShipmentTrackingList",
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
            type_hints = typing.get_type_hints(DataboxEdgeOrderShipmentTrackingList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataboxEdgeOrderShipmentTrackingOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataboxEdgeOrderShipmentTrackingList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataboxEdgeOrderShipmentTrackingOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataboxEdgeOrderShipmentTrackingList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataboxEdgeOrderShipmentTrackingList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataboxEdgeOrderShipmentTrackingList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataboxEdgeOrderShipmentTrackingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.databoxEdgeOrder.DataboxEdgeOrderShipmentTrackingOutputReference",
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
            type_hints = typing.get_type_hints(DataboxEdgeOrderShipmentTrackingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="carrierName")
    def carrier_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "carrierName"))

    @builtins.property
    @jsii.member(jsii_name="serialNumber")
    def serial_number(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serialNumber"))

    @builtins.property
    @jsii.member(jsii_name="trackingId")
    def tracking_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "trackingId"))

    @builtins.property
    @jsii.member(jsii_name="trackingUrl")
    def tracking_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "trackingUrl"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataboxEdgeOrderShipmentTracking]:
        return typing.cast(typing.Optional[DataboxEdgeOrderShipmentTracking], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataboxEdgeOrderShipmentTracking],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataboxEdgeOrderShipmentTrackingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.databoxEdgeOrder.DataboxEdgeOrderStatus",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataboxEdgeOrderStatus:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataboxEdgeOrderStatus(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataboxEdgeOrderStatusList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.databoxEdgeOrder.DataboxEdgeOrderStatusList",
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
            type_hints = typing.get_type_hints(DataboxEdgeOrderStatusList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DataboxEdgeOrderStatusOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataboxEdgeOrderStatusList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataboxEdgeOrderStatusOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataboxEdgeOrderStatusList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataboxEdgeOrderStatusList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataboxEdgeOrderStatusList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataboxEdgeOrderStatusOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.databoxEdgeOrder.DataboxEdgeOrderStatusOutputReference",
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
            type_hints = typing.get_type_hints(DataboxEdgeOrderStatusOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="additionalDetails")
    def additional_details(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "additionalDetails"))

    @builtins.property
    @jsii.member(jsii_name="comments")
    def comments(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comments"))

    @builtins.property
    @jsii.member(jsii_name="info")
    def info(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "info"))

    @builtins.property
    @jsii.member(jsii_name="lastUpdate")
    def last_update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastUpdate"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataboxEdgeOrderStatus]:
        return typing.cast(typing.Optional[DataboxEdgeOrderStatus], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DataboxEdgeOrderStatus]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataboxEdgeOrderStatusOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.databoxEdgeOrder.DataboxEdgeOrderTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class DataboxEdgeOrderTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#create DataboxEdgeOrder#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#delete DataboxEdgeOrder#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#read DataboxEdgeOrder#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#update DataboxEdgeOrder#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataboxEdgeOrderTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#create DataboxEdgeOrder#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#delete DataboxEdgeOrder#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#read DataboxEdgeOrder#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databox_edge_order#update DataboxEdgeOrder#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataboxEdgeOrderTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataboxEdgeOrderTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.databoxEdgeOrder.DataboxEdgeOrderTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(DataboxEdgeOrderTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(DataboxEdgeOrderTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataboxEdgeOrderTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataboxEdgeOrderTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataboxEdgeOrderTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataboxEdgeOrderTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataboxEdgeOrderTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataboxEdgeOrderTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataboxEdgeOrderTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataboxEdgeOrder",
    "DataboxEdgeOrderConfig",
    "DataboxEdgeOrderContact",
    "DataboxEdgeOrderContactOutputReference",
    "DataboxEdgeOrderReturnTracking",
    "DataboxEdgeOrderReturnTrackingList",
    "DataboxEdgeOrderReturnTrackingOutputReference",
    "DataboxEdgeOrderShipmentAddress",
    "DataboxEdgeOrderShipmentAddressOutputReference",
    "DataboxEdgeOrderShipmentHistory",
    "DataboxEdgeOrderShipmentHistoryList",
    "DataboxEdgeOrderShipmentHistoryOutputReference",
    "DataboxEdgeOrderShipmentTracking",
    "DataboxEdgeOrderShipmentTrackingList",
    "DataboxEdgeOrderShipmentTrackingOutputReference",
    "DataboxEdgeOrderStatus",
    "DataboxEdgeOrderStatusList",
    "DataboxEdgeOrderStatusOutputReference",
    "DataboxEdgeOrderTimeouts",
    "DataboxEdgeOrderTimeoutsOutputReference",
]

publication.publish()
