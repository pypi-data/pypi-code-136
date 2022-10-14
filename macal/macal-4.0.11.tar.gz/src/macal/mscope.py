#
# Product:   Macal
# Author:    Marco Caspers
# Date:      15-09-2022
#

from __future__ import annotations
import typing
from . import types
from . import exceptions
from . import variable
from . import ast
from . import token
from . import ast_function_definition


class Scope:
    def __init__(self, name: str) -> Scope:
        self.Name: str = name
        self.Parent = None
        self.Root = None
        self.Variables: typing.List[variable.Variable] = []
        self.Functions: typing.List[ast_function_definition.FunctionDefinition] = []
        self.Includes: typing.List[Scope] = []
        self.includeFolder: str = '/Library'
        self.externFolder: str = '/Library/Extern'
        self.isLoop: bool = False
        self.isLoopRoot = False
        self.isFunction: bool = False
        self.Break: bool = False
        self.Halt: bool = False
        self.Continue: bool = False
        self.Return: bool = False
        self.Source: str = None
        self.Tokens: typing.List[token.LexToken] = None
        self.AST: typing.List[ast.AST] = None
        self.iter = 0
        self.RunFunction: typing.Callable = None



    def createTempScope(self, name: str) -> Scope:
        name = f'{self.Name}{name}'
        tempScope = Scope(name)
        tempScope.Root = self.Root
        tempScope.includeFolder = self.includeFolder
        tempScope.externFolder = self.externFolder
        tempScope.isLoop = self.isLoop
        tempScope.Parent = self
        return tempScope



    def findInclude(self, name: str) -> Scope:
        for include in self.Includes:
            if include.Name == name:
                return include
        if self.Parent != None:
            return self.Parent.findInclude(name)
        return None



    def findFunction(self, name: str, scope: Scope) -> ast_function_definition.FunctionDefinition:
        for fn in scope.Functions:
            if fn.Name == name:
                return fn
        for incl in scope.Includes:
            fn = incl.findFunction(name, incl)
            if fn is not None:
                return fn
        if scope.Parent is not None:
            return self.findFunction(name, scope.Parent)
        return None



    @staticmethod
    def newVariable(tok: token.LexToken, name: str) -> variable.Variable:
        return variable.Variable(tok, name)



    def addVariable(self, var: variable.Variable):
        self.Variables.append(var)


    
    def getVariable(self, name: str) -> variable.Variable:
        for var in self.Variables:
            if var.Name == name:
                return var
        return None



    def findVariableInIncludes(self, name: str) -> variable.Variable:
        for incl in self.Includes:
            var = incl.findVariable(name)
            if var is not None: return var
        if self.Parent is not None:
            return self.Parent.findVariableInIncludes(name)



    def findVariable(self, name: str) -> variable.Variable:
        var = self.getVariable(name)
        if var is None:
            var = self.findVariableInIncludes(name)
        if var is None and self.Parent is not None and not self.isFunction:
            var = self.Parent.findVariable(name)
        return var



    def createAndAppendFunctionReturnVariable(self, tok: token.LexToken) -> variable.Variable:
        returnVar = self.newVariable(tok, f'?return_var{self.Name}')
        self.Variables.append(returnVar)
        return returnVar



    def getFunctionReturnVariable(self) -> variable.Variable:
        return self.getVariable(f'?return_var{self.Name}')



    def setReturnValue(self, value: typing.Any) -> None:
        var = self.getFunctionReturnVariable()
        var.setValue(value)



    def setHalt(self, value: bool) -> None:
        self.Halt = value
        if self.Parent is not None:
            self.Parent.setHalt(value)



    def __repr__(self) -> str:
        return f'Scope(Name="{self.Name}");'

        if tok.Type == types.LexTokenTypes.String:
            return types.VariableTypes.String
        if tok.Type == types.LexTokenTypes.Number:
            if tok.Lexeme.contains('.'):
                return types.VariableTypes.Float
            return types.VariableTypes.Int
        if tok.Type == types.LexTokenTypes.Identifier and (tok.Lexeme == 'false' or tok.Lexeme == 'true'):
            return types.VariableTypes.Bool
        if tok.Type == types.LexTokenTypes.Identifier and tok.Lexeme == 'nil':
            return types.VariableTypes.Nil
        if isinstance(tok.Lexeme, list):
            return types.VariableTypes.Array
        if isinstance(tok.Lexeme, dict):
            return types.VariableTypes.Record
        raise exceptions.RuntimeError(f"Invalid token type: {tok.Type}.", tok.Location, filename)