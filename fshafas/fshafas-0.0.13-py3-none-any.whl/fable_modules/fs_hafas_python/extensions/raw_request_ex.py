from __future__ import annotations
from typing import (Literal, Callable, Any, Optional)
from ...fable_library.list import (FSharpList, last)
from ...fable_library.map import (of_seq, FSharpMap__TryFind)
from ...fable_library.reg_exp import replace
from ...fable_library.string import (substring, to_text, printf, to_console, replace as replace_1)
from ...fable_library.util import compare_primitives
from ...fable_simple_json_python.json_converter import Convert_serialize
from ...fable_simple_json_python.type_info_converter import create_type_info
from ...fable_simple_json_python.simple_json import (SimpleJson_toString, SimpleJson_mapKeysByPath, SimpleJson_parseNative)
from ..types_raw_hafas_client import (SvcReq, Cfg_reflection, LocMatchRequest, LocMatchRequest_reflection, TripSearchRequest, TripSearchRequest_reflection, JourneyDetailsRequest, JourneyDetailsRequest_reflection, StationBoardRequest, StationBoardRequest_reflection, ReconstructionRequest, ReconstructionRequest_reflection, JourneyMatchRequest, JourneyMatchRequest_reflection, LocGeoPosRequest, LocGeoPosRequest_reflection, LocGeoReachRequest, LocGeoReachRequest_reflection, LocDetailsRequest, LocDetailsRequest_reflection, JourneyGeoPosRequest, JourneyGeoPosRequest_reflection, HimSearchRequest, HimSearchRequest_reflection, LineMatchRequest, LineMatchRequest_reflection, SearchOnTripRequest, SearchOnTripRequest_reflection, RawRequest, RawRequestClient_reflection, RawRequestAuth_reflection)

class ObjectExpr299:
    @property
    def Compare(self) -> Callable[[str, str], int]:
        def _arrow298(x: str, y: str) -> int:
            return compare_primitives(x, y)

        return _arrow298


replacements: Any = of_seq([("a_tzoffset", "aTZOffset"), ("crd_enc_yx", "crdEncYX"), ("d_tzoffset", "dTZOffset"), ("d_trn_cmp_sx", "dTrnCmpSX"), ("get_ist", "getIST"), ("get_iv", "getIV"), ("get_pois", "getPOIs"), ("get_pt", "getPT"), ("only_rt", "onlyRT"), ("planrt_ts", "planrtTS"), ("poly_xl", "polyXL"), ("show_arslink", "showARSLink")], ObjectExpr299())

def undashify(input: str) -> str:
    def _arrow300(m: Any, input: str=input) -> str:
        return substring(m[0], 1, 1).upper()

    return replace(input, "_[a-z]", _arrow300)


def to_undashed(xs: FSharpList[str]) -> Optional[str]:
    v: str = last(xs)
    match_value: Optional[str] = FSharpMap__TryFind(replacements, v)
    if match_value is None:
        return undashify(v)

    else: 
        return match_value



def encode_svc_req(svc_req: SvcReq) -> str:
    cfg: str = Convert_serialize(svc_req.cfg, create_type_info(Cfg_reflection()))
    req: str
    match_value: Any = svc_req.req
    req = Convert_serialize(match_value, create_type_info(LocMatchRequest_reflection())) if isinstance(match_value, LocMatchRequest) else (Convert_serialize(match_value, create_type_info(TripSearchRequest_reflection())) if isinstance(match_value, TripSearchRequest) else (Convert_serialize(match_value, create_type_info(JourneyDetailsRequest_reflection())) if isinstance(match_value, JourneyDetailsRequest) else (Convert_serialize(match_value, create_type_info(StationBoardRequest_reflection())) if isinstance(match_value, StationBoardRequest) else (Convert_serialize(match_value, create_type_info(ReconstructionRequest_reflection())) if isinstance(match_value, ReconstructionRequest) else (Convert_serialize(match_value, create_type_info(JourneyMatchRequest_reflection())) if isinstance(match_value, JourneyMatchRequest) else (Convert_serialize(match_value, create_type_info(LocGeoPosRequest_reflection())) if isinstance(match_value, LocGeoPosRequest) else (Convert_serialize(match_value, create_type_info(LocGeoReachRequest_reflection())) if isinstance(match_value, LocGeoReachRequest) else (Convert_serialize(match_value, create_type_info(LocDetailsRequest_reflection())) if isinstance(match_value, LocDetailsRequest) else (Convert_serialize(match_value, create_type_info(JourneyGeoPosRequest_reflection())) if isinstance(match_value, JourneyGeoPosRequest) else (Convert_serialize(match_value, create_type_info(HimSearchRequest_reflection())) if isinstance(match_value, HimSearchRequest) else (Convert_serialize(match_value, create_type_info(LineMatchRequest_reflection())) if isinstance(match_value, LineMatchRequest) else (Convert_serialize(match_value, create_type_info(SearchOnTripRequest_reflection())) if isinstance(match_value, SearchOnTripRequest) else "{}"))))))))))))
    return to_text(printf("{\"cfg\":%s, \"meth\":\"%s\", \"req\":%s}"))(cfg)(svc_req.meth)(req)


def encode(request: RawRequest) -> str:
    try: 
        svcreql: str = ("[" + encode_svc_req(request.svc_req_l[0])) + "]"
        client: str = Convert_serialize(request.client, create_type_info(RawRequestClient_reflection()))
        auth: str = Convert_serialize(request.auth, create_type_info(RawRequestAuth_reflection()))
        ext_1: str
        match_value: Optional[str] = request.ext
        if match_value is None:
            ext_1 = ""

        else: 
            ext: str = match_value
            ext_1 = to_text(printf("\"ext\":\"%s\","))(ext)

        def _arrow301(xs: FSharpList[str]) -> Optional[str]:
            return to_undashed(xs)

        return SimpleJson_toString(SimpleJson_mapKeysByPath(_arrow301, SimpleJson_parseNative(replace_1(replace_1(to_text(printf("{\"lang\":\"%s\", \"svcReqL\":%s, \"client\":%s, %s\"ver\":\"%s\", \"auth\":%s}"))(request.lang)(svcreql)(client)(ext_1)(request.ver)(auth), ", \"meta\": null", ""), ",\"name\":null", ""))))

    except Exception as e:
        arg_7: str = str(e)
        to_console(printf("error encode: %s"))(arg_7)
        raise Exception(str(e))



__all__ = ["replacements", "undashify", "to_undashed", "encode_svc_req", "encode"]

