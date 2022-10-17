# -*- coding: utf-8 -*-
# Copyright (c) 2022, KarjaKAK
# All rights reserved.

from dataclasses import dataclass
from types import MappingProxyType as mpt


__all__ = ["EvalExp"]


@dataclass(frozen=True, slots=True)
class EvalExp:
    """Class eval that controled what can be express"""

    expression: str
    _all: dict | None

    def __post_init__(self):

        match (
            isinstance(self.expression, str),
            isinstance(self._all, dict|None)
        ):
            case (False, _):
                raise TypeError(f"{self.expression!r} Expected String type!")
            case (_, False):
                raise TypeError(f"{self._all!r} Expected Dict or None!")
            case _:
                if self._all is not None: 
                    super(EvalExp, self).__setattr__("_all", mpt(self._all))

    def evlex(self):
        """Expression that controled by what allowed"""

        comp = compile(self.expression, "<string>", "eval",)
        try:
            for name in comp.co_names:
                if name not in self._all:
                    raise NameError(f"{name!r} is not allowed for expression!")
            else:
                return eval(self.expression, {"__builtins__": None}, self._all)
        except:
            raise
        finally:
            del comp
