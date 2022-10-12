'''
# `google_apigee_instance`

Refer to the Terraform Registory for docs: [`google_apigee_instance`](https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance).
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


class GoogleApigeeInstance(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleApigeeInstance.GoogleApigeeInstance",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance google_apigee_instance}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        name: builtins.str,
        org_id: builtins.str,
        consumer_accept_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        disk_encryption_key_name: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        ip_range: typing.Optional[builtins.str] = None,
        peering_cidr_range: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleApigeeInstanceTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance google_apigee_instance} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: Required. Compute Engine location where the instance resides. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance#location GoogleApigeeInstance#location}
        :param name: Resource ID of the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance#name GoogleApigeeInstance#name}
        :param org_id: The Apigee Organization associated with the Apigee instance, in the format 'organizations/{{org_name}}'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance#org_id GoogleApigeeInstance#org_id}
        :param consumer_accept_list: Optional. Customer accept list represents the list of projects (id/number) on customer side that can privately connect to the service attachment. It is an optional field which the customers can provide during the instance creation. By default, the customer project associated with the Apigee organization will be included to the list. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance#consumer_accept_list GoogleApigeeInstance#consumer_accept_list}
        :param description: Description of the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance#description GoogleApigeeInstance#description}
        :param disk_encryption_key_name: Customer Managed Encryption Key (CMEK) used for disk and volume encryption. Required for Apigee paid subscriptions only. Use the following format: 'projects/([^/]+)/locations/([^/]+)/keyRings/([^/]+)/cryptoKeys/([^/]+)' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance#disk_encryption_key_name GoogleApigeeInstance#disk_encryption_key_name}
        :param display_name: Display name of the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance#display_name GoogleApigeeInstance#display_name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance#id GoogleApigeeInstance#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ip_range: IP range represents the customer-provided CIDR block of length 22 that will be used for the Apigee instance creation. This optional range, if provided, should be freely available as part of larger named range the customer has allocated to the Service Networking peering. If this is not provided, Apigee will automatically request for any available /22 CIDR block from Service Networking. The customer should use this CIDR block for configuring their firewall needs to allow traffic from Apigee. Input format: "a.b.c.d/22" Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance#ip_range GoogleApigeeInstance#ip_range}
        :param peering_cidr_range: The size of the CIDR block range that will be reserved by the instance. For valid values, see `CidrRange <https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances#CidrRange>`_ on the documentation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance#peering_cidr_range GoogleApigeeInstance#peering_cidr_range}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance#timeouts GoogleApigeeInstance#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleApigeeInstance.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleApigeeInstanceConfig(
            location=location,
            name=name,
            org_id=org_id,
            consumer_accept_list=consumer_accept_list,
            description=description,
            disk_encryption_key_name=disk_encryption_key_name,
            display_name=display_name,
            id=id,
            ip_range=ip_range,
            peering_cidr_range=peering_cidr_range,
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
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance#create GoogleApigeeInstance#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance#delete GoogleApigeeInstance#delete}.
        '''
        value = GoogleApigeeInstanceTimeouts(create=create, delete=delete)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetConsumerAcceptList")
    def reset_consumer_accept_list(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConsumerAcceptList", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDiskEncryptionKeyName")
    def reset_disk_encryption_key_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskEncryptionKeyName", []))

    @jsii.member(jsii_name="resetDisplayName")
    def reset_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayName", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIpRange")
    def reset_ip_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpRange", []))

    @jsii.member(jsii_name="resetPeeringCidrRange")
    def reset_peering_cidr_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPeeringCidrRange", []))

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
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "port"))

    @builtins.property
    @jsii.member(jsii_name="serviceAttachment")
    def service_attachment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAttachment"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleApigeeInstanceTimeoutsOutputReference":
        return typing.cast("GoogleApigeeInstanceTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="consumerAcceptListInput")
    def consumer_accept_list_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "consumerAcceptListInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionKeyNameInput")
    def disk_encryption_key_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "diskEncryptionKeyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ipRangeInput")
    def ip_range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="orgIdInput")
    def org_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "orgIdInput"))

    @builtins.property
    @jsii.member(jsii_name="peeringCidrRangeInput")
    def peering_cidr_range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "peeringCidrRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleApigeeInstanceTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleApigeeInstanceTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="consumerAcceptList")
    def consumer_accept_list(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "consumerAcceptList"))

    @consumer_accept_list.setter
    def consumer_accept_list(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApigeeInstance, "consumer_accept_list").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consumerAcceptList", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApigeeInstance, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionKeyName")
    def disk_encryption_key_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "diskEncryptionKeyName"))

    @disk_encryption_key_name.setter
    def disk_encryption_key_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApigeeInstance, "disk_encryption_key_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskEncryptionKeyName", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApigeeInstance, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApigeeInstance, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ipRange")
    def ip_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipRange"))

    @ip_range.setter
    def ip_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApigeeInstance, "ip_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipRange", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApigeeInstance, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApigeeInstance, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="orgId")
    def org_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "orgId"))

    @org_id.setter
    def org_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApigeeInstance, "org_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "orgId", value)

    @builtins.property
    @jsii.member(jsii_name="peeringCidrRange")
    def peering_cidr_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "peeringCidrRange"))

    @peering_cidr_range.setter
    def peering_cidr_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApigeeInstance, "peering_cidr_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "peeringCidrRange", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleApigeeInstance.GoogleApigeeInstanceConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "location": "location",
        "name": "name",
        "org_id": "orgId",
        "consumer_accept_list": "consumerAcceptList",
        "description": "description",
        "disk_encryption_key_name": "diskEncryptionKeyName",
        "display_name": "displayName",
        "id": "id",
        "ip_range": "ipRange",
        "peering_cidr_range": "peeringCidrRange",
        "timeouts": "timeouts",
    },
)
class GoogleApigeeInstanceConfig(cdktf.TerraformMetaArguments):
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
        location: builtins.str,
        name: builtins.str,
        org_id: builtins.str,
        consumer_accept_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        disk_encryption_key_name: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        ip_range: typing.Optional[builtins.str] = None,
        peering_cidr_range: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleApigeeInstanceTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: Required. Compute Engine location where the instance resides. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance#location GoogleApigeeInstance#location}
        :param name: Resource ID of the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance#name GoogleApigeeInstance#name}
        :param org_id: The Apigee Organization associated with the Apigee instance, in the format 'organizations/{{org_name}}'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance#org_id GoogleApigeeInstance#org_id}
        :param consumer_accept_list: Optional. Customer accept list represents the list of projects (id/number) on customer side that can privately connect to the service attachment. It is an optional field which the customers can provide during the instance creation. By default, the customer project associated with the Apigee organization will be included to the list. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance#consumer_accept_list GoogleApigeeInstance#consumer_accept_list}
        :param description: Description of the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance#description GoogleApigeeInstance#description}
        :param disk_encryption_key_name: Customer Managed Encryption Key (CMEK) used for disk and volume encryption. Required for Apigee paid subscriptions only. Use the following format: 'projects/([^/]+)/locations/([^/]+)/keyRings/([^/]+)/cryptoKeys/([^/]+)' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance#disk_encryption_key_name GoogleApigeeInstance#disk_encryption_key_name}
        :param display_name: Display name of the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance#display_name GoogleApigeeInstance#display_name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance#id GoogleApigeeInstance#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ip_range: IP range represents the customer-provided CIDR block of length 22 that will be used for the Apigee instance creation. This optional range, if provided, should be freely available as part of larger named range the customer has allocated to the Service Networking peering. If this is not provided, Apigee will automatically request for any available /22 CIDR block from Service Networking. The customer should use this CIDR block for configuring their firewall needs to allow traffic from Apigee. Input format: "a.b.c.d/22" Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance#ip_range GoogleApigeeInstance#ip_range}
        :param peering_cidr_range: The size of the CIDR block range that will be reserved by the instance. For valid values, see `CidrRange <https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances#CidrRange>`_ on the documentation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance#peering_cidr_range GoogleApigeeInstance#peering_cidr_range}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance#timeouts GoogleApigeeInstance#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = GoogleApigeeInstanceTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleApigeeInstanceConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument org_id", value=org_id, expected_type=type_hints["org_id"])
            check_type(argname="argument consumer_accept_list", value=consumer_accept_list, expected_type=type_hints["consumer_accept_list"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument disk_encryption_key_name", value=disk_encryption_key_name, expected_type=type_hints["disk_encryption_key_name"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ip_range", value=ip_range, expected_type=type_hints["ip_range"])
            check_type(argname="argument peering_cidr_range", value=peering_cidr_range, expected_type=type_hints["peering_cidr_range"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "location": location,
            "name": name,
            "org_id": org_id,
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
        if consumer_accept_list is not None:
            self._values["consumer_accept_list"] = consumer_accept_list
        if description is not None:
            self._values["description"] = description
        if disk_encryption_key_name is not None:
            self._values["disk_encryption_key_name"] = disk_encryption_key_name
        if display_name is not None:
            self._values["display_name"] = display_name
        if id is not None:
            self._values["id"] = id
        if ip_range is not None:
            self._values["ip_range"] = ip_range
        if peering_cidr_range is not None:
            self._values["peering_cidr_range"] = peering_cidr_range
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
    def location(self) -> builtins.str:
        '''Required. Compute Engine location where the instance resides.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance#location GoogleApigeeInstance#location}
        '''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Resource ID of the instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance#name GoogleApigeeInstance#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def org_id(self) -> builtins.str:
        '''The Apigee Organization associated with the Apigee instance, in the format 'organizations/{{org_name}}'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance#org_id GoogleApigeeInstance#org_id}
        '''
        result = self._values.get("org_id")
        assert result is not None, "Required property 'org_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def consumer_accept_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        Customer accept list represents the list of projects (id/number) on customer
        side that can privately connect to the service attachment. It is an optional field
        which the customers can provide during the instance creation. By default, the customer
        project associated with the Apigee organization will be included to the list.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance#consumer_accept_list GoogleApigeeInstance#consumer_accept_list}
        '''
        result = self._values.get("consumer_accept_list")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of the instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance#description GoogleApigeeInstance#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disk_encryption_key_name(self) -> typing.Optional[builtins.str]:
        '''Customer Managed Encryption Key (CMEK) used for disk and volume encryption.

        Required for Apigee paid subscriptions only.
        Use the following format: 'projects/([^/]+)/locations/([^/]+)/keyRings/([^/]+)/cryptoKeys/([^/]+)'

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance#disk_encryption_key_name GoogleApigeeInstance#disk_encryption_key_name}
        '''
        result = self._values.get("disk_encryption_key_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''Display name of the instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance#display_name GoogleApigeeInstance#display_name}
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance#id GoogleApigeeInstance#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_range(self) -> typing.Optional[builtins.str]:
        '''IP range represents the customer-provided CIDR block of length 22 that will be used for the Apigee instance creation.

        This optional range, if provided, should be freely
        available as part of larger named range the customer has allocated to the Service
        Networking peering. If this is not provided, Apigee will automatically request for any
        available /22 CIDR block from Service Networking. The customer should use this CIDR block
        for configuring their firewall needs to allow traffic from Apigee.
        Input format: "a.b.c.d/22"

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance#ip_range GoogleApigeeInstance#ip_range}
        '''
        result = self._values.get("ip_range")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def peering_cidr_range(self) -> typing.Optional[builtins.str]:
        '''The size of the CIDR block range that will be reserved by the instance.

        For valid values,
        see `CidrRange <https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances#CidrRange>`_ on the documentation.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance#peering_cidr_range GoogleApigeeInstance#peering_cidr_range}
        '''
        result = self._values.get("peering_cidr_range")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleApigeeInstanceTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance#timeouts GoogleApigeeInstance#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleApigeeInstanceTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleApigeeInstanceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleApigeeInstance.GoogleApigeeInstanceTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete"},
)
class GoogleApigeeInstanceTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance#create GoogleApigeeInstance#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance#delete GoogleApigeeInstance#delete}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleApigeeInstanceTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance#create GoogleApigeeInstance#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apigee_instance#delete GoogleApigeeInstance#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleApigeeInstanceTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleApigeeInstanceTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleApigeeInstance.GoogleApigeeInstanceTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleApigeeInstanceTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApigeeInstanceTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApigeeInstanceTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleApigeeInstanceTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleApigeeInstanceTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleApigeeInstanceTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApigeeInstanceTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleApigeeInstance",
    "GoogleApigeeInstanceConfig",
    "GoogleApigeeInstanceTimeouts",
    "GoogleApigeeInstanceTimeoutsOutputReference",
]

publication.publish()
