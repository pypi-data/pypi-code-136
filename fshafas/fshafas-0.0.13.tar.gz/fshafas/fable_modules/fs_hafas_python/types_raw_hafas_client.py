from __future__ import annotations
from dataclasses import dataclass
from typing import (Optional, Any)
from ..fable_library.reflection import (TypeInfo, string_type, record_type, int32_type, option_type, array_type, bool_type, obj_type)
from ..fable_library.types import (Record, Array)

def _expr165() -> TypeInfo:
    return record_type("FsHafas.Raw.RawPltf", [], RawPltf, lambda: [("type", string_type), ("txt", string_type)])


@dataclass(eq = False, repr = False)
class RawPltf(Record):
    type: str
    txt: str

RawPltf_reflection = _expr165

def _expr166() -> TypeInfo:
    return record_type("FsHafas.Raw.RawTrnCmpSX", [], RawTrnCmpSX, lambda: [("tc_m", option_type(int32_type)), ("tcoc_x", option_type(array_type(int32_type)))])


@dataclass(eq = False, repr = False)
class RawTrnCmpSX(Record):
    tc_m: Optional[int]
    tcoc_x: Optional[Array[int]]

RawTrnCmpSX_reflection = _expr166

def _expr167() -> TypeInfo:
    return record_type("FsHafas.Raw.RawDep", [], RawDep, lambda: [("loc_x", option_type(int32_type)), ("idx", option_type(int32_type)), ("d_prod_x", option_type(int32_type)), ("d_platf_s", option_type(string_type)), ("d_in_r", option_type(bool_type)), ("d_time_s", option_type(string_type)), ("d_prog_type", option_type(string_type)), ("d_trn_cmp_sx", option_type(RawTrnCmpSX_reflection())), ("d_tzoffset", option_type(int32_type)), ("type", option_type(string_type)), ("d_time_r", option_type(string_type)), ("d_cncl", option_type(bool_type)), ("d_pltf_s", option_type(RawPltf_reflection())), ("d_platf_r", option_type(string_type)), ("d_pltf_r", option_type(RawPltf_reflection()))])


@dataclass(eq = False, repr = False)
class RawDep(Record):
    loc_x: Optional[int]
    idx: Optional[int]
    d_prod_x: Optional[int]
    d_platf_s: Optional[str]
    d_in_r: Optional[bool]
    d_time_s: Optional[str]
    d_prog_type: Optional[str]
    d_trn_cmp_sx: Optional[RawTrnCmpSX]
    d_tzoffset: Optional[int]
    type: Optional[str]
    d_time_r: Optional[str]
    d_cncl: Optional[bool]
    d_pltf_s: Optional[RawPltf]
    d_platf_r: Optional[str]
    d_pltf_r: Optional[RawPltf]

RawDep_reflection = _expr167

def _expr168() -> TypeInfo:
    return record_type("FsHafas.Raw.RawArr", [], RawArr, lambda: [("loc_x", option_type(int32_type)), ("idx", option_type(int32_type)), ("a_platf_s", option_type(string_type)), ("a_out_r", option_type(bool_type)), ("a_time_s", option_type(string_type)), ("a_prog_type", option_type(string_type)), ("a_tzoffset", option_type(int32_type)), ("type", option_type(string_type)), ("a_time_r", option_type(string_type)), ("a_cncl", option_type(bool_type)), ("a_pltf_s", option_type(RawPltf_reflection())), ("a_platf_r", option_type(string_type)), ("a_pltf_r", option_type(RawPltf_reflection())), ("prod_l", option_type(array_type(RawProd_reflection())))])


@dataclass(eq = False, repr = False)
class RawArr(Record):
    loc_x: Optional[int]
    idx: Optional[int]
    a_platf_s: Optional[str]
    a_out_r: Optional[bool]
    a_time_s: Optional[str]
    a_prog_type: Optional[str]
    a_tzoffset: Optional[int]
    type: Optional[str]
    a_time_r: Optional[str]
    a_cncl: Optional[bool]
    a_pltf_s: Optional[RawPltf]
    a_platf_r: Optional[str]
    a_pltf_r: Optional[RawPltf]
    prod_l: Optional[Array[RawProd]]

RawArr_reflection = _expr168

def _expr169() -> TypeInfo:
    return record_type("FsHafas.Raw.PubCh", [], PubCh, lambda: [("name", string_type), ("f_date", string_type), ("f_time", string_type), ("t_date", string_type), ("t_time", string_type)])


@dataclass(eq = False, repr = False)
class PubCh(Record):
    name: str
    f_date: str
    f_time: str
    t_date: str
    t_time: str

PubCh_reflection = _expr169

def _expr170() -> TypeInfo:
    return record_type("FsHafas.Raw.RawHim", [], RawHim, lambda: [("hid", string_type), ("act", bool_type), ("pub", option_type(string_type)), ("head", option_type(string_type)), ("lead", option_type(string_type)), ("text", option_type(string_type)), ("tckr", option_type(string_type)), ("ico_x", int32_type), ("prio", int32_type), ("f_loc_x", option_type(int32_type)), ("t_loc_x", option_type(int32_type)), ("prod", option_type(int32_type)), ("l_mod_date", option_type(string_type)), ("l_mod_time", option_type(string_type)), ("s_date", option_type(string_type)), ("s_time", option_type(string_type)), ("e_date", option_type(string_type)), ("e_time", option_type(string_type)), ("cat", option_type(int32_type)), ("pub_ch_l", option_type(array_type(PubCh_reflection()))), ("edge_ref_l", option_type(array_type(int32_type))), ("region_ref_l", option_type(array_type(int32_type))), ("cat_ref_l", option_type(array_type(int32_type))), ("event_ref_l", option_type(array_type(int32_type))), ("aff_prod_ref_l", option_type(array_type(int32_type))), ("comp", option_type(string_type))])


@dataclass(eq = False, repr = False)
class RawHim(Record):
    hid: str
    act: bool
    pub: Optional[str]
    head: Optional[str]
    lead: Optional[str]
    text: Optional[str]
    tckr: Optional[str]
    ico_x: int
    prio: int
    f_loc_x: Optional[int]
    t_loc_x: Optional[int]
    prod: Optional[int]
    l_mod_date: Optional[str]
    l_mod_time: Optional[str]
    s_date: Optional[str]
    s_time: Optional[str]
    e_date: Optional[str]
    e_time: Optional[str]
    cat: Optional[int]
    pub_ch_l: Optional[Array[PubCh]]
    edge_ref_l: Optional[Array[int]]
    region_ref_l: Optional[Array[int]]
    cat_ref_l: Optional[Array[int]]
    event_ref_l: Optional[Array[int]]
    aff_prod_ref_l: Optional[Array[int]]
    comp: Optional[str]

RawHim_reflection = _expr170

def _expr171() -> TypeInfo:
    return record_type("FsHafas.Raw.RawMsg", [], RawMsg, lambda: [("type", string_type), ("rem_x", option_type(int32_type)), ("f_loc_x", option_type(int32_type)), ("t_loc_x", option_type(int32_type)), ("f_idx", option_type(int32_type)), ("t_idx", option_type(int32_type)), ("him_x", option_type(int32_type)), ("tag_l", option_type(array_type(string_type)))])


