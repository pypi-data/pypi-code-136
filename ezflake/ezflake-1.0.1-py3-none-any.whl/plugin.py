from __future__ import annotations

import ast
from abc import abstractmethod, ABC
from typing import Tuple, List, Type, Iterator

from .violation import Violation, ViolationFactory


class Visitor(ast.NodeVisitor):
    def __init__(self, plugin: Plugin):
        super().__init__()
        self.plugin = plugin
        self.violate = plugin.violate


class Plugin(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @property
    @abstractmethod
    def visitors(self) -> List[Type[Visitor]]:
        ...

    def __init__(self, tree: ast.AST):
        self._tree = tree
        self.violations: List[Violation] = []

    def violate(self, violation_type: ViolationFactory, node: ast.AST, **kwargs) -> None:
        violation = violation_type(node.lineno, node.col_offset, kwargs)
        self.violations.append(violation)

    def _run(self) -> List[Violation]:
        for visitor_type in self.visitors:
            visitor = visitor_type(self)
            visitor.visit(self._tree)

        return self.violations

    def run(self) -> Iterator[Tuple[int, int, str, type]]:
        yield from (violation.as_tuple(self.__class__) for violation in self.violations)
