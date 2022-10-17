from __future__ import annotations
from typing import (Any, TypeVar, Optional, Callable, Tuple, Literal)
from ...fable_library.array import (fold, filter)
from ...fable_library.date import create
from ...fable_library.int32 import parse
from ...fable_library.option import (value as value_6, map)
from ...fable_library.string import substring
from ...fable_library.types import Array
from ...fable_library.util import int32_to_string
from ..context import (Profile, Profile__get_formatStation, Profile__get_departuresGetPasslist, Profile__get_departuresStbFltrEquiv, Profile__get_journeysOutFrwd, Profile__get_transformJourneysQuery)
from ..extensions.date_time_ex import (format_date as format_date_1, format_time as format_time_1)
from ..extra_types import (IndexMap_2, IndexMap_2__get_Item_2B595)
from ..lib.transformations import (Default_LocationsOptions, Coordinate_fromFloat, Default_DeparturesArrivalsOptions, Default_RefreshJourneyOptions, Default_TripsByNameOptions, Default_StopOptions, Default_NearByOptions, Default_ReachableFromOptions, Default_RadarOptions, Default_TripOptions, Default_LinesOptions, Default_ServerOptions, Default_RemarksOptions, Default_JourneysOptions, Default_JourneysFromTripOptions)
from ..types_hafas_client import (ProductType, LocationsOptions, Location, Station, Stop, DeparturesArrivalsOptions, RefreshJourneyOptions, TripsByNameOptions, StopOptions, NearByOptions, ReachableFromOptions, BoundingBox, RadarOptions, TripOptions, LinesOptions, ServerOptions, RemarksOptions, JourneysOptions, StopOver, JourneysFromTripOptions)
from ..types_raw_hafas_client import (JnyFltr, Loc, LocMatchInput, LocMatchRequest, StationBoardRequest, ReconstructionRequest, JourneyMatchRequest, LocDetailsRequest, RawcCrd, RawRing, LocGeoPosRequest, LocGeoReachRequest, RawCrd, RawRect, JourneyGeoPosRequest, JourneyDetailsRequest, LineMatchRequest, ServerInfoRequest, HimSearchRequest, LocViaInput, TripSearchRequest, LocData, SearchOnTripRequest)

_A = TypeVar("_A")

_B = TypeVar("_B")

def ParseIsoString(datetime: str) -> Any:
    year: int = parse(substring(datetime, 0, 4), 511, False, 32) or 0
    month: int = parse(substring(datetime, 5, 2), 511, False, 32) or 0
    day: int = parse(substring(datetime, 8, 2), 511, False, 32) or 0
    hour: int = parse(substring(datetime, 11, 2), 511, False, 32) or 0
    minute: int = parse(substring(datetime, 14, 2), 511, False, 32) or 0
    tz_offset: int = (60 * parse(substring(datetime, 20, 2), 511, False, 32)) or 0
    return create(year, month, day, hour, minute, 0)


def maybe_get_option_value(opt: Optional[_A], getter: Callable[[_A], Optional[_B]]) -> Optional[_B]:
    if opt is None:
        return None

    else: 
        return getter(value_6(opt))



def get_option_value(opt: Optional[_A], getter: Callable[[_A], Optional[_B]], default_opt: _A) -> _B:
    default_value: _B
    match_value: Optional[_B] = getter(default_opt)
    if match_value is None:
        raise Exception("getOptionValue: value expected")

    else: 
        default_value = value_6(match_value)

    if opt is None:
        return default_value

    else: 
        match_value_1: Optional[_B] = getter(value_6(opt))
        if match_value_1 is None:
            return default_value

        else: 
            return value_6(match_value_1)




def format_date(dt: Any) -> str:
    return format_date_1(dt, "yyyyMMdd")


def format_time(dt: Any) -> str:
    return format_time_1(dt, "HHmm") + "00"