@dataclass(eq = False, repr = False)
class RawMsg(Record):
    type: str
    rem_x: Optional[int]
    f_loc_x: Optional[int]
    t_loc_x: Optional[int]
    f_idx: Optional[int]
    t_idx: Optional[int]
    him_x: Optional[int]
    tag_l: Optional[Array[str]]

RawMsg_reflection = _expr171

def _expr172() -> TypeInfo:
    return record_type("FsHafas.Raw.RawRem", [], RawRem, lambda: [("type", string_type), ("code", string_type), ("prio", option_type(int32_type)), ("ico_x", option_type(int32_type)), ("txt_n", option_type(string_type)), ("txt_s", option_type(string_type)), ("jid", option_type(string_type))])


@dataclass(eq = False, repr = False)
class RawRem(Record):
    type: str
    code: str
    prio: Optional[int]
    ico_x: Optional[int]
    txt_n: Optional[str]
    txt_s: Optional[str]
    jid: Optional[str]

RawRem_reflection = _expr172

def _expr173() -> TypeInfo:
    return record_type("FsHafas.Raw.RawStop", [], RawStop, lambda: [("loc_x", int32_type), ("idx", option_type(int32_type)), ("d_prod_x", option_type(int32_type)), ("d_in_r", option_type(bool_type)), ("d_time_s", option_type(string_type)), ("d_time_r", option_type(string_type)), ("d_tzoffset", option_type(int32_type)), ("d_cncl", option_type(bool_type)), ("d_in_s", option_type(bool_type)), ("d_platf_s", option_type(string_type)), ("d_pltf_s", option_type(RawPltf_reflection())), ("d_platf_r", option_type(string_type)), ("d_pltf_r", option_type(RawPltf_reflection())), ("d_prog_type", option_type(string_type)), ("d_dir_txt", option_type(string_type)), ("d_dir_flg", option_type(string_type)), ("d_trn_cmp_sx", option_type(RawTrnCmpSX_reflection())), ("a_prod_x", option_type(int32_type)), ("a_platf_s", option_type(string_type)), ("a_pltf_s", option_type(RawPltf_reflection())), ("a_platf_r", option_type(string_type)), ("a_pltf_r", option_type(RawPltf_reflection())), ("a_out_r", option_type(bool_type)), ("a_time_s", option_type(string_type)), ("a_time_r", option_type(string_type)), ("a_tzoffset", option_type(int32_type)), ("a_cncl", option_type(bool_type)), ("a_out_s", option_type(bool_type)), ("a_platf_ch", option_type(bool_type)), ("a_prog_type", option_type(string_type)), ("type", option_type(string_type)), ("msg_l", option_type(array_type(RawMsg_reflection()))), ("rem_l", option_type(array_type(RawRem_reflection())))])


@dataclass(eq = False, repr = False)
class RawStop(Record):
    loc_x: int
    idx: Optional[int]
    d_prod_x: Optional[int]
    d_in_r: Optional[bool]
    d_time_s: Optional[str]
    d_time_r: Optional[str]
    d_tzoffset: Optional[int]
    d_cncl: Optional[bool]
    d_in_s: Optional[bool]
    d_platf_s: Optional[str]
    d_pltf_s: Optional[RawPltf]
    d_platf_r: Optional[str]
    d_pltf_r: Optional[RawPltf]
    d_prog_type: Optional[str]
    d_dir_txt: Optional[str]
    d_dir_flg: Optional[str]
    d_trn_cmp_sx: Optional[RawTrnCmpSX]
    a_prod_x: Optional[int]
    a_platf_s: Optional[str]
    a_pltf_s: Optional[RawPltf]
    a_platf_r: Optional[str]
    a_pltf_r: Optional[RawPltf]
    a_out_r: Optional[bool]
    a_time_s: Optional[str]
    a_time_r: Optional[str]
    a_tzoffset: Optional[int]
    a_cncl: Optional[bool]
    a_out_s: Optional[bool]
    a_platf_ch: Optional[bool]
    a_prog_type: Optional[str]
    type: Optional[str]
    msg_l: Optional[Array[RawMsg]]
    rem_l: Optional[Array[RawRem]]

RawStop_reflection = _expr173

def _expr174() -> TypeInfo:
    return record_type("FsHafas.Raw.PpLocRef", [], PpLocRef, lambda: [("pp_idx", int32_type), ("loc_x", int32_type)])


@dataclass(eq = False, repr = False)
class PpLocRef(Record):
    pp_idx: int
    loc_x: int

PpLocRef_reflection = _expr174

def _expr175() -> TypeInfo:
    return record_type("FsHafas.Raw.RawPoly", [], RawPoly, lambda: [("delta", bool_type), ("dim", int32_type), ("type", option_type(string_type)), ("crd_enc_yx", string_type), ("crd_enc_z", option_type(string_type)), ("crd_enc_s", string_type), ("crd_enc_f", string_type), ("pp_loc_ref_l", option_type(array_type(PpLocRef_reflection())))])


@dataclass(eq = False, repr = False)
class RawPoly(Record):
    delta: bool
    dim: int
    type: Optional[str]
    crd_enc_yx: str
    crd_enc_z: Optional[str]
    crd_enc_s: str
    crd_enc_f: str
    pp_loc_ref_l: Optional[Array[PpLocRef]]

RawPoly_reflection = _expr175

def _expr176() -> TypeInfo:
    return record_type("FsHafas.Raw.PolyG", [], PolyG, lambda: [("poly_xl", array_type(int32_type))])


@dataclass(eq = False, repr = False)
class PolyG(Record):
    poly_xl: Array[int]

PolyG_reflection = _expr176

def _expr177() -> TypeInfo:
    return record_type("FsHafas.Raw.RawAni", [], RawAni, lambda: [("m_sec", array_type(int32_type)), ("proc", array_type(int32_type)), ("proc_abs", option_type(array_type(int32_type))), ("f_loc_x", array_type(int32_type)), ("t_loc_x", array_type(int32_type)), ("dir_geo", array_type(int32_type)), ("stc_output_x", array_type(int32_type)), ("poly_g", option_type(PolyG_reflection())), ("state", array_type(string_type)), ("poly", option_type(RawPoly_reflection()))])


@dataclass(eq = False, repr = False)
class RawAni(Record):
    m_sec: Array[int]
    proc: Array[int]
    proc_abs: Optional[Array[int]]
    f_loc_x: Array[int]
    t_loc_x: Array[int]
    dir_geo: Array[int]
    stc_output_x: Array[int]
    poly_g: Optional[PolyG]
    state: Array[str]
    poly: Optional[RawPoly]

RawAni_reflection = _expr177

def _expr178() -> TypeInfo:
    return record_type("FsHafas.Raw.RawSDays", [], RawSDays, lambda: [("f_loc_x", option_type(int32_type)), ("t_loc_x", option_type(int32_type)), ("s_days_r", option_type(string_type)), ("s_days_i", option_type(string_type)), ("s_days_b", option_type(string_type))])


