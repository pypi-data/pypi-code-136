from __future__ import annotations
from dataclasses import dataclass
from typing import (Any, Optional, Literal, Callable)
from ..fable_library.reflection import (TypeInfo, bool_type, record_type, array_type, obj_type, option_type, string_type, int32_type, class_type)
from ..fable_library.types import (Record, Array)
from ..fable_library.util import curry
from .extra_types import (Icon, Icon_reflection, IndexMap_2)
from .types_hafas_client import (FeatureCollection, Line, Operator, Operator_reflection, Line_reflection, FeatureCollection_reflection, ProductType, JourneysOptions, Alternative, Journey, Leg, Movement, StopOver, Trip, Warning)
from .types_raw_hafas_client import (Cfg, RawRequest, TripSearchRequest, RawCommon, RawJny, RawRem, RawIco, RawPoly, RawLoc, RawProd, RawOutCon, RawSec, RawOp, RawStop, RawHim, RawResult, RawResult_reflection)

def _expr302() -> TypeInfo:
    return record_type("FsHafas.Endpoint.Options", [], Options, lambda: [("remarks", bool_type), ("stopovers", bool_type), ("polylines", bool_type), ("scheduled_days", bool_type), ("sub_stops", bool_type), ("entrances", bool_type), ("lines_of_stops", bool_type), ("first_class", bool_type)])


@dataclass(eq = False, repr = False)
class Options(Record):
    remarks: bool
    stopovers: bool
    polylines: bool
    scheduled_days: bool
    sub_stops: bool
    entrances: bool
    lines_of_stops: bool
    first_class: bool

Options_reflection = _expr302

def _expr303() -> TypeInfo:
    return record_type("FsHafas.Endpoint.CommonData", [], CommonData, lambda: [("operators", array_type(Operator_reflection())), ("locations", array_type(obj_type)), ("lines", array_type(Line_reflection())), ("hints", array_type(option_type(obj_type))), ("icons", array_type(Icon_reflection())), ("polylines", array_type(FeatureCollection_reflection()))])


@dataclass(eq = False, repr = False)
class CommonData(Record):
    operators: Array[Operator]
    locations: Array[Any]
    lines: Array[Line]
    hints: Array[Optional[Any]]
    icons: Array[Icon]
    polylines: Array[FeatureCollection]

CommonData_reflection = _expr303

def _expr304() -> TypeInfo:
    return record_type("FsHafas.Endpoint.ParsedWhen", [], ParsedWhen, lambda: [("when", option_type(string_type)), ("planned_when", option_type(string_type)), ("prognosed_when", option_type(string_type)), ("delay", option_type(int32_type))])


@dataclass(eq = False, repr = False)
class ParsedWhen(Record):
    when: Optional[str]
    planned_when: Optional[str]
    prognosed_when: Optional[str]
    delay: Optional[int]

ParsedWhen_reflection = _expr304

def _expr305() -> TypeInfo:
    return record_type("FsHafas.Endpoint.Platform", [], Platform, lambda: [("platform", option_type(string_type)), ("planned_platform", option_type(string_type)), ("prognosed_platform", option_type(string_type))])


@dataclass(eq = False, repr = False)
class Platform(Record):
    platform: Optional[str]
    planned_platform: Optional[str]
    prognosed_platform: Optional[str]

Platform_reflection = _expr305

def _expr306() -> TypeInfo:
    return class_type("FsHafas.Endpoint.Profile", None, Profile)


