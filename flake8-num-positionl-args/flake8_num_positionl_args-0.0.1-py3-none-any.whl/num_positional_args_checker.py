import ast
from dataclasses import dataclass
from typing import Any, Generator, Iterator

CODE = "X"
FUNCTION_ARGS_CODE = f"{CODE}001"
ASYNC_FUNCTION_ARGS_CODE = f"{CODE}002"


@dataclass
class Problem:
    lineno: int
    col_offset: int
    reason: str


class NumPositionalArgsVisitor(ast.NodeVisitor):
    _problems: list[Problem]

    def __init__(self, max_n_args: int = 1) -> None:
        self._max_n_args = max_n_args
        self._problems = []

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        n_args = len(node.args.args)
        if self._max_n_args < n_args:
            self._problems.append(
                Problem(
                    lineno=node.lineno,
                    col_offset=node.col_offset,
                    reason=self._build_reason(
                        FUNCTION_ARGS_CODE,
                        n_args,
                    ),
                ),
            )

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        n_args = len(node.args.args)
        if self._max_n_args < n_args:
            self._problems.append(
                Problem(
                    lineno=node.lineno,
                    col_offset=node.col_offset,
                    reason=self._build_reason(
                        ASYNC_FUNCTION_ARGS_CODE,
                        n_args,
                    ),
                ),
            )

    @classmethod
    def _build_reason(cls, code: str, n_args: int):
        return f"{code} Found {n_args} positional args."

    def get_problems(self) -> Iterator[Problem]:
        yield from self._problems


class NumPositionalArgsChecker:
    name = "num_positional_args"
    version = "0.0.1"
    code = CODE

    def __init__(self, tree: ast.AST) -> None:
        self.tree = tree

    def run(self) -> Generator[tuple[int, int, str, type[Any]], None, None]:
        visitor = NumPositionalArgsVisitor()
        visitor.visit(self.tree)
        for problem in visitor.get_problems():
            yield problem.lineno, problem.col_offset, problem.reason, type(self)
