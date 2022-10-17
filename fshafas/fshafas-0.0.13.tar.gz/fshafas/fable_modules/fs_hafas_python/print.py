from __future__ import annotations
from typing import (Optional, TypeVar, Literal, Any, Callable)
from ..fable_library.array import fold as fold_1
from ..fable_library.double import divide
from ..fable_library.option import (to_array, value as value_2)
from ..fable_library.seq import fold
from ..fable_library.string import (replicate, to_text, printf)
from ..fable_library.types import Array
from ..fable_library.util import int32_to_string
from .parse.journey import distance_of_journey
from .types_hafas_client import (Location as Location_1, Stop as Stop_1, Station as Station_1, Alternative as Alternative_1, Hint, Status, Warning as Warning_1, Leg as Leg_1, Line as Line_1, StopOver as StopOver_1, Trip as Trip_1, Journey as Journey_1, Price, Journeys as Journeys_1, Duration as Duration_1, Movement as Movement_1)

_A = TypeVar("_A")

nl: str = "\n"

def printf_s(ident: int, prefix: str, s: Optional[str]=None) -> str:
    ident_s: str = replicate(ident, " ")
    def folder(s_1: str, value: str, ident: int=ident, prefix: str=prefix, s: Optional[str]=s) -> str:
        return s_1 + (to_text(printf("%s%s%s%s"))(ident_s)(prefix)(value)(")") if (prefix == "(") else to_text(printf("%s%s%s"))(ident_s)(prefix)(value))

    return fold(folder, "", to_array(s))


def printfn_s(ident: int, prefix: str, s: Optional[str]=None) -> str:
    return printf_s(ident, prefix, s) + nl


def printfn_arr_l(ident: int, prefix: str, arr: Optional[Array[_A]]=None) -> str:
    ident_s: str = replicate(ident, " ")
    (pattern_matching_result, value_1) = (None, None)
    if arr is not None:
        if len(arr) > 0:
            pattern_matching_result = 0
            value_1 = arr

        else: 
            pattern_matching_result = 1


    else: 
        pattern_matching_result = 1

    if pattern_matching_result == 0:
        def _arrow532(__unit: Literal[None]=None, ident: int=ident, prefix: str=prefix, arr: Optional[Array[_A]]=arr) -> str:
            arg_2: int = len(value_1) or 0
            return to_text(printf("%s%s%d"))(ident_s)(prefix)(arg_2)

        return _arrow532() + nl

    elif pattern_matching_result == 1:
        return ""



def printfn_b(ident: int, prefix: str, b: Optional[bool]=None) -> str:
    ident_s: str = replicate(ident, " ")
    (pattern_matching_result, value_1) = (None, None)
    if b is not None:
        if b:
            pattern_matching_result = 0
            value_1 = b

        else: 
            pattern_matching_result = 1


    else: 
        pattern_matching_result = 1

    if pattern_matching_result == 0:
        return to_text(printf("%s%s%b"))(ident_s)(prefix)(value_1) + nl

    elif pattern_matching_result == 1:
        return ""



def print_distance(ident: int, d: Optional[int]=None) -> str:
    ident_s: str = replicate(ident, " ")
    (pattern_matching_result, d_2) = (None, None)
    if d is not None:
        if d > 0:
            pattern_matching_result = 0
            d_2 = d

        else: 
            pattern_matching_result = 1


    else: 
        pattern_matching_result = 1

    if pattern_matching_result == 0:
        km: float = divide(d_2, 1000.0)
        return to_text(printf("%s%s%0.3f"))(ident_s)("distance: ")(km) + nl

    elif pattern_matching_result == 1:
        return ""



def print_lon_lat(ident: int, lon: Optional[float]=None, lat: Optional[float]=None) -> str:
    ident_s: str = replicate(ident, " ")
    (pattern_matching_result, lat_1, lon_1) = (None, None, None)
    if lon is not None:
        if lat is not None:
            pattern_matching_result = 0
            lat_1 = lat
            lon_1 = lon

        else: 
            pattern_matching_result = 1


    else: 
        pattern_matching_result = 1

    if pattern_matching_result == 0:
        return to_text(printf("%s%s%f,%f"))(ident_s)("lonlat: ")(lon_1)(lat_1)

    elif pattern_matching_result == 1:
        return ""