class Profile:
    def __init__(self, locale: str, timezone: str, format_station: Callable[[str], str], transform_journeys_query: Callable[[Optional[JourneysOptions], TripSearchRequest], TripSearchRequest], parse_common: Callable[[Context, RawCommon], CommonData], parse_arrival: Callable[[Context, RawJny], Alternative], parse_departure: Callable[[Context, RawJny], Alternative], parse_hint: Callable[[Context, RawRem], Optional[Any]], parse_icon: Callable[[Context, RawIco], Optional[Icon]], parse_polyline: Callable[[Context, RawPoly], FeatureCollection], parse_locations: Callable[[Context, Array[RawLoc]], Array[Any]], parse_line: Callable[[Context, RawProd], Line], parse_journey: Callable[[Context, RawOutCon], Journey], parse_journey_leg: Callable[[Context, RawSec, str], Leg], parse_movement: Callable[[Context, RawJny], Movement], parse_operator: Callable[[Context, RawOp], Operator], parse_platform: Callable[[Context, Optional[str], Optional[str], Optional[bool]], Platform], parse_stopover: Callable[[Context, RawStop, str], StopOver], parse_stopovers: Callable[[Context, Optional[Array[RawStop]], str], Optional[Array[StopOver]]], parse_trip: Callable[[Context, RawJny], Trip], parse_when: Callable[[Context, str, Optional[str], Optional[str], Optional[int], Optional[bool]], ParsedWhen], parse_date_time: Callable[[Context, str, Optional[str], Optional[int]], Optional[str]], parse_bitmask: Callable[[Context, int], IndexMap_2[str, bool]], parse_warning: Callable[[Context, RawHim], Warning], parse_prognosis_type: Callable[[Context, Optional[str]], Optional[str]]) -> None:
        self._salt: str = ""
        self._add_checksum: bool = False
        self._add_mic_mac: bool = False
        self._cfg: Optional[Cfg] = None
        self._base_request: Optional[RawRequest] = None
        self._journeys_out_frwd: bool = False
        self._departures_get_passlist: bool = True
        self._departures_stb_fltr_equiv: bool = True
        self._format_station: Callable[[str], str] = format_station
        self._transform_journeys_query: Callable[[Optional[JourneysOptions], TripSearchRequest], TripSearchRequest] = transform_journeys_query
        self._parse_common: Callable[[Context, RawCommon], CommonData] = parse_common
        self._parse_arrival: Callable[[Context, RawJny], Alternative] = parse_arrival
        self._parse_departure: Callable[[Context, RawJny], Alternative] = parse_departure
        self._parse_hint: Callable[[Context, RawRem], Optional[Any]] = parse_hint
        self._parse_icon: Callable[[Context, RawIco], Optional[Icon]] = parse_icon
        self._parse_polyline: Callable[[Context, RawPoly], FeatureCollection] = parse_polyline
        self._parse_locations: Callable[[Context, Array[RawLoc]], Array[Any]] = parse_locations
        self._parse_line: Callable[[Context, RawProd], Line] = parse_line
        self._parse_journey: Callable[[Context, RawOutCon], Journey] = parse_journey
        self._parse_journey_leg: Callable[[Context, RawSec, str], Leg] = parse_journey_leg
        self._parse_movement: Callable[[Context, RawJny], Movement] = parse_movement
        self._parse_operator: Callable[[Context, RawOp], Operator] = parse_operator
        self._parse_platform: Callable[[Context, Optional[str], Optional[str], Optional[bool]], Platform] = parse_platform
        self._parse_stopover: Callable[[Context, RawStop, str], StopOver] = parse_stopover
        self._parse_stopovers: Callable[[Context, Optional[Array[RawStop]], str], Optional[Array[StopOver]]] = parse_stopovers
        self._parse_trip: Callable[[Context, RawJny], Trip] = parse_trip
        self._parse_when: Callable[[Context, str, Optional[str], Optional[str], Optional[int], Optional[bool]], ParsedWhen] = parse_when
        self._parse_date_time: Callable[[Context, str, Optional[str], Optional[int]], Optional[str]] = parse_date_time
        self._parse_bitmask: Callable[[Context, int], IndexMap_2[str, bool]] = parse_bitmask
        self._parse_warning: Callable[[Context, RawHim], Warning] = parse_warning
        self._parse_prognosis_type: Callable[[Context, Optional[str]], Optional[str]] = parse_prognosis_type
        self.__locale: str = locale
        self.__timezone: str = timezone
        self.__endpoint: str = ""
        self.__products: Array[ProductType] = []
        self.__trip: Optional[bool] = None
        self.__radar: Optional[bool] = None
        self.__refreshJourney: Optional[bool] = None
        self.__journeysFromTrip: Optional[bool] = None
        self.__reachableFrom: Optional[bool] = None
        self.__journeysWalkingSpeed: Optional[bool] = None
        self.__tripsByName: Optional[bool] = None
        self.__remarks: Optional[bool] = None
        self.__remarksGetPolyline: Optional[bool] = None
        self.__lines: Optional[bool] = None

    @property
    def locale(self, __unit: Literal[None]=None) -> str:
        __: Profile = self
        return Profile__get__locale(__)

    @property
    def timezone(self, __unit: Literal[None]=None) -> str:
        __: Profile = self
        return Profile__get__timezone(__)

    @property
    def endpoint(self, __unit: Literal[None]=None) -> str:
        __: Profile = self
        return Profile__get__endpoint(__)

    @property
    def products(self, __unit: Literal[None]=None) -> Array[ProductType]:
        __: Profile = self
        return Profile__get__products(__)

    @property
    def trip(self, __unit: Literal[None]=None) -> Optional[bool]:
        __: Profile = self
        return Profile__get__trip(__)

    @property
    def radar(self, __unit: Literal[None]=None) -> Optional[bool]:
        __: Profile = self
        return Profile__get__radar(__)

    @property
    def refresh_journey(self, __unit: Literal[None]=None) -> Optional[bool]:
        __: Profile = self
        return Profile__get__refreshJourney(__)

    @property
    def journeys_from_trip(self, __unit: Literal[None]=None) -> Optional[bool]:
        __: Profile = self
        return Profile__get__journeysFromTrip(__)

    @property
    def reachable_from(self, __unit: Literal[None]=None) -> Optional[bool]:
        __: Profile = self
        return Profile__get__reachableFrom(__)

    @property
    def journeys_walking_speed(self, __unit: Literal[None]=None) -> Optional[bool]:
        __: Profile = self
        return Profile__get__journeysWalkingSpeed(__)

    @property
    def trips_by_name(self, __unit: Literal[None]=None) -> Optional[bool]:
        __: Profile = self
        return Profile__get__tripsByName(__)

    @property
    def remarks(self, __unit: Literal[None]=None) -> Optional[bool]:
        __: Profile = self
        return Profile__get__remarks(__)

    @property
    def remarks_get_polyline(self, __unit: Literal[None]=None) -> Optional[bool]:
        __: Profile = self
        return Profile__get__remarksGetPolyline(__)

    @property
    def lines(self, __unit: Literal[None]=None) -> Optional[bool]:
        __: Profile = self
        return Profile__get__lines(__)