@dataclass(eq = False, repr = False)
class RawSDays(Record):
    f_loc_x: Optional[int]
    t_loc_x: Optional[int]
    s_days_r: Optional[str]
    s_days_i: Optional[str]
    s_days_b: Optional[str]

RawSDays_reflection = _expr178

def _expr179() -> TypeInfo:
    return record_type("FsHafas.Raw.RawPolyG", [], RawPolyG, lambda: [("poly_xl", array_type(int32_type))])


@dataclass(eq = False, repr = False)
class RawPolyG(Record):
    poly_xl: Array[int]

RawPolyG_reflection = _expr179

def _expr180() -> TypeInfo:
    return record_type("FsHafas.Raw.RawCrd", [], RawCrd, lambda: [("x", int32_type), ("y", int32_type), ("z", option_type(int32_type))])


@dataclass(eq = False, repr = False)
class RawCrd(Record):
    x: int
    y: int
    z: Optional[int]

RawCrd_reflection = _expr180

def _expr181() -> TypeInfo:
    return record_type("FsHafas.Raw.RawFreq", [], RawFreq, lambda: [("jny_l", option_type(array_type(RawJny_reflection()))), ("min_c", option_type(int32_type)), ("max_c", option_type(int32_type)), ("num_c", option_type(int32_type))])


@dataclass(eq = False, repr = False)
class RawFreq(Record):
    jny_l: Optional[Array[RawJny]]
    min_c: Optional[int]
    max_c: Optional[int]
    num_c: Optional[int]

RawFreq_reflection = _expr181

def _expr182() -> TypeInfo:
    return record_type("FsHafas.Raw.RawJny", [], RawJny, lambda: [("jid", string_type), ("prod_x", int32_type), ("dir_txt", option_type(string_type)), ("status", option_type(string_type)), ("is_rchbl", option_type(bool_type)), ("ctx_recon", option_type(string_type)), ("rem_l", option_type(array_type(RawRem_reflection()))), ("msg_l", option_type(array_type(RawMsg_reflection()))), ("stb_stop", option_type(RawStop_reflection())), ("subscr", option_type(string_type)), ("poly", option_type(RawPoly_reflection())), ("stop_l", option_type(array_type(RawStop_reflection()))), ("date", option_type(string_type)), ("s_days_l", option_type(array_type(RawSDays_reflection()))), ("d_trn_cmp_sx", option_type(RawTrnCmpSX_reflection())), ("poly_g", option_type(RawPolyG_reflection())), ("ani", option_type(RawAni_reflection())), ("pos", option_type(RawCrd_reflection())), ("freq", option_type(RawFreq_reflection())), ("prod_l", option_type(array_type(RawProd_reflection())))])


@dataclass(eq = False, repr = False)
class RawJny(Record):
    jid: str
    prod_x: int
    dir_txt: Optional[str]
    status: Optional[str]
    is_rchbl: Optional[bool]
    ctx_recon: Optional[str]
    rem_l: Optional[Array[RawRem]]
    msg_l: Optional[Array[RawMsg]]
    stb_stop: Optional[RawStop]
    subscr: Optional[str]
    poly: Optional[RawPoly]
    stop_l: Optional[Array[RawStop]]
    date: Optional[str]
    s_days_l: Optional[Array[RawSDays]]
    d_trn_cmp_sx: Optional[RawTrnCmpSX]
    poly_g: Optional[RawPolyG]
    ani: Optional[RawAni]
    pos: Optional[RawCrd]
    freq: Optional[RawFreq]
    prod_l: Optional[Array[RawProd]]

RawJny_reflection = _expr182

def _expr183() -> TypeInfo:
    return record_type("FsHafas.Raw.RawGis", [], RawGis, lambda: [("dist", option_type(int32_type)), ("dur_s", option_type(string_type)), ("dir_geo", option_type(int32_type)), ("ctx", option_type(string_type)), ("gis_prvr", option_type(string_type)), ("get_descr", option_type(bool_type)), ("get_poly", option_type(bool_type)), ("msg_l", option_type(array_type(RawMsg_reflection())))])


@dataclass(eq = False, repr = False)
class RawGis(Record):
    dist: Optional[int]
    dur_s: Optional[str]
    dir_geo: Optional[int]
    ctx: Optional[str]
    gis_prvr: Optional[str]
    get_descr: Optional[bool]
    get_poly: Optional[bool]
    msg_l: Optional[Array[RawMsg]]

RawGis_reflection = _expr183

def _expr184() -> TypeInfo:
    return record_type("FsHafas.Raw.RawSec", [], RawSec, lambda: [("type", string_type), ("ico_x", option_type(int32_type)), ("dep", RawDep_reflection()), ("arr", RawArr_reflection()), ("jny", option_type(RawJny_reflection())), ("res_state", option_type(string_type)), ("res_recommendation", option_type(string_type)), ("gis", option_type(RawGis_reflection()))])


@dataclass(eq = False, repr = False)
class RawSec(Record):
    type: str
    ico_x: Optional[int]
    dep: RawDep
    arr: RawArr
    jny: Optional[RawJny]
    res_state: Optional[str]
    res_recommendation: Optional[str]
    gis: Optional[RawGis]

RawSec_reflection = _expr184

def _expr185() -> TypeInfo:
    return record_type("FsHafas.Raw.RawSotCtxt", [], RawSotCtxt, lambda: [("cn_loc_x", option_type(int32_type)), ("calc_date", string_type), ("jid", option_type(string_type)), ("loc_mode", string_type), ("p_loc_x", option_type(int32_type)), ("req_mode", string_type), ("sect_x", option_type(int32_type)), ("calc_time", string_type)])


@dataclass(eq = False, repr = False)
class RawSotCtxt(Record):
    cn_loc_x: Optional[int]
    calc_date: str
    jid: Optional[str]
    loc_mode: str
    p_loc_x: Optional[int]
    req_mode: str
    sect_x: Optional[int]
    calc_time: str

RawSotCtxt_reflection = _expr185

def _expr186() -> TypeInfo:
    return record_type("FsHafas.Raw.Content", [], Content, lambda: [("type", string_type), ("content", string_type)])


@dataclass(eq = False, repr = False)
class Content(Record):
    type: str
    content: str

Content_reflection = _expr186

def _expr187() -> TypeInfo:
    return record_type("FsHafas.Raw.ExtCont", [], ExtCont, lambda: [("content", Content_reflection())])


@dataclass(eq = False, repr = False)
class ExtCont(Record):
    content: Content

ExtCont_reflection = _expr187

def _expr188() -> TypeInfo:
    return record_type("FsHafas.Raw.RawTicket", [], RawTicket, lambda: [("name", string_type), ("prc", int32_type), ("cur", string_type), ("ext_cont", ExtCont_reflection())])


@dataclass(eq = False, repr = False)
class RawTicket(Record):
    name: str
    prc: int
    cur: str
    ext_cont: ExtCont

RawTicket_reflection = _expr188

def _expr189() -> TypeInfo:
    return record_type("FsHafas.Raw.RawPrice", [], RawPrice, lambda: [("amount", option_type(int32_type))])


@dataclass(eq = False, repr = False)
class RawPrice(Record):
    amount: Optional[int]

RawPrice_reflection = _expr189