def format_products_bitmask(profile: Profile, products: IndexMap_2[str, bool]) -> int:
    def folder(bitmask: int, p_1: ProductType, profile: Profile=profile, products: IndexMap_2[str, bool]=products) -> int:
        return p_1.bitmasks[0] | bitmask

    def predicate(p: ProductType, profile: Profile=profile, products: IndexMap_2[str, bool]=products) -> bool:
        return IndexMap_2__get_Item_2B595(products, p.id)

    return fold(folder, 0, filter(predicate, profile.products))


def make_filters(profile: Profile, products: IndexMap_2[str, bool]) -> Array[JnyFltr]:
    bitmask: int = format_products_bitmask(profile, products) or 0
    if bitmask != 0:
        return [JnyFltr("PROD", "INC", int32_to_string(bitmask), None)]

    else: 
        return []



def location_request(profile: Profile, name: str, opt: Optional[LocationsOptions]=None) -> Tuple[str, LocMatchRequest]:
    def _arrow367(v: LocationsOptions, profile: Profile=profile, name: str=name, opt: Optional[LocationsOptions]=opt) -> Optional[bool]:
        return v.fuzzy

    fuzzy: bool = get_option_value(opt, _arrow367, Default_LocationsOptions)
    def _arrow368(v_1: LocationsOptions, profile: Profile=profile, name: str=name, opt: Optional[LocationsOptions]=opt) -> Optional[int]:
        return v_1.results

    results: int = get_option_value(opt, _arrow368, Default_LocationsOptions) or 0
    def _arrow369(v_2: LocationsOptions, profile: Profile=profile, name: str=name, opt: Optional[LocationsOptions]=opt) -> Optional[str]:
        return v_2.language

    return (get_option_value(opt, _arrow369, Default_LocationsOptions), LocMatchRequest(LocMatchInput(Loc("ALL", name + ("?" if fuzzy else ""), None), results, "S")))


def make_loc_ltype_s(profile: Profile, id: str) -> Loc:
    return Loc("S", None, ("A=1@L=" + Profile__get_formatStation(profile)(id)) + "@")


def make_locl_type_a(location: Location) -> Loc:
    x: int
    match_value: Optional[float] = location.longitude
    if match_value is None:
        raise Exception("location.longitude")

    else: 
        x = Coordinate_fromFloat(match_value)

    y: int
    match_value_1: Optional[float] = location.latitude
    if match_value_1 is None:
        raise Exception("location.latitude")

    else: 
        y = Coordinate_fromFloat(match_value_1)

    xs: str = int32_to_string(x)
    ys: str = int32_to_string(y)
    match_value_2: Optional[str] = location.address
    if match_value_2 is None:
        return Loc("A", None, ((("A=1@X=" + xs) + "@Y=") + ys) + "@")

    else: 
        name: str = match_value_2
        return Loc("A", name, ((((("A=2@O=" + name) + "@X=") + xs) + "@Y=") + ys) + "@")



def make_loc_type(profile: Profile, s: Any=None) -> Loc:
    (pattern_matching_result, v_3, v_4, v_5, v_6, v_7) = (None, None, None, None, None, None)
    if isinstance(s, Station):
        if s.id is not None:
            pattern_matching_result = 1
            v_4 = s

        else: 
            pattern_matching_result = 5


    elif isinstance(s, Stop):
        if s.id is not None:
            pattern_matching_result = 2
            v_5 = s

        else: 
            pattern_matching_result = 5


    elif isinstance(s, Location):
        if s.id is not None:
            pattern_matching_result = 3
            v_6 = s

        else: 
            pattern_matching_result = 4
            v_7 = s


    else: 
        pattern_matching_result = 0
        v_3 = s

    if pattern_matching_result == 0:
        return make_loc_ltype_s(profile, v_3)

    elif pattern_matching_result == 1:
        return make_loc_ltype_s(profile, value_6(v_4.id))

    elif pattern_matching_result == 2:
        return make_loc_ltype_s(profile, value_6(v_5.id))

    elif pattern_matching_result == 3:
        return make_loc_ltype_s(profile, value_6(v_6.id))

    elif pattern_matching_result == 4:
        return make_locl_type_a(v_7)

    elif pattern_matching_result == 5:
        raise Exception("makeLocType")