Profile_reflection = _expr306

def Profile__ctor_Z4BA06F5C(locale: str, timezone: str, format_station: Callable[[str], str], transform_journeys_query: Callable[[Optional[JourneysOptions], TripSearchRequest], TripSearchRequest], parse_common: Callable[[Context, RawCommon], CommonData], parse_arrival: Callable[[Context, RawJny], Alternative], parse_departure: Callable[[Context, RawJny], Alternative], parse_hint: Callable[[Context, RawRem], Optional[Any]], parse_icon: Callable[[Context, RawIco], Optional[Icon]], parse_polyline: Callable[[Context, RawPoly], FeatureCollection], parse_locations: Callable[[Context, Array[RawLoc]], Array[Any]], parse_line: Callable[[Context, RawProd], Line], parse_journey: Callable[[Context, RawOutCon], Journey], parse_journey_leg: Callable[[Context, RawSec, str], Leg], parse_movement: Callable[[Context, RawJny], Movement], parse_operator: Callable[[Context, RawOp], Operator], parse_platform: Callable[[Context, Optional[str], Optional[str], Optional[bool]], Platform], parse_stopover: Callable[[Context, RawStop, str], StopOver], parse_stopovers: Callable[[Context, Optional[Array[RawStop]], str], Optional[Array[StopOver]]], parse_trip: Callable[[Context, RawJny], Trip], parse_when: Callable[[Context, str, Optional[str], Optional[str], Optional[int], Optional[bool]], ParsedWhen], parse_date_time: Callable[[Context, str, Optional[str], Optional[int]], Optional[str]], parse_bitmask: Callable[[Context, int], IndexMap_2[str, bool]], parse_warning: Callable[[Context, RawHim], Warning], parse_prognosis_type: Callable[[Context, Optional[str]], Optional[str]]) -> Profile:
    return Profile(locale, timezone, format_station, transform_journeys_query, parse_common, parse_arrival, parse_departure, parse_hint, parse_icon, parse_polyline, parse_locations, parse_line, parse_journey, parse_journey_leg, parse_movement, parse_operator, parse_platform, parse_stopover, parse_stopovers, parse_trip, parse_when, parse_date_time, parse_bitmask, parse_warning, parse_prognosis_type)


