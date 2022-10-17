from __future__ import annotations
from typing import (Literal, Optional, Callable, Any, Tuple, TypeVar)
from ..fable_library.array import (filter as filter_1, fold)
from ..fable_library.async_builder import (singleton, Async)
from ..fable_library.reflection import (TypeInfo, class_type)
from ..fable_library.types import Array
from ..fable_library.util import IDisposable
from .context import (Profile, Profile__get_cfg, Profile__get_baseRequest, Profile__get_addChecksum, Profile__get_addMicMac, Profile__get_salt)
from .extra_types import (IndexMap_2, IndexMap_2__set_Item_541DA560, IndexMap_2__ctor_2B594, Log_Print)
from .format.format_request import (journey_request, reconstruction_request, search_on_trip_request, trip_request, station_board_request, location_request, loc_details_request, loc_geo_pos_request, loc_geo_reach_request, journey_geo_pos_request, journey_match_request, him_search_request, line_match_request, server_info_request)
from .hafas_raw_client import (HafasRawClient__Dispose, HafasRawClient__ctor_48FA4CB7, HafasRawClient, HafasRawClient__AsyncTripSearch_Z4D007EE, HafasRawClient__AsyncReconstruction_Z19A33557, HafasRawClient__AsyncSearchOnTrip_5D40A373, HafasRawClient__AsyncJourneyDetails_73FB16B1, HafasRawClient__AsyncStationBoard_3FCEEA3, HafasRawClient__AsyncLocMatch_781FF3B0, HafasRawClient__AsyncLocDetails_2FCF6141, HafasRawClient__AsyncLocGeoPos_3C0E4562, HafasRawClient__AsyncLocGeoReach_320A81B3, HafasRawClient__AsyncJourneyGeoPos_Z6DB7B6AE, HafasRawClient__AsyncJourneyMatch_Z61E31480, HafasRawClient__AsyncHimSearch_Z6033479F, HafasRawClient__AsyncLineMatch_Z69AA7EA2, HafasRawClient__AsyncServerInfo_Z684EE398)
from .lib.transformations import (MergeOptions_JourneysOptions, Default_Journey, MergeOptions_JourneysFromTripOptions, Default_Trip, MergeOptions_LocationsOptions, MergeOptions_NearByOptions)
from .parse.arrival_or_departure import (DEP, ARR)
from .parse.journey import distance_of_journey
from .parser import (parse_journeys, parse_common, default_options, parse_journey, parse_journeys_array, parse_trip, parse_departures_arrivals, parse_locations, parse_location, parse_durations, parse_movements, parse_trips, parse_warnings, parse_lines, parse_server_info)
from .types_hafas_client import (ProductType, JourneysOptions, Journeys, RefreshJourneyOptions, Journey, StopOver, JourneysFromTripOptions, TripOptions, Trip, DeparturesArrivalsOptions, Alternative, LocationsOptions, StopOptions, Location, NearByOptions, ReachableFromOptions, Duration, BoundingBox, RadarOptions, Movement, TripsByNameOptions, RemarksOptions, Warning, LinesOptions, Line, ServerOptions, ServerInfo)
from .types_raw_hafas_client import (Cfg, RawRequest, TripSearchRequest, RawCommon, RawResult, RawOutCon, ReconstructionRequest, SearchOnTripRequest, JourneyDetailsRequest, RawJny, StationBoardRequest, LocMatchRequest, RawLoc, LocDetailsRequest, LocGeoPosRequest, LocGeoReachRequest, RawPos, JourneyGeoPosRequest, JourneyMatchRequest, HimSearchRequest, RawHim, LineMatchRequest, RawLine, ServerInfoRequest)

__A = TypeVar("__A")

def _expr485() -> TypeInfo:
    return class_type("FsHafas.Api.HafasAsyncClient", None, HafasAsyncClient)


