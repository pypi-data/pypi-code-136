from __future__ import annotations
from typing import (Optional, Tuple, Literal, TypeVar, Any)
from ..fable_library.async_builder import (singleton, Async)
from ..fable_library.option import default_arg
from ..fable_library.reflection import (TypeInfo, class_type)
from ..fable_library.string import (to_console, printf)
from ..fable_library.types import Array
from .extensions.raw_request_ex import encode
from .extensions.raw_response import decode
from .extra_types import (HafasError, Log_Print, HafasError__ctor_Z384F8060)
from .lib.request import (HttpClient__ctor, HttpClient, HttpClient__Dispose, HttpClient__PostAsync)
from .types_raw_hafas_client import (Cfg, RawRequest, LocMatchRequest, RawResult, RawMatch, RawCommon, RawLoc, TripSearchRequest, RawOutCon, JourneyDetailsRequest, RawJny, StationBoardRequest, ReconstructionRequest, JourneyMatchRequest, LocGeoPosRequest, LocGeoReachRequest, RawPos, LocDetailsRequest, JourneyGeoPosRequest, HimSearchRequest, RawHim, LineMatchRequest, RawLine, ServerInfoRequest, SearchOnTripRequest, SvcReq, RawResponse, SvcRes)

__A = TypeVar("__A")

def _expr317() -> TypeInfo:
    return class_type("FsHafas.Api.HafasRawClient", None, HafasRawClient)


class HafasRawClient:
    def __init__(self, endpoint: str, add_checksum: bool, add_mic_mac: bool, salt: str, cfg: Cfg, base_request: RawRequest) -> None:
        self.endpoint: str = endpoint
        self.add_checksum: bool = add_checksum
        self.add_mic_mac: bool = add_mic_mac
        self.salt: str = salt
        self.cfg: Cfg = cfg
        self.base_request: RawRequest = base_request
        self.http_client: HttpClient = HttpClient__ctor()


HafasRawClient_reflection = _expr317

def HafasRawClient__ctor_48FA4CB7(endpoint: str, add_checksum: bool, add_mic_mac: bool, salt: str, cfg: Cfg, base_request: RawRequest) -> HafasRawClient:
    return HafasRawClient(endpoint, add_checksum, add_mic_mac, salt, cfg, base_request)


def HafasRawClient__Dispose(__: HafasRawClient) -> None:
    HttpClient__Dispose(__.http_client)


def HafasRawClient__AsyncLocMatch_781FF3B0(__: HafasRawClient, lang: str, loc_match_request: LocMatchRequest) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawLoc]]]]:
    def _arrow319(__unit: Literal[None]=None, __: HafasRawClient=__, lang: str=lang, loc_match_request: LocMatchRequest=loc_match_request) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawLoc]]]]:
        def _arrow318(_arg: RawResult) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawLoc]]]]:
            res: RawResult = _arg
            match_value: Optional[RawMatch] = res.match
            if match_value is not None:
                match: RawMatch = match_value
                return singleton.Return((res.common, res, match.loc_l))

            else: 
                return singleton.Return((None, None, None))


        return singleton.Bind(HafasRawClient__asyncPost_737B0FC(__, HafasRawClient__makeRequest(__, "LocMatch", lang, loc_match_request)), _arrow318)

    return singleton.Delay(_arrow319)


def HafasRawClient__AsyncTripSearch_Z4D007EE(__: HafasRawClient, lang: str, trip_search_request: TripSearchRequest) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawOutCon]]]]:
    def _arrow321(__unit: Literal[None]=None, __: HafasRawClient=__, lang: str=lang, trip_search_request: TripSearchRequest=trip_search_request) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawOutCon]]]]:
        def _arrow320(_arg: RawResult) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawOutCon]]]]:
            res: RawResult = _arg
            return singleton.Return((res.common, res, res.out_con_l))

        return singleton.Bind(HafasRawClient__asyncPost_737B0FC(__, HafasRawClient__makeRequest(__, "TripSearch", lang, trip_search_request)), _arrow320)

    return singleton.Delay(_arrow321)