def _expr190() -> TypeInfo:
    return record_type("FsHafas.Raw.RawFare", [], RawFare, lambda: [("price", option_type(RawPrice_reflection())), ("is_from_price", option_type(bool_type)), ("is_bookable", option_type(bool_type)), ("is_upsell", option_type(bool_type)), ("target_ctx", option_type(string_type)), ("button_text", option_type(string_type)), ("name", option_type(string_type)), ("ticket_l", option_type(array_type(RawTicket_reflection())))])


@dataclass(eq = False, repr = False)
class RawFare(Record):
    price: Optional[RawPrice]
    is_from_price: Optional[bool]
    is_bookable: Optional[bool]
    is_upsell: Optional[bool]
    target_ctx: Optional[str]
    button_text: Optional[str]
    name: Optional[str]
    ticket_l: Optional[Array[RawTicket]]

RawFare_reflection = _expr190

def _expr191() -> TypeInfo:
    return record_type("FsHafas.Raw.RawFareSet", [], RawFareSet, lambda: [("desc", option_type(string_type)), ("fare_l", array_type(RawFare_reflection()))])


@dataclass(eq = False, repr = False)
class RawFareSet(Record):
    desc: Optional[str]
    fare_l: Array[RawFare]

RawFareSet_reflection = _expr191

def _expr192() -> TypeInfo:
    return record_type("FsHafas.Raw.RawTrfRes", [], RawTrfRes, lambda: [("status_code", option_type(string_type)), ("fare_set_l", option_type(array_type(RawFareSet_reflection())))])


@dataclass(eq = False, repr = False)
class RawTrfRes(Record):
    status_code: Optional[str]
    fare_set_l: Optional[Array[RawFareSet]]

RawTrfRes_reflection = _expr192

def _expr193() -> TypeInfo:
    return record_type("FsHafas.Raw.RawRecon", [], RawRecon, lambda: [("ctx", option_type(string_type))])


@dataclass(eq = False, repr = False)
class RawRecon(Record):
    ctx: Optional[str]

RawRecon_reflection = _expr193

def _expr194() -> TypeInfo:
    return record_type("FsHafas.Raw.RawOutCon", [], RawOutCon, lambda: [("cid", string_type), ("date", string_type), ("dur", string_type), ("chg", int32_type), ("s_days", RawSDays_reflection()), ("dep", RawDep_reflection()), ("arr", RawArr_reflection()), ("sec_l", array_type(RawSec_reflection())), ("ctx_recon", option_type(string_type)), ("trf_res", option_type(RawTrfRes_reflection())), ("con_subscr", string_type), ("res_state", option_type(string_type)), ("res_recommendation", option_type(string_type)), ("rec_state", string_type), ("sot_rating", option_type(int32_type)), ("is_sot_con", option_type(bool_type)), ("show_arslink", option_type(bool_type)), ("sot_ctxt", option_type(RawSotCtxt_reflection())), ("cksum", string_type), ("msg_l", option_type(array_type(RawMsg_reflection()))), ("recon", option_type(RawRecon_reflection())), ("freq", option_type(RawFreq_reflection()))])


@dataclass(eq = False, repr = False)
class RawOutCon(Record):
    cid: str
    date: str
    dur: str
    chg: int
    s_days: RawSDays
    dep: RawDep
    arr: RawArr
    sec_l: Array[RawSec]
    ctx_recon: Optional[str]
    trf_res: Optional[RawTrfRes]
    con_subscr: str
    res_state: Optional[str]
    res_recommendation: Optional[str]
    rec_state: str
    sot_rating: Optional[int]
    is_sot_con: Optional[bool]
    show_arslink: Optional[bool]
    sot_ctxt: Optional[RawSotCtxt]
    cksum: str
    msg_l: Optional[Array[RawMsg]]
    recon: Optional[RawRecon]
    freq: Optional[RawFreq]

RawOutCon_reflection = _expr194

def _expr195() -> TypeInfo:
    return record_type("FsHafas.Raw.RawItem", [], RawItem, lambda: [("col", int32_type), ("row", int32_type), ("msg_l", option_type(array_type(RawMsg_reflection()))), ("rem_l", option_type(array_type(int32_type)))])


@dataclass(eq = False, repr = False)
class RawItem(Record):
    col: int
    row: int
    msg_l: Optional[Array[RawMsg]]
    rem_l: Optional[Array[int]]

RawItem_reflection = _expr195

def _expr196() -> TypeInfo:
    return record_type("FsHafas.Raw.RawGrid", [], RawGrid, lambda: [("n_cols", int32_type), ("n_rows", int32_type), ("item_l", array_type(RawItem_reflection())), ("type", string_type), ("title", string_type)])


@dataclass(eq = False, repr = False)
class RawGrid(Record):
    n_cols: int
    n_rows: int
    item_l: Array[RawItem]
    type: str
    title: str

RawGrid_reflection = _expr196

def _expr197() -> TypeInfo:
    return record_type("FsHafas.Raw.RawLoc", [], RawLoc, lambda: [("lid", option_type(string_type)), ("type", option_type(string_type)), ("name", string_type), ("ico_x", option_type(int32_type)), ("ext_id", option_type(string_type)), ("state", string_type), ("crd", option_type(RawCrd_reflection())), ("p_cls", option_type(int32_type)), ("entry", option_type(bool_type)), ("m_mast_loc_x", option_type(int32_type)), ("p_ref_l", option_type(array_type(int32_type))), ("wt", option_type(int32_type)), ("entry_loc_l", option_type(array_type(int32_type))), ("stop_loc_l", option_type(array_type(int32_type))), ("msg_l", option_type(array_type(RawMsg_reflection()))), ("grid_l", option_type(array_type(RawGrid_reflection()))), ("is_main_mast", option_type(bool_type)), ("meta", option_type(bool_type)), ("dist", option_type(int32_type)), ("dur", option_type(int32_type))])


@dataclass(eq = False, repr = False)
class RawLoc(Record):
    lid: Optional[str]
    type: Optional[str]
    name: str
    ico_x: Optional[int]
    ext_id: Optional[str]
    state: str
    crd: Optional[RawCrd]
    p_cls: Optional[int]
    entry: Optional[bool]
    m_mast_loc_x: Optional[int]
    p_ref_l: Optional[Array[int]]
    wt: Optional[int]
    entry_loc_l: Optional[Array[int]]
    stop_loc_l: Optional[Array[int]]
    msg_l: Optional[Array[RawMsg]]
    grid_l: Optional[Array[RawGrid]]
    is_main_mast: Optional[bool]
    meta: Optional[bool]
    dist: Optional[int]
    dur: Optional[int]

RawLoc_reflection = _expr197

def _expr198() -> TypeInfo:
    return record_type("FsHafas.Raw.RawProdCtx", [], RawProdCtx, lambda: [("name", option_type(string_type)), ("num", option_type(string_type)), ("match_id", option_type(string_type)), ("cat_out", option_type(string_type)), ("cat_out_s", option_type(string_type)), ("cat_out_l", option_type(string_type)), ("cat_in", option_type(string_type)), ("cat_code", option_type(string_type)), ("admin", option_type(string_type)), ("line_id", option_type(string_type))])


