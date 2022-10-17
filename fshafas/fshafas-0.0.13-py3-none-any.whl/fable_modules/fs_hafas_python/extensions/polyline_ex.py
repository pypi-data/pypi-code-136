from dataclasses import dataclass
from typing import Callable
from ...fable_library.reflection import (TypeInfo, string_type, float64_type, array_type, lambda_type, record_type)
from ...fable_library.types import (Record, Array)

def _expr294() -> TypeInfo:
    return record_type("FsHafas.Extensions.PolylineEx.GooglePolyline", [], GooglePolyline, lambda: [("decode", lambda_type(string_type, array_type(array_type(float64_type))))])


@dataclass(eq = False, repr = False)
class GooglePolyline(Record):
    decode: Callable[[str], Array[Array[float]]]

GooglePolyline_reflection = _expr294

__all__ = ["GooglePolyline_reflection"]