class HafasAsyncClient(IDisposable):
    def __init__(self, profile: Profile) -> None:
        self.profile: Profile = profile
        cfg_1: Cfg
        match_value: Optional[Cfg] = Profile__get_cfg(self.profile)
        if match_value is None:
            raise Exception("profile.cfg")

        else: 
            cfg_1 = match_value

        base_request_1: RawRequest
        match_value_1: Optional[RawRequest] = Profile__get_baseRequest(self.profile)
        if match_value_1 is None:
            raise Exception("profile.baseRequest")

        else: 
            base_request_1 = match_value_1

        self.http_client: HafasRawClient = HafasRawClient__ctor_48FA4CB7(self.profile.endpoint, Profile__get_addChecksum(self.profile), Profile__get_addMicMac(self.profile), Profile__get_salt(self.profile), cfg_1, base_request_1)

    def Dispose(self, __unit: Literal[None]=None) -> None:
        __: HafasAsyncClient = self
        HafasRawClient__Dispose(__.http_client)


HafasAsyncClient_reflection = _expr485

def HafasAsyncClient__ctor_Z3AB94A1B(profile: Profile) -> HafasAsyncClient:
    return HafasAsyncClient(profile)


def HafasAsyncClient_initSerializer(__unit: Literal[None]=None) -> None:
    pass


def HafasAsyncClient_productsOfFilter(profile: Profile, filter: Callable[[ProductType], bool]) -> IndexMap_2[str, bool]:
    array_1: Array[ProductType] = filter_1(filter, profile.products)
    def folder(m: IndexMap_2[str, bool], p: ProductType, profile: Profile=profile, filter: Callable[[ProductType], bool]=filter) -> IndexMap_2[str, bool]:
        IndexMap_2__set_Item_541DA560(m, p.id, True)
        return m

    return fold(folder, IndexMap_2__ctor_2B594(False), array_1)


def HafasAsyncClient_productsOfMode(profile: Profile, mode: str) -> IndexMap_2[str, bool]:
    def _arrow486(p: ProductType, profile: Profile=profile, mode: str=mode) -> bool:
        return (p.name != "Tram") if (p.mode == mode) else False

    return HafasAsyncClient_productsOfFilter(profile, _arrow486)


def HafasAsyncClient__AsyncJourneys(__: HafasAsyncClient, from_: Any=None, to: Any=None, opt: Optional[JourneysOptions]=None) -> Async[Journeys]:
    def _arrow489(__unit: Literal[None]=None, __: HafasAsyncClient=__, from_: Any=from_, to: Any=to, opt: Optional[JourneysOptions]=opt) -> Async[Journeys]:
        def _arrow487(__unit: Literal[None]=None) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawOutCon]]]]:
            tupled_arg: Tuple[str, TripSearchRequest] = journey_request(__.profile, from_, to, opt)
            return HafasRawClient__AsyncTripSearch_Z4D007EE(__.http_client, tupled_arg[0], tupled_arg[1])

        def _arrow488(_arg: Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawOutCon]]]) -> Async[Journeys]:
            return singleton.Return(parse_journeys(_arg[2], parse_common(__.profile, MergeOptions_JourneysOptions(default_options, opt), _arg[0], _arg[1])))

        return singleton.Bind(_arrow487(), _arrow488)

    return singleton.Delay(_arrow489)


def HafasAsyncClient__AsyncRefreshJourney(__: HafasAsyncClient, refresh_token: str, opt: Optional[RefreshJourneyOptions]=None) -> Async[Journey]:
    def _arrow492(__unit: Literal[None]=None, __: HafasAsyncClient=__, refresh_token: str=refresh_token, opt: Optional[RefreshJourneyOptions]=opt) -> Async[Journey]:
        def _arrow490(__unit: Literal[None]=None) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawOutCon]]]]:
            tupled_arg: Tuple[str, ReconstructionRequest] = reconstruction_request(__.profile, refresh_token, opt)
            return HafasRawClient__AsyncReconstruction_Z19A33557(__.http_client, tupled_arg[0], tupled_arg[1])

        def _arrow491(_arg: Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawOutCon]]]) -> Async[Journey]:
            return singleton.Return(parse_journey(_arg[2], parse_common(__.profile, default_options, _arg[0], _arg[1])))

        return singleton.Bind(_arrow490(), _arrow491) if HafasAsyncClient__enabled_6FCE9E49(__, __.profile.refresh_journey) else singleton.Return(Default_Journey)

    return singleton.Delay(_arrow492)


