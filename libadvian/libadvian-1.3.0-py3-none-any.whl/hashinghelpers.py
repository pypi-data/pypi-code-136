"""Helpers to convert various mutable structures to immutable"""
from typing import Mapping, Sequence, Union, Dict, List, Any
from json import JSONEncoder
import logging

from frozendict import frozendict  # type: ignore # False positive on has no attribute "frozendict"


ValidKeyTypes = Union[str, int, float]  # python actually supports just about any hashable type as key
IMTypes = Union[str, bytes, int, float, bool, None, frozendict]  # if you change this look at line 24 too
HandledSubTypes = Union[Mapping[ValidKeyTypes, IMTypes], Sequence[IMTypes], IMTypes]
HandledTypes = Union[Mapping[ValidKeyTypes, HandledSubTypes], Sequence[HandledSubTypes], IMTypes]
LOGGER = logging.getLogger(__name__)


class ImmobilizeError(ValueError):
    """Raised if we could not figure out what to do"""


class FrozendictEncoder(JSONEncoder):
    """Handle frozendict in JSON"""

    def default(self, o: Any) -> Any:
        if isinstance(o, frozendict):
            return dict(o)
        return super().default(o)


class ForgivingEncoder(FrozendictEncoder):
    """Set un-encodable values to None"""

    def default(self, o: Any) -> Any:
        try:
            return super().default(o)
        except TypeError as exc:
            LOGGER.warning("Encoding error {}, encoding as None".format(exc))
            return None


def immobilize(data_in: HandledTypes, none_on_fallthru: bool = False) -> Union[HandledTypes, frozendict]:
    """Recurse over the input making types immutable

    if none_on_fallthru is true then this returns None for a type it does not know how to handle, otherwise
    raises ImmobilizeError"""
    if data_in is None:
        return None
    if isinstance(data_in, (str, bytes, int, float, bool, frozendict)):
        return data_in
    if isinstance(data_in, Mapping):
        new_dict: Dict[ValidKeyTypes, HandledSubTypes] = {}
        for key in data_in.keys():
            new_dict[key] = immobilize(data_in[key])
        return frozendict(new_dict)
    if isinstance(data_in, Sequence):
        new_list: List[HandledSubTypes] = []
        for value in data_in:
            new_list.append(immobilize(value))
        return tuple(new_list)
    # fail-safe for hashable types we did not enumerate
    try:
        hash(data_in)
        return data_in
    except TypeError:
        pass
    # Fall through
    if none_on_fallthru:
        return None
    raise ImmobilizeError(f"Could not figure out what to do with {repr(data_in)}")