def _expr307() -> TypeInfo:
    return record_type("FsHafas.Endpoint.Context", [], Context, lambda: [("profile", Profile_reflection()), ("opt", Options_reflection()), ("common", CommonData_reflection()), ("res", RawResult_reflection())])


@dataclass(eq = False, repr = False)
class Context(Record):
    profile: Profile
    opt: Options
    common: CommonData
    res: RawResult

Context_reflection = _expr307

def Profile__get_salt(__: Profile) -> str:
    return __._salt


def Profile__set_salt_Z721C83C5(__: Profile, v: str) -> None:
    __._salt = v


def Profile__get_addChecksum(__: Profile) -> bool:
    return __._add_checksum


def Profile__set_addChecksum_Z1FBCCD16(__: Profile, v: bool) -> None:
    __._add_checksum = v


def Profile__get_addMicMac(__: Profile) -> bool:
    return __._add_mic_mac


def Profile__set_addMicMac_Z1FBCCD16(__: Profile, v: bool) -> None:
    __._add_mic_mac = v


def Profile__get_cfg(__: Profile) -> Optional[Cfg]:
    return __._cfg


def Profile__set_cfg_Z3219B2F8(__: Profile, v: Optional[Cfg]=None) -> None:
    __._cfg = v


def Profile__get_baseRequest(__: Profile) -> Optional[RawRequest]:
    return __._base_request


def Profile__set_baseRequest_Z42C91061(__: Profile, v: Optional[RawRequest]=None) -> None:
    __._base_request = v


def Profile__get_journeysOutFrwd(__: Profile) -> bool:
    return __._journeys_out_frwd


def Profile__set_journeysOutFrwd_Z1FBCCD16(__: Profile, v: bool) -> None:
    __._journeys_out_frwd = v


def Profile__get_departuresGetPasslist(__: Profile) -> bool:
    return __._departures_get_passlist


def Profile__set_departuresGetPasslist_Z1FBCCD16(__: Profile, v: bool) -> None:
    __._departures_get_passlist = v


def Profile__get_departuresStbFltrEquiv(__: Profile) -> bool:
    return __._departures_stb_fltr_equiv


def Profile__set_departuresStbFltrEquiv_Z1FBCCD16(__: Profile, v: bool) -> None:
    __._departures_stb_fltr_equiv = v


def Profile__get_formatStation(__: Profile) -> Callable[[str], str]:
    return __._format_station


def Profile__set_formatStation_11D407F6(__: Profile, v: Callable[[str], str]) -> None:
    __._format_station = v


def Profile__get_transformJourneysQuery(__: Profile) -> Callable[[Optional[JourneysOptions], TripSearchRequest], TripSearchRequest]:
    return curry(2, __._transform_journeys_query)


def Profile__set_transformJourneysQuery_4AA4AF64(__: Profile, v: Callable[[Optional[JourneysOptions], TripSearchRequest], TripSearchRequest]) -> None:
    __._transform_journeys_query = v


def Profile__get_parseCommon(__: Profile) -> Callable[[Context, RawCommon], CommonData]:
    return curry(2, __._parse_common)


def Profile__set_parseCommon_7B6CA622(__: Profile, v: Callable[[Context, RawCommon], CommonData]) -> None:
    __._parse_common = v


def Profile__get_parseArrival(__: Profile) -> Callable[[Context, RawJny], Alternative]:
    return curry(2, __._parse_arrival)


def Profile__set_parseArrival_537DC5A(__: Profile, v: Callable[[Context, RawJny], Alternative]) -> None:
    __._parse_arrival = v


def Profile__get_parseDeparture(__: Profile) -> Callable[[Context, RawJny], Alternative]:
    return curry(2, __._parse_departure)


def Profile__set_parseDeparture_537DC5A(__: Profile, v: Callable[[Context, RawJny], Alternative]) -> None:
    __._parse_departure = v


def Profile__get_parseHint(__: Profile) -> Callable[[Context, RawRem], Optional[Any]]:
    return curry(2, __._parse_hint)


def Profile__set_parseHint_2044943E(__: Profile, v: Callable[[Context, RawRem], Optional[Any]]) -> None:
    __._parse_hint = v


def Profile__get_parseIcon(__: Profile) -> Callable[[Context, RawIco], Optional[Icon]]:
    return curry(2, __._parse_icon)