def HafasAsyncClient__AsyncJourneysFromTrip(__: HafasAsyncClient, from_trip_id: str, previous_stop_over: StopOver, to: Any=None, opt: Optional[JourneysFromTripOptions]=None) -> Async[Array[Journey]]:
    def _arrow495(__unit: Literal[None]=None, __: HafasAsyncClient=__, from_trip_id: str=from_trip_id, previous_stop_over: StopOver=previous_stop_over, to: Any=to, opt: Optional[JourneysFromTripOptions]=opt) -> Async[Array[Journey]]:
        def _arrow493(__unit: Literal[None]=None) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawOutCon]]]]:
            tupled_arg: Tuple[str, SearchOnTripRequest] = search_on_trip_request(__.profile, from_trip_id, previous_stop_over, to, opt)
            return HafasRawClient__AsyncSearchOnTrip_5D40A373(__.http_client, tupled_arg[0], tupled_arg[1])

        def _arrow494(_arg: Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawOutCon]]]) -> Async[Array[Journey]]:
            return singleton.Return(parse_journeys_array(_arg[2], parse_common(__.profile, MergeOptions_JourneysFromTripOptions(default_options, opt), _arg[0], _arg[1])))

        return singleton.Bind(_arrow493(), _arrow494) if HafasAsyncClient__enabled_6FCE9E49(__, __.profile.journeys_from_trip) else singleton.Return([])

    return singleton.Delay(_arrow495)


def HafasAsyncClient__AsyncTrip(__: HafasAsyncClient, id: str, name: str, opt: Optional[TripOptions]=None) -> Async[Trip]:
    def _arrow498(__unit: Literal[None]=None, __: HafasAsyncClient=__, id: str=id, name: str=name, opt: Optional[TripOptions]=opt) -> Async[Trip]:
        def _arrow496(__unit: Literal[None]=None) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[RawJny]]]:
            tupled_arg: Tuple[str, JourneyDetailsRequest] = trip_request(__.profile, id, name, opt)
            return HafasRawClient__AsyncJourneyDetails_73FB16B1(__.http_client, tupled_arg[0], tupled_arg[1])

        def _arrow497(_arg: Tuple[Optional[RawCommon], Optional[RawResult], Optional[RawJny]]) -> Async[Trip]:
            return singleton.Return(parse_trip(_arg[2], parse_common(__.profile, default_options, _arg[0], _arg[1])))

        return singleton.Bind(_arrow496(), _arrow497) if HafasAsyncClient__enabled_6FCE9E49(__, __.profile.trip) else singleton.Return(Default_Trip)

    return singleton.Delay(_arrow498)


def HafasAsyncClient__AsyncDepartures(__: HafasAsyncClient, name: Any=None, opt: Optional[DeparturesArrivalsOptions]=None) -> Async[Array[Alternative]]:
    def _arrow501(__unit: Literal[None]=None, __: HafasAsyncClient=__, name: Any=name, opt: Optional[DeparturesArrivalsOptions]=opt) -> Async[Array[Alternative]]:
        def _arrow499(__unit: Literal[None]=None) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawJny]]]]:
            tupled_arg: Tuple[str, StationBoardRequest] = station_board_request(__.profile, DEP, name, opt)
            return HafasRawClient__AsyncStationBoard_3FCEEA3(__.http_client, tupled_arg[0], tupled_arg[1])

        def _arrow500(_arg: Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawJny]]]) -> Async[Array[Alternative]]:
            return singleton.Return(parse_departures_arrivals(DEP, _arg[2], parse_common(__.profile, default_options, _arg[0], _arg[1])))

        return singleton.Bind(_arrow499(), _arrow500)

    return singleton.Delay(_arrow501)


