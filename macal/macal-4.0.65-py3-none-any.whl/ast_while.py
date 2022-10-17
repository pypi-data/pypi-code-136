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


class While(ast.AST):
    def __init__(self, tok: token.LexToken) -> None:
        super().__init__(tok, types.AstTypes.While)
        self.Condition: ast_expr.Expr = None
        self.Block: ast_block.Block = None


    def __str__(self):
        return f'while {self.Condition} {self.__mask_linefeeds__(f"{self.Block}")}'