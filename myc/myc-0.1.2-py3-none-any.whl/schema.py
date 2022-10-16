import functools
from dataclasses import dataclass
from typing import List, Optional
import inspect


@dataclass
class FunctionParamSchema:
    name: str
    index: Optional[int]
    typ: type


class FunctionSchema:
    def __init__(self, params: List[FunctionParamSchema]):
        self._params = params
        self._param_map = {p.name: p for p in self._params}

    @property
    def params(self) -> List[FunctionParamSchema]:
        return self._params

    def get_param_by_index(self, index: int) -> Optional[FunctionParamSchema]:
        if index < len(self._params):
            p = self._params[index]
            if p.index == index:
                return p

    def get_param_by_name(self, name: str) -> Optional[FunctionParamSchema]:
        return self._param_map.get(name)


@functools.cache
def build_default_function_schema(fn) -> FunctionSchema:
    """
    Uses Python's reflection facilities to build a default schema for the specified function.
    """
    sig = inspect.signature(fn)

    params = []
    for i, (name, param) in enumerate(sig.parameters.items()):
        params.append(
            FunctionParamSchema(
                name=name,
                index=i if param.kind != inspect.Parameter.KEYWORD_ONLY else None,
                typ=param.annotation,
            )
        )

    return FunctionSchema(params=params)