def Profile__set_parseIcon_ZB647E9B(__: Profile, v: Callable[[Context, RawIco], Optional[Icon]]) -> None:
    __._parse_icon = v


def Profile__get_parsePolyline(__: Profile) -> Callable[[Context, RawPoly], FeatureCollection]:
    return curry(2, __._parse_polyline)


def Profile__set_parsePolyline_20B28720(__: Profile, v: Callable[[Context, RawPoly], FeatureCollection]) -> None:
    __._parse_polyline = v


def Profile__get_parseLocations(__: Profile) -> Callable[[Context, Array[RawLoc]], Array[Any]]:
    return curry(2, __._parse_locations)


def Profile__set_parseLocations_E0B75C7(__: Profile, v: Callable[[Context, Array[RawLoc]], Array[Any]]) -> None:
    __._parse_locations = v


def Profile__get_parseLine(__: Profile) -> Callable[[Context, RawProd], Line]:
    return curry(2, __._parse_line)


def Profile__set_parseLine_718F82F(__: Profile, v: Callable[[Context, RawProd], Line]) -> None:
    __._parse_line = v


def Profile__get_parseJourney(__: Profile) -> Callable[[Context, RawOutCon], Journey]:
    return curry(2, __._parse_journey)


def Profile__set_parseJourney_Z1F35F4C(__: Profile, v: Callable[[Context, RawOutCon], Journey]) -> None:
    __._parse_journey = v


def Profile__get_parseJourneyLeg(__: Profile) -> Callable[[Context, RawSec, str], Leg]:
    return curry(3, __._parse_journey_leg)


def Profile__set_parseJourneyLeg_3913217E(__: Profile, v: Callable[[Context, RawSec, str], Leg]) -> None:
    __._parse_journey_leg = v


def Profile__get_parseMovement(__: Profile) -> Callable[[Context, RawJny], Movement]:
    return curry(2, __._parse_movement)


def Profile__set_parseMovement_Z6A30A80A(__: Profile, v: Callable[[Context, RawJny], Movement]) -> None:
    __._parse_movement = v


def Profile__get_parseOperator(__: Profile) -> Callable[[Context, RawOp], Operator]:
    return curry(2, __._parse_operator)


def Profile__set_parseOperator_1470F537(__: Profile, v: Callable[[Context, RawOp], Operator]) -> None:
    __._parse_operator = v


def Profile__get_parsePlatform(__: Profile) -> Callable[[Context, Optional[str], Optional[str], Optional[bool]], Platform]:
    return curry(4, __._parse_platform)


def Profile__set_parsePlatform_5B26FC49(__: Profile, v: Callable[[Context, Optional[str], Optional[str], Optional[bool]], Platform]) -> None:
    __._parse_platform = v


def Profile__get_parseStopover(__: Profile) -> Callable[[Context, RawStop, str], StopOver]:
    return curry(3, __._parse_stopover)


def Profile__set_parseStopover_Z23BF7DB5(__: Profile, v: Callable[[Context, RawStop, str], StopOver]) -> None:
    __._parse_stopover = v


def Profile__get_parseStopovers(__: Profile) -> Callable[[Context, Optional[Array[RawStop]], str], Optional[Array[StopOver]]]:
    return curry(3, __._parse_stopovers)


def Profile__set_parseStopovers_Z256E0AD5(__: Profile, v: Callable[[Context, Optional[Array[RawStop]], str], Optional[Array[StopOver]]]) -> None:
    __._parse_stopovers = v


def Profile__get_parseTrip(__: Profile) -> Callable[[Context, RawJny], Trip]:
    return curry(2, __._parse_trip)


def Profile__set_parseTrip_Z4AA6F376(__: Profile, v: Callable[[Context, RawJny], Trip]) -> None:
    __._parse_trip = v


def Profile__get_parseWhen(__: Profile) -> Callable[[Context, str, Optional[str], Optional[str], Optional[int], Optional[bool]], ParsedWhen]:
    return curry(6, __._parse_when)


def Profile__set_parseWhen_58E948D7(__: Profile, v: Callable[[Context, str, Optional[str], Optional[str], Optional[int], Optional[bool]], ParsedWhen]) -> None:
    __._parse_when = v


def Profile__get_parseDateTime(__: Profile) -> Callable[[Context, str, Optional[str], Optional[int]], Optional[str]]:
    return curry(4, __._parse_date_time)


