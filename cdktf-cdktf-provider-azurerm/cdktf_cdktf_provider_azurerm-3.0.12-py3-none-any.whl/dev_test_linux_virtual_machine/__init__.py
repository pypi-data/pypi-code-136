'''
# `azurerm_dev_test_linux_virtual_machine`

Refer to the Terraform Registory for docs: [`azurerm_dev_test_linux_virtual_machine`](https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine).
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


class DevTestLinuxVirtualMachine(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.devTestLinuxVirtualMachine.DevTestLinuxVirtualMachine",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine azurerm_dev_test_linux_virtual_machine}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        gallery_image_reference: typing.Union["DevTestLinuxVirtualMachineGalleryImageReference", typing.Dict[str, typing.Any]],
        lab_name: builtins.str,
        lab_subnet_name: builtins.str,
        lab_virtual_network_id: builtins.str,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        size: builtins.str,
        storage_type: builtins.str,
        username: builtins.str,
        allow_claim: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        disallow_public_ip_address: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        inbound_nat_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DevTestLinuxVirtualMachineInboundNatRule", typing.Dict[str, typing.Any]]]]] = None,
        notes: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        ssh_key: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["DevTestLinuxVirtualMachineTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine azurerm_dev_test_linux_virtual_machine} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param gallery_image_reference: gallery_image_reference block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#gallery_image_reference DevTestLinuxVirtualMachine#gallery_image_reference}
        :param lab_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#lab_name DevTestLinuxVirtualMachine#lab_name}.
        :param lab_subnet_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#lab_subnet_name DevTestLinuxVirtualMachine#lab_subnet_name}.
        :param lab_virtual_network_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#lab_virtual_network_id DevTestLinuxVirtualMachine#lab_virtual_network_id}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#location DevTestLinuxVirtualMachine#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#name DevTestLinuxVirtualMachine#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#resource_group_name DevTestLinuxVirtualMachine#resource_group_name}.
        :param size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#size DevTestLinuxVirtualMachine#size}.
        :param storage_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#storage_type DevTestLinuxVirtualMachine#storage_type}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#username DevTestLinuxVirtualMachine#username}.
        :param allow_claim: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#allow_claim DevTestLinuxVirtualMachine#allow_claim}.
        :param disallow_public_ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#disallow_public_ip_address DevTestLinuxVirtualMachine#disallow_public_ip_address}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#id DevTestLinuxVirtualMachine#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param inbound_nat_rule: inbound_nat_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#inbound_nat_rule DevTestLinuxVirtualMachine#inbound_nat_rule}
        :param notes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#notes DevTestLinuxVirtualMachine#notes}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#password DevTestLinuxVirtualMachine#password}.
        :param ssh_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#ssh_key DevTestLinuxVirtualMachine#ssh_key}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#tags DevTestLinuxVirtualMachine#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#timeouts DevTestLinuxVirtualMachine#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DevTestLinuxVirtualMachine.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DevTestLinuxVirtualMachineConfig(
            gallery_image_reference=gallery_image_reference,
            lab_name=lab_name,
            lab_subnet_name=lab_subnet_name,
            lab_virtual_network_id=lab_virtual_network_id,
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            size=size,
            storage_type=storage_type,
            username=username,
            allow_claim=allow_claim,
            disallow_public_ip_address=disallow_public_ip_address,
            id=id,
            inbound_nat_rule=inbound_nat_rule,
            notes=notes,
            password=password,
            ssh_key=ssh_key,
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

    @jsii.member(jsii_name="putGalleryImageReference")
    def put_gallery_image_reference(
        self,
        *,
        offer: builtins.str,
        publisher: builtins.str,
        sku: builtins.str,
        version: builtins.str,
    ) -> None:
        '''
        :param offer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#offer DevTestLinuxVirtualMachine#offer}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#publisher DevTestLinuxVirtualMachine#publisher}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#sku DevTestLinuxVirtualMachine#sku}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#version DevTestLinuxVirtualMachine#version}.
        '''
        value = DevTestLinuxVirtualMachineGalleryImageReference(
            offer=offer, publisher=publisher, sku=sku, version=version
        )

        return typing.cast(None, jsii.invoke(self, "putGalleryImageReference", [value]))

    @jsii.member(jsii_name="putInboundNatRule")
    def put_inbound_nat_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DevTestLinuxVirtualMachineInboundNatRule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DevTestLinuxVirtualMachine.put_inbound_nat_rule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInboundNatRule", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#create DevTestLinuxVirtualMachine#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#delete DevTestLinuxVirtualMachine#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#read DevTestLinuxVirtualMachine#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#update DevTestLinuxVirtualMachine#update}.
        '''
        value = DevTestLinuxVirtualMachineTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAllowClaim")
    def reset_allow_claim(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowClaim", []))

    @jsii.member(jsii_name="resetDisallowPublicIpAddress")
    def reset_disallow_public_ip_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisallowPublicIpAddress", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInboundNatRule")
    def reset_inbound_nat_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInboundNatRule", []))

    @jsii.member(jsii_name="resetNotes")
    def reset_notes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotes", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetSshKey")
    def reset_ssh_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSshKey", []))

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
    @jsii.member(jsii_name="fqdn")
    def fqdn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fqdn"))

    @builtins.property
    @jsii.member(jsii_name="galleryImageReference")
    def gallery_image_reference(
        self,
    ) -> "DevTestLinuxVirtualMachineGalleryImageReferenceOutputReference":
        return typing.cast("DevTestLinuxVirtualMachineGalleryImageReferenceOutputReference", jsii.get(self, "galleryImageReference"))

    @builtins.property
    @jsii.member(jsii_name="inboundNatRule")
    def inbound_nat_rule(self) -> "DevTestLinuxVirtualMachineInboundNatRuleList":
        return typing.cast("DevTestLinuxVirtualMachineInboundNatRuleList", jsii.get(self, "inboundNatRule"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "DevTestLinuxVirtualMachineTimeoutsOutputReference":
        return typing.cast("DevTestLinuxVirtualMachineTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="uniqueIdentifier")
    def unique_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uniqueIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="allowClaimInput")
    def allow_claim_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowClaimInput"))

    @builtins.property
    @jsii.member(jsii_name="disallowPublicIpAddressInput")
    def disallow_public_ip_address_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disallowPublicIpAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="galleryImageReferenceInput")
    def gallery_image_reference_input(
        self,
    ) -> typing.Optional["DevTestLinuxVirtualMachineGalleryImageReference"]:
        return typing.cast(typing.Optional["DevTestLinuxVirtualMachineGalleryImageReference"], jsii.get(self, "galleryImageReferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="inboundNatRuleInput")
    def inbound_nat_rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DevTestLinuxVirtualMachineInboundNatRule"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DevTestLinuxVirtualMachineInboundNatRule"]]], jsii.get(self, "inboundNatRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="labNameInput")
    def lab_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "labNameInput"))

    @builtins.property
    @jsii.member(jsii_name="labSubnetNameInput")
    def lab_subnet_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "labSubnetNameInput"))

    @builtins.property
    @jsii.member(jsii_name="labVirtualNetworkIdInput")
    def lab_virtual_network_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "labVirtualNetworkIdInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="notesInput")
    def notes_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notesInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeInput")
    def size_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sizeInput"))

    @builtins.property
    @jsii.member(jsii_name="sshKeyInput")
    def ssh_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sshKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="storageTypeInput")
    def storage_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["DevTestLinuxVirtualMachineTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DevTestLinuxVirtualMachineTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="allowClaim")
    def allow_claim(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowClaim"))

    @allow_claim.setter
    def allow_claim(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevTestLinuxVirtualMachine, "allow_claim").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowClaim", value)

    @builtins.property
    @jsii.member(jsii_name="disallowPublicIpAddress")
    def disallow_public_ip_address(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disallowPublicIpAddress"))

    @disallow_public_ip_address.setter
    def disallow_public_ip_address(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevTestLinuxVirtualMachine, "disallow_public_ip_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disallowPublicIpAddress", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevTestLinuxVirtualMachine, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="labName")
    def lab_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "labName"))

    @lab_name.setter
    def lab_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevTestLinuxVirtualMachine, "lab_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labName", value)

    @builtins.property
    @jsii.member(jsii_name="labSubnetName")
    def lab_subnet_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "labSubnetName"))

    @lab_subnet_name.setter
    def lab_subnet_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevTestLinuxVirtualMachine, "lab_subnet_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labSubnetName", value)

    @builtins.property
    @jsii.member(jsii_name="labVirtualNetworkId")
    def lab_virtual_network_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "labVirtualNetworkId"))

    @lab_virtual_network_id.setter
    def lab_virtual_network_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevTestLinuxVirtualMachine, "lab_virtual_network_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labVirtualNetworkId", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevTestLinuxVirtualMachine, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevTestLinuxVirtualMachine, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="notes")
    def notes(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notes"))

    @notes.setter
    def notes(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevTestLinuxVirtualMachine, "notes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notes", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevTestLinuxVirtualMachine, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevTestLinuxVirtualMachine, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "size"))

    @size.setter
    def size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevTestLinuxVirtualMachine, "size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "size", value)

    @builtins.property
    @jsii.member(jsii_name="sshKey")
    def ssh_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sshKey"))

    @ssh_key.setter
    def ssh_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevTestLinuxVirtualMachine, "ssh_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sshKey", value)

    @builtins.property
    @jsii.member(jsii_name="storageType")
    def storage_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageType"))

    @storage_type.setter
    def storage_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevTestLinuxVirtualMachine, "storage_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageType", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevTestLinuxVirtualMachine, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevTestLinuxVirtualMachine, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.devTestLinuxVirtualMachine.DevTestLinuxVirtualMachineConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "gallery_image_reference": "galleryImageReference",
        "lab_name": "labName",
        "lab_subnet_name": "labSubnetName",
        "lab_virtual_network_id": "labVirtualNetworkId",
        "location": "location",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "size": "size",
        "storage_type": "storageType",
        "username": "username",
        "allow_claim": "allowClaim",
        "disallow_public_ip_address": "disallowPublicIpAddress",
        "id": "id",
        "inbound_nat_rule": "inboundNatRule",
        "notes": "notes",
        "password": "password",
        "ssh_key": "sshKey",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class DevTestLinuxVirtualMachineConfig(cdktf.TerraformMetaArguments):
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
        gallery_image_reference: typing.Union["DevTestLinuxVirtualMachineGalleryImageReference", typing.Dict[str, typing.Any]],
        lab_name: builtins.str,
        lab_subnet_name: builtins.str,
        lab_virtual_network_id: builtins.str,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        size: builtins.str,
        storage_type: builtins.str,
        username: builtins.str,
        allow_claim: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        disallow_public_ip_address: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        inbound_nat_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DevTestLinuxVirtualMachineInboundNatRule", typing.Dict[str, typing.Any]]]]] = None,
        notes: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        ssh_key: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["DevTestLinuxVirtualMachineTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param gallery_image_reference: gallery_image_reference block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#gallery_image_reference DevTestLinuxVirtualMachine#gallery_image_reference}
        :param lab_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#lab_name DevTestLinuxVirtualMachine#lab_name}.
        :param lab_subnet_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#lab_subnet_name DevTestLinuxVirtualMachine#lab_subnet_name}.
        :param lab_virtual_network_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#lab_virtual_network_id DevTestLinuxVirtualMachine#lab_virtual_network_id}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#location DevTestLinuxVirtualMachine#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#name DevTestLinuxVirtualMachine#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#resource_group_name DevTestLinuxVirtualMachine#resource_group_name}.
        :param size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#size DevTestLinuxVirtualMachine#size}.
        :param storage_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#storage_type DevTestLinuxVirtualMachine#storage_type}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#username DevTestLinuxVirtualMachine#username}.
        :param allow_claim: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#allow_claim DevTestLinuxVirtualMachine#allow_claim}.
        :param disallow_public_ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#disallow_public_ip_address DevTestLinuxVirtualMachine#disallow_public_ip_address}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#id DevTestLinuxVirtualMachine#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param inbound_nat_rule: inbound_nat_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#inbound_nat_rule DevTestLinuxVirtualMachine#inbound_nat_rule}
        :param notes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#notes DevTestLinuxVirtualMachine#notes}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#password DevTestLinuxVirtualMachine#password}.
        :param ssh_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#ssh_key DevTestLinuxVirtualMachine#ssh_key}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#tags DevTestLinuxVirtualMachine#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#timeouts DevTestLinuxVirtualMachine#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(gallery_image_reference, dict):
            gallery_image_reference = DevTestLinuxVirtualMachineGalleryImageReference(**gallery_image_reference)
        if isinstance(timeouts, dict):
            timeouts = DevTestLinuxVirtualMachineTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(DevTestLinuxVirtualMachineConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument gallery_image_reference", value=gallery_image_reference, expected_type=type_hints["gallery_image_reference"])
            check_type(argname="argument lab_name", value=lab_name, expected_type=type_hints["lab_name"])
            check_type(argname="argument lab_subnet_name", value=lab_subnet_name, expected_type=type_hints["lab_subnet_name"])
            check_type(argname="argument lab_virtual_network_id", value=lab_virtual_network_id, expected_type=type_hints["lab_virtual_network_id"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument size", value=size, expected_type=type_hints["size"])
            check_type(argname="argument storage_type", value=storage_type, expected_type=type_hints["storage_type"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument allow_claim", value=allow_claim, expected_type=type_hints["allow_claim"])
            check_type(argname="argument disallow_public_ip_address", value=disallow_public_ip_address, expected_type=type_hints["disallow_public_ip_address"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument inbound_nat_rule", value=inbound_nat_rule, expected_type=type_hints["inbound_nat_rule"])
            check_type(argname="argument notes", value=notes, expected_type=type_hints["notes"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument ssh_key", value=ssh_key, expected_type=type_hints["ssh_key"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "gallery_image_reference": gallery_image_reference,
            "lab_name": lab_name,
            "lab_subnet_name": lab_subnet_name,
            "lab_virtual_network_id": lab_virtual_network_id,
            "location": location,
            "name": name,
            "resource_group_name": resource_group_name,
            "size": size,
            "storage_type": storage_type,
            "username": username,
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
        if allow_claim is not None:
            self._values["allow_claim"] = allow_claim
        if disallow_public_ip_address is not None:
            self._values["disallow_public_ip_address"] = disallow_public_ip_address
        if id is not None:
            self._values["id"] = id
        if inbound_nat_rule is not None:
            self._values["inbound_nat_rule"] = inbound_nat_rule
        if notes is not None:
            self._values["notes"] = notes
        if password is not None:
            self._values["password"] = password
        if ssh_key is not None:
            self._values["ssh_key"] = ssh_key
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
    def gallery_image_reference(
        self,
    ) -> "DevTestLinuxVirtualMachineGalleryImageReference":
        '''gallery_image_reference block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#gallery_image_reference DevTestLinuxVirtualMachine#gallery_image_reference}
        '''
        result = self._values.get("gallery_image_reference")
        assert result is not None, "Required property 'gallery_image_reference' is missing"
        return typing.cast("DevTestLinuxVirtualMachineGalleryImageReference", result)

    @builtins.property
    def lab_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#lab_name DevTestLinuxVirtualMachine#lab_name}.'''
        result = self._values.get("lab_name")
        assert result is not None, "Required property 'lab_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lab_subnet_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#lab_subnet_name DevTestLinuxVirtualMachine#lab_subnet_name}.'''
        result = self._values.get("lab_subnet_name")
        assert result is not None, "Required property 'lab_subnet_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lab_virtual_network_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#lab_virtual_network_id DevTestLinuxVirtualMachine#lab_virtual_network_id}.'''
        result = self._values.get("lab_virtual_network_id")
        assert result is not None, "Required property 'lab_virtual_network_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#location DevTestLinuxVirtualMachine#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#name DevTestLinuxVirtualMachine#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#resource_group_name DevTestLinuxVirtualMachine#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def size(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#size DevTestLinuxVirtualMachine#size}.'''
        result = self._values.get("size")
        assert result is not None, "Required property 'size' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#storage_type DevTestLinuxVirtualMachine#storage_type}.'''
        result = self._values.get("storage_type")
        assert result is not None, "Required property 'storage_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#username DevTestLinuxVirtualMachine#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_claim(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#allow_claim DevTestLinuxVirtualMachine#allow_claim}.'''
        result = self._values.get("allow_claim")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def disallow_public_ip_address(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#disallow_public_ip_address DevTestLinuxVirtualMachine#disallow_public_ip_address}.'''
        result = self._values.get("disallow_public_ip_address")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#id DevTestLinuxVirtualMachine#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def inbound_nat_rule(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DevTestLinuxVirtualMachineInboundNatRule"]]]:
        '''inbound_nat_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#inbound_nat_rule DevTestLinuxVirtualMachine#inbound_nat_rule}
        '''
        result = self._values.get("inbound_nat_rule")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DevTestLinuxVirtualMachineInboundNatRule"]]], result)

    @builtins.property
    def notes(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#notes DevTestLinuxVirtualMachine#notes}.'''
        result = self._values.get("notes")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#password DevTestLinuxVirtualMachine#password}.'''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssh_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#ssh_key DevTestLinuxVirtualMachine#ssh_key}.'''
        result = self._values.get("ssh_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#tags DevTestLinuxVirtualMachine#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DevTestLinuxVirtualMachineTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#timeouts DevTestLinuxVirtualMachine#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DevTestLinuxVirtualMachineTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DevTestLinuxVirtualMachineConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.devTestLinuxVirtualMachine.DevTestLinuxVirtualMachineGalleryImageReference",
    jsii_struct_bases=[],
    name_mapping={
        "offer": "offer",
        "publisher": "publisher",
        "sku": "sku",
        "version": "version",
    },
)
class DevTestLinuxVirtualMachineGalleryImageReference:
    def __init__(
        self,
        *,
        offer: builtins.str,
        publisher: builtins.str,
        sku: builtins.str,
        version: builtins.str,
    ) -> None:
        '''
        :param offer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#offer DevTestLinuxVirtualMachine#offer}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#publisher DevTestLinuxVirtualMachine#publisher}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#sku DevTestLinuxVirtualMachine#sku}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#version DevTestLinuxVirtualMachine#version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DevTestLinuxVirtualMachineGalleryImageReference.__init__)
            check_type(argname="argument offer", value=offer, expected_type=type_hints["offer"])
            check_type(argname="argument publisher", value=publisher, expected_type=type_hints["publisher"])
            check_type(argname="argument sku", value=sku, expected_type=type_hints["sku"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[str, typing.Any] = {
            "offer": offer,
            "publisher": publisher,
            "sku": sku,
            "version": version,
        }

    @builtins.property
    def offer(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#offer DevTestLinuxVirtualMachine#offer}.'''
        result = self._values.get("offer")
        assert result is not None, "Required property 'offer' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def publisher(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#publisher DevTestLinuxVirtualMachine#publisher}.'''
        result = self._values.get("publisher")
        assert result is not None, "Required property 'publisher' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sku(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#sku DevTestLinuxVirtualMachine#sku}.'''
        result = self._values.get("sku")
        assert result is not None, "Required property 'sku' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#version DevTestLinuxVirtualMachine#version}.'''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DevTestLinuxVirtualMachineGalleryImageReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DevTestLinuxVirtualMachineGalleryImageReferenceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.devTestLinuxVirtualMachine.DevTestLinuxVirtualMachineGalleryImageReferenceOutputReference",
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
            type_hints = typing.get_type_hints(DevTestLinuxVirtualMachineGalleryImageReferenceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="offerInput")
    def offer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "offerInput"))

    @builtins.property
    @jsii.member(jsii_name="publisherInput")
    def publisher_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publisherInput"))

    @builtins.property
    @jsii.member(jsii_name="skuInput")
    def sku_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "skuInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="offer")
    def offer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "offer"))

    @offer.setter
    def offer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevTestLinuxVirtualMachineGalleryImageReferenceOutputReference, "offer").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "offer", value)

    @builtins.property
    @jsii.member(jsii_name="publisher")
    def publisher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publisher"))

    @publisher.setter
    def publisher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevTestLinuxVirtualMachineGalleryImageReferenceOutputReference, "publisher").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publisher", value)

    @builtins.property
    @jsii.member(jsii_name="sku")
    def sku(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sku"))

    @sku.setter
    def sku(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevTestLinuxVirtualMachineGalleryImageReferenceOutputReference, "sku").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sku", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevTestLinuxVirtualMachineGalleryImageReferenceOutputReference, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DevTestLinuxVirtualMachineGalleryImageReference]:
        return typing.cast(typing.Optional[DevTestLinuxVirtualMachineGalleryImageReference], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DevTestLinuxVirtualMachineGalleryImageReference],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevTestLinuxVirtualMachineGalleryImageReferenceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.devTestLinuxVirtualMachine.DevTestLinuxVirtualMachineInboundNatRule",
    jsii_struct_bases=[],
    name_mapping={"backend_port": "backendPort", "protocol": "protocol"},
)
class DevTestLinuxVirtualMachineInboundNatRule:
    def __init__(self, *, backend_port: jsii.Number, protocol: builtins.str) -> None:
        '''
        :param backend_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#backend_port DevTestLinuxVirtualMachine#backend_port}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#protocol DevTestLinuxVirtualMachine#protocol}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DevTestLinuxVirtualMachineInboundNatRule.__init__)
            check_type(argname="argument backend_port", value=backend_port, expected_type=type_hints["backend_port"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
        self._values: typing.Dict[str, typing.Any] = {
            "backend_port": backend_port,
            "protocol": protocol,
        }

    @builtins.property
    def backend_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#backend_port DevTestLinuxVirtualMachine#backend_port}.'''
        result = self._values.get("backend_port")
        assert result is not None, "Required property 'backend_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#protocol DevTestLinuxVirtualMachine#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DevTestLinuxVirtualMachineInboundNatRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DevTestLinuxVirtualMachineInboundNatRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.devTestLinuxVirtualMachine.DevTestLinuxVirtualMachineInboundNatRuleList",
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
            type_hints = typing.get_type_hints(DevTestLinuxVirtualMachineInboundNatRuleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DevTestLinuxVirtualMachineInboundNatRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DevTestLinuxVirtualMachineInboundNatRuleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DevTestLinuxVirtualMachineInboundNatRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevTestLinuxVirtualMachineInboundNatRuleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DevTestLinuxVirtualMachineInboundNatRuleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DevTestLinuxVirtualMachineInboundNatRuleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DevTestLinuxVirtualMachineInboundNatRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DevTestLinuxVirtualMachineInboundNatRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DevTestLinuxVirtualMachineInboundNatRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevTestLinuxVirtualMachineInboundNatRuleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DevTestLinuxVirtualMachineInboundNatRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.devTestLinuxVirtualMachine.DevTestLinuxVirtualMachineInboundNatRuleOutputReference",
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
            type_hints = typing.get_type_hints(DevTestLinuxVirtualMachineInboundNatRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="frontendPort")
    def frontend_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "frontendPort"))

    @builtins.property
    @jsii.member(jsii_name="backendPortInput")
    def backend_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "backendPortInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="backendPort")
    def backend_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "backendPort"))

    @backend_port.setter
    def backend_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevTestLinuxVirtualMachineInboundNatRuleOutputReference, "backend_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backendPort", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevTestLinuxVirtualMachineInboundNatRuleOutputReference, "protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DevTestLinuxVirtualMachineInboundNatRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DevTestLinuxVirtualMachineInboundNatRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DevTestLinuxVirtualMachineInboundNatRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevTestLinuxVirtualMachineInboundNatRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.devTestLinuxVirtualMachine.DevTestLinuxVirtualMachineTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class DevTestLinuxVirtualMachineTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#create DevTestLinuxVirtualMachine#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#delete DevTestLinuxVirtualMachine#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#read DevTestLinuxVirtualMachine#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#update DevTestLinuxVirtualMachine#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DevTestLinuxVirtualMachineTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#create DevTestLinuxVirtualMachine#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#delete DevTestLinuxVirtualMachine#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#read DevTestLinuxVirtualMachine#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine#update DevTestLinuxVirtualMachine#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DevTestLinuxVirtualMachineTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DevTestLinuxVirtualMachineTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.devTestLinuxVirtualMachine.DevTestLinuxVirtualMachineTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(DevTestLinuxVirtualMachineTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(DevTestLinuxVirtualMachineTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevTestLinuxVirtualMachineTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevTestLinuxVirtualMachineTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevTestLinuxVirtualMachineTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DevTestLinuxVirtualMachineTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DevTestLinuxVirtualMachineTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DevTestLinuxVirtualMachineTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevTestLinuxVirtualMachineTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DevTestLinuxVirtualMachine",
    "DevTestLinuxVirtualMachineConfig",
    "DevTestLinuxVirtualMachineGalleryImageReference",
    "DevTestLinuxVirtualMachineGalleryImageReferenceOutputReference",
    "DevTestLinuxVirtualMachineInboundNatRule",
    "DevTestLinuxVirtualMachineInboundNatRuleList",
    "DevTestLinuxVirtualMachineInboundNatRuleOutputReference",
    "DevTestLinuxVirtualMachineTimeouts",
    "DevTestLinuxVirtualMachineTimeoutsOutputReference",
]

publication.publish()
