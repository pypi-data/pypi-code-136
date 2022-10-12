'''
# `azurerm_media_asset_filter`

Refer to the Terraform Registory for docs: [`azurerm_media_asset_filter`](https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter).
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


class MediaAssetFilter(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaAssetFilter.MediaAssetFilter",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter azurerm_media_asset_filter}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        asset_id: builtins.str,
        name: builtins.str,
        first_quality_bitrate: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        presentation_time_range: typing.Optional[typing.Union["MediaAssetFilterPresentationTimeRange", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["MediaAssetFilterTimeouts", typing.Dict[str, typing.Any]]] = None,
        track_selection: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MediaAssetFilterTrackSelection", typing.Dict[str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter azurerm_media_asset_filter} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param asset_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#asset_id MediaAssetFilter#asset_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#name MediaAssetFilter#name}.
        :param first_quality_bitrate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#first_quality_bitrate MediaAssetFilter#first_quality_bitrate}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#id MediaAssetFilter#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param presentation_time_range: presentation_time_range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#presentation_time_range MediaAssetFilter#presentation_time_range}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#timeouts MediaAssetFilter#timeouts}
        :param track_selection: track_selection block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#track_selection MediaAssetFilter#track_selection}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaAssetFilter.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MediaAssetFilterConfig(
            asset_id=asset_id,
            name=name,
            first_quality_bitrate=first_quality_bitrate,
            id=id,
            presentation_time_range=presentation_time_range,
            timeouts=timeouts,
            track_selection=track_selection,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putPresentationTimeRange")
    def put_presentation_time_range(
        self,
        *,
        end_in_units: typing.Optional[jsii.Number] = None,
        force_end: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        live_backoff_in_units: typing.Optional[jsii.Number] = None,
        presentation_window_in_units: typing.Optional[jsii.Number] = None,
        start_in_units: typing.Optional[jsii.Number] = None,
        unit_timescale_in_miliseconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param end_in_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#end_in_units MediaAssetFilter#end_in_units}.
        :param force_end: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#force_end MediaAssetFilter#force_end}.
        :param live_backoff_in_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#live_backoff_in_units MediaAssetFilter#live_backoff_in_units}.
        :param presentation_window_in_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#presentation_window_in_units MediaAssetFilter#presentation_window_in_units}.
        :param start_in_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#start_in_units MediaAssetFilter#start_in_units}.
        :param unit_timescale_in_miliseconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#unit_timescale_in_miliseconds MediaAssetFilter#unit_timescale_in_miliseconds}.
        '''
        value = MediaAssetFilterPresentationTimeRange(
            end_in_units=end_in_units,
            force_end=force_end,
            live_backoff_in_units=live_backoff_in_units,
            presentation_window_in_units=presentation_window_in_units,
            start_in_units=start_in_units,
            unit_timescale_in_miliseconds=unit_timescale_in_miliseconds,
        )

        return typing.cast(None, jsii.invoke(self, "putPresentationTimeRange", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#create MediaAssetFilter#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#delete MediaAssetFilter#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#read MediaAssetFilter#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#update MediaAssetFilter#update}.
        '''
        value = MediaAssetFilterTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putTrackSelection")
    def put_track_selection(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MediaAssetFilterTrackSelection", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaAssetFilter.put_track_selection)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTrackSelection", [value]))

    @jsii.member(jsii_name="resetFirstQualityBitrate")
    def reset_first_quality_bitrate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFirstQualityBitrate", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPresentationTimeRange")
    def reset_presentation_time_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPresentationTimeRange", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTrackSelection")
    def reset_track_selection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrackSelection", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="presentationTimeRange")
    def presentation_time_range(
        self,
    ) -> "MediaAssetFilterPresentationTimeRangeOutputReference":
        return typing.cast("MediaAssetFilterPresentationTimeRangeOutputReference", jsii.get(self, "presentationTimeRange"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "MediaAssetFilterTimeoutsOutputReference":
        return typing.cast("MediaAssetFilterTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="trackSelection")
    def track_selection(self) -> "MediaAssetFilterTrackSelectionList":
        return typing.cast("MediaAssetFilterTrackSelectionList", jsii.get(self, "trackSelection"))

    @builtins.property
    @jsii.member(jsii_name="assetIdInput")
    def asset_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "assetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="firstQualityBitrateInput")
    def first_quality_bitrate_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "firstQualityBitrateInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="presentationTimeRangeInput")
    def presentation_time_range_input(
        self,
    ) -> typing.Optional["MediaAssetFilterPresentationTimeRange"]:
        return typing.cast(typing.Optional["MediaAssetFilterPresentationTimeRange"], jsii.get(self, "presentationTimeRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["MediaAssetFilterTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["MediaAssetFilterTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="trackSelectionInput")
    def track_selection_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MediaAssetFilterTrackSelection"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MediaAssetFilterTrackSelection"]]], jsii.get(self, "trackSelectionInput"))

    @builtins.property
    @jsii.member(jsii_name="assetId")
    def asset_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "assetId"))

    @asset_id.setter
    def asset_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaAssetFilter, "asset_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assetId", value)

    @builtins.property
    @jsii.member(jsii_name="firstQualityBitrate")
    def first_quality_bitrate(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "firstQualityBitrate"))

    @first_quality_bitrate.setter
    def first_quality_bitrate(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaAssetFilter, "first_quality_bitrate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firstQualityBitrate", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaAssetFilter, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaAssetFilter, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaAssetFilter.MediaAssetFilterConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "asset_id": "assetId",
        "name": "name",
        "first_quality_bitrate": "firstQualityBitrate",
        "id": "id",
        "presentation_time_range": "presentationTimeRange",
        "timeouts": "timeouts",
        "track_selection": "trackSelection",
    },
)
class MediaAssetFilterConfig(cdktf.TerraformMetaArguments):
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
        asset_id: builtins.str,
        name: builtins.str,
        first_quality_bitrate: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        presentation_time_range: typing.Optional[typing.Union["MediaAssetFilterPresentationTimeRange", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["MediaAssetFilterTimeouts", typing.Dict[str, typing.Any]]] = None,
        track_selection: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MediaAssetFilterTrackSelection", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param asset_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#asset_id MediaAssetFilter#asset_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#name MediaAssetFilter#name}.
        :param first_quality_bitrate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#first_quality_bitrate MediaAssetFilter#first_quality_bitrate}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#id MediaAssetFilter#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param presentation_time_range: presentation_time_range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#presentation_time_range MediaAssetFilter#presentation_time_range}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#timeouts MediaAssetFilter#timeouts}
        :param track_selection: track_selection block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#track_selection MediaAssetFilter#track_selection}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(presentation_time_range, dict):
            presentation_time_range = MediaAssetFilterPresentationTimeRange(**presentation_time_range)
        if isinstance(timeouts, dict):
            timeouts = MediaAssetFilterTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(MediaAssetFilterConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument asset_id", value=asset_id, expected_type=type_hints["asset_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument first_quality_bitrate", value=first_quality_bitrate, expected_type=type_hints["first_quality_bitrate"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument presentation_time_range", value=presentation_time_range, expected_type=type_hints["presentation_time_range"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument track_selection", value=track_selection, expected_type=type_hints["track_selection"])
        self._values: typing.Dict[str, typing.Any] = {
            "asset_id": asset_id,
            "name": name,
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
        if first_quality_bitrate is not None:
            self._values["first_quality_bitrate"] = first_quality_bitrate
        if id is not None:
            self._values["id"] = id
        if presentation_time_range is not None:
            self._values["presentation_time_range"] = presentation_time_range
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if track_selection is not None:
            self._values["track_selection"] = track_selection

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
    def asset_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#asset_id MediaAssetFilter#asset_id}.'''
        result = self._values.get("asset_id")
        assert result is not None, "Required property 'asset_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#name MediaAssetFilter#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def first_quality_bitrate(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#first_quality_bitrate MediaAssetFilter#first_quality_bitrate}.'''
        result = self._values.get("first_quality_bitrate")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#id MediaAssetFilter#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def presentation_time_range(
        self,
    ) -> typing.Optional["MediaAssetFilterPresentationTimeRange"]:
        '''presentation_time_range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#presentation_time_range MediaAssetFilter#presentation_time_range}
        '''
        result = self._values.get("presentation_time_range")
        return typing.cast(typing.Optional["MediaAssetFilterPresentationTimeRange"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["MediaAssetFilterTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#timeouts MediaAssetFilter#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["MediaAssetFilterTimeouts"], result)

    @builtins.property
    def track_selection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MediaAssetFilterTrackSelection"]]]:
        '''track_selection block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#track_selection MediaAssetFilter#track_selection}
        '''
        result = self._values.get("track_selection")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MediaAssetFilterTrackSelection"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaAssetFilterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaAssetFilter.MediaAssetFilterPresentationTimeRange",
    jsii_struct_bases=[],
    name_mapping={
        "end_in_units": "endInUnits",
        "force_end": "forceEnd",
        "live_backoff_in_units": "liveBackoffInUnits",
        "presentation_window_in_units": "presentationWindowInUnits",
        "start_in_units": "startInUnits",
        "unit_timescale_in_miliseconds": "unitTimescaleInMiliseconds",
    },
)
class MediaAssetFilterPresentationTimeRange:
    def __init__(
        self,
        *,
        end_in_units: typing.Optional[jsii.Number] = None,
        force_end: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        live_backoff_in_units: typing.Optional[jsii.Number] = None,
        presentation_window_in_units: typing.Optional[jsii.Number] = None,
        start_in_units: typing.Optional[jsii.Number] = None,
        unit_timescale_in_miliseconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param end_in_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#end_in_units MediaAssetFilter#end_in_units}.
        :param force_end: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#force_end MediaAssetFilter#force_end}.
        :param live_backoff_in_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#live_backoff_in_units MediaAssetFilter#live_backoff_in_units}.
        :param presentation_window_in_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#presentation_window_in_units MediaAssetFilter#presentation_window_in_units}.
        :param start_in_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#start_in_units MediaAssetFilter#start_in_units}.
        :param unit_timescale_in_miliseconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#unit_timescale_in_miliseconds MediaAssetFilter#unit_timescale_in_miliseconds}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaAssetFilterPresentationTimeRange.__init__)
            check_type(argname="argument end_in_units", value=end_in_units, expected_type=type_hints["end_in_units"])
            check_type(argname="argument force_end", value=force_end, expected_type=type_hints["force_end"])
            check_type(argname="argument live_backoff_in_units", value=live_backoff_in_units, expected_type=type_hints["live_backoff_in_units"])
            check_type(argname="argument presentation_window_in_units", value=presentation_window_in_units, expected_type=type_hints["presentation_window_in_units"])
            check_type(argname="argument start_in_units", value=start_in_units, expected_type=type_hints["start_in_units"])
            check_type(argname="argument unit_timescale_in_miliseconds", value=unit_timescale_in_miliseconds, expected_type=type_hints["unit_timescale_in_miliseconds"])
        self._values: typing.Dict[str, typing.Any] = {}
        if end_in_units is not None:
            self._values["end_in_units"] = end_in_units
        if force_end is not None:
            self._values["force_end"] = force_end
        if live_backoff_in_units is not None:
            self._values["live_backoff_in_units"] = live_backoff_in_units
        if presentation_window_in_units is not None:
            self._values["presentation_window_in_units"] = presentation_window_in_units
        if start_in_units is not None:
            self._values["start_in_units"] = start_in_units
        if unit_timescale_in_miliseconds is not None:
            self._values["unit_timescale_in_miliseconds"] = unit_timescale_in_miliseconds

    @builtins.property
    def end_in_units(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#end_in_units MediaAssetFilter#end_in_units}.'''
        result = self._values.get("end_in_units")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def force_end(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#force_end MediaAssetFilter#force_end}.'''
        result = self._values.get("force_end")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def live_backoff_in_units(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#live_backoff_in_units MediaAssetFilter#live_backoff_in_units}.'''
        result = self._values.get("live_backoff_in_units")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def presentation_window_in_units(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#presentation_window_in_units MediaAssetFilter#presentation_window_in_units}.'''
        result = self._values.get("presentation_window_in_units")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def start_in_units(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#start_in_units MediaAssetFilter#start_in_units}.'''
        result = self._values.get("start_in_units")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def unit_timescale_in_miliseconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#unit_timescale_in_miliseconds MediaAssetFilter#unit_timescale_in_miliseconds}.'''
        result = self._values.get("unit_timescale_in_miliseconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaAssetFilterPresentationTimeRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MediaAssetFilterPresentationTimeRangeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaAssetFilter.MediaAssetFilterPresentationTimeRangeOutputReference",
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
            type_hints = typing.get_type_hints(MediaAssetFilterPresentationTimeRangeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEndInUnits")
    def reset_end_in_units(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndInUnits", []))

    @jsii.member(jsii_name="resetForceEnd")
    def reset_force_end(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceEnd", []))

    @jsii.member(jsii_name="resetLiveBackoffInUnits")
    def reset_live_backoff_in_units(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLiveBackoffInUnits", []))

    @jsii.member(jsii_name="resetPresentationWindowInUnits")
    def reset_presentation_window_in_units(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPresentationWindowInUnits", []))

    @jsii.member(jsii_name="resetStartInUnits")
    def reset_start_in_units(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartInUnits", []))

    @jsii.member(jsii_name="resetUnitTimescaleInMiliseconds")
    def reset_unit_timescale_in_miliseconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnitTimescaleInMiliseconds", []))

    @builtins.property
    @jsii.member(jsii_name="endInUnitsInput")
    def end_in_units_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "endInUnitsInput"))

    @builtins.property
    @jsii.member(jsii_name="forceEndInput")
    def force_end_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "forceEndInput"))

    @builtins.property
    @jsii.member(jsii_name="liveBackoffInUnitsInput")
    def live_backoff_in_units_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "liveBackoffInUnitsInput"))

    @builtins.property
    @jsii.member(jsii_name="presentationWindowInUnitsInput")
    def presentation_window_in_units_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "presentationWindowInUnitsInput"))

    @builtins.property
    @jsii.member(jsii_name="startInUnitsInput")
    def start_in_units_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "startInUnitsInput"))

    @builtins.property
    @jsii.member(jsii_name="unitTimescaleInMilisecondsInput")
    def unit_timescale_in_miliseconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "unitTimescaleInMilisecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="endInUnits")
    def end_in_units(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "endInUnits"))

    @end_in_units.setter
    def end_in_units(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaAssetFilterPresentationTimeRangeOutputReference, "end_in_units").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endInUnits", value)

    @builtins.property
    @jsii.member(jsii_name="forceEnd")
    def force_end(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "forceEnd"))

    @force_end.setter
    def force_end(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaAssetFilterPresentationTimeRangeOutputReference, "force_end").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceEnd", value)

    @builtins.property
    @jsii.member(jsii_name="liveBackoffInUnits")
    def live_backoff_in_units(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "liveBackoffInUnits"))

    @live_backoff_in_units.setter
    def live_backoff_in_units(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaAssetFilterPresentationTimeRangeOutputReference, "live_backoff_in_units").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "liveBackoffInUnits", value)

    @builtins.property
    @jsii.member(jsii_name="presentationWindowInUnits")
    def presentation_window_in_units(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "presentationWindowInUnits"))

    @presentation_window_in_units.setter
    def presentation_window_in_units(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaAssetFilterPresentationTimeRangeOutputReference, "presentation_window_in_units").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "presentationWindowInUnits", value)

    @builtins.property
    @jsii.member(jsii_name="startInUnits")
    def start_in_units(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "startInUnits"))

    @start_in_units.setter
    def start_in_units(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaAssetFilterPresentationTimeRangeOutputReference, "start_in_units").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startInUnits", value)

    @builtins.property
    @jsii.member(jsii_name="unitTimescaleInMiliseconds")
    def unit_timescale_in_miliseconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "unitTimescaleInMiliseconds"))

    @unit_timescale_in_miliseconds.setter
    def unit_timescale_in_miliseconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaAssetFilterPresentationTimeRangeOutputReference, "unit_timescale_in_miliseconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unitTimescaleInMiliseconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MediaAssetFilterPresentationTimeRange]:
        return typing.cast(typing.Optional[MediaAssetFilterPresentationTimeRange], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MediaAssetFilterPresentationTimeRange],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaAssetFilterPresentationTimeRangeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaAssetFilter.MediaAssetFilterTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class MediaAssetFilterTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#create MediaAssetFilter#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#delete MediaAssetFilter#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#read MediaAssetFilter#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#update MediaAssetFilter#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaAssetFilterTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#create MediaAssetFilter#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#delete MediaAssetFilter#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#read MediaAssetFilter#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#update MediaAssetFilter#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaAssetFilterTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MediaAssetFilterTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaAssetFilter.MediaAssetFilterTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(MediaAssetFilterTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(MediaAssetFilterTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaAssetFilterTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaAssetFilterTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaAssetFilterTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MediaAssetFilterTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MediaAssetFilterTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MediaAssetFilterTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaAssetFilterTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaAssetFilter.MediaAssetFilterTrackSelection",
    jsii_struct_bases=[],
    name_mapping={"condition": "condition"},
)
class MediaAssetFilterTrackSelection:
    def __init__(
        self,
        *,
        condition: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MediaAssetFilterTrackSelectionCondition", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param condition: condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#condition MediaAssetFilter#condition}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaAssetFilterTrackSelection.__init__)
            check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
        self._values: typing.Dict[str, typing.Any] = {
            "condition": condition,
        }

    @builtins.property
    def condition(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["MediaAssetFilterTrackSelectionCondition"]]:
        '''condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#condition MediaAssetFilter#condition}
        '''
        result = self._values.get("condition")
        assert result is not None, "Required property 'condition' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["MediaAssetFilterTrackSelectionCondition"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaAssetFilterTrackSelection(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mediaAssetFilter.MediaAssetFilterTrackSelectionCondition",
    jsii_struct_bases=[],
    name_mapping={"operation": "operation", "property": "property", "value": "value"},
)
class MediaAssetFilterTrackSelectionCondition:
    def __init__(
        self,
        *,
        operation: typing.Optional[builtins.str] = None,
        property: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param operation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#operation MediaAssetFilter#operation}.
        :param property: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#property MediaAssetFilter#property}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#value MediaAssetFilter#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaAssetFilterTrackSelectionCondition.__init__)
            check_type(argname="argument operation", value=operation, expected_type=type_hints["operation"])
            check_type(argname="argument property", value=property, expected_type=type_hints["property"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if operation is not None:
            self._values["operation"] = operation
        if property is not None:
            self._values["property"] = property
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def operation(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#operation MediaAssetFilter#operation}.'''
        result = self._values.get("operation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def property(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#property MediaAssetFilter#property}.'''
        result = self._values.get("property")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/media_asset_filter#value MediaAssetFilter#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaAssetFilterTrackSelectionCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MediaAssetFilterTrackSelectionConditionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaAssetFilter.MediaAssetFilterTrackSelectionConditionList",
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
            type_hints = typing.get_type_hints(MediaAssetFilterTrackSelectionConditionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MediaAssetFilterTrackSelectionConditionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaAssetFilterTrackSelectionConditionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MediaAssetFilterTrackSelectionConditionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaAssetFilterTrackSelectionConditionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MediaAssetFilterTrackSelectionConditionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MediaAssetFilterTrackSelectionConditionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MediaAssetFilterTrackSelectionCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MediaAssetFilterTrackSelectionCondition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MediaAssetFilterTrackSelectionCondition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaAssetFilterTrackSelectionConditionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MediaAssetFilterTrackSelectionConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaAssetFilter.MediaAssetFilterTrackSelectionConditionOutputReference",
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
            type_hints = typing.get_type_hints(MediaAssetFilterTrackSelectionConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetOperation")
    def reset_operation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperation", []))

    @jsii.member(jsii_name="resetProperty")
    def reset_property(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProperty", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="operationInput")
    def operation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operationInput"))

    @builtins.property
    @jsii.member(jsii_name="propertyInput")
    def property_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "propertyInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="operation")
    def operation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operation"))

    @operation.setter
    def operation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaAssetFilterTrackSelectionConditionOutputReference, "operation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operation", value)

    @builtins.property
    @jsii.member(jsii_name="property")
    def property(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "property"))

    @property.setter
    def property(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaAssetFilterTrackSelectionConditionOutputReference, "property").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "property", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaAssetFilterTrackSelectionConditionOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MediaAssetFilterTrackSelectionCondition, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MediaAssetFilterTrackSelectionCondition, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MediaAssetFilterTrackSelectionCondition, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaAssetFilterTrackSelectionConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MediaAssetFilterTrackSelectionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaAssetFilter.MediaAssetFilterTrackSelectionList",
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
            type_hints = typing.get_type_hints(MediaAssetFilterTrackSelectionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MediaAssetFilterTrackSelectionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaAssetFilterTrackSelectionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MediaAssetFilterTrackSelectionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaAssetFilterTrackSelectionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MediaAssetFilterTrackSelectionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MediaAssetFilterTrackSelectionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MediaAssetFilterTrackSelection]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MediaAssetFilterTrackSelection]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MediaAssetFilterTrackSelection]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaAssetFilterTrackSelectionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MediaAssetFilterTrackSelectionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mediaAssetFilter.MediaAssetFilterTrackSelectionOutputReference",
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
            type_hints = typing.get_type_hints(MediaAssetFilterTrackSelectionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCondition")
    def put_condition(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[MediaAssetFilterTrackSelectionCondition, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MediaAssetFilterTrackSelectionOutputReference.put_condition)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCondition", [value]))

    @builtins.property
    @jsii.member(jsii_name="condition")
    def condition(self) -> MediaAssetFilterTrackSelectionConditionList:
        return typing.cast(MediaAssetFilterTrackSelectionConditionList, jsii.get(self, "condition"))

    @builtins.property
    @jsii.member(jsii_name="conditionInput")
    def condition_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MediaAssetFilterTrackSelectionCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MediaAssetFilterTrackSelectionCondition]]], jsii.get(self, "conditionInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MediaAssetFilterTrackSelection, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MediaAssetFilterTrackSelection, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MediaAssetFilterTrackSelection, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MediaAssetFilterTrackSelectionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MediaAssetFilter",
    "MediaAssetFilterConfig",
    "MediaAssetFilterPresentationTimeRange",
    "MediaAssetFilterPresentationTimeRangeOutputReference",
    "MediaAssetFilterTimeouts",
    "MediaAssetFilterTimeoutsOutputReference",
    "MediaAssetFilterTrackSelection",
    "MediaAssetFilterTrackSelectionCondition",
    "MediaAssetFilterTrackSelectionConditionList",
    "MediaAssetFilterTrackSelectionConditionOutputReference",
    "MediaAssetFilterTrackSelectionList",
    "MediaAssetFilterTrackSelectionOutputReference",
]

publication.publish()
