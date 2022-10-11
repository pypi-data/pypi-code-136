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


class Elif(ast.AST):
    def __init__(self, tok: token.LexToken) -> None:
        super().__init__(tok, types.AstTypes.Elif)
        self.Condition: ast_expr.Expr = None
        self.Block: ast_block.Block = None



    def __str__(self):
        return f'elif {self.Condition} {self.__mask_linefeeds__(f"{self.Block}")}\\n'


class If(ast.AST):
    def __init__(self, tok: token.LexToken) -> None:
        super().__init__(tok, types.AstTypes.If)
        self.Condition: ast_expr.Expr = None
        self.Block: ast_block.Block = None
        self.Elif: typing.List[Elif] = []
        self.Else: ast_block.Block = None


    
    def Add(self, elfi: Elif) -> None:
        self.Elif.append(elfi)



    def __str__(self):
        s = f'if {self.Condition} {self.__mask_linefeeds__(f"{self.Block}")} '
        for lefi in self.Elif:
            s = f'{s}{lefi} '
        if self.Else is not None:
            s = f'{s}else {self.__mask_linefeeds__(f"{self.Else}")}'
        return s