def HafasRawClient__AsyncJourneyDetails_73FB16B1(__: HafasRawClient, lang: str, journey_details_request: JourneyDetailsRequest) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[RawJny]]]:
    def _arrow323(__unit: Literal[None]=None, __: HafasRawClient=__, lang: str=lang, journey_details_request: JourneyDetailsRequest=journey_details_request) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[RawJny]]]:
        def _arrow322(_arg: RawResult) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[RawJny]]]:
            res: RawResult = _arg
            return singleton.Return((res.common, res, res.journey))

        return singleton.Bind(HafasRawClient__asyncPost_737B0FC(__, HafasRawClient__makeRequest(__, "JourneyDetails", lang, journey_details_request)), _arrow322)

    return singleton.Delay(_arrow323)


def HafasRawClient__AsyncStationBoard_3FCEEA3(__: HafasRawClient, lang: str, station_board_request: StationBoardRequest) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawJny]]]]:
    def _arrow325(__unit: Literal[None]=None, __: HafasRawClient=__, lang: str=lang, station_board_request: StationBoardRequest=station_board_request) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawJny]]]]:
        def _arrow324(_arg: RawResult) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawJny]]]]:
            res: RawResult = _arg
            return singleton.Return((res.common, res, res.jny_l))

        return singleton.Bind(HafasRawClient__asyncPost_737B0FC(__, HafasRawClient__makeRequest(__, "StationBoard", lang, station_board_request)), _arrow324)

    return singleton.Delay(_arrow325)


def HafasRawClient__AsyncReconstruction_Z19A33557(__: HafasRawClient, lang: str, reconstruction_request: ReconstructionRequest) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawOutCon]]]]:
    def _arrow327(__unit: Literal[None]=None, __: HafasRawClient=__, lang: str=lang, reconstruction_request: ReconstructionRequest=reconstruction_request) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawOutCon]]]]:
        def _arrow326(_arg: RawResult) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawOutCon]]]]:
            res: RawResult = _arg
            return singleton.Return((res.common, res, res.out_con_l))

        return singleton.Bind(HafasRawClient__asyncPost_737B0FC(__, HafasRawClient__makeRequest(__, "Reconstruction", lang, reconstruction_request)), _arrow326)

    return singleton.Delay(_arrow327)


def HafasRawClient__AsyncJourneyMatch_Z61E31480(__: HafasRawClient, lang: str, journey_match_request: JourneyMatchRequest) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawJny]]]]:
    def _arrow329(__unit: Literal[None]=None, __: HafasRawClient=__, lang: str=lang, journey_match_request: JourneyMatchRequest=journey_match_request) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawJny]]]]:
        def _arrow328(_arg: RawResult) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawJny]]]]:
            res: RawResult = _arg
            return singleton.Return((res.common, res, res.jny_l))

        return singleton.Bind(HafasRawClient__asyncPost_737B0FC(__, HafasRawClient__makeRequest(__, "JourneyMatch", lang, journey_match_request)), _arrow328)

    return singleton.Delay(_arrow329)


def HafasRawClient__AsyncLocGeoPos_3C0E4562(__: HafasRawClient, lang: str, loc_geo_pos_request: LocGeoPosRequest) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawLoc]]]]:
    def _arrow331(__unit: Literal[None]=None, __: HafasRawClient=__, lang: str=lang, loc_geo_pos_request: LocGeoPosRequest=loc_geo_pos_request) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawLoc]]]]:
        def _arrow330(_arg: RawResult) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawLoc]]]]:
            res: RawResult = _arg
            return singleton.Return((res.common, res, res.loc_l))

        return singleton.Bind(HafasRawClient__asyncPost_737B0FC(__, HafasRawClient__makeRequest(__, "LocGeoPos", lang, loc_geo_pos_request)), _arrow330)

    return singleton.Delay(_arrow331)


