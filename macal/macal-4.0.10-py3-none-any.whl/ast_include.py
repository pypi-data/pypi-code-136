#
# Product:   Macal
# Author:    Marco Caspers
# Date:      12-09-2022
#

import typing
from . import ast
from . import types
from . import token


class Include(ast.AST):
    def __init__(self, tok: token.LexToken) -> None:
        super().__init__(tok, types.AstTypes.Include)
        self.Includes: typing.List[token.LexToken] = []

    

    def Add(self, include: token.LexToken):
        self.Includes.append(include)
    

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        lst = ', '.join([lib.Lexeme for lib in self.Includes])
        return f'include {lst};'