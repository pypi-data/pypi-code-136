#
# Product:   Macal
# Author:    Marco Caspers
# Date:      07-09-2022
#

from . import location

class LexError(Exception):
    """Exception that is thrown in the lexer if something bad happened."""
    def __init__(self, message: str, loc: location.SourceLocation, filename: str) -> None:
        self.Message = message
        self.Location = loc
        self.Filename = filename



    def __repr__(self) -> str:
        return f"LexError(message='{self.Message}', loc={self.Location}, filename='{self.Filename}')"



    def __str__(self) -> str:
        return f"Lex Error: {self.Message} {self.Location} , in: {self.Filename}"



class ParserError(Exception):
    """Exception that is thrown in the parser if something bad happened."""
    def __init__(self, message: str, loc: location.SourceLocation, filename: str) -> None:
        self.Message = message
        self.Location = loc
        self.Filename = filename



    def __repr__(self) -> str:
        return f"ParserError(message='{self.Message}', loc={self.Location}, filename='{self.Filename}')"



    def __str__(self) -> str:
        return f"Parser Error: {self.Message} {self.Location} , in: {self.Filename}"



class RuntimeError(Exception):
    """Exception that is thrown in the interpreter if something bad happened."""
    def __init__(self, message: str, loc: location.SourceLocation, filename: str) -> None:
        self.Message = message
        self.Location = loc
        self.Filename = filename



    def __repr__(self) -> str:
        return f"RuntimeError(message='{self.Message}', loc={self.Location}, filename='{self.Filename}')"



    def __str__(self) -> str:
        l = f' {self.Location}' if self.Location is not None else ''
        f = f', in: {self.Filename}' if self.Filename is not None else ''
        return f"Runtime Error: {self.Message}{l}{f}"
