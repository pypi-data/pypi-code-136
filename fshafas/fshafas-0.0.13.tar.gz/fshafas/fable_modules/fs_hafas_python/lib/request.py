from __future__ import annotations
from hashlib import md5
from json import dumps
from requests import post
from typing import (Literal, Any, TypeVar)
from ...fable_library.async_builder import (singleton, Async)
from ...fable_library.map_util import add_to_dict
from ...fable_library.reflection import (TypeInfo, class_type)
from ..extra_types import Log_Print

__A = TypeVar("__A")

def _expr315() -> TypeInfo:
    return class_type("FsHafas.Client.Request.HttpClient", None, HttpClient)


class HttpClient:
    def __init__(self, __unit: Literal[None]=None) -> None:
        pass


HttpClient_reflection = _expr315

def HttpClient__ctor(__unit: Literal[None]=None) -> HttpClient:
    return HttpClient(__unit)


def HttpClient__Dispose(__: HttpClient) -> None:
    pass


def HttpClient__PostAsync(__: HttpClient, url: str, add_checksum: bool, add_mic_mac: bool, salt: str, json: str) -> Async[str]:
    url_escaped: str
    if (len(salt) > 0) if add_checksum else False:
        url_escaped = (url + "?checksum=") + HttpClient__getMd5_Z721C83C5(__, json + salt)

    elif (len(salt) > 0) if add_mic_mac else False:
        mic: str = HttpClient__getMd5_Z721C83C5(__, json)
        url_escaped = (((url + "?mic=") + mic) + "&mac=") + HttpClient__getMd5_Z721C83C5(__, mic + salt)

    else: 
        url_escaped = url

    HttpClient__log(__, "url: ", url_escaped)
    headers: Any = dict([])
    add_to_dict(headers, "Content-Type", "application/json; charset=utf-8")
    add_to_dict(headers, "Accept-Encoding", "gzip, br, deflate")
    add_to_dict(headers, "Accept", "application/json")
    add_to_dict(headers, "User-Agent", "agent")
    def _arrow316(__unit: Literal[None]=None, __: HttpClient=__, url: str=url, add_checksum: bool=add_checksum, add_mic_mac: bool=add_mic_mac, salt: str=salt, json: str=json) -> Async[str]:
        r: Any = post(url_escaped, data=json.encode('utf-8'), headers=headers)
        if (r.status_code) == 200:
            return singleton.Return(dumps(r.json()))

        else: 
            HttpClient__log(__, "statusCode: ", r.status_code)
            HttpClient__log(__, "text: ", r.text)
            return singleton.Return("")


    return singleton.Delay(_arrow316)


def HttpClient__log(this: HttpClient, msg: str, o: Any) -> None:
    Log_Print(msg, o)


def HttpClient__getMd5_Z721C83C5(this: HttpClient, s: str) -> str:
    return md5(s.encode()).hexdigest()


__all__ = ["HttpClient_reflection", "HttpClient__Dispose", "HttpClient__PostAsync", "HttpClient__log", "HttpClient__getMd5_Z721C83C5"]

