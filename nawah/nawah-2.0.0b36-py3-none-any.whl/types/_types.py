"""Provides types used in Nawah"""

from typing import (TYPE_CHECKING, Any, Literal, MutableMapping,
                    MutableSequence, TypedDict, Union)

from nawah.enums import Event

if TYPE_CHECKING:
    from nawah.classes import Package, Var


class Results(TypedDict):
    """Provides type-hint for return of Nawah Function"""

    status: int
    msg: str
    args: "ResultsArgs"


ResultsArgs = MutableMapping[str, Any]


class AppPackage(TypedDict):
    """Provides type-hint for item of 'Config.packages'"""

    package: "Package"
    modules: MutableSequence[str]


NawahEvents = MutableSequence[Event]


class NawahConn(TypedDict):
    """Provides type-hint for base values for 'session' dict"""

    REMOTE_ADDR: str
    HTTP_USER_AGENT: str
    HTTP_ORIGIN: str
    client_app: str
    args: MutableMapping[str, Any]


class NawahSession(TypedDict):
    """Provides type-hint for 'session' dict"""

    # session doc attributes
    _id: str
    user: MutableMapping
    groups: MutableSequence[str]
    host_add: str
    user_agent: str
    expiry: str
    token: str
    token_hash: str
    create_time: str
    # Nawah session attributes
    conn: "NawahConn"


class NawahQuerySpecialGroup(TypedDict):
    """Provides type-hint for '$group' in 'NawahQuery'"""

    by: str
    count: int


class NawahQuerySpecialGeoNear(TypedDict):
    """Provides type-hint for '$geo_near' in 'NawahQuery'"""

    val: str
    attr: str
    dist: int


# Following TypedDict type can't be defined as class as keys include $
NawahQuerySpecial = TypedDict(
    "NawahQuerySpecial",
    {
        "$search": str,
        "$sort": MutableMapping[str, Literal[1, -1]],
        "$skip": int,
        "$limit": int,
        "$extn": Union[bool, MutableSequence[str]],
        "$attrs": MutableSequence[str],
        "$group": MutableSequence[NawahQuerySpecialGroup],
        "$geo_near": NawahQuerySpecialGeoNear,
        "$deleted": bool,
    },
    total=False,
)

NawahQueryOperEq = TypedDict("NawahQueryOperEq", {"$eq": Any})
NawahQueryOperNe = TypedDict("NawahQueryOperNe", {"$ne": Any})
NawahQueryOperGt = TypedDict("NawahQueryOperGt", {"$gt": Union[int, float, str, "Var"]})
NawahQueryOperGte = TypedDict(
    "NawahQueryOperGte", {"$gte": Union[int, float, str, "Var"]}
)
NawahQueryOperLt = TypedDict("NawahQueryOperLt", {"$lt": Union[int, float, str, "Var"]})
NawahQueryOperLte = TypedDict(
    "NawahQueryOperLte", {"$lte": Union[int, float, str, "Var"]}
)
NawahQueryOperAll = TypedDict("NawahQueryOperAll", {"$all": Union[list[Any], "Var"]})
NawahQueryOperIn = TypedDict("NawahQueryOperIn", {"$in": Union[list[Any], "Var"]})
NawahQueryOperNin = TypedDict("NawahQueryOperNin", {"$nin": Union[list[Any], "Var"]})
NawahQueryOperRegex = TypedDict("NawahQueryOperRegex", {"$regex": Union[str, "Var"]})
NawahQueryStep = dict[
    str,
    Union[
        NawahQueryOperEq,
        NawahQueryOperNe,
        NawahQueryOperGt,
        NawahQueryOperGte,
        NawahQueryOperLt,
        NawahQueryOperLte,
        NawahQueryOperAll,
        NawahQueryOperIn,
        NawahQueryOperNin,
        NawahQueryOperRegex,
    ],
]

NawahQueryOperOr = TypedDict("NawahQueryOperOr", {"$or": list[NawahQueryStep]})
NawahQueryOperAnd = TypedDict("NawahQueryOperAnd", {"$and": list[NawahQueryStep]})

NawahQueryIndex = TypedDict(
    "NawahQueryIndex", {"$index": dict[str, list[tuple[str, Any]]]}
)

NawahDoc = MutableMapping[str, Any]