def station_board_request(profile: Profile, type: str, name: Any=None, opt: Optional[DeparturesArrivalsOptions]=None) -> Tuple[str, StationBoardRequest]:
    def _arrow370(v: DeparturesArrivalsOptions, profile: Profile=profile, type: str=type, name: Any=name, opt: Optional[DeparturesArrivalsOptions]=opt) -> Optional[Any]:
        return v.when

    dt: Any = get_option_value(opt, _arrow370, Default_DeparturesArrivalsOptions)
    date: str = format_date(dt)
    time: str = format_time(dt)
    def _arrow371(v_1: DeparturesArrivalsOptions, profile: Profile=profile, type: str=type, name: Any=name, opt: Optional[DeparturesArrivalsOptions]=opt) -> Optional[int]:
        return v_1.duration

    duration: int = get_option_value(opt, _arrow371, Default_DeparturesArrivalsOptions) or 0
    def _arrow372(v_2: DeparturesArrivalsOptions, profile: Profile=profile, type: str=type, name: Any=name, opt: Optional[DeparturesArrivalsOptions]=opt) -> Optional[bool]:
        return v_2.stopovers

    stopovers: bool = get_option_value(opt, _arrow372, Default_DeparturesArrivalsOptions) if Profile__get_departuresGetPasslist(profile) else False
    def _arrow373(v_3: DeparturesArrivalsOptions, profile: Profile=profile, type: str=type, name: Any=name, opt: Optional[DeparturesArrivalsOptions]=opt) -> Optional[bool]:
        return v_3.include_related_stations

    include_related_stations: bool = get_option_value(opt, _arrow373, Default_DeparturesArrivalsOptions) if Profile__get_departuresStbFltrEquiv(profile) else False
    def _arrow374(v_4: DeparturesArrivalsOptions, profile: Profile=profile, type: str=type, name: Any=name, opt: Optional[DeparturesArrivalsOptions]=opt) -> Optional[IndexMap_2[str, bool]]:
        return v_4.products

    filters: Array[JnyFltr] = make_filters(profile, get_option_value(opt, _arrow374, Default_DeparturesArrivalsOptions))
    def _arrow375(v_5: DeparturesArrivalsOptions, profile: Profile=profile, type: str=type, name: Any=name, opt: Optional[DeparturesArrivalsOptions]=opt) -> Optional[str]:
        return v_5.language

    return (get_option_value(opt, _arrow375, Default_DeparturesArrivalsOptions), StationBoardRequest(type, date, time, make_loc_type(profile, name), filters, duration))


def reconstruction_request(profile: Profile, refresh_token: str, opt: Optional[RefreshJourneyOptions]=None) -> Tuple[str, ReconstructionRequest]:
    def _arrow376(v: RefreshJourneyOptions, profile: Profile=profile, refresh_token: str=refresh_token, opt: Optional[RefreshJourneyOptions]=opt) -> Optional[bool]:
        return v.polylines

    polylines: bool = get_option_value(opt, _arrow376, Default_RefreshJourneyOptions)
    def _arrow377(v_1: RefreshJourneyOptions, profile: Profile=profile, refresh_token: str=refresh_token, opt: Optional[RefreshJourneyOptions]=opt) -> Optional[bool]:
        return v_1.stopovers

    stopovers: bool = get_option_value(opt, _arrow377, Default_RefreshJourneyOptions)
    def _arrow378(v_2: RefreshJourneyOptions, profile: Profile=profile, refresh_token: str=refresh_token, opt: Optional[RefreshJourneyOptions]=opt) -> Optional[bool]:
        return v_2.tickets

    tickets: bool = get_option_value(opt, _arrow378, Default_RefreshJourneyOptions)
    def _arrow379(v_3: RefreshJourneyOptions, profile: Profile=profile, refresh_token: str=refresh_token, opt: Optional[RefreshJourneyOptions]=opt) -> Optional[str]:
        return v_3.language

    return (get_option_value(opt, _arrow379, Default_RefreshJourneyOptions), ReconstructionRequest(True, stopovers, polylines, tickets, refresh_token))


