from typing import (Any, List)
from ..fable_library.reflection import (TypeInfo, float64_type, string_type, bool_type, list_type, class_type, union_type)
from ..fable_library.types import (Array, Union)

def _expr3() -> TypeInfo:
    return union_type("Fable.SimpleJson.Python.Json", [], Json, lambda: [[("Item", float64_type)], [("Item", string_type)], [("Item", bool_type)], [], [("Item", list_type(Json_reflection()))], [("Item", class_type("Microsoft.FSharp.Collections.FSharpMap`2", [string_type, Json_reflection()]))]])


class Json(Union):
    def __init__(self, tag: int, *fields: Any) -> None:
        super().__init__()
        self.tag: int = tag or 0
        self.fields: Array[Any] = list(fields)

    @staticmethod
    def cases() -> List[str]:
        return ["JNumber", "JString", "JBool", "JNull", "JArray", "JObject"]


Json_reflection = _expr3

__all__ = ["Json_reflection"]

