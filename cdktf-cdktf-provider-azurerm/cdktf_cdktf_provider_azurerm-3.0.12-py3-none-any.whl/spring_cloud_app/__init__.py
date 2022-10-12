'''
# `azurerm_spring_cloud_app`

Refer to the Terraform Registory for docs: [`azurerm_spring_cloud_app`](https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app).
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


class SpringCloudApp(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.springCloudApp.SpringCloudApp",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app azurerm_spring_cloud_app}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        resource_group_name: builtins.str,
        service_name: builtins.str,
        addon_json: typing.Optional[builtins.str] = None,
        custom_persistent_disk: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SpringCloudAppCustomPersistentDisk", typing.Dict[str, typing.Any]]]]] = None,
        https_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["SpringCloudAppIdentity", typing.Dict[str, typing.Any]]] = None,
        is_public: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        persistent_disk: typing.Optional[typing.Union["SpringCloudAppPersistentDisk", typing.Dict[str, typing.Any]]] = None,
        public_endpoint_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["SpringCloudAppTimeouts", typing.Dict[str, typing.Any]]] = None,
        tls_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app azurerm_spring_cloud_app} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#name SpringCloudApp#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#resource_group_name SpringCloudApp#resource_group_name}.
        :param service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#service_name SpringCloudApp#service_name}.
        :param addon_json: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#addon_json SpringCloudApp#addon_json}.
        :param custom_persistent_disk: custom_persistent_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#custom_persistent_disk SpringCloudApp#custom_persistent_disk}
        :param https_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#https_only SpringCloudApp#https_only}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#id SpringCloudApp#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#identity SpringCloudApp#identity}
        :param is_public: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#is_public SpringCloudApp#is_public}.
        :param persistent_disk: persistent_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#persistent_disk SpringCloudApp#persistent_disk}
        :param public_endpoint_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#public_endpoint_enabled SpringCloudApp#public_endpoint_enabled}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#timeouts SpringCloudApp#timeouts}
        :param tls_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#tls_enabled SpringCloudApp#tls_enabled}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SpringCloudApp.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SpringCloudAppConfig(
            name=name,
            resource_group_name=resource_group_name,
            service_name=service_name,
            addon_json=addon_json,
            custom_persistent_disk=custom_persistent_disk,
            https_only=https_only,
            id=id,
            identity=identity,
            is_public=is_public,
            persistent_disk=persistent_disk,
            public_endpoint_enabled=public_endpoint_enabled,
            timeouts=timeouts,
            tls_enabled=tls_enabled,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCustomPersistentDisk")
    def put_custom_persistent_disk(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SpringCloudAppCustomPersistentDisk", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SpringCloudApp.put_custom_persistent_disk)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCustomPersistentDisk", [value]))

    @jsii.member(jsii_name="putIdentity")
    def put_identity(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#type SpringCloudApp#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#identity_ids SpringCloudApp#identity_ids}.
        '''
        value = SpringCloudAppIdentity(type=type, identity_ids=identity_ids)

        return typing.cast(None, jsii.invoke(self, "putIdentity", [value]))

    @jsii.member(jsii_name="putPersistentDisk")
    def put_persistent_disk(
        self,
        *,
        size_in_gb: jsii.Number,
        mount_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param size_in_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#size_in_gb SpringCloudApp#size_in_gb}.
        :param mount_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#mount_path SpringCloudApp#mount_path}.
        '''
        value = SpringCloudAppPersistentDisk(
            size_in_gb=size_in_gb, mount_path=mount_path
        )

        return typing.cast(None, jsii.invoke(self, "putPersistentDisk", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#create SpringCloudApp#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#delete SpringCloudApp#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#read SpringCloudApp#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#update SpringCloudApp#update}.
        '''
        value = SpringCloudAppTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAddonJson")
    def reset_addon_json(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddonJson", []))

    @jsii.member(jsii_name="resetCustomPersistentDisk")
    def reset_custom_persistent_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomPersistentDisk", []))

    @jsii.member(jsii_name="resetHttpsOnly")
    def reset_https_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpsOnly", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentity")
    def reset_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentity", []))

    @jsii.member(jsii_name="resetIsPublic")
    def reset_is_public(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsPublic", []))

    @jsii.member(jsii_name="resetPersistentDisk")
    def reset_persistent_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPersistentDisk", []))

    @jsii.member(jsii_name="resetPublicEndpointEnabled")
    def reset_public_endpoint_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicEndpointEnabled", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTlsEnabled")
    def reset_tls_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsEnabled", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="customPersistentDisk")
    def custom_persistent_disk(self) -> "SpringCloudAppCustomPersistentDiskList":
        return typing.cast("SpringCloudAppCustomPersistentDiskList", jsii.get(self, "customPersistentDisk"))

    @builtins.property
    @jsii.member(jsii_name="fqdn")
    def fqdn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fqdn"))

    @builtins.property
    @jsii.member(jsii_name="identity")
    def identity(self) -> "SpringCloudAppIdentityOutputReference":
        return typing.cast("SpringCloudAppIdentityOutputReference", jsii.get(self, "identity"))

    @builtins.property
    @jsii.member(jsii_name="persistentDisk")
    def persistent_disk(self) -> "SpringCloudAppPersistentDiskOutputReference":
        return typing.cast("SpringCloudAppPersistentDiskOutputReference", jsii.get(self, "persistentDisk"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "SpringCloudAppTimeoutsOutputReference":
        return typing.cast("SpringCloudAppTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @builtins.property
    @jsii.member(jsii_name="addonJsonInput")
    def addon_json_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addonJsonInput"))

    @builtins.property
    @jsii.member(jsii_name="customPersistentDiskInput")
    def custom_persistent_disk_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SpringCloudAppCustomPersistentDisk"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SpringCloudAppCustomPersistentDisk"]]], jsii.get(self, "customPersistentDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="httpsOnlyInput")
    def https_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "httpsOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="identityInput")
    def identity_input(self) -> typing.Optional["SpringCloudAppIdentity"]:
        return typing.cast(typing.Optional["SpringCloudAppIdentity"], jsii.get(self, "identityInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="isPublicInput")
    def is_public_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isPublicInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="persistentDiskInput")
    def persistent_disk_input(self) -> typing.Optional["SpringCloudAppPersistentDisk"]:
        return typing.cast(typing.Optional["SpringCloudAppPersistentDisk"], jsii.get(self, "persistentDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="publicEndpointEnabledInput")
    def public_endpoint_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "publicEndpointEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceNameInput")
    def service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["SpringCloudAppTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["SpringCloudAppTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsEnabledInput")
    def tls_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "tlsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="addonJson")
    def addon_json(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "addonJson"))

    @addon_json.setter
    def addon_json(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudApp, "addon_json").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addonJson", value)

    @builtins.property
    @jsii.member(jsii_name="httpsOnly")
    def https_only(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "httpsOnly"))

    @https_only.setter
    def https_only(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudApp, "https_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpsOnly", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudApp, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="isPublic")
    def is_public(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isPublic"))

    @is_public.setter
    def is_public(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudApp, "is_public").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isPublic", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudApp, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="publicEndpointEnabled")
    def public_endpoint_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "publicEndpointEnabled"))

    @public_endpoint_enabled.setter
    def public_endpoint_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudApp, "public_endpoint_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicEndpointEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudApp, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceName"))

    @service_name.setter
    def service_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudApp, "service_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceName", value)

    @builtins.property
    @jsii.member(jsii_name="tlsEnabled")
    def tls_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "tlsEnabled"))

    @tls_enabled.setter
    def tls_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudApp, "tls_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsEnabled", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.springCloudApp.SpringCloudAppConfig",
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
        "resource_group_name": "resourceGroupName",
        "service_name": "serviceName",
        "addon_json": "addonJson",
        "custom_persistent_disk": "customPersistentDisk",
        "https_only": "httpsOnly",
        "id": "id",
        "identity": "identity",
        "is_public": "isPublic",
        "persistent_disk": "persistentDisk",
        "public_endpoint_enabled": "publicEndpointEnabled",
        "timeouts": "timeouts",
        "tls_enabled": "tlsEnabled",
    },
)
class SpringCloudAppConfig(cdktf.TerraformMetaArguments):
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
        resource_group_name: builtins.str,
        service_name: builtins.str,
        addon_json: typing.Optional[builtins.str] = None,
        custom_persistent_disk: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SpringCloudAppCustomPersistentDisk", typing.Dict[str, typing.Any]]]]] = None,
        https_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["SpringCloudAppIdentity", typing.Dict[str, typing.Any]]] = None,
        is_public: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        persistent_disk: typing.Optional[typing.Union["SpringCloudAppPersistentDisk", typing.Dict[str, typing.Any]]] = None,
        public_endpoint_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["SpringCloudAppTimeouts", typing.Dict[str, typing.Any]]] = None,
        tls_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#name SpringCloudApp#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#resource_group_name SpringCloudApp#resource_group_name}.
        :param service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#service_name SpringCloudApp#service_name}.
        :param addon_json: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#addon_json SpringCloudApp#addon_json}.
        :param custom_persistent_disk: custom_persistent_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#custom_persistent_disk SpringCloudApp#custom_persistent_disk}
        :param https_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#https_only SpringCloudApp#https_only}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#id SpringCloudApp#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#identity SpringCloudApp#identity}
        :param is_public: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#is_public SpringCloudApp#is_public}.
        :param persistent_disk: persistent_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#persistent_disk SpringCloudApp#persistent_disk}
        :param public_endpoint_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#public_endpoint_enabled SpringCloudApp#public_endpoint_enabled}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#timeouts SpringCloudApp#timeouts}
        :param tls_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#tls_enabled SpringCloudApp#tls_enabled}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(identity, dict):
            identity = SpringCloudAppIdentity(**identity)
        if isinstance(persistent_disk, dict):
            persistent_disk = SpringCloudAppPersistentDisk(**persistent_disk)
        if isinstance(timeouts, dict):
            timeouts = SpringCloudAppTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(SpringCloudAppConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
            check_type(argname="argument addon_json", value=addon_json, expected_type=type_hints["addon_json"])
            check_type(argname="argument custom_persistent_disk", value=custom_persistent_disk, expected_type=type_hints["custom_persistent_disk"])
            check_type(argname="argument https_only", value=https_only, expected_type=type_hints["https_only"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument is_public", value=is_public, expected_type=type_hints["is_public"])
            check_type(argname="argument persistent_disk", value=persistent_disk, expected_type=type_hints["persistent_disk"])
            check_type(argname="argument public_endpoint_enabled", value=public_endpoint_enabled, expected_type=type_hints["public_endpoint_enabled"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument tls_enabled", value=tls_enabled, expected_type=type_hints["tls_enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "resource_group_name": resource_group_name,
            "service_name": service_name,
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
        if addon_json is not None:
            self._values["addon_json"] = addon_json
        if custom_persistent_disk is not None:
            self._values["custom_persistent_disk"] = custom_persistent_disk
        if https_only is not None:
            self._values["https_only"] = https_only
        if id is not None:
            self._values["id"] = id
        if identity is not None:
            self._values["identity"] = identity
        if is_public is not None:
            self._values["is_public"] = is_public
        if persistent_disk is not None:
            self._values["persistent_disk"] = persistent_disk
        if public_endpoint_enabled is not None:
            self._values["public_endpoint_enabled"] = public_endpoint_enabled
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if tls_enabled is not None:
            self._values["tls_enabled"] = tls_enabled

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#name SpringCloudApp#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#resource_group_name SpringCloudApp#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#service_name SpringCloudApp#service_name}.'''
        result = self._values.get("service_name")
        assert result is not None, "Required property 'service_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def addon_json(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#addon_json SpringCloudApp#addon_json}.'''
        result = self._values.get("addon_json")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_persistent_disk(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SpringCloudAppCustomPersistentDisk"]]]:
        '''custom_persistent_disk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#custom_persistent_disk SpringCloudApp#custom_persistent_disk}
        '''
        result = self._values.get("custom_persistent_disk")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SpringCloudAppCustomPersistentDisk"]]], result)

    @builtins.property
    def https_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#https_only SpringCloudApp#https_only}.'''
        result = self._values.get("https_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#id SpringCloudApp#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity(self) -> typing.Optional["SpringCloudAppIdentity"]:
        '''identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#identity SpringCloudApp#identity}
        '''
        result = self._values.get("identity")
        return typing.cast(typing.Optional["SpringCloudAppIdentity"], result)

    @builtins.property
    def is_public(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#is_public SpringCloudApp#is_public}.'''
        result = self._values.get("is_public")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def persistent_disk(self) -> typing.Optional["SpringCloudAppPersistentDisk"]:
        '''persistent_disk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#persistent_disk SpringCloudApp#persistent_disk}
        '''
        result = self._values.get("persistent_disk")
        return typing.cast(typing.Optional["SpringCloudAppPersistentDisk"], result)

    @builtins.property
    def public_endpoint_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#public_endpoint_enabled SpringCloudApp#public_endpoint_enabled}.'''
        result = self._values.get("public_endpoint_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["SpringCloudAppTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#timeouts SpringCloudApp#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["SpringCloudAppTimeouts"], result)

    @builtins.property
    def tls_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#tls_enabled SpringCloudApp#tls_enabled}.'''
        result = self._values.get("tls_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpringCloudAppConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.springCloudApp.SpringCloudAppCustomPersistentDisk",
    jsii_struct_bases=[],
    name_mapping={
        "mount_path": "mountPath",
        "share_name": "shareName",
        "storage_name": "storageName",
        "mount_options": "mountOptions",
        "read_only_enabled": "readOnlyEnabled",
    },
)
class SpringCloudAppCustomPersistentDisk:
    def __init__(
        self,
        *,
        mount_path: builtins.str,
        share_name: builtins.str,
        storage_name: builtins.str,
        mount_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        read_only_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param mount_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#mount_path SpringCloudApp#mount_path}.
        :param share_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#share_name SpringCloudApp#share_name}.
        :param storage_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#storage_name SpringCloudApp#storage_name}.
        :param mount_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#mount_options SpringCloudApp#mount_options}.
        :param read_only_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#read_only_enabled SpringCloudApp#read_only_enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SpringCloudAppCustomPersistentDisk.__init__)
            check_type(argname="argument mount_path", value=mount_path, expected_type=type_hints["mount_path"])
            check_type(argname="argument share_name", value=share_name, expected_type=type_hints["share_name"])
            check_type(argname="argument storage_name", value=storage_name, expected_type=type_hints["storage_name"])
            check_type(argname="argument mount_options", value=mount_options, expected_type=type_hints["mount_options"])
            check_type(argname="argument read_only_enabled", value=read_only_enabled, expected_type=type_hints["read_only_enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "mount_path": mount_path,
            "share_name": share_name,
            "storage_name": storage_name,
        }
        if mount_options is not None:
            self._values["mount_options"] = mount_options
        if read_only_enabled is not None:
            self._values["read_only_enabled"] = read_only_enabled

    @builtins.property
    def mount_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#mount_path SpringCloudApp#mount_path}.'''
        result = self._values.get("mount_path")
        assert result is not None, "Required property 'mount_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def share_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#share_name SpringCloudApp#share_name}.'''
        result = self._values.get("share_name")
        assert result is not None, "Required property 'share_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#storage_name SpringCloudApp#storage_name}.'''
        result = self._values.get("storage_name")
        assert result is not None, "Required property 'storage_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mount_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#mount_options SpringCloudApp#mount_options}.'''
        result = self._values.get("mount_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def read_only_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#read_only_enabled SpringCloudApp#read_only_enabled}.'''
        result = self._values.get("read_only_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpringCloudAppCustomPersistentDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SpringCloudAppCustomPersistentDiskList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.springCloudApp.SpringCloudAppCustomPersistentDiskList",
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
            type_hints = typing.get_type_hints(SpringCloudAppCustomPersistentDiskList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SpringCloudAppCustomPersistentDiskOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SpringCloudAppCustomPersistentDiskList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SpringCloudAppCustomPersistentDiskOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudAppCustomPersistentDiskList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SpringCloudAppCustomPersistentDiskList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SpringCloudAppCustomPersistentDiskList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SpringCloudAppCustomPersistentDisk]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SpringCloudAppCustomPersistentDisk]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SpringCloudAppCustomPersistentDisk]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudAppCustomPersistentDiskList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SpringCloudAppCustomPersistentDiskOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.springCloudApp.SpringCloudAppCustomPersistentDiskOutputReference",
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
            type_hints = typing.get_type_hints(SpringCloudAppCustomPersistentDiskOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMountOptions")
    def reset_mount_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMountOptions", []))

    @jsii.member(jsii_name="resetReadOnlyEnabled")
    def reset_read_only_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnlyEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="mountOptionsInput")
    def mount_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "mountOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="mountPathInput")
    def mount_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mountPathInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyEnabledInput")
    def read_only_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "readOnlyEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="shareNameInput")
    def share_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shareNameInput"))

    @builtins.property
    @jsii.member(jsii_name="storageNameInput")
    def storage_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageNameInput"))

    @builtins.property
    @jsii.member(jsii_name="mountOptions")
    def mount_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "mountOptions"))

    @mount_options.setter
    def mount_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudAppCustomPersistentDiskOutputReference, "mount_options").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mountOptions", value)

    @builtins.property
    @jsii.member(jsii_name="mountPath")
    def mount_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mountPath"))

    @mount_path.setter
    def mount_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudAppCustomPersistentDiskOutputReference, "mount_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mountPath", value)

    @builtins.property
    @jsii.member(jsii_name="readOnlyEnabled")
    def read_only_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "readOnlyEnabled"))

    @read_only_enabled.setter
    def read_only_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudAppCustomPersistentDiskOutputReference, "read_only_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnlyEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="shareName")
    def share_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "shareName"))

    @share_name.setter
    def share_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudAppCustomPersistentDiskOutputReference, "share_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shareName", value)

    @builtins.property
    @jsii.member(jsii_name="storageName")
    def storage_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageName"))

    @storage_name.setter
    def storage_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudAppCustomPersistentDiskOutputReference, "storage_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SpringCloudAppCustomPersistentDisk, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SpringCloudAppCustomPersistentDisk, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SpringCloudAppCustomPersistentDisk, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudAppCustomPersistentDiskOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.springCloudApp.SpringCloudAppIdentity",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "identity_ids": "identityIds"},
)
class SpringCloudAppIdentity:
    def __init__(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#type SpringCloudApp#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#identity_ids SpringCloudApp#identity_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SpringCloudAppIdentity.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument identity_ids", value=identity_ids, expected_type=type_hints["identity_ids"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if identity_ids is not None:
            self._values["identity_ids"] = identity_ids

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#type SpringCloudApp#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#identity_ids SpringCloudApp#identity_ids}.'''
        result = self._values.get("identity_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpringCloudAppIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SpringCloudAppIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.springCloudApp.SpringCloudAppIdentityOutputReference",
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
            type_hints = typing.get_type_hints(SpringCloudAppIdentityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIdentityIds")
    def reset_identity_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityIds", []))

    @builtins.property
    @jsii.member(jsii_name="principalId")
    def principal_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "principalId"))

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

    @builtins.property
    @jsii.member(jsii_name="identityIdsInput")
    def identity_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "identityIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="identityIds")
    def identity_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "identityIds"))

    @identity_ids.setter
    def identity_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudAppIdentityOutputReference, "identity_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityIds", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudAppIdentityOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SpringCloudAppIdentity]:
        return typing.cast(typing.Optional[SpringCloudAppIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SpringCloudAppIdentity]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudAppIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.springCloudApp.SpringCloudAppPersistentDisk",
    jsii_struct_bases=[],
    name_mapping={"size_in_gb": "sizeInGb", "mount_path": "mountPath"},
)
class SpringCloudAppPersistentDisk:
    def __init__(
        self,
        *,
        size_in_gb: jsii.Number,
        mount_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param size_in_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#size_in_gb SpringCloudApp#size_in_gb}.
        :param mount_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#mount_path SpringCloudApp#mount_path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SpringCloudAppPersistentDisk.__init__)
            check_type(argname="argument size_in_gb", value=size_in_gb, expected_type=type_hints["size_in_gb"])
            check_type(argname="argument mount_path", value=mount_path, expected_type=type_hints["mount_path"])
        self._values: typing.Dict[str, typing.Any] = {
            "size_in_gb": size_in_gb,
        }
        if mount_path is not None:
            self._values["mount_path"] = mount_path

    @builtins.property
    def size_in_gb(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#size_in_gb SpringCloudApp#size_in_gb}.'''
        result = self._values.get("size_in_gb")
        assert result is not None, "Required property 'size_in_gb' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def mount_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#mount_path SpringCloudApp#mount_path}.'''
        result = self._values.get("mount_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpringCloudAppPersistentDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SpringCloudAppPersistentDiskOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.springCloudApp.SpringCloudAppPersistentDiskOutputReference",
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
            type_hints = typing.get_type_hints(SpringCloudAppPersistentDiskOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMountPath")
    def reset_mount_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMountPath", []))

    @builtins.property
    @jsii.member(jsii_name="mountPathInput")
    def mount_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mountPathInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeInGbInput")
    def size_in_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeInGbInput"))

    @builtins.property
    @jsii.member(jsii_name="mountPath")
    def mount_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mountPath"))

    @mount_path.setter
    def mount_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudAppPersistentDiskOutputReference, "mount_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mountPath", value)

    @builtins.property
    @jsii.member(jsii_name="sizeInGb")
    def size_in_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sizeInGb"))

    @size_in_gb.setter
    def size_in_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudAppPersistentDiskOutputReference, "size_in_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sizeInGb", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SpringCloudAppPersistentDisk]:
        return typing.cast(typing.Optional[SpringCloudAppPersistentDisk], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SpringCloudAppPersistentDisk],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudAppPersistentDiskOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.springCloudApp.SpringCloudAppTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class SpringCloudAppTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#create SpringCloudApp#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#delete SpringCloudApp#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#read SpringCloudApp#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#update SpringCloudApp#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SpringCloudAppTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#create SpringCloudApp#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#delete SpringCloudApp#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#read SpringCloudApp#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_app#update SpringCloudApp#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpringCloudAppTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SpringCloudAppTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.springCloudApp.SpringCloudAppTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(SpringCloudAppTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(SpringCloudAppTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudAppTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudAppTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudAppTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SpringCloudAppTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SpringCloudAppTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SpringCloudAppTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudAppTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SpringCloudApp",
    "SpringCloudAppConfig",
    "SpringCloudAppCustomPersistentDisk",
    "SpringCloudAppCustomPersistentDiskList",
    "SpringCloudAppCustomPersistentDiskOutputReference",
    "SpringCloudAppIdentity",
    "SpringCloudAppIdentityOutputReference",
    "SpringCloudAppPersistentDisk",
    "SpringCloudAppPersistentDiskOutputReference",
    "SpringCloudAppTimeouts",
    "SpringCloudAppTimeoutsOutputReference",
]

publication.publish()