def print_name_id(ident: int, name: Optional[str]=None, id: Optional[str]=None) -> str:
    return printf_s(ident, "", name) + printf_s(ident, "(", id)


def Location(ident: int, location: Location_1) -> str:
    return ((((print_name_id(ident, location.name, location.id) + " ") if (location.name is not None) else ((print_name_id(ident, location.address, location.id) + " ") if (location.address is not None) else "")) + print_lon_lat(ident, location.longitude, location.latitude)) + nl) + print_distance(ident + 2, location.distance)


def Stop(ident: int, stop: Stop_1) -> str:
    def _arrow533(__unit: Literal[None]=None, ident: int=ident, stop: Stop_1=stop) -> str:
        match_value: Optional[Location_1] = stop.location
        if match_value is None:
            return ""

        else: 
            location: Location_1 = match_value
            return " " + print_lon_lat(ident, location.longitude, location.latitude)


    return ((print_name_id(ident, stop.name, stop.id) + _arrow533()) + nl) + print_distance(ident + 2, stop.distance)


def Station(ident: int, station: Station_1) -> str:
    return (print_name_id(ident, station.name, station.id) + nl) + print_distance(ident + 2, station.distance)


def Alternative(ident: int, alternative: Alternative_1) -> str:
    def _arrow534(__unit: Literal[None]=None, ident: int=ident, alternative: Alternative_1=alternative) -> str:
        match_value: Optional[Any] = alternative.stop
        if match_value is not None:
            stop: Any = value_2(match_value)
            return (printf_s(ident, "stop: ", "") + Stop(0, stop)) if isinstance(stop, Stop_1) else ""

        else: 
            return ""


    return (printfn_s(ident, "direction: ", alternative.direction) + printfn_s(ident, "when: ", alternative.when)) + _arrow534()


def Comment(ident: int, s: str) -> str:
    if len(s) > 0:
        return printfn_s(ident, "---", "")

    else: 
        return ""



def Remark(ident: int, remark: Any=None) -> str:
    if isinstance(remark, Hint):
        return printfn_s(ident, "hint: ", remark.text)

    elif isinstance(remark, Status):
        return printfn_s(ident, "status: ", remark.text)

    else: 
        return ""



def Warning(ident: int, w: Warning_1) -> str:
    return (printfn_s(ident, "warning: ", w.summary) + printfn_s(ident + 2, "validFrom: ", w.valid_from)) + printfn_s(ident + 2, "validUntil: ", w.valid_until)


def Remarks(ident: int, remarks: Optional[Array[Any]]=None) -> str:
    if remarks is None:
        return ""

    else: 
        def folder(s: str, r: Any=None, ident: int=ident, remarks: Optional[Array[Any]]=remarks) -> str:
            return s + Remark(ident + 2, r)

        return fold_1(folder, "", remarks)



def ProductOfLeg(ident: int, leg: Leg_1) -> str:
    match_value: Optional[Line_1] = leg.line
    if match_value is None:
        return ""

    else: 
        match_value_1: Optional[str] = match_value.product
        if match_value_1 is None:
            return ""

        else: 
            return printfn_s(ident, "product: ", match_value_1)




def StopOverStop(ident: int, so: StopOver_1) -> str:
    match_value: Optional[Any] = so.stop
    if match_value is not None:
        if isinstance(value_2(match_value), Station_1):
            s_1: Station_1 = value_2(match_value)
            return printf_s(ident, "", "") + Station(0, s_1)

        else: 
            s: Stop_1 = value_2(match_value)
            return printf_s(ident, "", "") + Stop(0, s)


    else: 
        return ""



