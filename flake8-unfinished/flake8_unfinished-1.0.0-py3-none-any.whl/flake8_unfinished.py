import ast
from typing import Generator, Tuple, List

UNF001 = "UNF001 Do not use 'NotImplementedError'"


class Plugin:
    def __init__(self, tree: ast.AST):
        self._tree = tree

    def run(self) -> Generator[Tuple[int, int, str, type], None, None]:
        visitor = Visitor()
        visitor.visit(self._tree)

        for line, col, msg in visitor.errors:
            yield line, col, msg, type(self)


class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.errors: List[Tuple[int, int, str]] = []

    def visit_Name(self, node: ast.Name) -> None:
        if node.id == 'NotImplementedError':
            self.errors.append((node.lineno, node.col_offset, UNF001))
        self.generic_visit(node)