def HafasRawClient__AsyncLocGeoReach_320A81B3(__: HafasRawClient, lang: str, loc_geo_reach_request: LocGeoReachRequest) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Array[RawPos]]]:
    def _arrow333(__unit: Literal[None]=None, __: HafasRawClient=__, lang: str=lang, loc_geo_reach_request: LocGeoReachRequest=loc_geo_reach_request) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Array[RawPos]]]:
        def _arrow332(_arg: RawResult) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Array[RawPos]]]:
            res: RawResult = _arg
            match_value: Optional[Array[RawPos]] = res.pos_l
            if match_value is not None:
                pos_l: Array[RawPos] = match_value
                return singleton.Return((res.common, res, pos_l))

            else: 
                return singleton.Return((None, None, [0] * 0))


        return singleton.Bind(HafasRawClient__asyncPost_737B0FC(__, HafasRawClient__makeRequest(__, "LocGeoReach", lang, loc_geo_reach_request)), _arrow332)

    return singleton.Delay(_arrow333)


def HafasRawClient__AsyncLocDetails_2FCF6141(__: HafasRawClient, lang: str, loc_details_request: LocDetailsRequest) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[RawLoc]]]:
    def _arrow335(__unit: Literal[None]=None, __: HafasRawClient=__, lang: str=lang, loc_details_request: LocDetailsRequest=loc_details_request) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[RawLoc]]]:
        def _arrow334(_arg: RawResult) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[RawLoc]]]:
            res: RawResult = _arg
            match_value: Optional[Array[RawLoc]] = res.loc_l
            (pattern_matching_result, loc_l_1) = (None, None)
            if match_value is not None:
                if len(match_value) > 0:
                    pattern_matching_result = 0
                    loc_l_1 = match_value

                else: 
                    pattern_matching_result = 1


            else: 
                pattern_matching_result = 1

            if pattern_matching_result == 0:
                return singleton.Return((res.common, res, loc_l_1[0]))

            elif pattern_matching_result == 1:
                return singleton.Return((None, None, None))


        return singleton.Bind(HafasRawClient__asyncPost_737B0FC(__, HafasRawClient__makeRequest(__, "LocDetails", lang, loc_details_request)), _arrow334)

    return singleton.Delay(_arrow335)


def HafasRawClient__AsyncJourneyGeoPos_Z6DB7B6AE(__: HafasRawClient, lang: str, journey_geo_pos_request: JourneyGeoPosRequest) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawJny]]]]:
    def _arrow337(__unit: Literal[None]=None, __: HafasRawClient=__, lang: str=lang, journey_geo_pos_request: JourneyGeoPosRequest=journey_geo_pos_request) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawJny]]]]:
        def _arrow336(_arg: RawResult) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawJny]]]]:
            res: RawResult = _arg
            return singleton.Return((res.common, res, res.jny_l))

        return singleton.Bind(HafasRawClient__asyncPost_737B0FC(__, HafasRawClient__makeRequest(__, "JourneyGeoPos", lang, journey_geo_pos_request)), _arrow336)

    return singleton.Delay(_arrow337)


def HafasRawClient__AsyncHimSearch_Z6033479F(__: HafasRawClient, lang: str, him_search_request: HimSearchRequest) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawHim]]]]:
    def _arrow339(__unit: Literal[None]=None, __: HafasRawClient=__, lang: str=lang, him_search_request: HimSearchRequest=him_search_request) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawHim]]]]:
        def _arrow338(_arg: RawResult) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawHim]]]]:
            res: RawResult = _arg
            return singleton.Return((res.common, res, res.msg_l))

        return singleton.Bind(HafasRawClient__asyncPost_737B0FC(__, HafasRawClient__makeRequest(__, "HimSearch", lang, him_search_request)), _arrow338)

    return singleton.Delay(_arrow339)


def HafasRawClient__AsyncLineMatch_Z69AA7EA2(__: HafasRawClient, lang: str, line_match_request: LineMatchRequest) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawLine]]]]:
    def _arrow341(__unit: Literal[None]=None, __: HafasRawClient=__, lang: str=lang, line_match_request: LineMatchRequest=line_match_request) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawLine]]]]:
        def _arrow340(_arg: RawResult) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawLine]]]]:
            res: RawResult = _arg
            return singleton.Return((res.common, res, res.line_l))

        return singleton.Bind(HafasRawClient__asyncPost_737B0FC(__, HafasRawClient__makeRequest(__, "LineMatch", lang, line_match_request)), _arrow340)

    return singleton.Delay(_arrow341)