def StopOver(ident: int, so: StopOver_1) -> str:
    def _arrow537(__unit: Literal[None]=None, ident: int=ident, so: StopOver_1=so) -> str:
        match_value: Optional[Any] = so.stop
        def _arrow535(__unit: Literal[None]=None) -> str:
            s_1: Station_1 = value_2(match_value)
            return printf_s(ident, "origin: ", "") + Station(0, s_1)

        def _arrow536(__unit: Literal[None]=None) -> str:
            s: Stop_1 = value_2(match_value)
            return printf_s(ident, "origin: ", "") + Stop(0, s)

        return (_arrow535() if isinstance(value_2(match_value), Station_1) else _arrow536()) if (match_value is not None) else ""

    def _arrow538(__unit: Literal[None]=None, ident: int=ident, so: StopOver_1=so) -> str:
        match_value_1: Optional[str] = so.departure
        if match_value_1 is None:
            return printfn_s(ident, "arrival: ", so.arrival)

        else: 
            departure: str = match_value_1
            return printfn_s(ident, "departure: ", so.departure)


    return _arrow537() + _arrow538()


def StopOvers(ident: int, stop_overs: Optional[Array[StopOver_1]]=None) -> str:
    if stop_overs is None:
        return ""

    else: 
        stop_overs_1: Array[StopOver_1] = stop_overs
        def folder(s: str, l: StopOver_1, ident: int=ident, stop_overs: Optional[Array[StopOver_1]]=stop_overs) -> str:
            return (s + Comment(ident + 2, s)) + StopOver(ident + 2, l)

        return printfn_s(ident, "stopOvers: ", "") + fold_1(folder, "", stop_overs_1)



def Leg(ident: int, leg: Leg_1, short: bool) -> str:
    def _arrow542(__unit: Literal[None]=None, ident: int=ident, leg: Leg_1=leg, short: bool=short) -> str:
        match_value: Optional[Any] = leg.origin
        def _arrow539(__unit: Literal[None]=None) -> str:
            s: Stop_1 = value_2(match_value)
            return printf_s(ident, "origin: ", "") + Stop(0, s)

        def _arrow540(__unit: Literal[None]=None) -> str:
            s_1: Station_1 = value_2(match_value)
            return printf_s(ident, "origin: ", "") + Station(0, s_1)

        def _arrow541(__unit: Literal[None]=None) -> str:
            l: Location_1 = value_2(match_value)
            return printf_s(ident, "origin: ", "") + Location(0, l)

        return (_arrow539() if isinstance(value_2(match_value), Stop_1) else (_arrow540() if isinstance(value_2(match_value), Station_1) else _arrow541())) if (match_value is not None) else ""

    def _arrow543(__unit: Literal[None]=None, ident: int=ident, leg: Leg_1=leg, short: bool=short) -> str:
        match_value_1: Optional[Any] = leg.destination
        (pattern_matching_result, s_2) = (None, None)
        if match_value_1 is not None:
            if isinstance(value_2(match_value_1), Stop_1):
                pattern_matching_result = 0
                s_2 = value_2(match_value_1)

            else: 
                pattern_matching_result = 1


        else: 
            pattern_matching_result = 1

        if pattern_matching_result == 0:
            return printf_s(ident, "destination: ", "") + Stop(0, s_2)

        elif pattern_matching_result == 1:
            return ""


    def _arrow544(__unit: Literal[None]=None, ident: int=ident, leg: Leg_1=leg, short: bool=short) -> str:
        match_value_2: Optional[Location_1] = leg.current_location
        if match_value_2 is None:
            return ""

        else: 
            location: Location_1 = match_value_2
            return ((replicate(ident, " ") + "currentLocation: ") + print_lon_lat(0, location.longitude, location.latitude)) + nl


    def _arrow545(__unit: Literal[None]=None, ident: int=ident, leg: Leg_1=leg, short: bool=short) -> str:
        match_value_3: Optional[Line_1] = leg.line
        (pattern_matching_result_1, line_1) = (None, None)
        if match_value_3 is not None:
            if match_value_3.name is not None:
                pattern_matching_result_1 = 0
                line_1 = match_value_3

            else: 
                pattern_matching_result_1 = 1


        else: 
            pattern_matching_result_1 = 1

        if pattern_matching_result_1 == 0:
            return printfn_s(ident, "Line: ", line_1.name)

        elif pattern_matching_result_1 == 1:
            return ""


    return (((((((printfn_s(ident, "tripId: ", leg.trip_id) + _arrow542()) + _arrow543()) + printfn_s(ident, "departure: ", leg.departure)) + printfn_s(ident, "arrival: ", leg.arrival)) + ("" if short else StopOvers(ident, leg.stopovers))) + printfn_b(ident, "cancelled: ", leg.cancelled)) + _arrow544()) + ((ProductOfLeg(ident, leg) + printfn_s(ident, "loadFactor: ", leg.load_factor)) if short else (((((_arrow545() + printfn_b(ident, "walking: ", leg.walking)) + printfn_b(ident, "transfer: ", leg.transfer)) + ProductOfLeg(ident, leg)) + printfn_s(ident, "loadFactor: ", leg.load_factor)) + Remarks(ident, leg.remarks)))


