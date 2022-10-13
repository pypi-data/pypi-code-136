#
# Product:   Macal
# Author:    Marco Caspers
# Date:      07-09-2022
#



import copy
from . import types
from . import location



class LexToken:
    """Lexer token"""
    def __init__(self, lexeme: str, type: types.LexTokenType, loc: location.SourceLocation, index: int):
        self.Lexeme:   str = lexeme
        self.Type:     types.LexTokenType = type
        self.Location: location.SourceLocation = loc
        self.Start:    int = index



    def __repr__(self):
        s = self.Lexeme
        if isinstance(self.Lexeme, str):
            s = s.replace('\n','')
            s = s.replace('\t', '    ')
        return f"LexToken(Lexeme='{s}', Type='{self.Type}', Location={self.Location}, Start = {self.Start}"



    def __str__(self):
        s = self.Lexeme
        if isinstance(self.Lexeme, str):
            s = s.replace('\n','')
            s = s.replace('\t', '    ')
        t = f'{self.Type}, ' if self.Type is not None else ''
        l = f', {self.Location}' if self.Location is not None else ''
        a = f', {self.Start}' if self.Start >= 0 else ''
        return f"{t}'{s}'{l}{a}"



    def Clone(self):
        return copy.deepcopy(self)
    
    @staticmethod
    def nullToken():
        return LexToken("Nil", types.LexTokenTypes.Nil, location.nullLoc(), -1)