def HafasAsyncClient__AsyncArrivals(__: HafasAsyncClient, name: Any=None, opt: Optional[DeparturesArrivalsOptions]=None) -> Async[Array[Alternative]]:
    def _arrow504(__unit: Literal[None]=None, __: HafasAsyncClient=__, name: Any=name, opt: Optional[DeparturesArrivalsOptions]=opt) -> Async[Array[Alternative]]:
        def _arrow502(__unit: Literal[None]=None) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawJny]]]]:
            tupled_arg: Tuple[str, StationBoardRequest] = station_board_request(__.profile, ARR, name, opt)
            return HafasRawClient__AsyncStationBoard_3FCEEA3(__.http_client, tupled_arg[0], tupled_arg[1])

        def _arrow503(_arg: Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawJny]]]) -> Async[Array[Alternative]]:
            return singleton.Return(parse_departures_arrivals(ARR, _arg[2], parse_common(__.profile, default_options, _arg[0], _arg[1])))

        return singleton.Bind(_arrow502(), _arrow503)

    return singleton.Delay(_arrow504)


def HafasAsyncClient__AsyncLocations(__: HafasAsyncClient, name: str, opt: Optional[LocationsOptions]=None) -> Async[Array[Any]]:
    def _arrow507(__unit: Literal[None]=None, __: HafasAsyncClient=__, name: str=name, opt: Optional[LocationsOptions]=opt) -> Async[Array[Any]]:
        def _arrow505(__unit: Literal[None]=None) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawLoc]]]]:
            tupled_arg: Tuple[str, LocMatchRequest] = location_request(__.profile, name, opt)
            return HafasRawClient__AsyncLocMatch_781FF3B0(__.http_client, tupled_arg[0], tupled_arg[1])

        def _arrow506(_arg: Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawLoc]]]) -> Async[Array[Any]]:
            return singleton.Return(parse_locations(_arg[2], parse_common(__.profile, MergeOptions_LocationsOptions(default_options, opt), _arg[0], _arg[1])))

        return singleton.Bind(_arrow505(), _arrow506)

    return singleton.Delay(_arrow507)


def HafasAsyncClient__AsyncStop(__: HafasAsyncClient, stop: Any=None, opt: Optional[StopOptions]=None) -> Async[Any]:
    def _arrow510(__unit: Literal[None]=None, __: HafasAsyncClient=__, stop: Any=stop, opt: Optional[StopOptions]=opt) -> Async[Any]:
        def _arrow508(__unit: Literal[None]=None) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[RawLoc]]]:
            tupled_arg: Tuple[str, LocDetailsRequest] = loc_details_request(__.profile, stop, opt)
            return HafasRawClient__AsyncLocDetails_2FCF6141(__.http_client, tupled_arg[0], tupled_arg[1])

        def _arrow509(_arg: Tuple[Optional[RawCommon], Optional[RawResult], Optional[RawLoc]]) -> Async[Any]:
            return singleton.Return(parse_location(_arg[2], parse_common(__.profile, default_options, _arg[0], _arg[1])))

        return singleton.Bind(_arrow508(), _arrow509)

    return singleton.Delay(_arrow510)


def HafasAsyncClient__AsyncNearby(__: HafasAsyncClient, l: Location, opt: Optional[NearByOptions]=None) -> Async[Array[Any]]:
    def _arrow513(__unit: Literal[None]=None, __: HafasAsyncClient=__, l: Location=l, opt: Optional[NearByOptions]=opt) -> Async[Array[Any]]:
        def _arrow511(__unit: Literal[None]=None) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawLoc]]]]:
            tupled_arg: Tuple[str, LocGeoPosRequest] = loc_geo_pos_request(__.profile, l, opt)
            return HafasRawClient__AsyncLocGeoPos_3C0E4562(__.http_client, tupled_arg[0], tupled_arg[1])

        def _arrow512(_arg: Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawLoc]]]) -> Async[Array[Any]]:
            return singleton.Return(parse_locations(_arg[2], parse_common(__.profile, MergeOptions_NearByOptions(default_options, opt), _arg[0], _arg[1])))

        return singleton.Bind(_arrow511(), _arrow512)

    return singleton.Delay(_arrow513)


