from __future__ import annotations
from dataclasses import dataclass
from typing import (Any, List)
from ..fable_library.reflection import (TypeInfo as TypeInfo_1, string_type, class_type, record_type, array_type, unit_type, lambda_type, tuple_type, union_type)
from ..fable_library.types import (Record, Array, Union)

def _expr0() -> TypeInfo_1:
    return record_type("Fable.SimpleJson.Python.RecordField", [], RecordField, lambda: [("FieldName", string_type), ("FieldType", TypeInfo_reflection()), ("PropertyInfo", class_type("System.Reflection.PropertyInfo"))])


@dataclass(eq = False, repr = False)
class RecordField(Record):
    FieldName: str
    FieldType: TypeInfo
    PropertyInfo: Any

RecordField_reflection = _expr0

def _expr1() -> TypeInfo_1:
    return record_type("Fable.SimpleJson.Python.UnionCase", [], UnionCase, lambda: [("CaseName", string_type), ("CaseTypes", array_type(TypeInfo_reflection())), ("Info", class_type("Microsoft.FSharp.Reflection.UnionCaseInfo"))])


@dataclass(eq = False, repr = False)
class UnionCase(Record):
    CaseName: str
    CaseTypes: Array[TypeInfo]
    Info: Any

UnionCase_reflection = _expr1

def _expr2() -> TypeInfo_1:
    return union_type("Fable.SimpleJson.Python.TypeInfo", [], TypeInfo, lambda: [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [("Item", lambda_type(unit_type, class_type("System.Type")))], [("Item", lambda_type(unit_type, TypeInfo_reflection()))], [("Item", lambda_type(unit_type, TypeInfo_reflection()))], [("Item", lambda_type(unit_type, TypeInfo_reflection()))], [("Item", lambda_type(unit_type, TypeInfo_reflection()))], [("Item", lambda_type(unit_type, TypeInfo_reflection()))], [("Item", lambda_type(unit_type, TypeInfo_reflection()))], [("Item", lambda_type(unit_type, TypeInfo_reflection()))], [("Item", lambda_type(unit_type, array_type(TypeInfo_reflection())))], [("Item", lambda_type(unit_type, tuple_type(TypeInfo_reflection(), TypeInfo_reflection())))], [("Item", lambda_type(unit_type, tuple_type(TypeInfo_reflection(), TypeInfo_reflection(), class_type("System.Type"))))], [("Item", lambda_type(unit_type, TypeInfo_reflection()))], [("Item", lambda_type(unit_type, TypeInfo_reflection()))], [("Item", lambda_type(unit_type, array_type(TypeInfo_reflection())))], [("Item", lambda_type(unit_type, tuple_type(TypeInfo_reflection(), class_type("System.Type"))))], [("Item", lambda_type(unit_type, tuple_type(array_type(RecordField_reflection()), class_type("System.Type"))))], [("Item", lambda_type(unit_type, tuple_type(array_type(UnionCase_reflection()), class_type("System.Type"))))]])


class TypeInfo(Union):
    def __init__(self, tag: int, *fields: Any) -> None:
        super().__init__()
        self.tag: int = tag or 0
        self.fields: Array[Any] = list(fields)

    @staticmethod
    def cases() -> List[str]:
        return ["Unit", "Char", "String", "UInt16", "UInt32", "UInt64", "Int32", "Bool", "Float32", "Float", "Decimal", "Short", "Long", "Byte", "SByte", "DateTime", "DateTimeOffset", "BigInt", "TimeSpan", "Guid", "Object", "Uri", "Any", "Async", "Promise", "Option", "List", "Set", "Array", "Seq", "Tuple", "Map", "Dictionary", "ResizeArray", "HashSet", "Func", "Enum", "Record", "Union"]


TypeInfo_reflection = _expr2

__all__ = ["RecordField_reflection", "UnionCase_reflection", "TypeInfo_reflection"]

