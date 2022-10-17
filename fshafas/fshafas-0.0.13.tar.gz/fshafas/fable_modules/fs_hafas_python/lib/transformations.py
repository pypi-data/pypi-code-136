from __future__ import annotations
from typing import (Any, Optional, TypeVar, Callable)
from ...fable_library.date import now
from ...fable_library.double import divide
from ...fable_library.option import (some, value as value_1)
from ...fable_library.util import round
from ..context import Options
from ..extra_types import IndexMap_2__ctor_2B594
from ..types_hafas_client import (Leg, Trip, Station, Stop, Location, JourneysOptions, JourneysFromTripOptions, LocationsOptions, NearByOptions, TripOptions, LinesOptions, RemarksOptions, RefreshJourneyOptions, TripsByNameOptions, DeparturesArrivalsOptions, StopOptions, ReachableFromOptions, RadarOptions, ServerOptions, StopOver, Movement, Alternative, Journey, Journeys, Line, Warning, ServerInfo)
from ..types_raw_hafas_client import (RawStop, RawDep, RawArr)

_A = TypeVar("_A")

_B = TypeVar("_B")

def Coordinate_toFloat(v: int) -> float:
    return divide(v, 1000000.0)


def Coordinate_fromFloat(x: float) -> int:
    return int(round(x * 1000000.0))


def RawDep_FromRawStopL(s: RawStop) -> RawDep:
    return RawDep(s.loc_x, s.idx, s.d_prod_x, s.d_platf_s, s.d_in_r, s.d_time_s, s.d_prog_type, None, s.d_tzoffset, None, s.d_time_r, s.d_cncl, s.d_pltf_s, s.d_platf_r, s.d_pltf_r)


def RawArr_FromRawStopL(s: RawStop) -> RawArr:
    return RawArr(s.loc_x, s.idx, s.a_platf_s, s.a_out_r, s.a_time_s, s.a_prog_type, s.a_tzoffset, None, s.a_time_r, s.a_cncl, s.a_pltf_s, s.a_platf_r, s.a_pltf_r, None)


def ToTrip_FromLeg(id: str, l: Leg) -> Trip:
    return Trip(id, l.origin, l.destination, l.departure, l.planned_departure, l.prognosed_arrival, l.departure_delay, l.departure_platform, l.prognosed_departure_platform, l.planned_departure_platform, l.arrival, l.planned_arrival, l.prognosed_departure, l.arrival_delay, l.arrival_platform, l.prognosed_arrival_platform, l.planned_arrival_platform, l.stopovers, l.schedule, l.price, l.operator, l.direction, l.line, l.reachable, l.cancelled, l.walking, l.load_factor, l.distance, l.public, l.transfer, l.cycle, l.alternatives, l.polyline, l.remarks)


def U2StationStop_FromU3StationStopLocation(u3: Any=None) -> Optional[Any]:
    if isinstance(u3, Station):
        return some(u3)

    elif isinstance(u3, Stop):
        return some(u3)

    else: 
        return None



def U2StationStop_FromSomeU3StationStopLocation(u3: Optional[Any]=None) -> Optional[Any]:
    (pattern_matching_result, s, s_1) = (None, None, None)
    if u3 is not None:
        if isinstance(value_1(u3), Station):
            pattern_matching_result = 0
            s = value_1(u3)

        elif isinstance(value_1(u3), Stop):
            pattern_matching_result = 1
            s_1 = value_1(u3)

        else: 
            pattern_matching_result = 2


    else: 
        pattern_matching_result = 2

    if pattern_matching_result == 0:
        return some(s)

    elif pattern_matching_result == 1:
        return some(s_1)

    elif pattern_matching_result == 2:
        return None



def U2StopLocation_FromU3StationStopLocation(u3: Any=None) -> Optional[Any]:
    if isinstance(u3, Stop):
        return some(u3)

    elif isinstance(u3, Location):
        return some(u3)

    else: 
        return None



