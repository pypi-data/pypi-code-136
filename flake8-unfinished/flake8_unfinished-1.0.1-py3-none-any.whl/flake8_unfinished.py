import ast
from typing import Generator, Tuple, List


UNF001 = "UNF001 Do not raise 'NotImplementedError'"


class Plugin:
    def __init__(self, tree: ast.AST):
        self._tree = tree

    def run(self) -> Generator[Tuple[int, int, str, type], None, None]:
        visitor = Visitor()
        visitor.visit(self._tree)

        for line, col, msg in visitor.violations:
            yield line, col, msg, type(self)


class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.violations: List[Tuple[int, int, str]] = []

    def visit_Raise(self, node: ast.Raise):
        if isinstance(node.exc, ast.Name):
            name = node.exc.id
        elif isinstance(node.exc, ast.Call):
            if isinstance(node.exc.func, ast.Name):
                name = node.exc.func.id
            elif isinstance(node.exc.func, ast.Attribute):
                name = node.exc.func.attr
            else:
                raise ValueError
        else:
            raise ValueError
        if name == 'NotImplementedError':
            self.violations.append((node.lineno, node.col_offset, UNF001))
        self.generic_visit(node)