def Trip(ident: int, trip: Trip_1) -> str:
    def _arrow546(__unit: Literal[None]=None, ident: int=ident, trip: Trip_1=trip) -> str:
        match_value: Optional[Any] = trip.origin
        (pattern_matching_result, s, s_1) = (None, None, None)
        if match_value is not None:
            if isinstance(value_2(match_value), Stop_1):
                pattern_matching_result = 0
                s = value_2(match_value)

            elif isinstance(value_2(match_value), Station_1):
                pattern_matching_result = 1
                s_1 = value_2(match_value)

            else: 
                pattern_matching_result = 2


        else: 
            pattern_matching_result = 2

        if pattern_matching_result == 0:
            return printf_s(ident, "origin: ", "") + Stop(0, s)

        elif pattern_matching_result == 1:
            return printf_s(ident, "origin: ", "") + Station(0, s_1)

        elif pattern_matching_result == 2:
            return ""


    def _arrow547(__unit: Literal[None]=None, ident: int=ident, trip: Trip_1=trip) -> str:
        match_value_1: Optional[Any] = trip.destination
        (pattern_matching_result_1, s_2) = (None, None)
        if match_value_1 is not None:
            if isinstance(value_2(match_value_1), Stop_1):
                pattern_matching_result_1 = 0
                s_2 = value_2(match_value_1)

            else: 
                pattern_matching_result_1 = 1


        else: 
            pattern_matching_result_1 = 1

        if pattern_matching_result_1 == 0:
            return printf_s(ident, "destination: ", "") + Stop(0, s_2)

        elif pattern_matching_result_1 == 1:
            return ""


    def _arrow548(__unit: Literal[None]=None, ident: int=ident, trip: Trip_1=trip) -> str:
        match_value_2: Optional[Line_1] = trip.line
        (pattern_matching_result_2, line_1) = (None, None)
        if match_value_2 is not None:
            if match_value_2.name is not None:
                pattern_matching_result_2 = 0
                line_1 = match_value_2

            else: 
                pattern_matching_result_2 = 1


        else: 
            pattern_matching_result_2 = 1

        if pattern_matching_result_2 == 0:
            return printfn_s(ident, "Line: ", line_1.name)

        elif pattern_matching_result_2 == 1:
            return ""


    return ((((((((_arrow546() + _arrow547()) + printfn_s(ident, "departure: ", trip.departure)) + printfn_s(ident, "arrival: ", trip.arrival)) + printfn_arr_l(ident, "stopovers: ", trip.stopovers)) + _arrow548()) + printfn_b(ident, "cancelled: ", trip.cancelled)) + printfn_b(ident, "walking: ", trip.walking)) + printfn_b(ident, "transfer: ", trip.transfer)) + Remarks(ident, trip.remarks)