def journey_match_request(profile: Profile, line_name: str, opt: Optional[TripsByNameOptions]=None) -> Tuple[str, JourneyMatchRequest]:
    def _arrow380(dt: Any, profile: Profile=profile, line_name: str=line_name, opt: Optional[TripsByNameOptions]=opt) -> str:
        return format_date(dt)

    def _arrow381(v: TripsByNameOptions, profile: Profile=profile, line_name: str=line_name, opt: Optional[TripsByNameOptions]=opt) -> Optional[Any]:
        return v.when

    date: Optional[str] = map(_arrow380, maybe_get_option_value(opt, _arrow381))
    def _arrow382(v_1: TripsByNameOptions, profile: Profile=profile, line_name: str=line_name, opt: Optional[TripsByNameOptions]=opt) -> Optional[str]:
        return "de"

    return (get_option_value(opt, _arrow382, Default_TripsByNameOptions), JourneyMatchRequest(line_name, date))


def loc_details_request(profile: Profile, stop: Any=None, opt: Optional[StopOptions]=None) -> Tuple[str, LocDetailsRequest]:
    id: str
    if isinstance(stop, Stop):
        if stop.id is not None:
            id = value_6(stop.id)

        else: 
            raise Exception("Stop expected")


    else: 
        id = stop

    def _arrow383(v: StopOptions, profile: Profile=profile, stop: Any=stop, opt: Optional[StopOptions]=opt) -> Optional[str]:
        return v.language

    return (get_option_value(opt, _arrow383, Default_StopOptions), LocDetailsRequest([make_loc_ltype_s(profile, id)]))


def loc_geo_pos_request(profile: Profile, location: Location, opt: Optional[NearByOptions]=None) -> Tuple[str, LocGeoPosRequest]:
    def _arrow384(v: NearByOptions, profile: Profile=profile, location: Location=location, opt: Optional[NearByOptions]=opt) -> Optional[int]:
        return v.results

    results: int = get_option_value(opt, _arrow384, Default_NearByOptions) or 0
    def _arrow385(v_1: NearByOptions, profile: Profile=profile, location: Location=location, opt: Optional[NearByOptions]=opt) -> Optional[bool]:
        return v_1.stops

    stops: bool = get_option_value(opt, _arrow385, Default_NearByOptions)
    def _arrow386(v_2: NearByOptions, profile: Profile=profile, location: Location=location, opt: Optional[NearByOptions]=opt) -> Optional[int]:
        return v_2.distance

    distance: int = get_option_value(opt, _arrow386, Default_NearByOptions) or 0
    def _arrow387(v_3: NearByOptions, profile: Profile=profile, location: Location=location, opt: Optional[NearByOptions]=opt) -> Optional[IndexMap_2[str, bool]]:
        return v_3.products

    filters: Array[JnyFltr] = make_filters(profile, get_option_value(opt, _arrow387, Default_NearByOptions))
    x: int
    match_value: Optional[float] = location.longitude
    if match_value is None:
        raise Exception("location.longitude")

    else: 
        x = Coordinate_fromFloat(match_value)

    y: int
    match_value_1: Optional[float] = location.latitude
    if match_value_1 is None:
        raise Exception("location.latitude")

    else: 
        y = Coordinate_fromFloat(match_value_1)

    def _arrow388(v_4: NearByOptions, profile: Profile=profile, location: Location=location, opt: Optional[NearByOptions]=opt) -> Optional[str]:
        return v_4.language

    return (get_option_value(opt, _arrow388, Default_NearByOptions), LocGeoPosRequest(RawRing(RawcCrd(x, y), distance, 0), filters, False, stops, results))