@dataclass(eq = False, repr = False)
class RawProdCtx(Record):
    name: Optional[str]
    num: Optional[str]
    match_id: Optional[str]
    cat_out: Optional[str]
    cat_out_s: Optional[str]
    cat_out_l: Optional[str]
    cat_in: Optional[str]
    cat_code: Optional[str]
    admin: Optional[str]
    line_id: Optional[str]

RawProdCtx_reflection = _expr198

def _expr199() -> TypeInfo:
    return record_type("FsHafas.Raw.RawOp", [], RawOp, lambda: [("name", string_type), ("ico_x", int32_type)])


@dataclass(eq = False, repr = False)
class RawOp(Record):
    name: str
    ico_x: int

RawOp_reflection = _expr199

def _expr200() -> TypeInfo:
    return record_type("FsHafas.Raw.RawProd", [], RawProd, lambda: [("name", option_type(string_type)), ("number", option_type(string_type)), ("ico_x", option_type(int32_type)), ("opr_x", option_type(int32_type)), ("prod_ctx", option_type(RawProdCtx_reflection())), ("cls", option_type(int32_type)), ("line", option_type(string_type)), ("add_name", option_type(string_type)), ("f_loc_x", option_type(int32_type)), ("t_loc_x", option_type(int32_type)), ("prod_x", option_type(int32_type)), ("f_idx", option_type(int32_type)), ("t_idx", option_type(int32_type))])


@dataclass(eq = False, repr = False)
class RawProd(Record):
    name: Optional[str]
    number: Optional[str]
    ico_x: Optional[int]
    opr_x: Optional[int]
    prod_ctx: Optional[RawProdCtx]
    cls: Optional[int]
    line: Optional[str]
    add_name: Optional[str]
    f_loc_x: Optional[int]
    t_loc_x: Optional[int]
    prod_x: Optional[int]
    f_idx: Optional[int]
    t_idx: Optional[int]

RawProd_reflection = _expr200

def _expr201() -> TypeInfo:
    return record_type("FsHafas.Raw.RawRGB", [], RawRGB, lambda: [("r", option_type(int32_type)), ("g", int32_type), ("b", int32_type)])


@dataclass(eq = False, repr = False)
class RawRGB(Record):
    r: Optional[int]
    g: int
    b: int

RawRGB_reflection = _expr201

def _expr202() -> TypeInfo:
    return record_type("FsHafas.Raw.RawIco", [], RawIco, lambda: [("res", option_type(string_type)), ("txt", option_type(string_type)), ("text", option_type(string_type)), ("txt_s", option_type(string_type)), ("fg", option_type(RawRGB_reflection())), ("bg", option_type(RawRGB_reflection()))])


@dataclass(eq = False, repr = False)
class RawIco(Record):
    res: Optional[str]
    txt: Optional[str]
    text: Optional[str]
    txt_s: Optional[str]
    fg: Optional[RawRGB]
    bg: Optional[RawRGB]

RawIco_reflection = _expr202

def _expr203() -> TypeInfo:
    return record_type("FsHafas.Raw.RawDir", [], RawDir, lambda: [("txt", string_type), ("flg", option_type(string_type))])


@dataclass(eq = False, repr = False)
class RawDir(Record):
    txt: str
    flg: Optional[str]

RawDir_reflection = _expr203

def _expr204() -> TypeInfo:
    return record_type("FsHafas.Raw.RawTcoc", [], RawTcoc, lambda: [("c", string_type), ("r", option_type(int32_type))])


@dataclass(eq = False, repr = False)
class RawTcoc(Record):
    c: str
    r: Optional[int]

RawTcoc_reflection = _expr204

def _expr205() -> TypeInfo:
    return record_type("FsHafas.Raw.RawHimMsgCat", [], RawHimMsgCat, lambda: [("id", int32_type)])


@dataclass(eq = False, repr = False)
class RawHimMsgCat(Record):
    id: int

RawHimMsgCat_reflection = _expr205

def _expr206() -> TypeInfo:
    return record_type("FsHafas.Raw.IcoCrd", [], IcoCrd, lambda: [("x", int32_type), ("y", int32_type), ("type", option_type(string_type))])


@dataclass(eq = False, repr = False)
class IcoCrd(Record):
    x: int
    y: int
    type: Optional[str]

IcoCrd_reflection = _expr206

def _expr207() -> TypeInfo:
    return record_type("FsHafas.Raw.RawHimMsgEdge", [], RawHimMsgEdge, lambda: [("f_loc_x", option_type(int32_type)), ("t_loc_x", option_type(int32_type)), ("dir", option_type(int32_type)), ("ico_crd", IcoCrd_reflection()), ("msg_ref_l", option_type(array_type(int32_type))), ("ico_x", option_type(int32_type))])


@dataclass(eq = False, repr = False)
class RawHimMsgEdge(Record):
    f_loc_x: Optional[int]
    t_loc_x: Optional[int]
    dir: Optional[int]
    ico_crd: IcoCrd
    msg_ref_l: Optional[Array[int]]
    ico_x: Optional[int]

RawHimMsgEdge_reflection = _expr207

def _expr208() -> TypeInfo:
    return record_type("FsHafas.Raw.RawHimMsgEvent", [], RawHimMsgEvent, lambda: [("f_loc_x", option_type(int32_type)), ("t_loc_x", option_type(int32_type)), ("f_date", string_type), ("f_time", string_type), ("t_date", string_type), ("t_time", string_type)])


@dataclass(eq = False, repr = False)
class RawHimMsgEvent(Record):
    f_loc_x: Optional[int]
    t_loc_x: Optional[int]
    f_date: str
    f_time: str
    t_date: str
    t_time: str

RawHimMsgEvent_reflection = _expr208

def _expr209() -> TypeInfo:
    return record_type("FsHafas.Raw.RawCommon", [], RawCommon, lambda: [("loc_l", option_type(array_type(RawLoc_reflection()))), ("prod_l", option_type(array_type(RawProd_reflection()))), ("rem_l", option_type(array_type(RawRem_reflection()))), ("ico_l", option_type(array_type(RawIco_reflection()))), ("op_l", option_type(array_type(RawOp_reflection()))), ("max_c", option_type(int32_type)), ("num_c", option_type(int32_type)), ("him_l", option_type(array_type(RawHim_reflection()))), ("poly_l", option_type(array_type(RawPoly_reflection()))), ("dir_l", option_type(array_type(RawDir_reflection()))), ("tcoc_l", option_type(array_type(RawTcoc_reflection()))), ("him_msg_cat_l", option_type(array_type(RawHimMsgCat_reflection()))), ("him_msg_edge_l", option_type(array_type(RawHimMsgEdge_reflection()))), ("him_msg_event_l", option_type(array_type(RawHimMsgEvent_reflection())))])


