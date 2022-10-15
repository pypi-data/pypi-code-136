#
# Product:   Macal
# Author:    Marco Caspers
# Date:      12-09-2022
#

import typing
from . import ast
from . import types
from . import ast_expr
from . import ast_block
from . import token
from . import location


class FunctionDefinition(ast.AST):
    def __init__(self, tok: token.LexToken) -> None:
        super().__init__(tok, types.AstTypes.FunctionDefinition)
        self.Name: str = tok.Lexeme
        self.Arguments: ast_expr.Expr = None
        self.Block: ast_block.Block = None
        self.IsExternal: bool = False
        self.ExternalModule: token.LexToken = None
        self.ExternalFunction: token.LexToken = None


    def registerArgument(self, name: str) -> None:
        if self.Arguments is None:
            self.Arguments = ast_expr.Expr(
                token.LexToken('(', 
                    types.LexTokenTypes.Punctuation, 
                    location.SourceLocation(-1,-1), 
                    -1))
            self.Arguments.ExprType = types.ExprTypes.ArgumentList
            self.Arguments.Left = []
        if name is None: 
            return
        expr = ast_expr.Expr(
            token.LexToken(name, 
                types.LexTokenTypes.Identifier,
                location.SourceLocation(-1,-1), 
                -1))
        expr.ExprType = types.ExprTypes.Variable
        self.Arguments.Left.append(expr)


    def __repr__(self):
        return f'FunctionDefinition(tok="{self.Token}")'



    def __str__(self):
        #a = ', '.join([f'{arg}' for arg in self.Arguments.Left])
        a = ', '.join([arg.Token.Lexeme for arg in self.Arguments.Left])
        s = f'{self.Name} => ({a})'
        if self.Block is not None:
            s = f'{s}{self.__mask_linefeeds__(f"{self.Block}")}'
        return s