def HafasAsyncClient__AsyncReachableFrom(__: HafasAsyncClient, l: Location, opt: Optional[ReachableFromOptions]=None) -> Async[Array[Duration]]:
    def _arrow516(__unit: Literal[None]=None, __: HafasAsyncClient=__, l: Location=l, opt: Optional[ReachableFromOptions]=opt) -> Async[Array[Duration]]:
        def _arrow514(__unit: Literal[None]=None) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Array[RawPos]]]:
            tupled_arg: Tuple[str, LocGeoReachRequest] = loc_geo_reach_request(__.profile, l, opt)
            return HafasRawClient__AsyncLocGeoReach_320A81B3(__.http_client, tupled_arg[0], tupled_arg[1])

        def _arrow515(_arg: Tuple[Optional[RawCommon], Optional[RawResult], Array[RawPos]]) -> Async[Array[Duration]]:
            return singleton.Return(parse_durations(_arg[2], parse_common(__.profile, default_options, _arg[0], _arg[1])))

        return singleton.Bind(_arrow514(), _arrow515) if HafasAsyncClient__enabled_6FCE9E49(__, __.profile.reachable_from) else singleton.Return([0] * 0)

    return singleton.Delay(_arrow516)


def HafasAsyncClient__AsyncRadar(__: HafasAsyncClient, rect: BoundingBox, opt: Optional[RadarOptions]=None) -> Async[Array[Movement]]:
    def _arrow519(__unit: Literal[None]=None, __: HafasAsyncClient=__, rect: BoundingBox=rect, opt: Optional[RadarOptions]=opt) -> Async[Array[Movement]]:
        def _arrow517(__unit: Literal[None]=None) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawJny]]]]:
            tupled_arg: Tuple[str, JourneyGeoPosRequest] = journey_geo_pos_request(__.profile, rect, opt)
            return HafasRawClient__AsyncJourneyGeoPos_Z6DB7B6AE(__.http_client, tupled_arg[0], tupled_arg[1])

        def _arrow518(_arg: Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawJny]]]) -> Async[Array[Movement]]:
            return singleton.Return(parse_movements(_arg[2], parse_common(__.profile, default_options, _arg[0], _arg[1])))

        return singleton.Bind(_arrow517(), _arrow518) if HafasAsyncClient__enabled_6FCE9E49(__, __.profile.radar) else singleton.Return([0] * 0)

    return singleton.Delay(_arrow519)


def HafasAsyncClient__AsyncTripsByName(__: HafasAsyncClient, line_name: str, opt: Optional[TripsByNameOptions]=None) -> Async[Array[Trip]]:
    def _arrow522(__unit: Literal[None]=None, __: HafasAsyncClient=__, line_name: str=line_name, opt: Optional[TripsByNameOptions]=opt) -> Async[Array[Trip]]:
        def _arrow520(__unit: Literal[None]=None) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawJny]]]]:
            tupled_arg: Tuple[str, JourneyMatchRequest] = journey_match_request(__.profile, line_name, opt)
            return HafasRawClient__AsyncJourneyMatch_Z61E31480(__.http_client, tupled_arg[0], tupled_arg[1])

        def _arrow521(_arg: Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawJny]]]) -> Async[Array[Trip]]:
            return singleton.Return(parse_trips(_arg[2], parse_common(__.profile, default_options, _arg[0], _arg[1])))

        return singleton.Bind(_arrow520(), _arrow521) if HafasAsyncClient__enabled_6FCE9E49(__, __.profile.trips_by_name) else singleton.Return([0] * 0)

    return singleton.Delay(_arrow522)


def HafasAsyncClient__AsyncRemarks_7D671456(__: HafasAsyncClient, opt: Optional[RemarksOptions]=None) -> Async[Array[Warning]]:
    def _arrow525(__unit: Literal[None]=None, __: HafasAsyncClient=__, opt: Optional[RemarksOptions]=opt) -> Async[Array[Warning]]:
        def _arrow523(__unit: Literal[None]=None) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawHim]]]]:
            tupled_arg: Tuple[str, HimSearchRequest] = him_search_request(__.profile, opt)
            return HafasRawClient__AsyncHimSearch_Z6033479F(__.http_client, tupled_arg[0], tupled_arg[1])

        def _arrow524(_arg: Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawHim]]]) -> Async[Array[Warning]]:
            return singleton.Return(parse_warnings(_arg[2], parse_common(__.profile, default_options, _arg[0], _arg[1])))

        return singleton.Bind(_arrow523(), _arrow524) if HafasAsyncClient__enabled_6FCE9E49(__, __.profile.remarks) else singleton.Return([0] * 0)

    return singleton.Delay(_arrow525)