def Legs(ident: int, legs: Array[Leg_1], short: bool) -> str:
    def folder(s: str, l: Leg_1, ident: int=ident, legs: Array[Leg_1]=legs, short: bool=short) -> str:
        return (s + Comment(ident + 2, s)) + Leg(ident + 2, l, short)

    return fold_1(folder, "", legs)


def JourneyLegs(ident: int, journey: Journey_1) -> str:
    return printfn_s(ident, "jouney:", "") + Legs(ident, journey.legs, True)


def Journey(ident: int, journey: Journey_1) -> str:
    short: bool = True
    def dist_s(__unit: Literal[None]=None, ident: int=ident, journey: Journey_1=journey) -> str:
        distance: float = distance_of_journey(journey)
        if distance > 0.0:
            ident_s: str = replicate(ident + 2, " ")
            return to_text(printf("%sdistance: %.2f"))(ident_s)(distance) + nl

        else: 
            return ""


    price_1: str
    match_value: Optional[Price] = journey.price
    if match_value is None:
        price_1 = ""

    else: 
        price: Price = match_value
        ident_s_1: str = replicate(ident + 2, " ")
        price_1 = to_text(printf("%sprice: %.2f %s"))(ident_s_1)(price.amount)(price.currency) + nl

    def _arrow549(__unit: Literal[None]=None, ident: int=ident, journey: Journey_1=journey) -> str:
        matchValue: Optional[str] = journey.refresh_token
        (pattern_matching_result,) = (None,)
        if short:
            pattern_matching_result = 1

        elif matchValue is not None:
            pattern_matching_result = 0

        else: 
            pattern_matching_result = 1

        if pattern_matching_result == 0:
            return printfn_s(ident + 2, "refreshToken: \'", matchValue + "\'")

        elif pattern_matching_result == 1:
            return ""


    return (((printfn_s(ident, "jouney:", "") + Legs(ident, journey.legs, short)) + price_1) + dist_s()) + _arrow549()


def JourneyItems(ident: int, journeys: Array[Journey_1]) -> str:
    def folder(s: str, j: Journey_1, ident: int=ident, journeys: Array[Journey_1]=journeys) -> str:
        return s + Journey(ident, j)

    return fold_1(folder, "", journeys)


def Journeys(journeys: Journeys_1) -> str:
    def folder(s: str, value: Array[Journey_1], journeys: Journeys_1=journeys) -> str:
        return s + JourneyItems(0, value)

    return fold(folder, "", to_array(journeys.journeys))


def U2StationStop(ident: int, location: Optional[Any]=None) -> str:
    if location is not None:
        if isinstance(value_2(location), Stop_1):
            s_1: Stop_1 = value_2(location)
            return Stop(ident + 2, s_1)

        else: 
            s: Station_1 = value_2(location)
            return Station(ident + 2, s)


    else: 
        return ""



def U3StationStopLocation(ident: int, location: Any=None) -> str:
    if isinstance(location, Location_1):
        return Location(ident + 2, location)

    elif isinstance(location, Stop_1):
        return Stop(ident + 2, location)

    else: 
        return ""



def Duration(ident: int, duration: Duration_1) -> str:
    def folder(s: str, j: Any=None, ident: int=ident, duration: Duration_1=duration) -> str:
        return s + U3StationStopLocation(ident + 2, j)

    return printfn_s(ident, "duration: ", int32_to_string(duration.duration)) + fold_1(folder, "", duration.stations)


def Directions(ident: int, directions: Optional[Array[str]]=None) -> str:
    if directions is None:
        return ""

    else: 
        def folder(s: str, j: str, ident: int=ident, directions: Optional[Array[str]]=directions) -> str:
            return s + printfn_s(ident + 2, "", j)

        return fold_1(folder, "", directions)



def Line(ident: int, l: Line_1) -> str:
    return (printfn_s(ident, "name: ", l.name) + printfn_arr_l(ident, "directions: ", l.directions)) + Directions(ident + 2, l.directions)