@dataclass(eq = False, repr = False)
class RawCommon(Record):
    loc_l: Optional[Array[RawLoc]]
    prod_l: Optional[Array[RawProd]]
    rem_l: Optional[Array[RawRem]]
    ico_l: Optional[Array[RawIco]]
    op_l: Optional[Array[RawOp]]
    max_c: Optional[int]
    num_c: Optional[int]
    him_l: Optional[Array[RawHim]]
    poly_l: Optional[Array[RawPoly]]
    dir_l: Optional[Array[RawDir]]
    tcoc_l: Optional[Array[RawTcoc]]
    him_msg_cat_l: Optional[Array[RawHimMsgCat]]
    him_msg_edge_l: Optional[Array[RawHimMsgEdge]]
    him_msg_event_l: Optional[Array[RawHimMsgEvent]]

RawCommon_reflection = _expr209

def _expr210() -> TypeInfo:
    return record_type("FsHafas.Raw.RawMatch", [], RawMatch, lambda: [("field", option_type(string_type)), ("state", option_type(string_type)), ("loc_l", option_type(array_type(RawLoc_reflection())))])


@dataclass(eq = False, repr = False)
class RawMatch(Record):
    field: Optional[str]
    state: Optional[str]
    loc_l: Optional[Array[RawLoc]]

RawMatch_reflection = _expr210

def _expr211() -> TypeInfo:
    return record_type("FsHafas.Raw.RawPos", [], RawPos, lambda: [("loc_x", int32_type), ("dur", int32_type)])


@dataclass(eq = False, repr = False)
class RawPos(Record):
    loc_x: int
    dur: int

RawPos_reflection = _expr211

def _expr212() -> TypeInfo:
    return record_type("FsHafas.Raw.RawLine", [], RawLine, lambda: [("line_id", option_type(string_type)), ("prod_x", int32_type), ("dir_ref_l", option_type(array_type(int32_type))), ("jny_l", option_type(array_type(RawJny_reflection())))])


@dataclass(eq = False, repr = False)
class RawLine(Record):
    line_id: Optional[str]
    prod_x: int
    dir_ref_l: Optional[Array[int]]
    jny_l: Optional[Array[RawJny]]

RawLine_reflection = _expr212

def _expr213() -> TypeInfo:
    return record_type("FsHafas.Raw.RawResult", [], RawResult, lambda: [("common", option_type(RawCommon_reflection())), ("msg_l", option_type(array_type(RawHim_reflection()))), ("type", option_type(string_type)), ("jny_l", option_type(array_type(RawJny_reflection()))), ("out_con_l", option_type(array_type(RawOutCon_reflection()))), ("out_ctx_scr_b", option_type(string_type)), ("out_ctx_scr_f", option_type(string_type)), ("planrt_ts", option_type(string_type)), ("match", option_type(RawMatch_reflection())), ("loc_l", option_type(array_type(RawLoc_reflection()))), ("journey", option_type(RawJny_reflection())), ("hci_version", option_type(string_type)), ("fp_e", option_type(string_type)), ("s_d", option_type(string_type)), ("s_t", option_type(string_type)), ("fp_b", option_type(string_type)), ("pos_l", option_type(array_type(RawPos_reflection()))), ("line_l", option_type(array_type(RawLine_reflection())))])


@dataclass(eq = False, repr = False)
class RawResult(Record):
    common: Optional[RawCommon]
    msg_l: Optional[Array[RawHim]]
    type: Optional[str]
    jny_l: Optional[Array[RawJny]]
    out_con_l: Optional[Array[RawOutCon]]
    out_ctx_scr_b: Optional[str]
    out_ctx_scr_f: Optional[str]
    planrt_ts: Optional[str]
    match: Optional[RawMatch]
    loc_l: Optional[Array[RawLoc]]
    journey: Optional[RawJny]
    hci_version: Optional[str]
    fp_e: Optional[str]
    s_d: Optional[str]
    s_t: Optional[str]
    fp_b: Optional[str]
    pos_l: Optional[Array[RawPos]]
    line_l: Optional[Array[RawLine]]

RawResult_reflection = _expr213

def _expr214() -> TypeInfo:
    return record_type("FsHafas.Raw.SvcRes", [], SvcRes, lambda: [("meth", string_type), ("err", option_type(string_type)), ("err_txt", option_type(string_type)), ("res", option_type(RawResult_reflection()))])


@dataclass(eq = False, repr = False)
class SvcRes(Record):
    meth: str
    err: Optional[str]
    err_txt: Optional[str]
    res: Optional[RawResult]

SvcRes_reflection = _expr214

def _expr215() -> TypeInfo:
    return record_type("FsHafas.Raw.RawResponse", [], RawResponse, lambda: [("ver", string_type), ("lang", string_type), ("id", option_type(string_type)), ("err", option_type(string_type)), ("err_txt", option_type(string_type)), ("svc_res_l", option_type(array_type(SvcRes_reflection())))])


@dataclass(eq = False, repr = False)
class RawResponse(Record):
    ver: str
    lang: str
    id: Optional[str]
    err: Optional[str]
    err_txt: Optional[str]
    svc_res_l: Optional[Array[SvcRes]]

RawResponse_reflection = _expr215

def _expr216() -> TypeInfo:
    return record_type("FsHafas.Raw.Cfg", [], Cfg, lambda: [("poly_enc", string_type), ("rt_mode", option_type(string_type))])


@dataclass(eq = False, repr = False)
class Cfg(Record):
    poly_enc: str
    rt_mode: Optional[str]

Cfg_reflection = _expr216

def _expr217() -> TypeInfo:
    return record_type("FsHafas.Raw.Loc", [], Loc, lambda: [("type", string_type), ("name", option_type(string_type)), ("lid", option_type(string_type))])


@dataclass(eq = False, repr = False)
class Loc(Record):
    type: str
    name: Optional[str]
    lid: Optional[str]

Loc_reflection = _expr217

def _expr218() -> TypeInfo:
    return record_type("FsHafas.Raw.LocViaInput", [], LocViaInput, lambda: [("loc", Loc_reflection())])


@dataclass(eq = False, repr = False)
class LocViaInput(Record):
    loc: Loc

LocViaInput_reflection = _expr218

def _expr219() -> TypeInfo:
    return record_type("FsHafas.Raw.LocMatchInput", [], LocMatchInput, lambda: [("loc", Loc_reflection()), ("max_loc", int32_type), ("field", string_type)])


@dataclass(eq = False, repr = False)
class LocMatchInput(Record):
    loc: Loc
    max_loc: int
    field: str

LocMatchInput_reflection = _expr219

def _expr220() -> TypeInfo:
    return record_type("FsHafas.Raw.LocMatchRequest", [], LocMatchRequest, lambda: [("input", LocMatchInput_reflection())])


@dataclass(eq = False, repr = False)
class LocMatchRequest(Record):
    input: LocMatchInput

LocMatchRequest_reflection = _expr220

def _expr221() -> TypeInfo:
    return record_type("FsHafas.Raw.LineMatchRequest", [], LineMatchRequest, lambda: [("input", string_type)])


@dataclass(eq = False, repr = False)
class LineMatchRequest(Record):
    input: str

LineMatchRequest_reflection = _expr221

def _expr222() -> TypeInfo:
    return record_type("FsHafas.Raw.JourneyDetailsRequest", [], JourneyDetailsRequest, lambda: [("jid", string_type), ("name", string_type), ("get_polyline", bool_type)])


@dataclass(eq = False, repr = False)
class JourneyDetailsRequest(Record):
    jid: str
    name: str
    get_polyline: bool

