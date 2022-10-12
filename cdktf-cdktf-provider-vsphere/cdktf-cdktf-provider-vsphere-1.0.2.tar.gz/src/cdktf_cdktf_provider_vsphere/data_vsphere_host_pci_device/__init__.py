'''
# `data_vsphere_host_pci_device`

Refer to the Terraform Registory for docs: [`data_vsphere_host_pci_device`](https://www.terraform.io/docs/providers/vsphere/d/host_pci_device).
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


class DataVsphereHostPciDevice(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vsphere.dataVsphereHostPciDevice.DataVsphereHostPciDevice",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vsphere/d/host_pci_device vsphere_host_pci_device}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        host_id: builtins.str,
        class_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        name_regex: typing.Optional[builtins.str] = None,
        vendor_id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vsphere/d/host_pci_device vsphere_host_pci_device} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param host_id: The Managed Object ID of the host system. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/host_pci_device#host_id DataVsphereHostPciDevice#host_id}
        :param class_id: The hexadecimal value of the PCI device's class ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/host_pci_device#class_id DataVsphereHostPciDevice#class_id}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/host_pci_device#id DataVsphereHostPciDevice#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name_regex: A regular expression used to match the PCI device name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/host_pci_device#name_regex DataVsphereHostPciDevice#name_regex}
        :param vendor_id: The hexadecimal value of the PCI device's vendor ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/host_pci_device#vendor_id DataVsphereHostPciDevice#vendor_id}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataVsphereHostPciDevice.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataVsphereHostPciDeviceConfig(
            host_id=host_id,
            class_id=class_id,
            id=id,
            name_regex=name_regex,
            vendor_id=vendor_id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetClassId")
    def reset_class_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClassId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNameRegex")
    def reset_name_regex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNameRegex", []))

    @jsii.member(jsii_name="resetVendorId")
    def reset_vendor_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVendorId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="classIdInput")
    def class_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "classIdInput"))

    @builtins.property
    @jsii.member(jsii_name="hostIdInput")
    def host_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameRegexInput")
    def name_regex_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameRegexInput"))

    @builtins.property
    @jsii.member(jsii_name="vendorIdInput")
    def vendor_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vendorIdInput"))

    @builtins.property
    @jsii.member(jsii_name="classId")
    def class_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "classId"))

    @class_id.setter
    def class_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereHostPciDevice, "class_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "classId", value)

    @builtins.property
    @jsii.member(jsii_name="hostId")
    def host_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostId"))

    @host_id.setter
    def host_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereHostPciDevice, "host_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereHostPciDevice, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="nameRegex")
    def name_regex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nameRegex"))

    @name_regex.setter
    def name_regex(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereHostPciDevice, "name_regex").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nameRegex", value)

    @builtins.property
    @jsii.member(jsii_name="vendorId")
    def vendor_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vendorId"))

    @vendor_id.setter
    def vendor_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereHostPciDevice, "vendor_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vendorId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vsphere.dataVsphereHostPciDevice.DataVsphereHostPciDeviceConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "host_id": "hostId",
        "class_id": "classId",
        "id": "id",
        "name_regex": "nameRegex",
        "vendor_id": "vendorId",
    },
)
class DataVsphereHostPciDeviceConfig(cdktf.TerraformMetaArguments):
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
        host_id: builtins.str,
        class_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        name_regex: typing.Optional[builtins.str] = None,
        vendor_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param host_id: The Managed Object ID of the host system. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/host_pci_device#host_id DataVsphereHostPciDevice#host_id}
        :param class_id: The hexadecimal value of the PCI device's class ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/host_pci_device#class_id DataVsphereHostPciDevice#class_id}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/host_pci_device#id DataVsphereHostPciDevice#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name_regex: A regular expression used to match the PCI device name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/host_pci_device#name_regex DataVsphereHostPciDevice#name_regex}
        :param vendor_id: The hexadecimal value of the PCI device's vendor ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/host_pci_device#vendor_id DataVsphereHostPciDevice#vendor_id}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataVsphereHostPciDeviceConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument host_id", value=host_id, expected_type=type_hints["host_id"])
            check_type(argname="argument class_id", value=class_id, expected_type=type_hints["class_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name_regex", value=name_regex, expected_type=type_hints["name_regex"])
            check_type(argname="argument vendor_id", value=vendor_id, expected_type=type_hints["vendor_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "host_id": host_id,
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
        if class_id is not None:
            self._values["class_id"] = class_id
        if id is not None:
            self._values["id"] = id
        if name_regex is not None:
            self._values["name_regex"] = name_regex
        if vendor_id is not None:
            self._values["vendor_id"] = vendor_id

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
    def host_id(self) -> builtins.str:
        '''The Managed Object ID of the host system.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/host_pci_device#host_id DataVsphereHostPciDevice#host_id}
        '''
        result = self._values.get("host_id")
        assert result is not None, "Required property 'host_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def class_id(self) -> typing.Optional[builtins.str]:
        '''The hexadecimal value of the PCI device's class ID.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/host_pci_device#class_id DataVsphereHostPciDevice#class_id}
        '''
        result = self._values.get("class_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/host_pci_device#id DataVsphereHostPciDevice#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name_regex(self) -> typing.Optional[builtins.str]:
        '''A regular expression used to match the PCI device name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/host_pci_device#name_regex DataVsphereHostPciDevice#name_regex}
        '''
        result = self._values.get("name_regex")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vendor_id(self) -> typing.Optional[builtins.str]:
        '''The hexadecimal value of the PCI device's vendor ID.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/host_pci_device#vendor_id DataVsphereHostPciDevice#vendor_id}
        '''
        result = self._values.get("vendor_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataVsphereHostPciDeviceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DataVsphereHostPciDevice",
    "DataVsphereHostPciDeviceConfig",
]

publication.publish()