def HafasRawClient__AsyncServerInfo_Z684EE398(__: HafasRawClient, lang: str, server_info_request: ServerInfoRequest) -> Async[Tuple[Optional[RawCommon], Optional[RawResult]]]:
    def _arrow343(__unit: Literal[None]=None, __: HafasRawClient=__, lang: str=lang, server_info_request: ServerInfoRequest=server_info_request) -> Async[Tuple[Optional[RawCommon], Optional[RawResult]]]:
        def _arrow342(_arg: RawResult) -> Async[Tuple[Optional[RawCommon], Optional[RawResult]]]:
            res: RawResult = _arg
            return singleton.Return((res.common, res))

        return singleton.Bind(HafasRawClient__asyncPost_737B0FC(__, HafasRawClient__makeRequest(__, "ServerInfo", lang, server_info_request)), _arrow342)

    return singleton.Delay(_arrow343)


def HafasRawClient__AsyncSearchOnTrip_5D40A373(__: HafasRawClient, lang: str, search_on_trip_request: SearchOnTripRequest) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawOutCon]]]]:
    def _arrow345(__unit: Literal[None]=None, __: HafasRawClient=__, lang: str=lang, search_on_trip_request: SearchOnTripRequest=search_on_trip_request) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawOutCon]]]]:
        def _arrow344(_arg: RawResult) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[Array[RawOutCon]]]]:
            res: RawResult = _arg
            return singleton.Return((res.common, res, res.out_con_l))

        return singleton.Bind(HafasRawClient__asyncPost_737B0FC(__, HafasRawClient__makeRequest(__, "SearchOnTrip", lang, search_on_trip_request)), _arrow344)

    return singleton.Delay(_arrow345)


def HafasRawClient__toException_ZAAE3ECF(this: HafasRawClient, ex: HafasError) -> HafasError:
    return ex


def HafasRawClient__log(this: HafasRawClient, msg: str, o: Any) -> None:
    Log_Print(msg, o)


def HafasRawClient__makeRequest(this: HafasRawClient, meth: str, lang: str, parameters: Any=None) -> RawRequest:
    input_record: RawRequest = this.base_request
    return RawRequest(lang, [SvcReq(this.cfg, meth, parameters)], input_record.client, input_record.ext, input_record.ver, input_record.auth)


