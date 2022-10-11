from typing import Any, Callable, Dict, List, Optional, Set, Tuple, Type as TypingType, Union

from mypy.options import Options
from mypy.plugin import CheckerPluginInterface, ClassDefContext, MethodContext, Plugin, SemanticAnalyzerPluginInterface
from mypy.plugins import dataclasses
from mypy.nodes import SymbolTableNode, AssignmentStmt
from mypy.types import (
    AnyType,
    CallableType,
    Instance,
    NoneType,
    Type,
    TypeOfAny,
    TypeType,
    TypeVarType,
    UnionType,
    get_proper_type,
)
from numpy import isin

DATACLASS_PATHS = {"runtype.dataclass.dataclass"}

def plugin(version: str) -> 'TypingType[Plugin]':
    """
    `version` is the mypy version string
    We might want to use this to print a warning if the mypy version being used is
    newer, or especially older, than we expect (or need).
    """
    return PydanticPlugin


# def copy_symbol_table_node(n):
#     kind: int,
#     node: Optional[SymbolNode],
#     module_public: bool = True,
#     implicit: bool = False,
#     module_hidden: bool = False,
#     *,
#     plugin_generated: bool = False,
#     no_serialize: bool = False) -> None:


def my_dataclass_class_maker_callback(ctx: dataclasses.ClassDefContext) -> bool:
    """Hooks into the class typechecking process to add support for dataclasses.
    """
    transformer = dataclasses.DataclassTransformer(ctx)
    res = transformer.transform()
    for stmt in ctx.cls.defs.body:
        if isinstance(stmt, AssignmentStmt):
            if isinstance(stmt.rvalue, dataclasses.NameExpr):
                if stmt.rvalue.fullname == 'builtins.None':
                    assert len(stmt.lvalues) == 1
                    lval ,= stmt.lvalues
                    name = lval.fullname
                    assert '.' not in name
                    stn = ctx.cls.info.names[name]
                    breakpoint()
                    stn.node.type = UnionType([stn.node.type, NoneType()])
    return res

class PydanticPlugin(Plugin):
    def __init__(self, options: Options) -> None:
        # self.plugin_config = PydanticPluginConfig(options)
        super().__init__(options)

    # def get_base_class_hook(self, fullname: str) -> 'Optional[Callable[[ClassDefContext], None]]':
    #     sym = self.lookup_fully_qualified(fullname)
    #     if sym and isinstance(sym.node, TypeInfo):  # pragma: no branch
    #         # No branching may occur if the mypy cache has not been cleared
    #         if any(get_fullname(base) == BASEMODEL_FULLNAME for base in sym.node.mro):
    #             return self._pydantic_model_class_maker_callback
    #     return None

    # def get_method_hook(self, fullname: str) -> Optional[Callable[[MethodContext], Type]]:
    #     if fullname.endswith('.from_orm'):
    #         return from_orm_callback
    #     return None

    def get_class_decorator_hook(self, fullname: str) -> Optional[Callable[[ClassDefContext], None]]:
        if fullname in DATACLASS_PATHS:
            return my_dataclass_class_maker_callback
        return None
