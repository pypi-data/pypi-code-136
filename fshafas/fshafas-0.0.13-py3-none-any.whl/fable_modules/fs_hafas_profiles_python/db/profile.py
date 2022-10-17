from __future__ import annotations
from dataclasses import dataclass
from typing import (Tuple, Optional, Any, Literal, TypeVar, Callable)
from ...fable_library.array import (try_find, map, append)
from ...fable_library.double import divide
from ...fable_library.option import (bind, value as value_2, some, default_arg)
from ...fable_library.reflection import (TypeInfo, string_type, record_type)
from ...fable_library.reg_exp import is_match
from ...fable_library.types import (Record, Array)
from ...fable_library.util import round
from ...fs_hafas_python.context import (Options, Context, Profile, Profile__set__locale_Z721C83C5, Profile__set__timezone_Z721C83C5, Profile__set__endpoint_Z721C83C5, Profile__set_salt_Z721C83C5, Profile__set_addChecksum_Z1FBCCD16, Profile__set_cfg_Z3219B2F8, Profile__set_baseRequest_Z42C91061, Profile__set__products_Z4ED450D4, Profile__set__trip_6FCE9E49, Profile__set__radar_6FCE9E49, Profile__set__tripsByName_6FCE9E49, Profile__set__reachableFrom_6FCE9E49, Profile__set__journeysFromTrip_6FCE9E49, Profile__set_journeysOutFrwd_Z1FBCCD16, Profile__set_formatStation_11D407F6, Profile__set_transformJourneysQuery_4AA4AF64, Profile__get_parseJourney, Profile__set_parseJourney_Z1F35F4C, Profile__get_parseJourneyLeg, Profile__set_parseJourneyLeg_3913217E, Profile__get_parseDeparture, Profile__set_parseDeparture_537DC5A, Profile__get_parseHint, Profile__set_parseHint_2044943E, Profile__get_parseLine, Profile__set_parseLine_718F82F)
from ...fs_hafas_python.lib.transformations import Default_JourneysOptions
from ...fs_hafas_python.profile import default_profile
from ...fs_hafas_python.types_hafas_client import (Hint, Status, Line, Leg, Alternative, Journey, Price, LoyaltyCard, JourneysOptions)
from ...fs_hafas_python.types_raw_hafas_client import (RawRem, RawProd, RawTcoc, RawSec, RawJny, RawTrnCmpSX, RawCommon, RawStop, RawOutCon, RawTrfRes, RawPrice, JnyFltr, TripSearchRequest, TvlrProf, TrfReq, Cfg)
from .products import products
from .request import request

_A = TypeVar("_A")

_B = TypeVar("_B")

def _expr552() -> TypeInfo:
    return record_type("FsHafas.Profiles.Db.HintByCode", [], HintByCode, lambda: [("type", string_type), ("code", string_type), ("summary", string_type)])


@dataclass(eq = False, repr = False)
class HintByCode(Record):
    type: str
    code: str
    summary: str

HintByCode_reflection = _expr552

