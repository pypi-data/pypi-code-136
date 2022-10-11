#
# Product:   Macal
# Author:    Marco Caspers
# Date:      13-09-2022
#

from . import ast
from . import token
from . import types
from . import exceptions

class SelectField(ast.AST):
    '''Contains the location in the source code.'''
    def __init__(self, tok: token.LexToken) -> None:
        super().__init__(tok, types.AstTypes.SelectField)
        self.__dict__['Name'] = tok.Lexeme
        self.__dict__['As'] = None
        self.__dict__['AsName'] = None



    def __repr__(self):
        return f'SelectField(tok={self.Token})'



    def __str__(self):
        sa = f' as {self.AsName}' if self.As is not None else ''
        return f'{self.Name}{sa}'



    def __setattr__(self, name, value):
        if name == 'Token':
            self.__dict__['Name'] = value.Lexeme
            self.__dict__['Token'] = value
            return
        if name == 'As':
            self.__dict__['AsName'] = value.Lexeme
            self.__dict__['As'] = value
            return
        if name == 'Type':
            self.__dict__['Type'] = value
            return
        if name == 'Name' or name == 'AsName':
            raise exceptions.ParserError(message = f'{name} is read-only.', loc = self.Token.Location ,filename = None)
        raise exceptions.ParserError(message = f'Attribute {name} does not exist in SelectField.', loc = self.Token.Location ,filename = None)