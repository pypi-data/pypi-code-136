#
# Product:   Macal
# Author:    Marco Caspers
# Date:      12-09-2022
#

from . import ast
from . import types
from . import ast_expr
from . import ast_block
from . import token


class Foreach(ast.AST):
    def __init__(self, tok: token.LexToken) -> None:
        super().__init__(tok, types.AstTypes.Foreach)
        self.Variable: ast_expr.Expr = None
        self.Block: ast_block.Block = None

    def __str__(self):
        return f'foreach {self.Variable} {self.__mask_linefeeds__(f"{self.Block}")}'