hints_by_code: Array[Tuple[str, HintByCode]] = [("fb", HintByCode("hint", "bicycle-conveyance", "bicycles conveyed")), ("fr", HintByCode("hint", "bicycle-conveyance-reservation", "bicycles conveyed, subject to reservation")), ("nf", HintByCode("hint", "no-bicycle-conveyance", "bicycles not conveyed")), ("k2", HintByCode("hint", "2nd-class-only", "2. class only")), ("eh", HintByCode("hint", "boarding-ramp", "vehicle-mounted boarding ramp available")), ("ro", HintByCode("hint", "wheelchairs-space", "space for wheelchairs")), ("oa", HintByCode("hint", "wheelchairs-space-reservation", "space for wheelchairs, subject to reservation")), ("wv", HintByCode("hint", "wifi", "WiFi available")), ("wi", HintByCode("hint", "wifi", "WiFi available")), ("sn", HintByCode("hint", "snacks", "snacks available for purchase")), ("mb", HintByCode("hint", "snacks", "snacks available for purchase")), ("mp", HintByCode("hint", "snacks", "snacks available for purchase at the seat")), ("bf", HintByCode("hint", "barrier-free", "barrier-free")), ("rg", HintByCode("hint", "barrier-free-vehicle", "barrier-free vehicle")), ("bt", HintByCode("hint", "on-board-bistro", "Bordbistro available")), ("br", HintByCode("hint", "on-board-restaurant", "Bordrestaurant available")), ("ki", HintByCode("hint", "childrens-area", "children\'s area available")), ("kk", HintByCode("hint", "parents-childrens-compartment", "parent-and-children compartment available")), ("kr", HintByCode("hint", "kids-service", "DB Kids Service available")), ("ls", HintByCode("hint", "power-sockets", "power sockets available")), ("ev", HintByCode("hint", "replacement-service", "replacement service")), ("kl", HintByCode("hint", "air-conditioned", "air-conditioned vehicle")), ("r0", HintByCode("hint", "upward-escalator", "upward escalator")), ("au", HintByCode("hint", "elevator", "elevator available")), ("ck", HintByCode("hint", "komfort-checkin", "Komfort-Checkin available")), ("it", HintByCode("hint", "ice-sprinter", "ICE Sprinter service")), ("rp", HintByCode("hint", "compulsory-reservation", "compulsory seat reservation")), ("rm", HintByCode("hint", "optional-reservation", "optional seat reservation")), ("scl", HintByCode("hint", "all-2nd-class-seats-reserved", "all 2nd class seats reserved")), ("cacl", HintByCode("hint", "all-seats-reserved", "all seats reserved")), ("sk", HintByCode("hint", "oversize-luggage-forbidden", "oversize luggage not allowed")), ("hu", HintByCode("hint", "animals-forbidden", "animals not allowed, except guide dogs")), ("ik", HintByCode("hint", "baby-cot-required", "baby cot/child seat required")), ("ee", HintByCode("hint", "on-board-entertainment", "on-board entertainment available")), ("toilet", HintByCode("hint", "toilet", "toilet available")), ("oc", HintByCode("hint", "wheelchair-accessible-toilet", "wheelchair-accessible toilet available")), ("iz", HintByCode("hint", "intercity-2", "Intercity 2"))]

codes_by_text: Array[Tuple[str, str]] = [("journey cancelled", "journey-cancelled"), ("stop cancelled", "stop-cancelled"), ("signal failure", "signal-failure"), ("signalstörung", "signal-failure"), ("additional stop", "additional-stopover"), ("platform change", "changed platform")]

def parse_hint_by_code(parsed: Hint, raw: RawRem) -> Hint:
    if raw.type == "K":
        match_value: Optional[str] = raw.txt_n
        if match_value is None:
            return parsed

        else: 
            return Hint(parsed.type, parsed.code, parsed.summary, match_value, parsed.trip_id)


    elif raw.type == "A":
        def predicate(tupled_arg: Tuple[str, HintByCode], parsed: Hint=parsed, raw: RawRem=raw) -> bool:
            return tupled_arg[0] == raw.code.lower()

        match_value_1: Optional[Tuple[str, HintByCode]] = try_find(predicate, hints_by_code)
        if match_value_1 is None:
            return parsed

        else: 
            h: HintByCode = match_value_1[1]
            return Hint(parsed.type, h.code, h.summary, parsed.text, parsed.trip_id)


    elif raw.txt_n is not None:
        def binder(tupled_arg_2: Tuple[str, str], parsed: Hint=parsed, raw: RawRem=raw) -> Optional[str]:
            return tupled_arg_2[1]

        def predicate_1(tupled_arg_1: Tuple[str, str], parsed: Hint=parsed, raw: RawRem=raw) -> bool:
            return tupled_arg_1[0] == value_2(raw.txt_n).lower()

        return Hint(parsed.type, bind(binder, try_find(predicate_1, codes_by_text)), parsed.summary, parsed.text, parsed.trip_id)

    else: 
        return parsed



