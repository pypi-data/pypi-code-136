#
# Product:   Macal
# Author:    Marco Caspers
#
# Description:
#

from __future__ import annotations
import typing
import copy
from . import token
from . import types
from . import exceptions
from . import ast_function_definition
from . import variable

class ValueItem:
    def __init__(self) -> ValueItem:
        self.Value: typing.Any = None
        self.Type: types.VariableType = None
        self.Token: token.LexToken = token.LexToken.nullToken()


    # value is still a python value.
    def SetFromMacal(self, tok: token.LexToken, type: types.VariableType, value: typing.Any) -> ValueItem:
        if tok is None:
            tok = token.LexToken.nullToken()
        self.Type = type
        self.Token = tok
        self.Value = value
        return self



    def SetFromPython(self, tok: token.LexToken, value: typing.Any) -> ValueItem:
        if tok is None:
            tok = token.LexToken.nullToken()
        self.Type = self.GetTypeFromPythonValue(value)
        self.Token = tok
        self.Value = self.FromPython(value).Value
        return self
   


    def GetTypeFromPythonValue(self, value: typing.Any) -> types.VariableType:
        if value is None:
            return types.VariableTypes.Nil
        elif isinstance(value, str):
            return types.VariableTypes.String
        elif isinstance(value, int):
            return types.VariableTypes.Int
        elif isinstance(value, float):
            return types.VariableTypes.Float
        elif isinstance(value, bool):
            return types.VariableTypes.Bool
        elif isinstance(value, list):
            return types.VariableTypes.Array
        elif isinstance(value, dict):
            return types.VariableTypes.Record
        # this one is here for set return value from an external library.
        elif isinstance(value, variable.Variable):
            return types.VariableTypes.Variable
        # this one is here for set return value from an external library.
        elif isinstance(value, ast_function_definition.FunctionDefinition):
            return types.VariableTypes.Function
        else:
            raise exceptions.RuntimeError(f"getTypeFromPythonValue() for type {type(value)} Not implemented.", self.Token.Location, None)



    def FromPython(self, val: typing.Any):
        if val is None:
            ret = ValueItem()
            ret.Token = self.Token
            ret.Type = types.VariableTypes.Nil
            ret.Value = types.VariableTypes.Nil
            return ret
        elif isinstance(val, str):
            ret = ValueItem()
            ret.Token = self.Token
            ret.Type = types.VariableTypes.String
            ret.Value = val
            return ret
        elif isinstance(val, int):
            ret = ValueItem()
            ret.Token = self.Token
            ret.Type = types.VariableTypes.Int
            ret.Value = val
            return ret
        elif isinstance(val, float):
            ret = ValueItem()
            ret.Token = self.Token
            ret.Type = types.VariableTypes.Float
            ret.Value = val
            return ret
        elif isinstance(val, bool):
            ret = ValueItem()
            ret.Token = self.Token
            ret.Type = types.VariableTypes.Bool
            ret.Value = val
            return ret
        elif isinstance(val, dict):
            return self.__fromPythonDict(val)
        elif isinstance(val, list):
            return self.__fromPythonList(val)
        # this one is here for set return value from an external library.
        elif isinstance(val, variable.Variable):
            return val
        # this one is here for set return value from an external library.
        elif isinstance(val, ast_function_definition.FunctionDefinition):
            return val
        elif isinstance(val, ValueItem):
            print("Debug: ValueItem.fromPython(value) value is ValueItem, this is a bug that should be fix, take notes!")
            ret = val.Clone()
        else:
            raise exceptions.RuntimeError(f"setValue() for type {type(val)} Not implemented.", self.Token.Location, None)



    def __fromPythonList(self, val: list) -> ValueItem:
        res = []
        for v in val:
            res.append(self.FromPython(v))
        ret = ValueItem()
        ret.Token = self.Token
        ret.Type = types.VariableTypes.Array
        ret.Value = res
        return ret



    def __fromPythonDict(self, val: dict) -> ValueItem:
        res = {}
        for (k, v) in val.items():
            res[k] = self.FromPython(v)
        ret = ValueItem()
        ret.Token = self.Token
        ret.Type = types.VariableTypes.Record
        ret.Value = res
        return ret



    def SetValue(self, tok: token.LexToken, type: types.VariableType, filename: str) -> None:
        self.Token = tok
        self.Type = type
        if self.Type == types.VariableTypes.Int:
            self.Value = int(tok.Lexeme)
        elif self.Type == types.VariableTypes.Float:
            self.Value = float(tok.Lexeme)
        elif self.Type == types.VariableTypes.Bool:
            self.Value = tok.Lexeme == 'true'
        elif self.Type == types.VariableTypes.String:
            self.Value = tok.Lexeme
        elif self.Type == types.VariableTypes.Array:
            self.Value = tok.Lexeme
        elif self.Type == types.VariableTypes.Record:
            self.Value = tok.Lexeme
        elif self.Type == types.VariableTypes.Nil:
            self.Value = 'nil'
        else:
            raise exceptions.RuntimeError(f"Invalid value type ({self.Type}).", tok.Location, filename)



    def __repr__(self) -> str:
        return f'ValueItem(token={self.Token}, value={self.Value}, type={self.Type});'



    def __eq__(self, other: ValueItem) -> ValueItem:
        if not isinstance(other, ValueItem):
            raise exceptions.RuntimeError(f'EQ: Other is not a ValueItem ({type(other)}) self: {self} other: {other}', None, None)
        res = ValueItem()
        res.Type = types.VariableTypes.Bool
        res.Token = self.Token.Clone()
        res.Value = self.Value == other.Value
        res.Token.Lexeme = 'true' if res.Value else 'false'
        res.Token.Type = types.LexTokenTypes.Identifier
        return res


    
    def __add__(self, other) -> ValueItem:
        if not isinstance(other, ValueItem):
            raise exceptions.RuntimeError(f'ADD: Other is not a ValueItem ({type(other)}) self: {self} other: {other}', None, None)
        res = ValueItem().SetFromMacal(self.Token.Clone(), 
            types.VariableTypes.Float if self.Type == types.VariableTypes.Int and other.Type == types.VariableTypes.Float else self.Type,
            self.Value + other.Value)
        res.Token.Lexeme = f'{res.Value}'
        return res



    def __sub__(self, other: ValueItem):
        if not isinstance(other, ValueItem):
            raise exceptions.RuntimeError(f'SUB: Other is not a ValueItem ({type(other)}) self: {self} other: {other}', None, None)
        res = ValueItem().SetFromMacal(self.Token.Clone(), 
            types.VariableTypes.Float if self.Type == types.VariableTypes.Int and other.Type == types.VariableTypes.Float else self.Type,
            self.Value - other.Value)
        res.Token.Lexeme = f'{res.Value}'
        return res



    def __mul__(self, other: ValueItem) -> ValueItem:
        if not isinstance(other, ValueItem):
            raise exceptions.RuntimeError(f'MUL: Other is not a ValueItem ({type(other)}) self: {self} other: {other}', None, None)
        res = ValueItem()
        res = ValueItem().SetFromMacal(self.Token.Clone(), 
            types.VariableTypes.Float if self.Type == types.VariableTypes.Int and other.Type == types.VariableTypes.Float else self.Type,
            self.Value * other.Value)
        res.Token.Lexeme = f'{res.Value}'
        return res



    def __pow__(self, other: ValueItem) -> ValueItem:
        if not isinstance(other, ValueItem):
            raise exceptions.RuntimeError(f'POW: Other is not a ValueItem ({type(other)}) self: {self} other: {other}', None, None)
        res = ValueItem()
        res = ValueItem().SetFromMacal(self.Token.Clone(), 
            types.VariableTypes.Float if self.Type == types.VariableTypes.Int and other.Type == types.VariableTypes.Float else self.Type,
            self.Value ** other.Value)
        res.Token.Lexeme = f'{res.Value}'
        return res



    def __mod__(self, other: ValueItem) -> ValueItem:
        if not isinstance(other, ValueItem):
            raise exceptions.RuntimeError(f'MOD: Other is not a ValueItem ({type(other)}) self: {self} other: {other}', None, None)
        if other.Value == 0 or other.Value == 0.0:
            raise exceptions.RuntimeError(f"Division by zero.", other.Token.Location, None)
        res = ValueItem()
        res = ValueItem().SetFromMacal(self.Token.Clone(), 
            types.VariableTypes.Int,
            self.Value % other.Value)
        res.Token.Lexeme = f'{res.Value}'
        return res



    def __truediv__(self, other: ValueItem) -> ValueItem:
        if not isinstance(other, ValueItem):
            raise exceptions.RuntimeError(f'DIV: Other is not a ValueItem ({type(other)}) self: {self} other: {other}', None, None)
        if other.Value == 0 or other.Value == 0.0:
            raise exceptions.RuntimeError(f"Division by zero.", other.Token.Location, None)
        res = ValueItem().SetFromMacal(self.Token.Clone(), types.VariableTypes.Float, self.Value / other.Value)
        res.Token.Lexeme = f'{res.Value}'
        return res



    def __gt__(self, other: ValueItem) -> ValueItem:
        if not isinstance(other, ValueItem):
            raise exceptions.RuntimeError(f'GT: Other is not a ValueItem ({type(other)}) self: {self} other: {other}', None, None)
        res = ValueItem().SetFromMacal(self.Token.Clone(), types.VariableTypes.Bool, self.Value > other.Value)
        res.Token.Lexeme = 'true' if res.Value else 'false'
        res.Token.Type = types.LexTokenTypes.Identifier
        return res
    


    def __lt__(self, other: ValueItem) -> ValueItem:
        if not isinstance(other, ValueItem):
            raise exceptions.RuntimeError(f'LT: Other is not a ValueItem ({type(other)}) self: {self} other: {other}', None, None)
        res = ValueItem().SetFromMacal(self.Token.Clone(), types.VariableTypes.Bool, self.Value < other.Value)
        res.Token.Lexeme = 'true' if res.Value else 'false'
        res.Token.Type = types.LexTokenTypes.Identifier
        return res


    
    def __ge__(self, other: ValueItem) -> ValueItem:
        if not isinstance(other, ValueItem):
            raise exceptions.RuntimeError(f'GTE: Other is not a ValueItem ({type(other)}) self: {self} other: {other}', None, None)
        res = ValueItem().SetFromMacal(self.Token.Clone(), types.VariableTypes.Bool, self.Value >= other.Value)
        res.Token.Lexeme = 'true' if res.Value else 'false'
        res.Token.Type = types.LexTokenTypes.Identifier
        return res



    def __le__(self, other: ValueItem) -> ValueItem:
        if not isinstance(other, ValueItem):
            raise exceptions.RuntimeError(f'LTE: Other is not a ValueItem ({type(other)}) self: {self} other: {other}', None, None)
        res = ValueItem().SetFromMacal(self.Token.Clone(), types.VariableTypes.Bool, self.Value <= other.Value)
        res.Token.Lexeme = 'true' if res.Value else 'false'
        res.Token.Type = types.LexTokenTypes.Identifier
        return res



    def __ne__(self, other: ValueItem) -> ValueItem:
        if not isinstance(other, ValueItem):
            raise exceptions.RuntimeError(f'NE: Other is not a ValueItem ({type(other)}) self: {self} other: {other}', None, None)
        res = ValueItem().SetFromMacal(self.Token.Clone(), types.VariableTypes.Bool, self.Value != other.Value)
        res.Token.Lexeme = 'true' if res.Value else 'false'
        res.Token.Type = types.LexTokenTypes.Identifier
        return res



    def __and__(self, other: ValueItem) -> ValueItem:
        if not isinstance(other, ValueItem):
            raise exceptions.RuntimeError(f'AND: Other is not a ValueItem ({type(other)}) self: {self} other: {other}', None, None)
        res = ValueItem().SetFromMacal(self.Token.Clone(), types.VariableTypes.Bool, self.Value and other.Value)
        res.Token.Lexeme = 'true' if res.Value else 'false'
        res.Token.Type = types.LexTokenTypes.Identifier
        return res



    def __or__(self, other: ValueItem) -> ValueItem:
        if not isinstance(other, ValueItem):
            raise exceptions.RuntimeError(f'OR: Other is not a ValueItem ({type(other)}) self: {self} other: {other}', None, None)
        res = ValueItem().SetFromMacal(self.Token.Clone(), types.VariableTypes.Bool, self.Value or other.Value)
        res.Token.Lexeme = 'true' if res.Value else 'false'
        res.Token.Type = types.LexTokenTypes.Identifier
        return res


    
    def Clone(self) -> ValueItem:
        return copy.deepcopy(self)


    def __str__(self) -> str:
        res = f'ValueItem(token={self.Token}, type={self.Type}, value='
        if self.Type == types.VariableTypes.Array:
            if not isinstance(self.Value, list):
                 raise exceptions.RuntimeError(f'self.Type is Array, but self.Value is not. ({type(self.Value)} (self: {self.Value}))', self.Token.Location, None)
            res = f'{res}[\n'
            for v in self.Value:
                res = f'{res}    {v}\n'
            res = f'{res}]);'
        elif self.Type == types.VariableTypes.Record:
            if not isinstance(self.Value, dict):
                 raise exceptions.RuntimeError(f'self.Type is Record, but self.Value is not. ({type(self.Value)} (self.Value: {self.Value}))', self.Token.Location, None)
            res = f'{res}{{\n'
            for (k,v) in self.Value.items():
                res = f'{res}    "{k}":{v}\n'
            res = f'{res}}});'
        else:
            res = f'{res}{self.Value});'
        return res
