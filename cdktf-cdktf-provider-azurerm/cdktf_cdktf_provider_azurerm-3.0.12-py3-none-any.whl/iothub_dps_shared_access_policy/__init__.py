'''
# `azurerm_iothub_dps_shared_access_policy`

Refer to the Terraform Registory for docs: [`azurerm_iothub_dps_shared_access_policy`](https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy).
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


class IothubDpsSharedAccessPolicy(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.iothubDpsSharedAccessPolicy.IothubDpsSharedAccessPolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy azurerm_iothub_dps_shared_access_policy}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        iothub_dps_name: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        enrollment_read: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enrollment_write: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        registration_read: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        registration_write: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        service_config: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["IothubDpsSharedAccessPolicyTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy azurerm_iothub_dps_shared_access_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param iothub_dps_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#iothub_dps_name IothubDpsSharedAccessPolicy#iothub_dps_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#name IothubDpsSharedAccessPolicy#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#resource_group_name IothubDpsSharedAccessPolicy#resource_group_name}.
        :param enrollment_read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#enrollment_read IothubDpsSharedAccessPolicy#enrollment_read}.
        :param enrollment_write: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#enrollment_write IothubDpsSharedAccessPolicy#enrollment_write}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#id IothubDpsSharedAccessPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param registration_read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#registration_read IothubDpsSharedAccessPolicy#registration_read}.
        :param registration_write: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#registration_write IothubDpsSharedAccessPolicy#registration_write}.
        :param service_config: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#service_config IothubDpsSharedAccessPolicy#service_config}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#timeouts IothubDpsSharedAccessPolicy#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IothubDpsSharedAccessPolicy.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = IothubDpsSharedAccessPolicyConfig(
            iothub_dps_name=iothub_dps_name,
            name=name,
            resource_group_name=resource_group_name,
            enrollment_read=enrollment_read,
            enrollment_write=enrollment_write,
            id=id,
            registration_read=registration_read,
            registration_write=registration_write,
            service_config=service_config,
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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#create IothubDpsSharedAccessPolicy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#delete IothubDpsSharedAccessPolicy#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#read IothubDpsSharedAccessPolicy#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#update IothubDpsSharedAccessPolicy#update}.
        '''
        value = IothubDpsSharedAccessPolicyTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetEnrollmentRead")
    def reset_enrollment_read(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnrollmentRead", []))

    @jsii.member(jsii_name="resetEnrollmentWrite")
    def reset_enrollment_write(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnrollmentWrite", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetRegistrationRead")
    def reset_registration_read(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegistrationRead", []))

    @jsii.member(jsii_name="resetRegistrationWrite")
    def reset_registration_write(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegistrationWrite", []))

    @jsii.member(jsii_name="resetServiceConfig")
    def reset_service_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceConfig", []))

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
    @jsii.member(jsii_name="primaryConnectionString")
    def primary_connection_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryConnectionString"))

    @builtins.property
    @jsii.member(jsii_name="primaryKey")
    def primary_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryKey"))

    @builtins.property
    @jsii.member(jsii_name="secondaryConnectionString")
    def secondary_connection_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondaryConnectionString"))

    @builtins.property
    @jsii.member(jsii_name="secondaryKey")
    def secondary_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondaryKey"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "IothubDpsSharedAccessPolicyTimeoutsOutputReference":
        return typing.cast("IothubDpsSharedAccessPolicyTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="enrollmentReadInput")
    def enrollment_read_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enrollmentReadInput"))

    @builtins.property
    @jsii.member(jsii_name="enrollmentWriteInput")
    def enrollment_write_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enrollmentWriteInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="iothubDpsNameInput")
    def iothub_dps_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iothubDpsNameInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="registrationReadInput")
    def registration_read_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "registrationReadInput"))

    @builtins.property
    @jsii.member(jsii_name="registrationWriteInput")
    def registration_write_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "registrationWriteInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceConfigInput")
    def service_config_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "serviceConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["IothubDpsSharedAccessPolicyTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["IothubDpsSharedAccessPolicyTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="enrollmentRead")
    def enrollment_read(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enrollmentRead"))

    @enrollment_read.setter
    def enrollment_read(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDpsSharedAccessPolicy, "enrollment_read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enrollmentRead", value)

    @builtins.property
    @jsii.member(jsii_name="enrollmentWrite")
    def enrollment_write(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enrollmentWrite"))

    @enrollment_write.setter
    def enrollment_write(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDpsSharedAccessPolicy, "enrollment_write").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enrollmentWrite", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDpsSharedAccessPolicy, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="iothubDpsName")
    def iothub_dps_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iothubDpsName"))

    @iothub_dps_name.setter
    def iothub_dps_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDpsSharedAccessPolicy, "iothub_dps_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iothubDpsName", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDpsSharedAccessPolicy, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="registrationRead")
    def registration_read(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "registrationRead"))

    @registration_read.setter
    def registration_read(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDpsSharedAccessPolicy, "registration_read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registrationRead", value)

    @builtins.property
    @jsii.member(jsii_name="registrationWrite")
    def registration_write(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "registrationWrite"))

    @registration_write.setter
    def registration_write(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDpsSharedAccessPolicy, "registration_write").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registrationWrite", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDpsSharedAccessPolicy, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="serviceConfig")
    def service_config(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "serviceConfig"))

    @service_config.setter
    def service_config(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDpsSharedAccessPolicy, "service_config").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceConfig", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.iothubDpsSharedAccessPolicy.IothubDpsSharedAccessPolicyConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "iothub_dps_name": "iothubDpsName",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "enrollment_read": "enrollmentRead",
        "enrollment_write": "enrollmentWrite",
        "id": "id",
        "registration_read": "registrationRead",
        "registration_write": "registrationWrite",
        "service_config": "serviceConfig",
        "timeouts": "timeouts",
    },
)
class IothubDpsSharedAccessPolicyConfig(cdktf.TerraformMetaArguments):
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
        iothub_dps_name: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        enrollment_read: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enrollment_write: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        registration_read: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        registration_write: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        service_config: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["IothubDpsSharedAccessPolicyTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param iothub_dps_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#iothub_dps_name IothubDpsSharedAccessPolicy#iothub_dps_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#name IothubDpsSharedAccessPolicy#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#resource_group_name IothubDpsSharedAccessPolicy#resource_group_name}.
        :param enrollment_read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#enrollment_read IothubDpsSharedAccessPolicy#enrollment_read}.
        :param enrollment_write: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#enrollment_write IothubDpsSharedAccessPolicy#enrollment_write}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#id IothubDpsSharedAccessPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param registration_read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#registration_read IothubDpsSharedAccessPolicy#registration_read}.
        :param registration_write: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#registration_write IothubDpsSharedAccessPolicy#registration_write}.
        :param service_config: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#service_config IothubDpsSharedAccessPolicy#service_config}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#timeouts IothubDpsSharedAccessPolicy#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = IothubDpsSharedAccessPolicyTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(IothubDpsSharedAccessPolicyConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument iothub_dps_name", value=iothub_dps_name, expected_type=type_hints["iothub_dps_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument enrollment_read", value=enrollment_read, expected_type=type_hints["enrollment_read"])
            check_type(argname="argument enrollment_write", value=enrollment_write, expected_type=type_hints["enrollment_write"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument registration_read", value=registration_read, expected_type=type_hints["registration_read"])
            check_type(argname="argument registration_write", value=registration_write, expected_type=type_hints["registration_write"])
            check_type(argname="argument service_config", value=service_config, expected_type=type_hints["service_config"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "iothub_dps_name": iothub_dps_name,
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
        if enrollment_read is not None:
            self._values["enrollment_read"] = enrollment_read
        if enrollment_write is not None:
            self._values["enrollment_write"] = enrollment_write
        if id is not None:
            self._values["id"] = id
        if registration_read is not None:
            self._values["registration_read"] = registration_read
        if registration_write is not None:
            self._values["registration_write"] = registration_write
        if service_config is not None:
            self._values["service_config"] = service_config
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
    def iothub_dps_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#iothub_dps_name IothubDpsSharedAccessPolicy#iothub_dps_name}.'''
        result = self._values.get("iothub_dps_name")
        assert result is not None, "Required property 'iothub_dps_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#name IothubDpsSharedAccessPolicy#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#resource_group_name IothubDpsSharedAccessPolicy#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enrollment_read(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#enrollment_read IothubDpsSharedAccessPolicy#enrollment_read}.'''
        result = self._values.get("enrollment_read")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enrollment_write(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#enrollment_write IothubDpsSharedAccessPolicy#enrollment_write}.'''
        result = self._values.get("enrollment_write")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#id IothubDpsSharedAccessPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def registration_read(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#registration_read IothubDpsSharedAccessPolicy#registration_read}.'''
        result = self._values.get("registration_read")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def registration_write(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#registration_write IothubDpsSharedAccessPolicy#registration_write}.'''
        result = self._values.get("registration_write")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def service_config(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#service_config IothubDpsSharedAccessPolicy#service_config}.'''
        result = self._values.get("service_config")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["IothubDpsSharedAccessPolicyTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#timeouts IothubDpsSharedAccessPolicy#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["IothubDpsSharedAccessPolicyTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IothubDpsSharedAccessPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.iothubDpsSharedAccessPolicy.IothubDpsSharedAccessPolicyTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class IothubDpsSharedAccessPolicyTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#create IothubDpsSharedAccessPolicy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#delete IothubDpsSharedAccessPolicy#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#read IothubDpsSharedAccessPolicy#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#update IothubDpsSharedAccessPolicy#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IothubDpsSharedAccessPolicyTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#create IothubDpsSharedAccessPolicy#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#delete IothubDpsSharedAccessPolicy#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#read IothubDpsSharedAccessPolicy#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iothub_dps_shared_access_policy#update IothubDpsSharedAccessPolicy#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IothubDpsSharedAccessPolicyTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IothubDpsSharedAccessPolicyTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.iothubDpsSharedAccessPolicy.IothubDpsSharedAccessPolicyTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(IothubDpsSharedAccessPolicyTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(IothubDpsSharedAccessPolicyTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDpsSharedAccessPolicyTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDpsSharedAccessPolicyTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDpsSharedAccessPolicyTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IothubDpsSharedAccessPolicyTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IothubDpsSharedAccessPolicyTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IothubDpsSharedAccessPolicyTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IothubDpsSharedAccessPolicyTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "IothubDpsSharedAccessPolicy",
    "IothubDpsSharedAccessPolicyConfig",
    "IothubDpsSharedAccessPolicyTimeouts",
    "IothubDpsSharedAccessPolicyTimeoutsOutputReference",
]

publication.publish()