def parse_status_by_code(parsed: Status, raw: RawRem) -> Status:
    if raw.type == "K":
        match_value: Optional[str] = raw.txt_n
        if match_value is None:
            return parsed

        else: 
            return Status(parsed.type, parsed.code, parsed.summary, match_value, parsed.trip_id)


    elif raw.txt_n is not None:
        def binder(tupled_arg_1: Tuple[str, str], parsed: Status=parsed, raw: RawRem=raw) -> Optional[str]:
            return tupled_arg_1[1]

        def predicate(tupled_arg: Tuple[str, str], parsed: Status=parsed, raw: RawRem=raw) -> bool:
            return tupled_arg[0] == value_2(raw.txt_n).lower()

        return Status(parsed.type, bind(binder, try_find(predicate, codes_by_text)), parsed.summary, parsed.text, parsed.trip_id)

    else: 
        return parsed



def parse_hint(parsed: Optional[Any], h: RawRem) -> Optional[Any]:
    (pattern_matching_result, parsed_hint, parsed_status) = (None, None, None)
    if parsed is not None:
        if isinstance(value_2(parsed), Hint):
            pattern_matching_result = 0
            parsed_hint = value_2(parsed)

        elif isinstance(value_2(parsed), Status):
            pattern_matching_result = 1
            parsed_status = value_2(parsed)

        else: 
            pattern_matching_result = 2


    else: 
        pattern_matching_result = 2

    if pattern_matching_result == 0:
        return some(parse_hint_by_code(parsed_hint, h))

    elif pattern_matching_result == 1:
        return some(parse_status_by_code(parsed_status, h))

    elif pattern_matching_result == 2:
        return parsed



def parse_line_with_additional_name(parsed: Line, p: RawProd) -> Line:
    if p.add_name is None:
        return parsed

    else: 
        return Line(parsed.type, parsed.id, p.add_name, parsed.admin_code, parsed.fahrt_nr, parsed.name, parsed.product, parsed.public, parsed.mode, parsed.routes, parsed.operator, parsed.express, parsed.metro, parsed.night, parsed.nr, parsed.symbol, parsed.directions, parsed.product_name)



load_factors: Array[str] = ["", "low-to-medium", "high", "very-high", "exceptionally-high"]

def parse_load_factor(opt: Options, tcoc_l: Array[RawTcoc], tcoc_x: Array[int]) -> Optional[str]:
    cls: str = "FIRST" if opt.first_class else "SECOND"
    def predicate(t: RawTcoc, opt: Options=opt, tcoc_l: Array[RawTcoc]=tcoc_l, tcoc_x: Array[int]=tcoc_x) -> bool:
        return t.c == cls

    def mapping(i: int, opt: Options=opt, tcoc_l: Array[RawTcoc]=tcoc_l, tcoc_x: Array[int]=tcoc_x) -> RawTcoc:
        return tcoc_l[i]

    match_value: Optional[RawTcoc] = try_find(predicate, map(mapping, tcoc_x, None))
    (pattern_matching_result, tcoc_1) = (None, None)
    if match_value is not None:
        if match_value.r is not None:
            pattern_matching_result = 0
            tcoc_1 = match_value

        else: 
            pattern_matching_result = 1


    else: 
        pattern_matching_result = 1

    if pattern_matching_result == 0:
        return load_factors[value_2(tcoc_1.r)]

    elif pattern_matching_result == 1:
        return None