def Movement(ident: int, m: Movement_1, with_stopovers: bool) -> str:
    def _arrow550(__unit: Literal[None]=None, ident: int=ident, m: Movement_1=m, with_stopovers: bool=with_stopovers) -> str:
        match_value: Optional[Line_1] = m.line
        (pattern_matching_result, line_1) = (None, None)
        if match_value is not None:
            if match_value.name is not None:
                pattern_matching_result = 0
                line_1 = match_value

            else: 
                pattern_matching_result = 1


        else: 
            pattern_matching_result = 1

        if pattern_matching_result == 0:
            return printfn_s(ident, "Line: ", line_1.name)

        elif pattern_matching_result == 1:
            return ""


    def _arrow551(__unit: Literal[None]=None, ident: int=ident, m: Movement_1=m, with_stopovers: bool=with_stopovers) -> str:
        match_value_1: Optional[Location_1] = m.location
        if match_value_1 is None:
            return ""

        else: 
            location: Location_1 = match_value_1
            return print_lon_lat(ident, location.longitude, location.latitude)


    return (((printfn_s(ident, "tripId: ", m.trip_id) + printfn_s(ident, "direction: ", m.direction)) + _arrow550()) + _arrow551()) + ((printfn_arr_l(ident, "stopovers: ", m.next_stopovers) + StopOvers(ident, m.next_stopovers)) if with_stopovers else "")


def Locations(locations: Array[Any]) -> str:
    def folder(s: str, j: Any=None, locations: Array[Any]=locations) -> str:
        return s + U3StationStopLocation(0, j)

    return fold_1(folder, "", locations)


def Durations(durations: Array[Duration_1]) -> str:
    def folder(s: str, j: Duration_1, durations: Array[Duration_1]=durations) -> str:
        return s + Duration(0, j)

    return fold_1(folder, "", durations)


def MovementsWithStopovers(durations: Array[Movement_1]) -> str:
    def folder(s: str, j: Movement_1, durations: Array[Movement_1]=durations) -> str:
        return s + Movement(0, j, True)

    return fold_1(folder, "", durations)


def Movements(durations: Array[Movement_1]) -> str:
    def folder(s: str, j: Movement_1, durations: Array[Movement_1]=durations) -> str:
        return s + Movement(0, j, False)

    return fold_1(folder, "", durations)


def Alternatives(alternatives: Array[Alternative_1]) -> str:
    def folder(s: str, a: Alternative_1, alternatives: Array[Alternative_1]=alternatives) -> str:
        return s + Alternative(0, a)

    return fold_1(folder, "", alternatives)


def Trips(trips: Array[Trip_1]) -> str:
    def folder(s: str, t: Trip_1, trips: Array[Trip_1]=trips) -> str:
        return s + Trip(0, t)

    return fold_1(folder, "", trips)


def Warnings(warnings: Array[Warning_1]) -> str:
    def folder(s: str, t: Warning_1, warnings: Array[Warning_1]=warnings) -> str:
        return s + Warning(0, t)

    return fold_1(folder, "", warnings)


def Lines(lines: Array[Line_1]) -> str:
    def folder(s: str, t: Line_1, lines: Array[Line_1]=lines) -> str:
        return s + Line(0, t)

    return fold_1(folder, "", lines)


__all__ = ["nl", "printf_s", "printfn_s", "printfn_arr_l", "printfn_b", "print_distance", "print_lon_lat", "print_name_id", "Location", "Stop", "Station", "Alternative", "Comment", "Remark", "Warning", "Remarks", "ProductOfLeg", "StopOverStop", "StopOver", "StopOvers", "Leg", "Trip", "Legs", "JourneyLegs", "Journey", "JourneyItems", "Journeys", "U2StationStop", "U3StationStopLocation", "Duration", "Directions", "Line", "Movement", "Locations", "Durations", "MovementsWithStopovers", "Movements", "Alternatives", "Trips", "Warnings", "Lines"]