JourneyDetailsRequest_reflection = _expr222

def _expr223() -> TypeInfo:
    return record_type("FsHafas.Raw.JnyFltr", [], JnyFltr, lambda: [("type", string_type), ("mode", string_type), ("value", option_type(string_type)), ("meta", option_type(string_type))])


@dataclass(eq = False, repr = False)
class JnyFltr(Record):
    type: str
    mode: str
    value: Optional[str]
    meta: Optional[str]

JnyFltr_reflection = _expr223

def _expr224() -> TypeInfo:
    return record_type("FsHafas.Raw.TvlrProf", [], TvlrProf, lambda: [("type", string_type), ("redtn_card", option_type(int32_type))])


@dataclass(eq = False, repr = False)
class TvlrProf(Record):
    type: str
    redtn_card: Optional[int]

TvlrProf_reflection = _expr224

def _expr225() -> TypeInfo:
    return record_type("FsHafas.Raw.TrfReq", [], TrfReq, lambda: [("jny_cl", int32_type), ("tvlr_prof", array_type(TvlrProf_reflection())), ("c_type", string_type)])


@dataclass(eq = False, repr = False)
class TrfReq(Record):
    jny_cl: int
    tvlr_prof: Array[TvlrProf]
    c_type: str

TrfReq_reflection = _expr225

def _expr226() -> TypeInfo:
    return record_type("FsHafas.Raw.StationBoardRequest", [], StationBoardRequest, lambda: [("type", string_type), ("date", string_type), ("time", string_type), ("stb_loc", Loc_reflection()), ("jny_fltr_l", array_type(JnyFltr_reflection())), ("dur", int32_type)])


@dataclass(eq = False, repr = False)
class StationBoardRequest(Record):
    type: str
    date: str
    time: str
    stb_loc: Loc
    jny_fltr_l: Array[JnyFltr]
    dur: int

StationBoardRequest_reflection = _expr226

def _expr227() -> TypeInfo:
    return record_type("FsHafas.Raw.HimSearchRequest", [], HimSearchRequest, lambda: [("him_fltr_l", array_type(JnyFltr_reflection())), ("get_polyline", bool_type), ("max_num", int32_type), ("date_b", string_type), ("time_b", string_type)])


@dataclass(eq = False, repr = False)
class HimSearchRequest(Record):
    him_fltr_l: Array[JnyFltr]
    get_polyline: bool
    max_num: int
    date_b: str
    time_b: str

HimSearchRequest_reflection = _expr227

def _expr228() -> TypeInfo:
    return record_type("FsHafas.Raw.ReconstructionRequest", [], ReconstructionRequest, lambda: [("get_ist", bool_type), ("get_passlist", bool_type), ("get_polyline", bool_type), ("get_tariff", bool_type), ("ctx_recon", option_type(string_type))])


@dataclass(eq = False, repr = False)
class ReconstructionRequest(Record):
    get_ist: bool
    get_passlist: bool
    get_polyline: bool
    get_tariff: bool
    ctx_recon: Optional[str]

ReconstructionRequest_reflection = _expr228

def _expr229() -> TypeInfo:
    return record_type("FsHafas.Raw.LocData", [], LocData, lambda: [("loc", Loc_reflection()), ("type", string_type), ("date", string_type), ("time", string_type)])


@dataclass(eq = False, repr = False)
class LocData(Record):
    loc: Loc
    type: str
    date: str
    time: str

LocData_reflection = _expr229

def _expr230() -> TypeInfo:
    return record_type("FsHafas.Raw.SearchOnTripRequest", [], SearchOnTripRequest, lambda: [("sot_mode", string_type), ("jid", string_type), ("loc_data", LocData_reflection()), ("arr_loc_l", array_type(Loc_reflection())), ("jny_fltr_l", array_type(JnyFltr_reflection())), ("get_passlist", bool_type), ("get_polyline", bool_type), ("min_chg_time", int32_type), ("get_tariff", bool_type)])


@dataclass(eq = False, repr = False)
class SearchOnTripRequest(Record):
    sot_mode: str
    jid: str
    loc_data: LocData
    arr_loc_l: Array[Loc]
    jny_fltr_l: Array[JnyFltr]
    get_passlist: bool
    get_polyline: bool
    min_chg_time: int
    get_tariff: bool

SearchOnTripRequest_reflection = _expr230

def _expr231() -> TypeInfo:
    return record_type("FsHafas.Raw.TripSearchRequest", [], TripSearchRequest, lambda: [("get_passlist", bool_type), ("max_chg", int32_type), ("min_chg_time", int32_type), ("dep_loc_l", array_type(Loc_reflection())), ("via_loc_l", option_type(array_type(LocViaInput_reflection()))), ("arr_loc_l", array_type(Loc_reflection())), ("jny_fltr_l", array_type(JnyFltr_reflection())), ("gis_fltr_l", array_type(JnyFltr_reflection())), ("get_tariff", bool_type), ("ushrp", bool_type), ("get_pt", bool_type), ("get_iv", bool_type), ("get_polyline", bool_type), ("out_date", string_type), ("out_time", string_type), ("num_f", int32_type), ("out_frwd", bool_type), ("trf_req", option_type(TrfReq_reflection()))])


@dataclass(eq = False, repr = False)
class TripSearchRequest(Record):
    get_passlist: bool
    max_chg: int
    min_chg_time: int
    dep_loc_l: Array[Loc]
    via_loc_l: Optional[Array[LocViaInput]]
    arr_loc_l: Array[Loc]
    jny_fltr_l: Array[JnyFltr]
    gis_fltr_l: Array[JnyFltr]
    get_tariff: bool
    ushrp: bool
    get_pt: bool
    get_iv: bool
    get_polyline: bool
    out_date: str
    out_time: str
    num_f: int
    out_frwd: bool
    trf_req: Optional[TrfReq]

TripSearchRequest_reflection = _expr231

def _expr232() -> TypeInfo:
    return record_type("FsHafas.Raw.JourneyMatchRequest", [], JourneyMatchRequest, lambda: [("input", string_type), ("date", option_type(string_type))])


@dataclass(eq = False, repr = False)
class JourneyMatchRequest(Record):
    input: str
    date: Optional[str]

JourneyMatchRequest_reflection = _expr232

def _expr233() -> TypeInfo:
    return record_type("FsHafas.Raw.RawcCrd", [], RawcCrd, lambda: [("x", int32_type), ("y", int32_type)])


@dataclass(eq = False, repr = False)
class RawcCrd(Record):
    x: int
    y: int

RawcCrd_reflection = _expr233

def _expr234() -> TypeInfo:
    return record_type("FsHafas.Raw.RawRing", [], RawRing, lambda: [("c_crd", RawcCrd_reflection()), ("max_dist", int32_type), ("min_dist", int32_type)])


@dataclass(eq = False, repr = False)
class RawRing(Record):
    c_crd: RawcCrd
    max_dist: int
    min_dist: int

RawRing_reflection = _expr234

def _expr235() -> TypeInfo:
    return record_type("FsHafas.Raw.LocGeoPosRequest", [], LocGeoPosRequest, lambda: [("ring", RawRing_reflection()), ("loc_fltr_l", array_type(JnyFltr_reflection())), ("get_pois", bool_type), ("get_stops", bool_type), ("max_loc", int32_type)])


