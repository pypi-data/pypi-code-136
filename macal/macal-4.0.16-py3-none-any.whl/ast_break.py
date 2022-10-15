#
# Product:   Macal
# Author:    Marco Caspers
# Date:      12-09-2022
#

from . import ast
from . import types
from . import token


class Break(ast.AST):
    def __init__(self, tok: token.LexToken) -> None:
        super().__init__(tok, types.AstTypes.Break)



    def __repr__(self):
        return f"Break(tok={self.Token})"



    def __str__(self):
        return "break;"