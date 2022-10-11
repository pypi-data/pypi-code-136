#
# Product:   Macal
# Author:    Marco Caspers
# Date:      12-09-2022
#

from . import ast
from . import types
from . import token
from . import ast_expr

class Return(ast.AST):
    def __init__(self, tok: token.LexToken) -> None:
        super().__init__(tok, types.AstTypes.Return)
        self.Value: ast_expr.Expr = None

    
    
    def __repr__(self):
        return f'Return(tok={self.Token})'


    
    def __str__(self):
        return f'return;'