def Profile__set_parseDateTime_ZC71C28B(__: Profile, v: Callable[[Context, str, Optional[str], Optional[int]], Optional[str]]) -> None:
    __._parse_date_time = v


def Profile__get_parseBitmask(__: Profile) -> Callable[[Context, int], IndexMap_2[str, bool]]:
    return curry(2, __._parse_bitmask)


def Profile__set_parseBitmask_797ABA12(__: Profile, v: Callable[[Context, int], IndexMap_2[str, bool]]) -> None:
    __._parse_bitmask = v


def Profile__get_parseWarning(__: Profile) -> Callable[[Context, RawHim], Warning]:
    return curry(2, __._parse_warning)


def Profile__set_parseWarning_1F58EC2E(__: Profile, v: Callable[[Context, RawHim], Warning]) -> None:
    __._parse_warning = v


def Profile__get_parsePrognosisType(__: Profile) -> Callable[[Context, Optional[str]], Optional[str]]:
    return curry(2, __._parse_prognosis_type)


def Profile__set_parsePrognosisType_Z334179EF(__: Profile, v: Callable[[Context, Optional[str]], Optional[str]]) -> None:
    __._parse_prognosis_type = v


def Profile__get__locale(__: Profile) -> str:
    return __.__locale


def Profile__set__locale_Z721C83C5(__: Profile, v: str) -> None:
    __.__locale = v


def Profile__get__timezone(__: Profile) -> str:
    return __.__timezone


def Profile__set__timezone_Z721C83C5(__: Profile, v: str) -> None:
    __.__timezone = v


def Profile__get__endpoint(__: Profile) -> str:
    return __.__endpoint


def Profile__set__endpoint_Z721C83C5(__: Profile, v: str) -> None:
    __.__endpoint = v


def Profile__get__products(__: Profile) -> Array[ProductType]:
    return __.__products


def Profile__set__products_Z4ED450D4(__: Profile, v: Array[ProductType]) -> None:
    __.__products = v


def Profile__get__trip(__: Profile) -> Optional[bool]:
    return __.__trip


def Profile__set__trip_6FCE9E49(__: Profile, v: Optional[bool]=None) -> None:
    __.__trip = v


def Profile__get__radar(__: Profile) -> Optional[bool]:
    return __.__radar


def Profile__set__radar_6FCE9E49(__: Profile, v: Optional[bool]=None) -> None:
    __.__radar = v


def Profile__get__refreshJourney(__: Profile) -> Optional[bool]:
    return __.__refreshJourney


def Profile__set__refreshJourney_6FCE9E49(__: Profile, v: Optional[bool]=None) -> None:
    __.__refreshJourney = v


def Profile__get__journeysFromTrip(__: Profile) -> Optional[bool]:
    return __.__journeysFromTrip


def Profile__set__journeysFromTrip_6FCE9E49(__: Profile, v: Optional[bool]=None) -> None:
    __.__journeysFromTrip = v


def Profile__get__reachableFrom(__: Profile) -> Optional[bool]:
    return __.__reachableFrom


def Profile__set__reachableFrom_6FCE9E49(__: Profile, v: Optional[bool]=None) -> None:
    __.__reachableFrom = v


def Profile__get__journeysWalkingSpeed(__: Profile) -> Optional[bool]:
    return __.__journeysWalkingSpeed


def Profile__set__journeysWalkingSpeed_6FCE9E49(__: Profile, v: Optional[bool]=None) -> None:
    __.__journeysWalkingSpeed = v


def Profile__get__tripsByName(__: Profile) -> Optional[bool]:
    return __.__tripsByName


def Profile__set__tripsByName_6FCE9E49(__: Profile, v: Optional[bool]=None) -> None:
    __.__tripsByName = v


def Profile__get__remarks(__: Profile) -> Optional[bool]:
    return __.__remarks


def Profile__set__remarks_6FCE9E49(__: Profile, v: Optional[bool]=None) -> None:
    __.__remarks = v


def Profile__get__remarksGetPolyline(__: Profile) -> Optional[bool]:
    return __.__remarksGetPolyline


def Profile__set__remarksGetPolyline_6FCE9E49(__: Profile, v: Optional[bool]=None) -> None:
    __.__remarksGetPolyline = v