def loc_geo_reach_request(profile: Profile, location: Location, opt: Optional[ReachableFromOptions]=None) -> Tuple[str, LocGeoReachRequest]:
    def _arrow389(v: ReachableFromOptions, profile: Profile=profile, location: Location=location, opt: Optional[ReachableFromOptions]=opt) -> Optional[Any]:
        return v.when

    dt: Any = get_option_value(opt, _arrow389, Default_ReachableFromOptions)
    date: str = format_date(dt)
    time: str = format_time(dt)
    def _arrow390(v_1: ReachableFromOptions, profile: Profile=profile, location: Location=location, opt: Optional[ReachableFromOptions]=opt) -> Optional[int]:
        return v_1.max_duration

    max_duration: int = get_option_value(opt, _arrow390, Default_ReachableFromOptions) or 0
    def _arrow391(v_2: ReachableFromOptions, profile: Profile=profile, location: Location=location, opt: Optional[ReachableFromOptions]=opt) -> Optional[int]:
        return v_2.max_transfers

    max_transfers: int = get_option_value(opt, _arrow391, Default_ReachableFromOptions) or 0
    def _arrow392(v_3: ReachableFromOptions, profile: Profile=profile, location: Location=location, opt: Optional[ReachableFromOptions]=opt) -> Optional[IndexMap_2[str, bool]]:
        return v_3.products

    filters: Array[JnyFltr] = make_filters(profile, get_option_value(opt, _arrow392, Default_ReachableFromOptions))
    def _arrow393(v_4: ReachableFromOptions, profile: Profile=profile, location: Location=location, opt: Optional[ReachableFromOptions]=opt) -> Optional[str]:
        return "de"

    return (get_option_value(opt, _arrow393, Default_ReachableFromOptions), LocGeoReachRequest(make_locl_type_a(location), max_duration, max_transfers, date, time, 120, filters))