def U2StopLocation_FromSomeU3StationStopLocation(u3: Optional[Any]=None) -> Optional[Any]:
    (pattern_matching_result, s, s_1) = (None, None, None)
    if u3 is not None:
        if isinstance(value_1(u3), Stop):
            pattern_matching_result = 0
            s = value_1(u3)

        elif isinstance(value_1(u3), Location):
            pattern_matching_result = 1
            s_1 = value_1(u3)

        else: 
            pattern_matching_result = 2


    else: 
        pattern_matching_result = 2

    if pattern_matching_result == 0:
        return some(s)

    elif pattern_matching_result == 1:
        return some(s_1)

    elif pattern_matching_result == 2:
        return None



def MergeOptions_getOptionValue(opt: Optional[_A], getter: Callable[[_A], Optional[_B]], default_value: _B) -> _B:
    if opt is None:
        return default_value

    else: 
        match_value: Optional[_B] = getter(value_1(opt))
        if match_value is None:
            return default_value

        else: 
            return value_1(match_value)




def MergeOptions_JourneysOptions(options: Options, opt: Optional[JourneysOptions]=None) -> Options:
    def _arrow308(v: JourneysOptions, options: Options=options, opt: Optional[JourneysOptions]=opt) -> Optional[bool]:
        return v.remarks

    def _arrow309(v_1: JourneysOptions, options: Options=options, opt: Optional[JourneysOptions]=opt) -> Optional[bool]:
        return v_1.stopovers

    def _arrow310(v_2: JourneysOptions, options: Options=options, opt: Optional[JourneysOptions]=opt) -> Optional[bool]:
        return v_2.scheduled_days

    def _arrow311(v_3: JourneysOptions, options: Options=options, opt: Optional[JourneysOptions]=opt) -> Optional[bool]:
        return v_3.first_class

    return Options(MergeOptions_getOptionValue(opt, _arrow308, options.remarks), MergeOptions_getOptionValue(opt, _arrow309, options.stopovers), options.polylines, MergeOptions_getOptionValue(opt, _arrow310, options.scheduled_days), options.sub_stops, options.entrances, options.lines_of_stops, MergeOptions_getOptionValue(opt, _arrow311, options.first_class))


def MergeOptions_JourneysFromTripOptions(options: Options, opt: Optional[JourneysFromTripOptions]=None) -> Options:
    def _arrow312(v: JourneysFromTripOptions, options: Options=options, opt: Optional[JourneysFromTripOptions]=opt) -> Optional[bool]:
        return v.stopovers

    return Options(options.remarks, MergeOptions_getOptionValue(opt, _arrow312, options.stopovers), options.polylines, options.scheduled_days, options.sub_stops, options.entrances, options.lines_of_stops, options.first_class)


def MergeOptions_LocationsOptions(options: Options, opt: Optional[LocationsOptions]=None) -> Options:
    def _arrow313(v: LocationsOptions, options: Options=options, opt: Optional[LocationsOptions]=opt) -> Optional[bool]:
        return v.lines_of_stops

    return Options(options.remarks, options.stopovers, options.polylines, options.scheduled_days, options.sub_stops, options.entrances, MergeOptions_getOptionValue(opt, _arrow313, options.lines_of_stops), options.first_class)


def MergeOptions_NearByOptions(options: Options, opt: Optional[NearByOptions]=None) -> Options:
    def _arrow314(v: NearByOptions, options: Options=options, opt: Optional[NearByOptions]=opt) -> Optional[bool]:
        return v.lines_of_stops

    return Options(options.remarks, options.stopovers, options.polylines, options.scheduled_days, options.sub_stops, options.entrances, MergeOptions_getOptionValue(opt, _arrow314, options.lines_of_stops), options.first_class)


Default_TripOptions: TripOptions = TripOptions(True, True, True, True, True, "de")

Default_LinesOptions: LinesOptions = LinesOptions("de")

Default_RemarksOptions: RemarksOptions = RemarksOptions(now(), None, 100, IndexMap_2__ctor_2B594(False), False, "de")