def parse_journey_leg_with_load_factor(parsed: Leg, ctx: Context, pt: RawSec, date: str) -> Leg:
    tcoc_x: Optional[Array[int]]
    match_value: Optional[RawJny] = pt.jny
    if match_value is None:
        tcoc_x = None

    else: 
        match_value_1: Optional[RawTrnCmpSX] = match_value.d_trn_cmp_sx
        tcoc_x = None if (match_value_1 is None) else match_value_1.tcoc_x

    tcoc_l: Optional[Array[RawTcoc]]
    match_value_2: Optional[RawCommon] = ctx.res.common
    tcoc_l = None if (match_value_2 is None) else match_value_2.tcoc_l
    (pattern_matching_result, tcoc_l_1, tcoc_x_1) = (None, None, None)
    if tcoc_x is not None:
        if tcoc_l is not None:
            pattern_matching_result = 0
            tcoc_l_1 = tcoc_l
            tcoc_x_1 = tcoc_x

        else: 
            pattern_matching_result = 1


    else: 
        pattern_matching_result = 1

    if pattern_matching_result == 0:
        return Leg(parsed.trip_id, parsed.origin, parsed.destination, parsed.departure, parsed.planned_departure, parsed.prognosed_arrival, parsed.departure_delay, parsed.departure_platform, parsed.prognosed_departure_platform, parsed.planned_departure_platform, parsed.arrival, parsed.planned_arrival, parsed.prognosed_departure, parsed.arrival_delay, parsed.arrival_platform, parsed.prognosed_arrival_platform, parsed.planned_arrival_platform, parsed.stopovers, parsed.schedule, parsed.price, parsed.operator, parsed.direction, parsed.line, parsed.reachable, parsed.cancelled, parsed.walking, parse_load_factor(ctx.opt, tcoc_l_1, tcoc_x_1), parsed.distance, parsed.public, parsed.transfer, parsed.cycle, parsed.alternatives, parsed.polyline, parsed.remarks, parsed.current_location, parsed.departure_prognosis_type, parsed.arrival_prognosis_type, parsed.checkin)

    elif pattern_matching_result == 1:
        return parsed



def parse_arr_or_dep_with_load_factor(parsed: Alternative, ctx: Context, d: RawJny) -> Alternative:
    tcoc_x: Optional[Array[int]]
    match_value: Optional[RawStop] = d.stb_stop
    if match_value is None:
        tcoc_x = None

    else: 
        match_value_1: Optional[RawTrnCmpSX] = match_value.d_trn_cmp_sx
        tcoc_x = None if (match_value_1 is None) else match_value_1.tcoc_x

    tcoc_l: Optional[Array[RawTcoc]]
    match_value_2: Optional[RawCommon] = ctx.res.common
    tcoc_l = None if (match_value_2 is None) else match_value_2.tcoc_l
    (pattern_matching_result, tcoc_l_1, tcoc_x_1) = (None, None, None)
    if tcoc_x is not None:
        if tcoc_l is not None:
            pattern_matching_result = 0
            tcoc_l_1 = tcoc_l
            tcoc_x_1 = tcoc_x

        else: 
            pattern_matching_result = 1


    else: 
        pattern_matching_result = 1

    if pattern_matching_result == 0:
        return Alternative(parsed.trip_id, parsed.direction, parsed.location, parsed.line, parsed.stop, parsed.when, parsed.planned_when, parsed.prognosed_when, parsed.delay, parsed.platform, parsed.planned_platform, parsed.prognosed_platform, parsed.remarks, parsed.cancelled, parse_load_factor(ctx.opt, tcoc_l_1, tcoc_x_1), parsed.provenance, parsed.previous_stopovers, parsed.next_stopovers, parsed.frames, parsed.polyline, parsed.current_trip_position, parsed.origin, parsed.destination, parsed.prognosis_type)

    elif pattern_matching_result == 1:
        return parsed