def HafasAsyncClient__AsyncLines(__: HafasAsyncClient, query: str, opt: Optional[LinesOptions]=None) -> Async[Array[Line]]:
    def _arrow528(__unit: Literal[None]=None, __: HafasAsyncClient=__, query: str=query, opt: Optional[LinesOptions]=opt) -> Async[Array[Line]]:
        def _arrow526(__unit: Literal[None]=None) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawLine]]]]:
            tupled_arg: Tuple[str, LineMatchRequest] = line_match_request(__.profile, query, opt)
            return HafasRawClient__AsyncLineMatch_Z69AA7EA2(__.http_client, tupled_arg[0], tupled_arg[1])

        def _arrow527(_arg: Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawLine]]]) -> Async[Array[Line]]:
            return singleton.Return(parse_lines(_arg[2], parse_common(__.profile, default_options, _arg[0], _arg[1])))

        return singleton.Bind(_arrow526(), _arrow527) if HafasAsyncClient__enabled_6FCE9E49(__, __.profile.lines) else singleton.Return([0] * 0)

    return singleton.Delay(_arrow528)


def HafasAsyncClient__AsyncServerInfo_70DF6D02(__: HafasAsyncClient, opt: Optional[ServerOptions]=None) -> Async[ServerInfo]:
    def _arrow531(__unit: Literal[None]=None, __: HafasAsyncClient=__, opt: Optional[ServerOptions]=opt) -> Async[ServerInfo]:
        def _arrow529(__unit: Literal[None]=None) -> Async[Tuple[Optional[RawCommon], Optional[RawResult]]]:
            tupled_arg: Tuple[str, ServerInfoRequest] = server_info_request(__.profile, opt)
            return HafasRawClient__AsyncServerInfo_Z684EE398(__.http_client, tupled_arg[0], tupled_arg[1])

        def _arrow530(_arg: Tuple[Optional[RawCommon], Optional[RawResult]]) -> Async[ServerInfo]:
            res: Optional[RawResult] = _arg[1]
            return singleton.Return(parse_server_info(res, parse_common(__.profile, default_options, _arg[0], res)))

        return singleton.Bind(_arrow529(), _arrow530)

    return singleton.Delay(_arrow531)


def HafasAsyncClient__distanceOfJourney_1E546A4(__: HafasAsyncClient, j: Journey) -> float:
    return distance_of_journey(j)


def HafasAsyncClient__log(this: HafasAsyncClient, msg: str, o: Any) -> None:
    Log_Print(msg, o)


def HafasAsyncClient__enabled_6FCE9E49(this: HafasAsyncClient, value: Optional[bool]=None) -> bool:
    if value is None:
        return False

    else: 
        return value



__all__ = ["HafasAsyncClient_reflection", "HafasAsyncClient_initSerializer", "HafasAsyncClient_productsOfFilter", "HafasAsyncClient_productsOfMode", "HafasAsyncClient__AsyncJourneys", "HafasAsyncClient__AsyncRefreshJourney", "HafasAsyncClient__AsyncJourneysFromTrip", "HafasAsyncClient__AsyncTrip", "HafasAsyncClient__AsyncDepartures", "HafasAsyncClient__AsyncArrivals", "HafasAsyncClient__AsyncLocations", "HafasAsyncClient__AsyncStop", "HafasAsyncClient__AsyncNearby", "HafasAsyncClient__AsyncReachableFrom", "HafasAsyncClient__AsyncRadar", "HafasAsyncClient__AsyncTripsByName", "HafasAsyncClient__AsyncRemarks_7D671456", "HafasAsyncClient__AsyncLines", "HafasAsyncClient__AsyncServerInfo_70DF6D02", "HafasAsyncClient__distanceOfJourney_1E546A4", "HafasAsyncClient__log", "HafasAsyncClient__enabled_6FCE9E49"]

