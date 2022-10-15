#
# Product:   Macal
# Author:    Marco Caspers
# Date:      12-09-2022
#

import typing
from . import ast
from . import types
from . import ast_expr
from . import token


class FunctionCall(ast.AST):
    def __init__(self, tok: token.LexToken, varIndex: ast_expr.Expr) -> None:
        super().__init__(tok, types.AstTypes.FunctionCall)
        self.Name = tok.Lexeme
        self.Args: typing.List[ast_expr.Expr]
        self.VarIndex: ast_expr.Expr = varIndex



    def __repr__(self):
        return f'FunctionCall(tok="{self.Token}", varIndex="{self.VarIndex}")'



    def __str__(self):
        a = ', '.join([f'{arg}' for arg in self.Args])
        return f'{self.Name}({a});'
        