def parse_journey_with_price(parsed: Journey, raw: RawOutCon) -> Journey:
    match_value: Optional[RawTrfRes] = raw.trf_res
    (pattern_matching_result, trf_res_1) = (None, None)
    if match_value is not None:
        def _arrow554(__unit: Literal[None]=None, parsed: Journey=parsed, raw: RawOutCon=raw) -> bool:
            trf_res: RawTrfRes = match_value
            return (len(value_2(trf_res.fare_set_l)[0].fare_l) > 0) if ((len(value_2(trf_res.fare_set_l)) > 0) if (trf_res.fare_set_l is not None) else False) else False

        if _arrow554():
            pattern_matching_result = 0
            trf_res_1 = match_value

        else: 
            pattern_matching_result = 1


    else: 
        pattern_matching_result = 1

    if pattern_matching_result == 0:
        match_value_1: Optional[RawPrice] = value_2(trf_res_1.fare_set_l)[0].fare_l[0].price
        (pattern_matching_result_1, price_1) = (None, None)
        if match_value_1 is not None:
            def _arrow553(__unit: Literal[None]=None, parsed: Journey=parsed, raw: RawOutCon=raw) -> bool:
                price: RawPrice = match_value_1
                return (value_2(price.amount) > 0) if (price.amount is not None) else False

            if _arrow553():
                pattern_matching_result_1 = 0
                price_1 = match_value_1

            else: 
                pattern_matching_result_1 = 1


        else: 
            pattern_matching_result_1 = 1

        if pattern_matching_result_1 == 0:
            return Journey(parsed.type, parsed.legs, parsed.refresh_token, parsed.remarks, Price(round(divide(value_2(price_1.amount), 100.0), 2), "EUR", None), parsed.cycle, parsed.scheduled_days)

        elif pattern_matching_result_1 == 1:
            return parsed


    elif pattern_matching_result == 1:
        return parsed



def format_station(id: str) -> str:
    if is_match(id, "^\\d{6,}$"):
        return id

    else: 
        raise Exception("station id: " + id)



bike_fltr: JnyFltr = JnyFltr("BC", "INC", None, None)

def get_option_value(opt: Optional[_A], getter: Callable[[_A], Optional[_B]], default_opt: _A) -> _B:
    default_value: _B
    match_value: Optional[_B] = getter(default_opt)
    if match_value is None:
        raise Exception("getOptionValue: value expected")

    else: 
        default_value = value_2(match_value)

    if opt is None:
        return default_value

    else: 
        match_value_1: Optional[_B] = getter(value_2(opt))
        if match_value_1 is None:
            return default_value

        else: 
            return value_2(match_value_1)




def format_loyalty_card(data: LoyaltyCard) -> int:
    cls: int = default_arg(data.class_, 2) or 0
    match_value: Optional[int] = data.discount
    if match_value is not None:
        discount: int = match_value or 0
        if data.type == "Bahncard":
            if discount == 25:
                if cls == 1:
                    return 1

                else: 
                    return 2


            elif discount == 50:
                if cls == 1:
                    return 3

                else: 
                    return 4


            else: 
                return 0


        else: 
            return 0


    else: 
        return 0



def age_group_from_age(age: Optional[int]=None) -> str:
    if age is None:
        return "E"

    else: 
        age_1: int = age or 0
        if age_1 < 6:
            return "B"

        elif age_1 < 15:
            return "K"

        elif age_1 < 27:
            return "Y"

        elif age_1 < 65:
            return "E"

        else: 
            return "S"




def transform_journeys_query(opt: Optional[JourneysOptions], q: TripSearchRequest) -> TripSearchRequest:
    def _arrow555(v: JourneysOptions, opt: Optional[JourneysOptions]=opt, q: TripSearchRequest=q) -> Optional[bool]:
        return v.bike

    bike: bool = get_option_value(opt, _arrow555, Default_JourneysOptions)
    def _arrow556(v_1: JourneysOptions, opt: Optional[JourneysOptions]=opt, q: TripSearchRequest=q) -> Optional[bool]:
        return v_1.first_class

    first_class: bool = get_option_value(opt, _arrow556, Default_JourneysOptions)
    jny_fltr_l: Array[JnyFltr] = append([bike_fltr], q.jny_fltr_l, None) if bike else q.jny_fltr_l
    def _arrow557(__unit: Literal[None]=None, opt: Optional[JourneysOptions]=opt, q: TripSearchRequest=q) -> Optional[int]:
        opt_2: JourneysOptions = opt
        return format_loyalty_card(value_2(opt_2.loyalty_card))

    redtn_card: Optional[int] = (_arrow557() if (opt.loyalty_card is not None) else None) if (opt is not None) else None
    return TripSearchRequest(q.get_passlist, q.max_chg, q.min_chg_time, q.dep_loc_l, q.via_loc_l, q.arr_loc_l, jny_fltr_l, q.gis_fltr_l, q.get_tariff, q.ushrp, q.get_pt, q.get_iv, q.get_polyline, q.out_date, q.out_time, q.num_f, q.out_frwd, TrfReq(1 if first_class else 2, [TvlrProf(age_group_from_age(None if (opt is None) else opt.age), redtn_card)], "PK"))