def Profile__get__lines(__: Profile) -> Optional[bool]:
    return __.__lines


def Profile__set__lines_6FCE9E49(__: Profile, v: Optional[bool]=None) -> None:
    __.__lines = v


__all__ = ["Options_reflection", "CommonData_reflection", "ParsedWhen_reflection", "Platform_reflection", "Profile_reflection", "Context_reflection", "Profile__get_salt", "Profile__set_salt_Z721C83C5", "Profile__get_addChecksum", "Profile__set_addChecksum_Z1FBCCD16", "Profile__get_addMicMac", "Profile__set_addMicMac_Z1FBCCD16", "Profile__get_cfg", "Profile__set_cfg_Z3219B2F8", "Profile__get_baseRequest", "Profile__set_baseRequest_Z42C91061", "Profile__get_journeysOutFrwd", "Profile__set_journeysOutFrwd_Z1FBCCD16", "Profile__get_departuresGetPasslist", "Profile__set_departuresGetPasslist_Z1FBCCD16", "Profile__get_departuresStbFltrEquiv", "Profile__set_departuresStbFltrEquiv_Z1FBCCD16", "Profile__get_formatStation", "Profile__set_formatStation_11D407F6", "Profile__get_transformJourneysQuery", "Profile__set_transformJourneysQuery_4AA4AF64", "Profile__get_parseCommon", "Profile__set_parseCommon_7B6CA622", "Profile__get_parseArrival", "Profile__set_parseArrival_537DC5A", "Profile__get_parseDeparture", "Profile__set_parseDeparture_537DC5A", "Profile__get_parseHint", "Profile__set_parseHint_2044943E", "Profile__get_parseIcon", "Profile__set_parseIcon_ZB647E9B", "Profile__get_parsePolyline", "Profile__set_parsePolyline_20B28720", "Profile__get_parseLocations", "Profile__set_parseLocations_E0B75C7", "Profile__get_parseLine", "Profile__set_parseLine_718F82F", "Profile__get_parseJourney", "Profile__set_parseJourney_Z1F35F4C", "Profile__get_parseJourneyLeg", "Profile__set_parseJourneyLeg_3913217E", "Profile__get_parseMovement", "Profile__set_parseMovement_Z6A30A80A", "Profile__get_parseOperator", "Profile__set_parseOperator_1470F537", "Profile__get_parsePlatform", "Profile__set_parsePlatform_5B26FC49", "Profile__get_parseStopover", "Profile__set_parseStopover_Z23BF7DB5", "Profile__get_parseStopovers", "Profile__set_parseStopovers_Z256E0AD5", "Profile__get_parseTrip", "Profile__set_parseTrip_Z4AA6F376", "Profile__get_parseWhen", "Profile__set_parseWhen_58E948D7", "Profile__get_parseDateTime", "Profile__set_parseDateTime_ZC71C28B", "Profile__get_parseBitmask", "Profile__set_parseBitmask_797ABA12", "Profile__get_parseWarning", "Profile__set_parseWarning_1F58EC2E", "Profile__get_parsePrognosisType", "Profile__set_parsePrognosisType_Z334179EF", "Profile__get__locale", "Profile__set__locale_Z721C83C5", "Profile__get__timezone", "Profile__set__timezone_Z721C83C5", "Profile__get__endpoint", "Profile__set__endpoint_Z721C83C5", "Profile__get__products", "Profile__set__products_Z4ED450D4", "Profile__get__trip", "Profile__set__trip_6FCE9E49", "Profile__get__radar", "Profile__set__radar_6FCE9E49", "Profile__get__refreshJourney", "Profile__set__refreshJourney_6FCE9E49", "Profile__get__journeysFromTrip", "Profile__set__journeysFromTrip_6FCE9E49", "Profile__get__reachableFrom", "Profile__set__reachableFrom_6FCE9E49", "Profile__get__journeysWalkingSpeed", "Profile__set__journeysWalkingSpeed_6FCE9E49", "Profile__get__tripsByName", "Profile__set__tripsByName_6FCE9E49", "Profile__get__remarks", "Profile__set__remarks_6FCE9E49", "Profile__get__remarksGetPolyline", "Profile__set__remarksGetPolyline_6FCE9E49", "Profile__get__lines", "Profile__set__lines_6FCE9E49"]