@dataclass(eq = False, repr = False)
class LocGeoPosRequest(Record):
    ring: RawRing
    loc_fltr_l: Array[JnyFltr]
    get_pois: bool
    get_stops: bool
    max_loc: int

LocGeoPosRequest_reflection = _expr235

def _expr236() -> TypeInfo:
    return record_type("FsHafas.Raw.LocGeoReachRequest", [], LocGeoReachRequest, lambda: [("loc", Loc_reflection()), ("max_dur", int32_type), ("max_chg", int32_type), ("date", string_type), ("time", string_type), ("period", int32_type), ("jny_fltr_l", array_type(JnyFltr_reflection()))])


@dataclass(eq = False, repr = False)
class LocGeoReachRequest(Record):
    loc: Loc
    max_dur: int
    max_chg: int
    date: str
    time: str
    period: int
    jny_fltr_l: Array[JnyFltr]

LocGeoReachRequest_reflection = _expr236

def _expr237() -> TypeInfo:
    return record_type("FsHafas.Raw.LocDetailsRequest", [], LocDetailsRequest, lambda: [("loc_l", array_type(Loc_reflection()))])


@dataclass(eq = False, repr = False)
class LocDetailsRequest(Record):
    loc_l: Array[Loc]

LocDetailsRequest_reflection = _expr237

def _expr238() -> TypeInfo:
    return record_type("FsHafas.Raw.ServerInfoRequest", [], ServerInfoRequest, lambda: [("get_version_info", bool_type)])


@dataclass(eq = False, repr = False)
class ServerInfoRequest(Record):
    get_version_info: bool

ServerInfoRequest_reflection = _expr238

def _expr239() -> TypeInfo:
    return record_type("FsHafas.Raw.RawRect", [], RawRect, lambda: [("ll_crd", RawCrd_reflection()), ("ur_crd", RawCrd_reflection())])


@dataclass(eq = False, repr = False)
class RawRect(Record):
    ll_crd: RawCrd
    ur_crd: RawCrd

RawRect_reflection = _expr239

def _expr240() -> TypeInfo:
    return record_type("FsHafas.Raw.JourneyGeoPosRequest", [], JourneyGeoPosRequest, lambda: [("max_jny", int32_type), ("only_rt", bool_type), ("date", string_type), ("time", string_type), ("rect", RawRect_reflection()), ("per_size", int32_type), ("per_step", int32_type), ("age_of_report", bool_type), ("jny_fltr_l", array_type(JnyFltr_reflection())), ("train_pos_mode", string_type)])


@dataclass(eq = False, repr = False)
class JourneyGeoPosRequest(Record):
    max_jny: int
    only_rt: bool
    date: str
    time: str
    rect: RawRect
    per_size: int
    per_step: int
    age_of_report: bool
    jny_fltr_l: Array[JnyFltr]
    train_pos_mode: str

JourneyGeoPosRequest_reflection = _expr240

def _expr241() -> TypeInfo:
    return record_type("FsHafas.Raw.SvcReq", [], SvcReq, lambda: [("cfg", Cfg_reflection()), ("meth", string_type), ("req", obj_type)])


@dataclass(eq = False, repr = False)
class SvcReq(Record):
    cfg: Cfg
    meth: str
    req: Any

SvcReq_reflection = _expr241

def _expr242() -> TypeInfo:
    return record_type("FsHafas.Raw.RawRequestClient", [], RawRequestClient, lambda: [("id", string_type), ("v", string_type), ("type", string_type), ("name", string_type)])


@dataclass(eq = False, repr = False)
class RawRequestClient(Record):
    id: str
    v: str
    type: str
    name: str

RawRequestClient_reflection = _expr242

def _expr243() -> TypeInfo:
    return record_type("FsHafas.Raw.RawRequestAuth", [], RawRequestAuth, lambda: [("type", string_type), ("aid", string_type)])


@dataclass(eq = False, repr = False)
class RawRequestAuth(Record):
    type: str
    aid: str

RawRequestAuth_reflection = _expr243

def _expr244() -> TypeInfo:
    return record_type("FsHafas.Raw.RawRequest", [], RawRequest, lambda: [("lang", string_type), ("svc_req_l", array_type(SvcReq_reflection())), ("client", RawRequestClient_reflection()), ("ext", option_type(string_type)), ("ver", string_type), ("auth", RawRequestAuth_reflection())])


@dataclass(eq = False, repr = False)
class RawRequest(Record):
    lang: str
    svc_req_l: Array[SvcReq]
    client: RawRequestClient
    ext: Optional[str]
    ver: str
    auth: RawRequestAuth

RawRequest_reflection = _expr244

__all__ = ["RawPltf_reflection", "RawTrnCmpSX_reflection", "RawDep_reflection", "RawArr_reflection", "PubCh_reflection", "RawHim_reflection", "RawMsg_reflection", "RawRem_reflection", "RawStop_reflection", "PpLocRef_reflection", "RawPoly_reflection", "PolyG_reflection", "RawAni_reflection", "RawSDays_reflection", "RawPolyG_reflection", "RawCrd_reflection", "RawFreq_reflection", "RawJny_reflection", "RawGis_reflection", "RawSec_reflection", "RawSotCtxt_reflection", "Content_reflection", "ExtCont_reflection", "RawTicket_reflection", "RawPrice_reflection", "RawFare_reflection", "RawFareSet_reflection", "RawTrfRes_reflection", "RawRecon_reflection", "RawOutCon_reflection", "RawItem_reflection", "RawGrid_reflection", "RawLoc_reflection", "RawProdCtx_reflection", "RawOp_reflection", "RawProd_reflection", "RawRGB_reflection", "RawIco_reflection", "RawDir_reflection", "RawTcoc_reflection", "RawHimMsgCat_reflection", "IcoCrd_reflection", "RawHimMsgEdge_reflection", "RawHimMsgEvent_reflection", "RawCommon_reflection", "RawMatch_reflection", "RawPos_reflection", "RawLine_reflection", "RawResult_reflection", "SvcRes_reflection", "RawResponse_reflection", "Cfg_reflection", "Loc_reflection", "LocViaInput_reflection", "LocMatchInput_reflection", "LocMatchRequest_reflection", "LineMatchRequest_reflection", "JourneyDetailsRequest_reflection", "JnyFltr_reflection", "TvlrProf_reflection", "TrfReq_reflection", "StationBoardRequest_reflection", "HimSearchRequest_reflection", "ReconstructionRequest_reflection", "LocData_reflection", "SearchOnTripRequest_reflection", "TripSearchRequest_reflection", "JourneyMatchRequest_reflection", "RawcCrd_reflection", "RawRing_reflection", "LocGeoPosRequest_reflection", "LocGeoReachRequest_reflection", "LocDetailsRequest_reflection", "ServerInfoRequest_reflection", "RawRect_reflection", "JourneyGeoPosRequest_reflection", "SvcReq_reflection", "RawRequestClient_reflection", "RawRequestAuth_reflection", "RawRequest_reflection"]