profile: Profile = default_profile()

Profile__set__locale_Z721C83C5(profile, "de-DE")

Profile__set__timezone_Z721C83C5(profile, "Europe/Berlin")

Profile__set__endpoint_Z721C83C5(profile, "https://reiseauskunft.bahn.de/bin/mgate.exe")

Profile__set_salt_Z721C83C5(profile, "bdI8UVj40K5fvxwf")

Profile__set_addChecksum_Z1FBCCD16(profile, True)

Profile__set_cfg_Z3219B2F8(profile, Cfg("GPA", "HYBRID"))

Profile__set_baseRequest_Z42C91061(profile, request)

Profile__set__products_Z4ED450D4(profile, products)

Profile__set__trip_6FCE9E49(profile, True)

Profile__set__radar_6FCE9E49(profile, True)

Profile__set__tripsByName_6FCE9E49(profile, True)

Profile__set__reachableFrom_6FCE9E49(profile, True)

Profile__set__journeysFromTrip_6FCE9E49(profile, True)

Profile__set_journeysOutFrwd_Z1FBCCD16(profile, True)

def _arrow558(id: str) -> str:
    return format_station(id)


Profile__set_formatStation_11D407F6(profile, _arrow558)

def _arrow559(opt: Optional[JourneysOptions], q: TripSearchRequest) -> TripSearchRequest:
    return transform_journeys_query(opt, q)


Profile__set_transformJourneysQuery_4AA4AF64(profile, _arrow559)

default_parse_journey: Callable[[Context, RawOutCon], Journey] = Profile__get_parseJourney(profile)

def _arrow560(ctx: Context, p: RawOutCon) -> Journey:
    return parse_journey_with_price(default_parse_journey(ctx)(p), p)


Profile__set_parseJourney_Z1F35F4C(profile, _arrow560)

default_parse_journey_leg: Callable[[Context, RawSec, str], Leg] = Profile__get_parseJourneyLeg(profile)

def _arrow561(ctx: Context, pt: RawSec, date: str) -> Leg:
    return parse_journey_leg_with_load_factor(default_parse_journey_leg(ctx)(pt)(date), ctx, pt, date)


Profile__set_parseJourneyLeg_3913217E(profile, _arrow561)

default_parse_departure: Callable[[Context, RawJny], Alternative] = Profile__get_parseDeparture(profile)

def _arrow562(ctx: Context, pt: RawJny) -> Alternative:
    return parse_arr_or_dep_with_load_factor(default_parse_departure(ctx)(pt), ctx, pt)


Profile__set_parseDeparture_537DC5A(profile, _arrow562)

default_parse_hint: Callable[[Context, RawRem], Optional[Any]] = Profile__get_parseHint(profile)

def _arrow563(ctx: Context, p: RawRem) -> Optional[Any]:
    return parse_hint(default_parse_hint(ctx)(p), p)


Profile__set_parseHint_2044943E(profile, _arrow563)

default_parse_line: Callable[[Context, RawProd], Line] = Profile__get_parseLine(profile)

def _arrow564(ctx: Context, p: RawProd) -> Line:
    return parse_line_with_additional_name(default_parse_line(ctx)(p), p)


Profile__set_parseLine_718F82F(profile, _arrow564)

__all__ = ["HintByCode_reflection", "hints_by_code", "codes_by_text", "parse_hint_by_code", "parse_status_by_code", "parse_hint", "parse_line_with_additional_name", "load_factors", "parse_load_factor", "parse_journey_leg_with_load_factor", "parse_arr_or_dep_with_load_factor", "parse_journey_with_price", "format_station", "bike_fltr", "get_option_value", "format_loyalty_card", "age_group_from_age", "transform_journeys_query", "profile", "default_parse_journey", "default_parse_journey_leg", "default_parse_departure", "default_parse_hint", "default_parse_line"]

