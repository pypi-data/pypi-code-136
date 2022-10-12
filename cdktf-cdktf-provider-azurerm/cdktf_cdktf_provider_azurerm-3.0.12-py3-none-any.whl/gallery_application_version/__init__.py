'''
# `azurerm_gallery_application_version`

Refer to the Terraform Registory for docs: [`azurerm_gallery_application_version`](https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version).
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


class GalleryApplicationVersion(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.galleryApplicationVersion.GalleryApplicationVersion",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version azurerm_gallery_application_version}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        gallery_application_id: builtins.str,
        location: builtins.str,
        manage_action: typing.Union["GalleryApplicationVersionManageAction", typing.Dict[str, typing.Any]],
        name: builtins.str,
        source: typing.Union["GalleryApplicationVersionSource", typing.Dict[str, typing.Any]],
        target_region: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GalleryApplicationVersionTargetRegion", typing.Dict[str, typing.Any]]]],
        enable_health_check: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        end_of_life_date: typing.Optional[builtins.str] = None,
        exclude_from_latest: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["GalleryApplicationVersionTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version azurerm_gallery_application_version} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param gallery_application_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#gallery_application_id GalleryApplicationVersion#gallery_application_id}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#location GalleryApplicationVersion#location}.
        :param manage_action: manage_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#manage_action GalleryApplicationVersion#manage_action}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#name GalleryApplicationVersion#name}.
        :param source: source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#source GalleryApplicationVersion#source}
        :param target_region: target_region block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#target_region GalleryApplicationVersion#target_region}
        :param enable_health_check: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#enable_health_check GalleryApplicationVersion#enable_health_check}.
        :param end_of_life_date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#end_of_life_date GalleryApplicationVersion#end_of_life_date}.
        :param exclude_from_latest: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#exclude_from_latest GalleryApplicationVersion#exclude_from_latest}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#id GalleryApplicationVersion#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#tags GalleryApplicationVersion#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#timeouts GalleryApplicationVersion#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GalleryApplicationVersion.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GalleryApplicationVersionConfig(
            gallery_application_id=gallery_application_id,
            location=location,
            manage_action=manage_action,
            name=name,
            source=source,
            target_region=target_region,
            enable_health_check=enable_health_check,
            end_of_life_date=end_of_life_date,
            exclude_from_latest=exclude_from_latest,
            id=id,
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

    @jsii.member(jsii_name="putManageAction")
    def put_manage_action(
        self,
        *,
        install: builtins.str,
        remove: builtins.str,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param install: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#install GalleryApplicationVersion#install}.
        :param remove: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#remove GalleryApplicationVersion#remove}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#update GalleryApplicationVersion#update}.
        '''
        value = GalleryApplicationVersionManageAction(
            install=install, remove=remove, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putManageAction", [value]))

    @jsii.member(jsii_name="putSource")
    def put_source(
        self,
        *,
        media_link: builtins.str,
        default_configuration_link: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param media_link: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#media_link GalleryApplicationVersion#media_link}.
        :param default_configuration_link: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#default_configuration_link GalleryApplicationVersion#default_configuration_link}.
        '''
        value = GalleryApplicationVersionSource(
            media_link=media_link,
            default_configuration_link=default_configuration_link,
        )

        return typing.cast(None, jsii.invoke(self, "putSource", [value]))

    @jsii.member(jsii_name="putTargetRegion")
    def put_target_region(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GalleryApplicationVersionTargetRegion", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GalleryApplicationVersion.put_target_region)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTargetRegion", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#create GalleryApplicationVersion#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#delete GalleryApplicationVersion#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#read GalleryApplicationVersion#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#update GalleryApplicationVersion#update}.
        '''
        value = GalleryApplicationVersionTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetEnableHealthCheck")
    def reset_enable_health_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableHealthCheck", []))

    @jsii.member(jsii_name="resetEndOfLifeDate")
    def reset_end_of_life_date(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndOfLifeDate", []))

    @jsii.member(jsii_name="resetExcludeFromLatest")
    def reset_exclude_from_latest(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludeFromLatest", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    @jsii.member(jsii_name="manageAction")
    def manage_action(self) -> "GalleryApplicationVersionManageActionOutputReference":
        return typing.cast("GalleryApplicationVersionManageActionOutputReference", jsii.get(self, "manageAction"))

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> "GalleryApplicationVersionSourceOutputReference":
        return typing.cast("GalleryApplicationVersionSourceOutputReference", jsii.get(self, "source"))

    @builtins.property
    @jsii.member(jsii_name="targetRegion")
    def target_region(self) -> "GalleryApplicationVersionTargetRegionList":
        return typing.cast("GalleryApplicationVersionTargetRegionList", jsii.get(self, "targetRegion"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GalleryApplicationVersionTimeoutsOutputReference":
        return typing.cast("GalleryApplicationVersionTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="enableHealthCheckInput")
    def enable_health_check_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableHealthCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="endOfLifeDateInput")
    def end_of_life_date_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endOfLifeDateInput"))

    @builtins.property
    @jsii.member(jsii_name="excludeFromLatestInput")
    def exclude_from_latest_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "excludeFromLatestInput"))

    @builtins.property
    @jsii.member(jsii_name="galleryApplicationIdInput")
    def gallery_application_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "galleryApplicationIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="manageActionInput")
    def manage_action_input(
        self,
    ) -> typing.Optional["GalleryApplicationVersionManageAction"]:
        return typing.cast(typing.Optional["GalleryApplicationVersionManageAction"], jsii.get(self, "manageActionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional["GalleryApplicationVersionSource"]:
        return typing.cast(typing.Optional["GalleryApplicationVersionSource"], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="targetRegionInput")
    def target_region_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GalleryApplicationVersionTargetRegion"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GalleryApplicationVersionTargetRegion"]]], jsii.get(self, "targetRegionInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GalleryApplicationVersionTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GalleryApplicationVersionTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="enableHealthCheck")
    def enable_health_check(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableHealthCheck"))

    @enable_health_check.setter
    def enable_health_check(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GalleryApplicationVersion, "enable_health_check").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableHealthCheck", value)

    @builtins.property
    @jsii.member(jsii_name="endOfLifeDate")
    def end_of_life_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endOfLifeDate"))

    @end_of_life_date.setter
    def end_of_life_date(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GalleryApplicationVersion, "end_of_life_date").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endOfLifeDate", value)

    @builtins.property
    @jsii.member(jsii_name="excludeFromLatest")
    def exclude_from_latest(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "excludeFromLatest"))

    @exclude_from_latest.setter
    def exclude_from_latest(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GalleryApplicationVersion, "exclude_from_latest").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludeFromLatest", value)

    @builtins.property
    @jsii.member(jsii_name="galleryApplicationId")
    def gallery_application_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "galleryApplicationId"))

    @gallery_application_id.setter
    def gallery_application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GalleryApplicationVersion, "gallery_application_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "galleryApplicationId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GalleryApplicationVersion, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GalleryApplicationVersion, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GalleryApplicationVersion, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GalleryApplicationVersion, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.galleryApplicationVersion.GalleryApplicationVersionConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "gallery_application_id": "galleryApplicationId",
        "location": "location",
        "manage_action": "manageAction",
        "name": "name",
        "source": "source",
        "target_region": "targetRegion",
        "enable_health_check": "enableHealthCheck",
        "end_of_life_date": "endOfLifeDate",
        "exclude_from_latest": "excludeFromLatest",
        "id": "id",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class GalleryApplicationVersionConfig(cdktf.TerraformMetaArguments):
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
        gallery_application_id: builtins.str,
        location: builtins.str,
        manage_action: typing.Union["GalleryApplicationVersionManageAction", typing.Dict[str, typing.Any]],
        name: builtins.str,
        source: typing.Union["GalleryApplicationVersionSource", typing.Dict[str, typing.Any]],
        target_region: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GalleryApplicationVersionTargetRegion", typing.Dict[str, typing.Any]]]],
        enable_health_check: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        end_of_life_date: typing.Optional[builtins.str] = None,
        exclude_from_latest: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["GalleryApplicationVersionTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param gallery_application_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#gallery_application_id GalleryApplicationVersion#gallery_application_id}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#location GalleryApplicationVersion#location}.
        :param manage_action: manage_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#manage_action GalleryApplicationVersion#manage_action}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#name GalleryApplicationVersion#name}.
        :param source: source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#source GalleryApplicationVersion#source}
        :param target_region: target_region block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#target_region GalleryApplicationVersion#target_region}
        :param enable_health_check: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#enable_health_check GalleryApplicationVersion#enable_health_check}.
        :param end_of_life_date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#end_of_life_date GalleryApplicationVersion#end_of_life_date}.
        :param exclude_from_latest: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#exclude_from_latest GalleryApplicationVersion#exclude_from_latest}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#id GalleryApplicationVersion#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#tags GalleryApplicationVersion#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#timeouts GalleryApplicationVersion#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(manage_action, dict):
            manage_action = GalleryApplicationVersionManageAction(**manage_action)
        if isinstance(source, dict):
            source = GalleryApplicationVersionSource(**source)
        if isinstance(timeouts, dict):
            timeouts = GalleryApplicationVersionTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GalleryApplicationVersionConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument gallery_application_id", value=gallery_application_id, expected_type=type_hints["gallery_application_id"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument manage_action", value=manage_action, expected_type=type_hints["manage_action"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument target_region", value=target_region, expected_type=type_hints["target_region"])
            check_type(argname="argument enable_health_check", value=enable_health_check, expected_type=type_hints["enable_health_check"])
            check_type(argname="argument end_of_life_date", value=end_of_life_date, expected_type=type_hints["end_of_life_date"])
            check_type(argname="argument exclude_from_latest", value=exclude_from_latest, expected_type=type_hints["exclude_from_latest"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "gallery_application_id": gallery_application_id,
            "location": location,
            "manage_action": manage_action,
            "name": name,
            "source": source,
            "target_region": target_region,
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
        if enable_health_check is not None:
            self._values["enable_health_check"] = enable_health_check
        if end_of_life_date is not None:
            self._values["end_of_life_date"] = end_of_life_date
        if exclude_from_latest is not None:
            self._values["exclude_from_latest"] = exclude_from_latest
        if id is not None:
            self._values["id"] = id
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
    def gallery_application_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#gallery_application_id GalleryApplicationVersion#gallery_application_id}.'''
        result = self._values.get("gallery_application_id")
        assert result is not None, "Required property 'gallery_application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#location GalleryApplicationVersion#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def manage_action(self) -> "GalleryApplicationVersionManageAction":
        '''manage_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#manage_action GalleryApplicationVersion#manage_action}
        '''
        result = self._values.get("manage_action")
        assert result is not None, "Required property 'manage_action' is missing"
        return typing.cast("GalleryApplicationVersionManageAction", result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#name GalleryApplicationVersion#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source(self) -> "GalleryApplicationVersionSource":
        '''source block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#source GalleryApplicationVersion#source}
        '''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast("GalleryApplicationVersionSource", result)

    @builtins.property
    def target_region(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["GalleryApplicationVersionTargetRegion"]]:
        '''target_region block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#target_region GalleryApplicationVersion#target_region}
        '''
        result = self._values.get("target_region")
        assert result is not None, "Required property 'target_region' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["GalleryApplicationVersionTargetRegion"]], result)

    @builtins.property
    def enable_health_check(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#enable_health_check GalleryApplicationVersion#enable_health_check}.'''
        result = self._values.get("enable_health_check")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def end_of_life_date(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#end_of_life_date GalleryApplicationVersion#end_of_life_date}.'''
        result = self._values.get("end_of_life_date")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def exclude_from_latest(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#exclude_from_latest GalleryApplicationVersion#exclude_from_latest}.'''
        result = self._values.get("exclude_from_latest")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#id GalleryApplicationVersion#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#tags GalleryApplicationVersion#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GalleryApplicationVersionTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#timeouts GalleryApplicationVersion#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GalleryApplicationVersionTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GalleryApplicationVersionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.galleryApplicationVersion.GalleryApplicationVersionManageAction",
    jsii_struct_bases=[],
    name_mapping={"install": "install", "remove": "remove", "update": "update"},
)
class GalleryApplicationVersionManageAction:
    def __init__(
        self,
        *,
        install: builtins.str,
        remove: builtins.str,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param install: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#install GalleryApplicationVersion#install}.
        :param remove: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#remove GalleryApplicationVersion#remove}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#update GalleryApplicationVersion#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GalleryApplicationVersionManageAction.__init__)
            check_type(argname="argument install", value=install, expected_type=type_hints["install"])
            check_type(argname="argument remove", value=remove, expected_type=type_hints["remove"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {
            "install": install,
            "remove": remove,
        }
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def install(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#install GalleryApplicationVersion#install}.'''
        result = self._values.get("install")
        assert result is not None, "Required property 'install' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def remove(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#remove GalleryApplicationVersion#remove}.'''
        result = self._values.get("remove")
        assert result is not None, "Required property 'remove' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#update GalleryApplicationVersion#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GalleryApplicationVersionManageAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GalleryApplicationVersionManageActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.galleryApplicationVersion.GalleryApplicationVersionManageActionOutputReference",
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
            type_hints = typing.get_type_hints(GalleryApplicationVersionManageActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="installInput")
    def install_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "installInput"))

    @builtins.property
    @jsii.member(jsii_name="removeInput")
    def remove_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "removeInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="install")
    def install(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "install"))

    @install.setter
    def install(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GalleryApplicationVersionManageActionOutputReference, "install").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "install", value)

    @builtins.property
    @jsii.member(jsii_name="remove")
    def remove(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "remove"))

    @remove.setter
    def remove(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GalleryApplicationVersionManageActionOutputReference, "remove").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "remove", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GalleryApplicationVersionManageActionOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GalleryApplicationVersionManageAction]:
        return typing.cast(typing.Optional[GalleryApplicationVersionManageAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GalleryApplicationVersionManageAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GalleryApplicationVersionManageActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.galleryApplicationVersion.GalleryApplicationVersionSource",
    jsii_struct_bases=[],
    name_mapping={
        "media_link": "mediaLink",
        "default_configuration_link": "defaultConfigurationLink",
    },
)
class GalleryApplicationVersionSource:
    def __init__(
        self,
        *,
        media_link: builtins.str,
        default_configuration_link: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param media_link: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#media_link GalleryApplicationVersion#media_link}.
        :param default_configuration_link: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#default_configuration_link GalleryApplicationVersion#default_configuration_link}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GalleryApplicationVersionSource.__init__)
            check_type(argname="argument media_link", value=media_link, expected_type=type_hints["media_link"])
            check_type(argname="argument default_configuration_link", value=default_configuration_link, expected_type=type_hints["default_configuration_link"])
        self._values: typing.Dict[str, typing.Any] = {
            "media_link": media_link,
        }
        if default_configuration_link is not None:
            self._values["default_configuration_link"] = default_configuration_link

    @builtins.property
    def media_link(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#media_link GalleryApplicationVersion#media_link}.'''
        result = self._values.get("media_link")
        assert result is not None, "Required property 'media_link' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_configuration_link(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#default_configuration_link GalleryApplicationVersion#default_configuration_link}.'''
        result = self._values.get("default_configuration_link")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GalleryApplicationVersionSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GalleryApplicationVersionSourceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.galleryApplicationVersion.GalleryApplicationVersionSourceOutputReference",
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
            type_hints = typing.get_type_hints(GalleryApplicationVersionSourceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDefaultConfigurationLink")
    def reset_default_configuration_link(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultConfigurationLink", []))

    @builtins.property
    @jsii.member(jsii_name="defaultConfigurationLinkInput")
    def default_configuration_link_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultConfigurationLinkInput"))

    @builtins.property
    @jsii.member(jsii_name="mediaLinkInput")
    def media_link_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mediaLinkInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultConfigurationLink")
    def default_configuration_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultConfigurationLink"))

    @default_configuration_link.setter
    def default_configuration_link(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GalleryApplicationVersionSourceOutputReference, "default_configuration_link").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultConfigurationLink", value)

    @builtins.property
    @jsii.member(jsii_name="mediaLink")
    def media_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mediaLink"))

    @media_link.setter
    def media_link(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GalleryApplicationVersionSourceOutputReference, "media_link").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mediaLink", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GalleryApplicationVersionSource]:
        return typing.cast(typing.Optional[GalleryApplicationVersionSource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GalleryApplicationVersionSource],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GalleryApplicationVersionSourceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.galleryApplicationVersion.GalleryApplicationVersionTargetRegion",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "regional_replica_count": "regionalReplicaCount",
        "storage_account_type": "storageAccountType",
    },
)
class GalleryApplicationVersionTargetRegion:
    def __init__(
        self,
        *,
        name: builtins.str,
        regional_replica_count: jsii.Number,
        storage_account_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#name GalleryApplicationVersion#name}.
        :param regional_replica_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#regional_replica_count GalleryApplicationVersion#regional_replica_count}.
        :param storage_account_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#storage_account_type GalleryApplicationVersion#storage_account_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GalleryApplicationVersionTargetRegion.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument regional_replica_count", value=regional_replica_count, expected_type=type_hints["regional_replica_count"])
            check_type(argname="argument storage_account_type", value=storage_account_type, expected_type=type_hints["storage_account_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "regional_replica_count": regional_replica_count,
        }
        if storage_account_type is not None:
            self._values["storage_account_type"] = storage_account_type

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#name GalleryApplicationVersion#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def regional_replica_count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#regional_replica_count GalleryApplicationVersion#regional_replica_count}.'''
        result = self._values.get("regional_replica_count")
        assert result is not None, "Required property 'regional_replica_count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def storage_account_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#storage_account_type GalleryApplicationVersion#storage_account_type}.'''
        result = self._values.get("storage_account_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GalleryApplicationVersionTargetRegion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GalleryApplicationVersionTargetRegionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.galleryApplicationVersion.GalleryApplicationVersionTargetRegionList",
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
            type_hints = typing.get_type_hints(GalleryApplicationVersionTargetRegionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GalleryApplicationVersionTargetRegionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GalleryApplicationVersionTargetRegionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GalleryApplicationVersionTargetRegionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GalleryApplicationVersionTargetRegionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GalleryApplicationVersionTargetRegionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GalleryApplicationVersionTargetRegionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GalleryApplicationVersionTargetRegion]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GalleryApplicationVersionTargetRegion]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GalleryApplicationVersionTargetRegion]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GalleryApplicationVersionTargetRegionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GalleryApplicationVersionTargetRegionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.galleryApplicationVersion.GalleryApplicationVersionTargetRegionOutputReference",
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
            type_hints = typing.get_type_hints(GalleryApplicationVersionTargetRegionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetStorageAccountType")
    def reset_storage_account_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageAccountType", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="regionalReplicaCountInput")
    def regional_replica_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "regionalReplicaCountInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountTypeInput")
    def storage_account_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GalleryApplicationVersionTargetRegionOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="regionalReplicaCount")
    def regional_replica_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "regionalReplicaCount"))

    @regional_replica_count.setter
    def regional_replica_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GalleryApplicationVersionTargetRegionOutputReference, "regional_replica_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regionalReplicaCount", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountType")
    def storage_account_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountType"))

    @storage_account_type.setter
    def storage_account_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GalleryApplicationVersionTargetRegionOutputReference, "storage_account_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GalleryApplicationVersionTargetRegion, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GalleryApplicationVersionTargetRegion, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GalleryApplicationVersionTargetRegion, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GalleryApplicationVersionTargetRegionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.galleryApplicationVersion.GalleryApplicationVersionTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class GalleryApplicationVersionTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#create GalleryApplicationVersion#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#delete GalleryApplicationVersion#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#read GalleryApplicationVersion#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#update GalleryApplicationVersion#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GalleryApplicationVersionTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#create GalleryApplicationVersion#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#delete GalleryApplicationVersion#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#read GalleryApplicationVersion#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/gallery_application_version#update GalleryApplicationVersion#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GalleryApplicationVersionTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GalleryApplicationVersionTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.galleryApplicationVersion.GalleryApplicationVersionTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GalleryApplicationVersionTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GalleryApplicationVersionTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GalleryApplicationVersionTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GalleryApplicationVersionTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GalleryApplicationVersionTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GalleryApplicationVersionTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GalleryApplicationVersionTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GalleryApplicationVersionTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GalleryApplicationVersionTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GalleryApplicationVersion",
    "GalleryApplicationVersionConfig",
    "GalleryApplicationVersionManageAction",
    "GalleryApplicationVersionManageActionOutputReference",
    "GalleryApplicationVersionSource",
    "GalleryApplicationVersionSourceOutputReference",
    "GalleryApplicationVersionTargetRegion",
    "GalleryApplicationVersionTargetRegionList",
    "GalleryApplicationVersionTargetRegionOutputReference",
    "GalleryApplicationVersionTimeouts",
    "GalleryApplicationVersionTimeoutsOutputReference",
]

publication.publish()