def HafasRawClient__asyncPost_737B0FC(this: HafasRawClient, request: RawRequest) -> Async[RawResult]:
    json: str = encode(request)
    HafasRawClient__log(this, "request:", json)
    def _arrow361(__unit: Literal[None]=None, this: HafasRawClient=this, request: RawRequest=request) -> Async[RawResult]:
        def _arrow360(_arg: str) -> Async[RawResult]:
            result: str = _arg
            HafasRawClient__log(this, "response:", result)
            def _arrow356(__unit: Literal[None]=None) -> Async[RawResult]:
                if len(result) == 0:
                    def _arrow346(__unit: Literal[None]=None) -> RawResult:
                        raise Exception("invalid response")

                    return singleton.Return(_arrow346())

                else: 
                    response: RawResponse = decode(result)
                    svc_res_l: Array[SvcRes] = default_arg(response.svc_res_l, [])
                    if len(svc_res_l) == 1:
                        svc_res: SvcRes = svc_res_l[0]
                        matchValue: Optional[str] = svc_res.err
                        matchValue_1: Optional[str] = svc_res.err_txt
                        matchValue_2: Optional[RawResult] = svc_res.res
                        (pattern_matching_result, err_3, err_txt_1, err_4, res) = (None, None, None, None, None)
                        if matchValue is not None:
                            if matchValue_1 is not None:
                                def _arrow350(__unit: Literal[None]=None) -> bool:
                                    err_txt: str = matchValue_1
                                    return matchValue != "OK"

                                if _arrow350():
                                    pattern_matching_result = 0
                                    err_3 = matchValue
                                    err_txt_1 = matchValue_1

                                elif matchValue != "OK":
                                    pattern_matching_result = 1
                                    err_4 = matchValue

                                elif matchValue_2 is not None:
                                    pattern_matching_result = 2
                                    res = matchValue_2

                                else: 
                                    pattern_matching_result = 3


                            elif matchValue != "OK":
                                pattern_matching_result = 1
                                err_4 = matchValue

                            elif matchValue_2 is not None:
                                pattern_matching_result = 2
                                res = matchValue_2

                            else: 
                                pattern_matching_result = 3


                        elif matchValue_2 is not None:
                            pattern_matching_result = 2
                            res = matchValue_2

                        else: 
                            pattern_matching_result = 3

                        if pattern_matching_result == 0:
                            def _arrow347(__unit: Literal[None]=None) -> RawResult:
                                raise HafasError__ctor_Z384F8060(err_3, err_txt_1)

                            return singleton.Return(_arrow347())

                        elif pattern_matching_result == 1:
                            def _arrow348(__unit: Literal[None]=None) -> RawResult:
                                raise HafasError__ctor_Z384F8060(err_4, err_4)

                            return singleton.Return(_arrow348())

                        elif pattern_matching_result == 2:
                            return singleton.Return(res)

                        elif pattern_matching_result == 3:
                            def _arrow349(__unit: Literal[None]=None) -> RawResult:
                                raise Exception("invalid response")

                            return singleton.Return(_arrow349())


                    else: 
                        matchValue_3: Optional[str] = response.err
                        matchValue_4: Optional[str] = response.err_txt
                        def _arrow352(__unit: Literal[None]=None) -> Async[RawResult]:
                            err_5: str = matchValue_3
                            err_txt_2: str = matchValue_4
                            def _arrow351(__unit: Literal[None]=None) -> RawResult:
                                raise HafasError__ctor_Z384F8060(err_5, err_txt_2)

                            return singleton.Return(_arrow351())

                        def _arrow354(__unit: Literal[None]=None) -> Async[RawResult]:
                            err_6: str = matchValue_3
                            def _arrow353(__unit: Literal[None]=None) -> RawResult:
                                raise HafasError__ctor_Z384F8060(err_6, err_6)

                            return singleton.Return(_arrow353())

                        def _arrow355(__unit: Literal[None]=None) -> RawResult:
                            raise Exception("invalid response")

                        return (_arrow352() if (matchValue_4 is not None) else _arrow354()) if (matchValue_3 is not None) else singleton.Return(_arrow355())



            def _arrow359(_arg_1: Exception) -> Async[RawResult]:
                if isinstance(_arg_1, HafasError):
                    def _arrow357(__unit: Literal[None]=None) -> RawResult:
                        raise HafasRawClient__toException_ZAAE3ECF(this, _arg_1)

                    return singleton.Return(_arrow357())

                else: 
                    arg_5: str = str(_arg_1)
                    to_console(printf("error: %s"))(arg_5)
                    def _arrow358(__unit: Literal[None]=None) -> RawResult:
                        raise Exception("invalid response")

                    return singleton.Return(_arrow358())


            return singleton.TryWith(singleton.Delay(_arrow356), _arrow359)

        return singleton.Bind(HttpClient__PostAsync(this.http_client, this.endpoint, this.add_checksum, this.add_mic_mac, this.salt, json), _arrow360)

    return singleton.Delay(_arrow361)


__all__ = ["HafasRawClient_reflection", "HafasRawClient__Dispose", "HafasRawClient__AsyncLocMatch_781FF3B0", "HafasRawClient__AsyncTripSearch_Z4D007EE", "HafasRawClient__AsyncJourneyDetails_73FB16B1", "HafasRawClient__AsyncStationBoard_3FCEEA3", "HafasRawClient__AsyncReconstruction_Z19A33557", "HafasRawClient__AsyncJourneyMatch_Z61E31480", "HafasRawClient__AsyncLocGeoPos_3C0E4562", "HafasRawClient__AsyncLocGeoReach_320A81B3", "HafasRawClient__AsyncLocDetails_2FCF6141", "HafasRawClient__AsyncJourneyGeoPos_Z6DB7B6AE", "HafasRawClient__AsyncHimSearch_Z6033479F", "HafasRawClient__AsyncLineMatch_Z69AA7EA2", "HafasRawClient__AsyncServerInfo_Z684EE398", "HafasRawClient__AsyncSearchOnTrip_5D40A373", "HafasRawClient__toException_ZAAE3ECF", "HafasRawClient__log", "HafasRawClient__makeRequest", "HafasRawClient__asyncPost_737B0FC"]