Default_LocationsOptions: LocationsOptions = LocationsOptions(True, 5, True, True, True, True, True, False, "de")

Default_RefreshJourneyOptions: RefreshJourneyOptions = RefreshJourneyOptions(True, False, False, None, None, None, "de")

Default_TripsByNameOptions: TripsByNameOptions = TripsByNameOptions(now(), None, None, None, None, None, None, None, None)

Default_NearByOptions: NearByOptions = NearByOptions(8, -1, None, True, IndexMap_2__ctor_2B594(False), None, None, None, "de")

Default_JourneysOptions: JourneysOptions = JourneysOptions(now(), None, None, None, 3, None, True, -1, 0, "none", False, IndexMap_2__ctor_2B594(False), False, False, True, True, True, "normal", True, "de", False, False, None, None, None)

Default_JourneysFromTripOptions: JourneysFromTripOptions = JourneysFromTripOptions(False, 0, "none", False, False, True, True, True, IndexMap_2__ctor_2B594(False))

Default_DeparturesArrivalsOptions: DeparturesArrivalsOptions = DeparturesArrivalsOptions(now(), None, None, 10, None, None, None, None, None, False, False, IndexMap_2__ctor_2B594(False), "de")

Default_StopOptions: StopOptions = StopOptions(None, None, None, None, "de")

Default_ReachableFromOptions: ReachableFromOptions = ReachableFromOptions(now(), 5, 20, IndexMap_2__ctor_2B594(False), None, None, None)

Default_RadarOptions: RadarOptions = RadarOptions(256, 3, IndexMap_2__ctor_2B594(False), 30, True, True, True, now())

Default_ServerOptions: ServerOptions = ServerOptions(True, "de")

Default_Location: Location = Location("location", None, None, None, None, None, None, None, None)

Default_Stop: Stop = Stop("stop", None, None, None, None, None, None, None, None, None, None, None, None, None)

Default_Station: Station = Station("station", None, None, None, None, None, None, None, None, None, None, None, None, None, None)

Default_Leg: Leg = Leg(None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)

Default_StopOver: StopOver = StopOver(None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)

Default_Trip: Trip = Trip("", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)

Default_Movement: Movement = Movement(None, None, None, None, None, None, None)

Default_Alternative: Alternative = Alternative("", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)

Default_Journey: Journey = Journey("journey", [], None, None, None, None, None)

Default_Journeys: Journeys = Journeys(None, None, None, None)

Default_Line: Line = Line("line", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)

Default_Warning: Warning = Warning("warning", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)

Default_ServerInfo: ServerInfo = ServerInfo(None, None, None, None, None)

__all__ = ["Coordinate_toFloat", "Coordinate_fromFloat", "RawDep_FromRawStopL", "RawArr_FromRawStopL", "ToTrip_FromLeg", "U2StationStop_FromU3StationStopLocation", "U2StationStop_FromSomeU3StationStopLocation", "U2StopLocation_FromU3StationStopLocation", "U2StopLocation_FromSomeU3StationStopLocation", "MergeOptions_getOptionValue", "MergeOptions_JourneysOptions", "MergeOptions_JourneysFromTripOptions", "MergeOptions_LocationsOptions", "MergeOptions_NearByOptions", "Default_TripOptions", "Default_LinesOptions", "Default_RemarksOptions", "Default_LocationsOptions", "Default_RefreshJourneyOptions", "Default_TripsByNameOptions", "Default_NearByOptions", "Default_JourneysOptions", "Default_JourneysFromTripOptions", "Default_DeparturesArrivalsOptions", "Default_StopOptions", "Default_ReachableFromOptions", "Default_RadarOptions", "Default_ServerOptions", "Default_Location", "Default_Stop", "Default_Station", "Default_Leg", "Default_StopOver", "Default_Trip", "Default_Movement", "Default_Alternative", "Default_Journey", "Default_Journeys", "Default_Line", "Default_Warning", "Default_ServerInfo"]