def journey_geo_pos_request(profile: Profile, rect: BoundingBox, opt: Optional[RadarOptions]=None) -> Tuple[str, JourneyGeoPosRequest]:
    if rect.north <= rect.south:
        raise Exception("north must be larger than south.")

    if rect.east <= rect.west:
        raise Exception("east must be larger than west.")

    def _arrow394(v: RadarOptions, profile: Profile=profile, rect: BoundingBox=rect, opt: Optional[RadarOptions]=opt) -> Optional[Any]:
        return v.when

    dt: Any = get_option_value(opt, _arrow394, Default_RadarOptions)
    date: str = format_date(dt)
    time: str = format_time(dt)
    def _arrow395(v_1: RadarOptions, profile: Profile=profile, rect: BoundingBox=rect, opt: Optional[RadarOptions]=opt) -> Optional[int]:
        return v_1.results

    results: int = get_option_value(opt, _arrow395, Default_RadarOptions) or 0
    def _arrow396(v_2: RadarOptions, profile: Profile=profile, rect: BoundingBox=rect, opt: Optional[RadarOptions]=opt) -> Optional[int]:
        return v_2.duration

    duration: int = get_option_value(opt, _arrow396, Default_RadarOptions) or 0
    def _arrow397(v_3: RadarOptions, profile: Profile=profile, rect: BoundingBox=rect, opt: Optional[RadarOptions]=opt) -> Optional[int]:
        return v_3.frames

    frames: int = get_option_value(opt, _arrow397, Default_RadarOptions) or 0
    def _arrow398(v_4: RadarOptions, profile: Profile=profile, rect: BoundingBox=rect, opt: Optional[RadarOptions]=opt) -> Optional[IndexMap_2[str, bool]]:
        return v_4.products

    filters: Array[JnyFltr] = make_filters(profile, get_option_value(opt, _arrow398, Default_RadarOptions))
    def _arrow399(v_5: RadarOptions, profile: Profile=profile, rect: BoundingBox=rect, opt: Optional[RadarOptions]=opt) -> Optional[str]:
        return "de"

    return (get_option_value(opt, _arrow399, Default_RadarOptions), JourneyGeoPosRequest(results, False, date, time, RawRect(RawCrd(Coordinate_fromFloat(rect.west), Coordinate_fromFloat(rect.south), None), RawCrd(Coordinate_fromFloat(rect.east), Coordinate_fromFloat(rect.north), None)), duration * 1000, (duration // frames) * 1000, True, filters, "CALC"))


def trip_request(profile: Profile, id: str, name: str, opt: Optional[TripOptions]=None) -> Tuple[str, JourneyDetailsRequest]:
    def _arrow400(v: TripOptions, profile: Profile=profile, id: str=id, name: str=name, opt: Optional[TripOptions]=opt) -> Optional[bool]:
        return v.polyline

    polyline: bool = get_option_value(opt, _arrow400, Default_TripOptions)
    def _arrow401(v_1: TripOptions, profile: Profile=profile, id: str=id, name: str=name, opt: Optional[TripOptions]=opt) -> Optional[str]:
        return v_1.language

    return (get_option_value(opt, _arrow401, Default_TripOptions), JourneyDetailsRequest(id, name, polyline))


def line_match_request(profile: Profile, query: str, opt: Optional[LinesOptions]=None) -> Tuple[str, LineMatchRequest]:
    def _arrow402(v: LinesOptions, profile: Profile=profile, query: str=query, opt: Optional[LinesOptions]=opt) -> Optional[str]:
        return v.language

    return (get_option_value(opt, _arrow402, Default_LinesOptions), LineMatchRequest(query))


def server_info_request(profile: Profile, opt: Optional[ServerOptions]=None) -> Tuple[str, ServerInfoRequest]:
    def _arrow403(v: ServerOptions, profile: Profile=profile, opt: Optional[ServerOptions]=opt) -> Optional[bool]:
        return v.version_info

    return ("de", ServerInfoRequest(get_option_value(opt, _arrow403, Default_ServerOptions)))


def him_search_request(profile: Profile, opt: Optional[RemarksOptions]=None) -> Tuple[str, HimSearchRequest]:
    def _arrow404(v: RemarksOptions, profile: Profile=profile, opt: Optional[RemarksOptions]=opt) -> Optional[Any]:
        return v.from_

    dt: Any = get_option_value(opt, _arrow404, Default_RemarksOptions)
    date: str = format_date(dt)
    time: str = format_time(dt)
    def _arrow405(v_1: RemarksOptions, profile: Profile=profile, opt: Optional[RemarksOptions]=opt) -> Optional[int]:
        return v_1.results

    results: int = get_option_value(opt, _arrow405, Default_RemarksOptions) or 0
    def _arrow406(v_2: RemarksOptions, profile: Profile=profile, opt: Optional[RemarksOptions]=opt) -> Optional[bool]:
        return v_2.polylines

    polylines: bool = get_option_value(opt, _arrow406, Default_RemarksOptions)
    def _arrow407(v_3: RemarksOptions, profile: Profile=profile, opt: Optional[RemarksOptions]=opt) -> Optional[IndexMap_2[str, bool]]:
        return v_3.products

    filters: Array[JnyFltr] = make_filters(profile, get_option_value(opt, _arrow407, Default_RemarksOptions))
    def _arrow408(v_4: RemarksOptions, profile: Profile=profile, opt: Optional[RemarksOptions]=opt) -> Optional[str]:
        return v_4.language

    return (get_option_value(opt, _arrow408, Default_RemarksOptions), HimSearchRequest(filters, polylines, results, date, time))


def journey_request(profile: Profile, from_: Any=None, to: Any=None, opt: Optional[JourneysOptions]=None) -> Tuple[str, TripSearchRequest]:
    if opt is None:
        pass

    else: 
        opt_1: JourneysOptions = opt
        if (not Profile__get_journeysOutFrwd(profile)) if (opt_1.arrival is not None) else False:
            raise Exception("opt.arrival is unsupported")

        if opt_1.earlier_than is not None:
            raise Exception("opt.earlierThan nyi")

        if opt_1.later_than is not None:
            raise Exception("opt.laterThan nyi")


    def _arrow409(__unit: Literal[None]=None, profile: Profile=profile, from_: Any=from_, to: Any=to, opt: Optional[JourneysOptions]=opt) -> Any:
        opt_v_1: JourneysOptions = opt
        return value_6(opt_v_1.arrival)

    def _arrow410(v: JourneysOptions, profile: Profile=profile, from_: Any=from_, to: Any=to, opt: Optional[JourneysOptions]=opt) -> Optional[Any]:
        return v.departure

    def _arrow411(v: JourneysOptions, profile: Profile=profile, from_: Any=from_, to: Any=to, opt: Optional[JourneysOptions]=opt) -> Optional[Any]:
        return v.departure

    dt: Any = (_arrow409() if (opt.arrival is not None) else get_option_value(opt, _arrow410, Default_JourneysOptions)) if (opt is not None) else get_option_value(opt, _arrow411, Default_JourneysOptions)
    date: str = format_date(dt)
    time: str = format_time(dt)
    out_frwd: bool = False if ((value_6(opt).arrival is not None) if (opt is not None) else False) else True
    def _arrow412(v_1: JourneysOptions, profile: Profile=profile, from_: Any=from_, to: Any=to, opt: Optional[JourneysOptions]=opt) -> Optional[int]:
        return v_1.results

    results: int = get_option_value(opt, _arrow412, Default_JourneysOptions) or 0
    def _arrow413(v_2: JourneysOptions, profile: Profile=profile, from_: Any=from_, to: Any=to, opt: Optional[JourneysOptions]=opt) -> Optional[bool]:
        return v_2.stopovers

    stopovers: bool = get_option_value(opt, _arrow413, Default_JourneysOptions)
    def _arrow414(v_3: JourneysOptions, profile: Profile=profile, from_: Any=from_, to: Any=to, opt: Optional[JourneysOptions]=opt) -> Optional[int]:
        return v_3.transfers

    transfers: int = get_option_value(opt, _arrow414, Default_JourneysOptions) or 0
    def _arrow415(v_4: JourneysOptions, profile: Profile=profile, from_: Any=from_, to: Any=to, opt: Optional[JourneysOptions]=opt) -> Optional[int]:
        return v_4.transfer_time

    transfer_time: int = get_option_value(opt, _arrow415, Default_JourneysOptions) or 0
    def _arrow416(v_5: JourneysOptions, profile: Profile=profile, from_: Any=from_, to: Any=to, opt: Optional[JourneysOptions]=opt) -> Optional[bool]:
        return v_5.tickets

    tickets: bool = get_option_value(opt, _arrow416, Default_JourneysOptions)
    def _arrow417(v_6: JourneysOptions, profile: Profile=profile, from_: Any=from_, to: Any=to, opt: Optional[JourneysOptions]=opt) -> Optional[bool]:
        return v_6.polylines

    polylines: bool = get_option_value(opt, _arrow417, Default_JourneysOptions)
    def _arrow418(v_7: JourneysOptions, profile: Profile=profile, from_: Any=from_, to: Any=to, opt: Optional[JourneysOptions]=opt) -> Optional[IndexMap_2[str, bool]]:
        return v_7.products

    filters: Array[JnyFltr] = make_filters(profile, get_option_value(opt, _arrow418, Default_JourneysOptions))
    via_loc_l: Optional[Array[LocViaInput]]
    def _arrow419(v_8: JourneysOptions, profile: Profile=profile, from_: Any=from_, to: Any=to, opt: Optional[JourneysOptions]=opt) -> Optional[str]:
        return v_8.via

    match_value: Optional[str] = maybe_get_option_value(opt, _arrow419)
    via_loc_l = None if (match_value is None) else [LocViaInput(make_loc_ltype_s(profile, match_value))]
    def _arrow420(v_9: JourneysOptions, profile: Profile=profile, from_: Any=from_, to: Any=to, opt: Optional[JourneysOptions]=opt) -> Optional[str]:
        return v_9.language

    return (get_option_value(opt, _arrow420, Default_JourneysOptions), Profile__get_transformJourneysQuery(profile)(opt)(TripSearchRequest(stopovers, transfers, transfer_time, [make_loc_type(profile, from_)], via_loc_l, [make_loc_type(profile, to)], filters, [], tickets, True, True, False, polylines, date, time, results, out_frwd, None)))


def search_on_trip_request(profile: Profile, trip_id: str, previous_stopover: StopOver, to: Any=None, opt: Optional[JourneysFromTripOptions]=None) -> Tuple[str, SearchOnTripRequest]:
    prev_stop_id: str
    match_value: Optional[Any] = previous_stopover.stop
    (pattern_matching_result, station_1, stop_1) = (None, None, None)
    if match_value is not None:
        if isinstance(value_6(match_value), Stop):
            if value_6(match_value).id is not None:
                pattern_matching_result = 1
                stop_1 = value_6(match_value)

            else: 
                pattern_matching_result = 2


        elif value_6(match_value).id is not None:
            pattern_matching_result = 0
            station_1 = value_6(match_value)

        else: 
            pattern_matching_result = 2


    else: 
        pattern_matching_result = 2

    if pattern_matching_result == 0:
        prev_stop_id = value_6(station_1.id)

    elif pattern_matching_result == 1:
        prev_stop_id = value_6(stop_1.id)

    elif pattern_matching_result == 2:
        raise Exception("previousStopover.stop must be a valid stop or station.")

    dep_at_prev_stop: Any
    matchValue: Optional[str] = previous_stopover.departure
    matchValue_1: Optional[str] = previous_stopover.planned_departure
    if matchValue is not None:
        dep_at_prev_stop = ParseIsoString(matchValue)

    elif matchValue_1 is not None:
        dep_at_prev_stop = ParseIsoString(matchValue_1)

    else: 
        raise Exception("previousStopover.(planned)departure is invalid.")

    def _arrow421(v: JourneysFromTripOptions, profile: Profile=profile, trip_id: str=trip_id, previous_stopover: StopOver=previous_stopover, to: Any=to, opt: Optional[JourneysFromTripOptions]=opt) -> Optional[bool]:
        return v.tickets

    tickets: bool = get_option_value(opt, _arrow421, Default_JourneysFromTripOptions)
    def _arrow422(v_1: JourneysFromTripOptions, profile: Profile=profile, trip_id: str=trip_id, previous_stopover: StopOver=previous_stopover, to: Any=to, opt: Optional[JourneysFromTripOptions]=opt) -> Optional[int]:
        return v_1.transfer_time

    transfer_time: int = get_option_value(opt, _arrow422, Default_JourneysFromTripOptions) or 0
    def _arrow423(v_2: JourneysFromTripOptions, profile: Profile=profile, trip_id: str=trip_id, previous_stopover: StopOver=previous_stopover, to: Any=to, opt: Optional[JourneysFromTripOptions]=opt) -> Optional[bool]:
        return v_2.polylines

    polylines: bool = get_option_value(opt, _arrow423, Default_JourneysFromTripOptions)
    def _arrow424(v_3: JourneysFromTripOptions, profile: Profile=profile, trip_id: str=trip_id, previous_stopover: StopOver=previous_stopover, to: Any=to, opt: Optional[JourneysFromTripOptions]=opt) -> Optional[bool]:
        return v_3.stopovers

    stopovers: bool = get_option_value(opt, _arrow424, Default_JourneysFromTripOptions)
    def _arrow425(v_4: JourneysFromTripOptions, profile: Profile=profile, trip_id: str=trip_id, previous_stopover: StopOver=previous_stopover, to: Any=to, opt: Optional[JourneysFromTripOptions]=opt) -> Optional[IndexMap_2[str, bool]]:
        return v_4.products

    filters: Array[JnyFltr] = make_filters(profile, get_option_value(opt, _arrow425, Default_JourneysFromTripOptions))
    return ("de", SearchOnTripRequest("JI", trip_id, LocData(make_loc_ltype_s(profile, prev_stop_id), "DEP", format_date(dep_at_prev_stop), format_time(dep_at_prev_stop)), [make_loc_type(profile, to)], filters, stopovers, polylines, transfer_time, tickets))


__all__ = ["ParseIsoString", "maybe_get_option_value", "get_option_value", "format_date", "format_time", "format_products_bitmask", "make_filters", "location_request", "make_loc_ltype_s", "make_locl_type_a", "make_loc_type", "station_board_request", "reconstruction_request", "journey_match_request", "loc_details_request", "loc_geo_pos_request", "loc_geo_reach_request", "journey_geo_pos_request", "trip_request", "line_match_request", "server_info_request", "him_search_request", "journey_request", "search_on_trip_request"]

