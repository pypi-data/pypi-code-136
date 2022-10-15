#
# Product:   Macal
# Author:    Marco Caspers
# Date:      12-09-2022
#

from . import ast
from . import types
from . import token


class Continue(ast.AST):
    def __init__(self, tok: token.LexToken) -> None:
        super().__init__(tok, types.AstTypes.Continue)



    def __repr__(self):
        return f'Continue(tok={self.Token})'


    
    def __str__(self):
        return f'continue;'