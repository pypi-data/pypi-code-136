'''
# `cloudflare_load_balancer_pool`

Refer to the Terraform Registory for docs: [`cloudflare_load_balancer_pool`](https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool).
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


class LoadBalancerPool(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.loadBalancerPool.LoadBalancerPool",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool cloudflare_load_balancer_pool}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        origins: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerPoolOrigins", typing.Dict[str, typing.Any]]]],
        check_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        latitude: typing.Optional[jsii.Number] = None,
        load_shedding: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerPoolLoadShedding", typing.Dict[str, typing.Any]]]]] = None,
        longitude: typing.Optional[jsii.Number] = None,
        minimum_origins: typing.Optional[jsii.Number] = None,
        monitor: typing.Optional[builtins.str] = None,
        notification_email: typing.Optional[builtins.str] = None,
        origin_steering: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerPoolOriginSteering", typing.Dict[str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool cloudflare_load_balancer_pool} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#name LoadBalancerPool#name}.
        :param origins: origins block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#origins LoadBalancerPool#origins}
        :param check_regions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#check_regions LoadBalancerPool#check_regions}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#description LoadBalancerPool#description}.
        :param enabled: Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#enabled LoadBalancerPool#enabled}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#id LoadBalancerPool#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param latitude: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#latitude LoadBalancerPool#latitude}.
        :param load_shedding: load_shedding block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#load_shedding LoadBalancerPool#load_shedding}
        :param longitude: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#longitude LoadBalancerPool#longitude}.
        :param minimum_origins: Defaults to ``1``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#minimum_origins LoadBalancerPool#minimum_origins}
        :param monitor: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#monitor LoadBalancerPool#monitor}.
        :param notification_email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#notification_email LoadBalancerPool#notification_email}.
        :param origin_steering: origin_steering block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#origin_steering LoadBalancerPool#origin_steering}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerPool.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LoadBalancerPoolConfig(
            name=name,
            origins=origins,
            check_regions=check_regions,
            description=description,
            enabled=enabled,
            id=id,
            latitude=latitude,
            load_shedding=load_shedding,
            longitude=longitude,
            minimum_origins=minimum_origins,
            monitor=monitor,
            notification_email=notification_email,
            origin_steering=origin_steering,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putLoadShedding")
    def put_load_shedding(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerPoolLoadShedding", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerPool.put_load_shedding)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLoadShedding", [value]))

    @jsii.member(jsii_name="putOrigins")
    def put_origins(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerPoolOrigins", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerPool.put_origins)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOrigins", [value]))

    @jsii.member(jsii_name="putOriginSteering")
    def put_origin_steering(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerPoolOriginSteering", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerPool.put_origin_steering)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOriginSteering", [value]))

    @jsii.member(jsii_name="resetCheckRegions")
    def reset_check_regions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCheckRegions", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLatitude")
    def reset_latitude(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLatitude", []))

    @jsii.member(jsii_name="resetLoadShedding")
    def reset_load_shedding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadShedding", []))

    @jsii.member(jsii_name="resetLongitude")
    def reset_longitude(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLongitude", []))

    @jsii.member(jsii_name="resetMinimumOrigins")
    def reset_minimum_origins(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinimumOrigins", []))

    @jsii.member(jsii_name="resetMonitor")
    def reset_monitor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonitor", []))

    @jsii.member(jsii_name="resetNotificationEmail")
    def reset_notification_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationEmail", []))

    @jsii.member(jsii_name="resetOriginSteering")
    def reset_origin_steering(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOriginSteering", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="createdOn")
    def created_on(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdOn"))

    @builtins.property
    @jsii.member(jsii_name="loadShedding")
    def load_shedding(self) -> "LoadBalancerPoolLoadSheddingList":
        return typing.cast("LoadBalancerPoolLoadSheddingList", jsii.get(self, "loadShedding"))

    @builtins.property
    @jsii.member(jsii_name="modifiedOn")
    def modified_on(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "modifiedOn"))

    @builtins.property
    @jsii.member(jsii_name="origins")
    def origins(self) -> "LoadBalancerPoolOriginsList":
        return typing.cast("LoadBalancerPoolOriginsList", jsii.get(self, "origins"))

    @builtins.property
    @jsii.member(jsii_name="originSteering")
    def origin_steering(self) -> "LoadBalancerPoolOriginSteeringList":
        return typing.cast("LoadBalancerPoolOriginSteeringList", jsii.get(self, "originSteering"))

    @builtins.property
    @jsii.member(jsii_name="checkRegionsInput")
    def check_regions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "checkRegionsInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="latitudeInput")
    def latitude_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "latitudeInput"))

    @builtins.property
    @jsii.member(jsii_name="loadSheddingInput")
    def load_shedding_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerPoolLoadShedding"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerPoolLoadShedding"]]], jsii.get(self, "loadSheddingInput"))

    @builtins.property
    @jsii.member(jsii_name="longitudeInput")
    def longitude_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "longitudeInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumOriginsInput")
    def minimum_origins_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minimumOriginsInput"))

    @builtins.property
    @jsii.member(jsii_name="monitorInput")
    def monitor_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "monitorInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationEmailInput")
    def notification_email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notificationEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="originsInput")
    def origins_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerPoolOrigins"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerPoolOrigins"]]], jsii.get(self, "originsInput"))

    @builtins.property
    @jsii.member(jsii_name="originSteeringInput")
    def origin_steering_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerPoolOriginSteering"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerPoolOriginSteering"]]], jsii.get(self, "originSteeringInput"))

    @builtins.property
    @jsii.member(jsii_name="checkRegions")
    def check_regions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "checkRegions"))

    @check_regions.setter
    def check_regions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerPool, "check_regions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "checkRegions", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerPool, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerPool, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerPool, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="latitude")
    def latitude(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "latitude"))

    @latitude.setter
    def latitude(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerPool, "latitude").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "latitude", value)

    @builtins.property
    @jsii.member(jsii_name="longitude")
    def longitude(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "longitude"))

    @longitude.setter
    def longitude(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerPool, "longitude").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "longitude", value)

    @builtins.property
    @jsii.member(jsii_name="minimumOrigins")
    def minimum_origins(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minimumOrigins"))

    @minimum_origins.setter
    def minimum_origins(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerPool, "minimum_origins").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumOrigins", value)

    @builtins.property
    @jsii.member(jsii_name="monitor")
    def monitor(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "monitor"))

    @monitor.setter
    def monitor(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerPool, "monitor").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monitor", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerPool, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="notificationEmail")
    def notification_email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notificationEmail"))

    @notification_email.setter
    def notification_email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerPool, "notification_email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationEmail", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.loadBalancerPool.LoadBalancerPoolConfig",
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
        "origins": "origins",
        "check_regions": "checkRegions",
        "description": "description",
        "enabled": "enabled",
        "id": "id",
        "latitude": "latitude",
        "load_shedding": "loadShedding",
        "longitude": "longitude",
        "minimum_origins": "minimumOrigins",
        "monitor": "monitor",
        "notification_email": "notificationEmail",
        "origin_steering": "originSteering",
    },
)
class LoadBalancerPoolConfig(cdktf.TerraformMetaArguments):
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
        origins: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerPoolOrigins", typing.Dict[str, typing.Any]]]],
        check_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        latitude: typing.Optional[jsii.Number] = None,
        load_shedding: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerPoolLoadShedding", typing.Dict[str, typing.Any]]]]] = None,
        longitude: typing.Optional[jsii.Number] = None,
        minimum_origins: typing.Optional[jsii.Number] = None,
        monitor: typing.Optional[builtins.str] = None,
        notification_email: typing.Optional[builtins.str] = None,
        origin_steering: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerPoolOriginSteering", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#name LoadBalancerPool#name}.
        :param origins: origins block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#origins LoadBalancerPool#origins}
        :param check_regions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#check_regions LoadBalancerPool#check_regions}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#description LoadBalancerPool#description}.
        :param enabled: Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#enabled LoadBalancerPool#enabled}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#id LoadBalancerPool#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param latitude: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#latitude LoadBalancerPool#latitude}.
        :param load_shedding: load_shedding block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#load_shedding LoadBalancerPool#load_shedding}
        :param longitude: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#longitude LoadBalancerPool#longitude}.
        :param minimum_origins: Defaults to ``1``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#minimum_origins LoadBalancerPool#minimum_origins}
        :param monitor: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#monitor LoadBalancerPool#monitor}.
        :param notification_email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#notification_email LoadBalancerPool#notification_email}.
        :param origin_steering: origin_steering block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#origin_steering LoadBalancerPool#origin_steering}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerPoolConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument origins", value=origins, expected_type=type_hints["origins"])
            check_type(argname="argument check_regions", value=check_regions, expected_type=type_hints["check_regions"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument latitude", value=latitude, expected_type=type_hints["latitude"])
            check_type(argname="argument load_shedding", value=load_shedding, expected_type=type_hints["load_shedding"])
            check_type(argname="argument longitude", value=longitude, expected_type=type_hints["longitude"])
            check_type(argname="argument minimum_origins", value=minimum_origins, expected_type=type_hints["minimum_origins"])
            check_type(argname="argument monitor", value=monitor, expected_type=type_hints["monitor"])
            check_type(argname="argument notification_email", value=notification_email, expected_type=type_hints["notification_email"])
            check_type(argname="argument origin_steering", value=origin_steering, expected_type=type_hints["origin_steering"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "origins": origins,
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
        if check_regions is not None:
            self._values["check_regions"] = check_regions
        if description is not None:
            self._values["description"] = description
        if enabled is not None:
            self._values["enabled"] = enabled
        if id is not None:
            self._values["id"] = id
        if latitude is not None:
            self._values["latitude"] = latitude
        if load_shedding is not None:
            self._values["load_shedding"] = load_shedding
        if longitude is not None:
            self._values["longitude"] = longitude
        if minimum_origins is not None:
            self._values["minimum_origins"] = minimum_origins
        if monitor is not None:
            self._values["monitor"] = monitor
        if notification_email is not None:
            self._values["notification_email"] = notification_email
        if origin_steering is not None:
            self._values["origin_steering"] = origin_steering

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#name LoadBalancerPool#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def origins(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["LoadBalancerPoolOrigins"]]:
        '''origins block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#origins LoadBalancerPool#origins}
        '''
        result = self._values.get("origins")
        assert result is not None, "Required property 'origins' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["LoadBalancerPoolOrigins"]], result)

    @builtins.property
    def check_regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#check_regions LoadBalancerPool#check_regions}.'''
        result = self._values.get("check_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#description LoadBalancerPool#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defaults to ``true``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#enabled LoadBalancerPool#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#id LoadBalancerPool#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def latitude(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#latitude LoadBalancerPool#latitude}.'''
        result = self._values.get("latitude")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def load_shedding(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerPoolLoadShedding"]]]:
        '''load_shedding block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#load_shedding LoadBalancerPool#load_shedding}
        '''
        result = self._values.get("load_shedding")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerPoolLoadShedding"]]], result)

    @builtins.property
    def longitude(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#longitude LoadBalancerPool#longitude}.'''
        result = self._values.get("longitude")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def minimum_origins(self) -> typing.Optional[jsii.Number]:
        '''Defaults to ``1``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#minimum_origins LoadBalancerPool#minimum_origins}
        '''
        result = self._values.get("minimum_origins")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def monitor(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#monitor LoadBalancerPool#monitor}.'''
        result = self._values.get("monitor")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_email(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#notification_email LoadBalancerPool#notification_email}.'''
        result = self._values.get("notification_email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_steering(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerPoolOriginSteering"]]]:
        '''origin_steering block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#origin_steering LoadBalancerPool#origin_steering}
        '''
        result = self._values.get("origin_steering")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerPoolOriginSteering"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadBalancerPoolConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.loadBalancerPool.LoadBalancerPoolLoadShedding",
    jsii_struct_bases=[],
    name_mapping={
        "default_percent": "defaultPercent",
        "default_policy": "defaultPolicy",
        "session_percent": "sessionPercent",
        "session_policy": "sessionPolicy",
    },
)
class LoadBalancerPoolLoadShedding:
    def __init__(
        self,
        *,
        default_percent: typing.Optional[jsii.Number] = None,
        default_policy: typing.Optional[builtins.str] = None,
        session_percent: typing.Optional[jsii.Number] = None,
        session_policy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param default_percent: Defaults to ``0``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#default_percent LoadBalancerPool#default_percent}
        :param default_policy: Defaults to ``""``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#default_policy LoadBalancerPool#default_policy}
        :param session_percent: Defaults to ``0``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#session_percent LoadBalancerPool#session_percent}
        :param session_policy: Defaults to ``""``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#session_policy LoadBalancerPool#session_policy}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerPoolLoadShedding.__init__)
            check_type(argname="argument default_percent", value=default_percent, expected_type=type_hints["default_percent"])
            check_type(argname="argument default_policy", value=default_policy, expected_type=type_hints["default_policy"])
            check_type(argname="argument session_percent", value=session_percent, expected_type=type_hints["session_percent"])
            check_type(argname="argument session_policy", value=session_policy, expected_type=type_hints["session_policy"])
        self._values: typing.Dict[str, typing.Any] = {}
        if default_percent is not None:
            self._values["default_percent"] = default_percent
        if default_policy is not None:
            self._values["default_policy"] = default_policy
        if session_percent is not None:
            self._values["session_percent"] = session_percent
        if session_policy is not None:
            self._values["session_policy"] = session_policy

    @builtins.property
    def default_percent(self) -> typing.Optional[jsii.Number]:
        '''Defaults to ``0``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#default_percent LoadBalancerPool#default_percent}
        '''
        result = self._values.get("default_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def default_policy(self) -> typing.Optional[builtins.str]:
        '''Defaults to ``""``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#default_policy LoadBalancerPool#default_policy}
        '''
        result = self._values.get("default_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_percent(self) -> typing.Optional[jsii.Number]:
        '''Defaults to ``0``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#session_percent LoadBalancerPool#session_percent}
        '''
        result = self._values.get("session_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def session_policy(self) -> typing.Optional[builtins.str]:
        '''Defaults to ``""``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#session_policy LoadBalancerPool#session_policy}
        '''
        result = self._values.get("session_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadBalancerPoolLoadShedding(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadBalancerPoolLoadSheddingList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.loadBalancerPool.LoadBalancerPoolLoadSheddingList",
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
            type_hints = typing.get_type_hints(LoadBalancerPoolLoadSheddingList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "LoadBalancerPoolLoadSheddingOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerPoolLoadSheddingList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LoadBalancerPoolLoadSheddingOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerPoolLoadSheddingList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadBalancerPoolLoadSheddingList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadBalancerPoolLoadSheddingList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerPoolLoadShedding]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerPoolLoadShedding]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerPoolLoadShedding]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerPoolLoadSheddingList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadBalancerPoolLoadSheddingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.loadBalancerPool.LoadBalancerPoolLoadSheddingOutputReference",
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
            type_hints = typing.get_type_hints(LoadBalancerPoolLoadSheddingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDefaultPercent")
    def reset_default_percent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultPercent", []))

    @jsii.member(jsii_name="resetDefaultPolicy")
    def reset_default_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultPolicy", []))

    @jsii.member(jsii_name="resetSessionPercent")
    def reset_session_percent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSessionPercent", []))

    @jsii.member(jsii_name="resetSessionPolicy")
    def reset_session_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSessionPolicy", []))

    @builtins.property
    @jsii.member(jsii_name="defaultPercentInput")
    def default_percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "defaultPercentInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultPolicyInput")
    def default_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="sessionPercentInput")
    def session_percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sessionPercentInput"))

    @builtins.property
    @jsii.member(jsii_name="sessionPolicyInput")
    def session_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sessionPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultPercent")
    def default_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultPercent"))

    @default_percent.setter
    def default_percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerPoolLoadSheddingOutputReference, "default_percent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultPercent", value)

    @builtins.property
    @jsii.member(jsii_name="defaultPolicy")
    def default_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultPolicy"))

    @default_policy.setter
    def default_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerPoolLoadSheddingOutputReference, "default_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="sessionPercent")
    def session_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sessionPercent"))

    @session_percent.setter
    def session_percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerPoolLoadSheddingOutputReference, "session_percent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionPercent", value)

    @builtins.property
    @jsii.member(jsii_name="sessionPolicy")
    def session_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sessionPolicy"))

    @session_policy.setter
    def session_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerPoolLoadSheddingOutputReference, "session_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LoadBalancerPoolLoadShedding, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LoadBalancerPoolLoadShedding, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LoadBalancerPoolLoadShedding, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerPoolLoadSheddingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.loadBalancerPool.LoadBalancerPoolOriginSteering",
    jsii_struct_bases=[],
    name_mapping={"policy": "policy"},
)
class LoadBalancerPoolOriginSteering:
    def __init__(self, *, policy: typing.Optional[builtins.str] = None) -> None:
        '''
        :param policy: Defaults to ``random``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#policy LoadBalancerPool#policy}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerPoolOriginSteering.__init__)
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
        self._values: typing.Dict[str, typing.Any] = {}
        if policy is not None:
            self._values["policy"] = policy

    @builtins.property
    def policy(self) -> typing.Optional[builtins.str]:
        '''Defaults to ``random``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#policy LoadBalancerPool#policy}
        '''
        result = self._values.get("policy")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadBalancerPoolOriginSteering(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadBalancerPoolOriginSteeringList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.loadBalancerPool.LoadBalancerPoolOriginSteeringList",
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
            type_hints = typing.get_type_hints(LoadBalancerPoolOriginSteeringList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LoadBalancerPoolOriginSteeringOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerPoolOriginSteeringList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LoadBalancerPoolOriginSteeringOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerPoolOriginSteeringList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadBalancerPoolOriginSteeringList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadBalancerPoolOriginSteeringList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerPoolOriginSteering]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerPoolOriginSteering]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerPoolOriginSteering]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerPoolOriginSteeringList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadBalancerPoolOriginSteeringOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.loadBalancerPool.LoadBalancerPoolOriginSteeringOutputReference",
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
            type_hints = typing.get_type_hints(LoadBalancerPoolOriginSteeringOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetPolicy")
    def reset_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicy", []))

    @builtins.property
    @jsii.member(jsii_name="policyInput")
    def policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyInput"))

    @builtins.property
    @jsii.member(jsii_name="policy")
    def policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policy"))

    @policy.setter
    def policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerPoolOriginSteeringOutputReference, "policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policy", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LoadBalancerPoolOriginSteering, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LoadBalancerPoolOriginSteering, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LoadBalancerPoolOriginSteering, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerPoolOriginSteeringOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.loadBalancerPool.LoadBalancerPoolOrigins",
    jsii_struct_bases=[],
    name_mapping={
        "address": "address",
        "name": "name",
        "enabled": "enabled",
        "header": "header",
        "weight": "weight",
    },
)
class LoadBalancerPoolOrigins:
    def __init__(
        self,
        *,
        address: builtins.str,
        name: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        header: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerPoolOriginsHeader", typing.Dict[str, typing.Any]]]]] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#address LoadBalancerPool#address}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#name LoadBalancerPool#name}.
        :param enabled: Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#enabled LoadBalancerPool#enabled}
        :param header: header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#header LoadBalancerPool#header}
        :param weight: Defaults to ``1``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#weight LoadBalancerPool#weight}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerPoolOrigins.__init__)
            check_type(argname="argument address", value=address, expected_type=type_hints["address"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument header", value=header, expected_type=type_hints["header"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[str, typing.Any] = {
            "address": address,
            "name": name,
        }
        if enabled is not None:
            self._values["enabled"] = enabled
        if header is not None:
            self._values["header"] = header
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def address(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#address LoadBalancerPool#address}.'''
        result = self._values.get("address")
        assert result is not None, "Required property 'address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#name LoadBalancerPool#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defaults to ``true``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#enabled LoadBalancerPool#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def header(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerPoolOriginsHeader"]]]:
        '''header block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#header LoadBalancerPool#header}
        '''
        result = self._values.get("header")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerPoolOriginsHeader"]]], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Defaults to ``1``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#weight LoadBalancerPool#weight}
        '''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadBalancerPoolOrigins(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.loadBalancerPool.LoadBalancerPoolOriginsHeader",
    jsii_struct_bases=[],
    name_mapping={"header": "header", "values": "values"},
)
class LoadBalancerPoolOriginsHeader:
    def __init__(
        self,
        *,
        header: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param header: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#header LoadBalancerPool#header}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#values LoadBalancerPool#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerPoolOriginsHeader.__init__)
            check_type(argname="argument header", value=header, expected_type=type_hints["header"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "header": header,
            "values": values,
        }

    @builtins.property
    def header(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#header LoadBalancerPool#header}.'''
        result = self._values.get("header")
        assert result is not None, "Required property 'header' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool#values LoadBalancerPool#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadBalancerPoolOriginsHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadBalancerPoolOriginsHeaderList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.loadBalancerPool.LoadBalancerPoolOriginsHeaderList",
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
            type_hints = typing.get_type_hints(LoadBalancerPoolOriginsHeaderList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "LoadBalancerPoolOriginsHeaderOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerPoolOriginsHeaderList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LoadBalancerPoolOriginsHeaderOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerPoolOriginsHeaderList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadBalancerPoolOriginsHeaderList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadBalancerPoolOriginsHeaderList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerPoolOriginsHeader]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerPoolOriginsHeader]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerPoolOriginsHeader]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerPoolOriginsHeaderList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadBalancerPoolOriginsHeaderOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.loadBalancerPool.LoadBalancerPoolOriginsHeaderOutputReference",
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
            type_hints = typing.get_type_hints(LoadBalancerPoolOriginsHeaderOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="headerInput")
    def header_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="header")
    def header(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "header"))

    @header.setter
    def header(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerPoolOriginsHeaderOutputReference, "header").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "header", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerPoolOriginsHeaderOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LoadBalancerPoolOriginsHeader, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LoadBalancerPoolOriginsHeader, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LoadBalancerPoolOriginsHeader, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerPoolOriginsHeaderOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadBalancerPoolOriginsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.loadBalancerPool.LoadBalancerPoolOriginsList",
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
            type_hints = typing.get_type_hints(LoadBalancerPoolOriginsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "LoadBalancerPoolOriginsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerPoolOriginsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LoadBalancerPoolOriginsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerPoolOriginsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadBalancerPoolOriginsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadBalancerPoolOriginsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerPoolOrigins]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerPoolOrigins]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerPoolOrigins]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerPoolOriginsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadBalancerPoolOriginsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.loadBalancerPool.LoadBalancerPoolOriginsOutputReference",
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
            type_hints = typing.get_type_hints(LoadBalancerPoolOriginsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putHeader")
    def put_header(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LoadBalancerPoolOriginsHeader, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerPoolOriginsOutputReference.put_header)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHeader", [value]))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetHeader")
    def reset_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeader", []))

    @jsii.member(jsii_name="resetWeight")
    def reset_weight(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeight", []))

    @builtins.property
    @jsii.member(jsii_name="header")
    def header(self) -> LoadBalancerPoolOriginsHeaderList:
        return typing.cast(LoadBalancerPoolOriginsHeaderList, jsii.get(self, "header"))

    @builtins.property
    @jsii.member(jsii_name="addressInput")
    def address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addressInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="headerInput")
    def header_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerPoolOriginsHeader]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerPoolOriginsHeader]]], jsii.get(self, "headerInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="weightInput")
    def weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weightInput"))

    @builtins.property
    @jsii.member(jsii_name="address")
    def address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "address"))

    @address.setter
    def address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerPoolOriginsOutputReference, "address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "address", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerPoolOriginsOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerPoolOriginsOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="weight")
    def weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weight"))

    @weight.setter
    def weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerPoolOriginsOutputReference, "weight").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weight", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LoadBalancerPoolOrigins, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LoadBalancerPoolOrigins, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LoadBalancerPoolOrigins, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerPoolOriginsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "LoadBalancerPool",
    "LoadBalancerPoolConfig",
    "LoadBalancerPoolLoadShedding",
    "LoadBalancerPoolLoadSheddingList",
    "LoadBalancerPoolLoadSheddingOutputReference",
    "LoadBalancerPoolOriginSteering",
    "LoadBalancerPoolOriginSteeringList",
    "LoadBalancerPoolOriginSteeringOutputReference",
    "LoadBalancerPoolOrigins",
    "LoadBalancerPoolOriginsHeader",
    "LoadBalancerPoolOriginsHeaderList",
    "LoadBalancerPoolOriginsHeaderOutputReference",
    "LoadBalancerPoolOriginsList",
    "LoadBalancerPoolOriginsOutputReference",
]

publication.publish()
