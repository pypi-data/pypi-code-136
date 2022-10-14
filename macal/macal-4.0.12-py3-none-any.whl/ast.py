#
# Product:   Macal
# Author:    Marco Caspers
# Date:      09-09-2022
#

from . import types
from . import token

class AST:
    """This is the base class for all AST node types"""
    def __init__(self, tok: token.LexToken, type: types.AstType) -> None:
        self.Token : token.LexToken = tok
        self.Type : types.AstType = type



    def __mask_linefeeds__(self, string: str) -> str:
        return string.replace('\n', '\\n')



    def __repr__(self) -> str:
        return f"AST(tok = {self.Token})"



    def __str__(self) -> str:
        return f"AST {self.Token}"