#
# Product:   Macal
# Author:    Marco Caspers
# Date:      15-09-2022
#

from __future__ import annotations
import typing
from . import variable
from . import ast
from . import token
from . import ast_function_definition


class Scope:
    def __init__(self, name: str) -> None:
        self.Name: str = name
        self.Parent: Scope = None
        self.Root: Scope = None
        self.Variables: typing.Dict[str, variable.Variable] = {}
        self.Functions: typing.Dict[str, ast_function_definition.FunctionDefinition] = {}
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



    def CreateTempScope(self, name: str) -> Scope:
        name = f'{self.Name}{name}'
        tempScope = Scope(name)
        tempScope.Root = self.Root
        tempScope.includeFolder = self.includeFolder
        tempScope.externFolder = self.externFolder
        tempScope.isLoop = self.isLoop
        tempScope.Parent = self
        return tempScope



    def FindInclude(self, name: str) -> Scope:
        for include in self.Includes:
            if include.Name == name:
                return include
        if self.Parent != None:
            return self.Parent.FindInclude(name)
        return None



    def FindFunction(self, name: str, scope: Scope) -> ast_function_definition.FunctionDefinition:
        if name in scope.Functions:
            return scope.Functions[name]
        for incl in scope.Includes:
            fn = incl.FindFunction(name, incl)
            if fn is not None:
                return fn
        if scope.Parent is not None:
            return self.FindFunction(name, scope.Parent)
        return None



    @staticmethod
    def NewVariable(tok: token.LexToken, name: str) -> variable.Variable:
        return variable.Variable(tok, name)



    def AddVariable(self, var: variable.Variable):
        self.Variables[var.Name] = var


    
    def GetVariable(self, name: str) -> variable.Variable:
        if name in self.Variables:
            return self.Variables[name]
        return None



    def FindVariableInIncludes(self, name: str) -> variable.Variable:
        for incl in self.Includes:
            var = incl.FindVariable(name)
            if var is not None: return var
        if self.Parent is not None:
            return self.Parent.FindVariableInIncludes(name)
        return None


    def FindVariable(self, name: str) -> variable.Variable:
        var = self.GetVariable(name)
        if var is None:
            var = self.FindVariableInIncludes(name)
        if var is None and self.Parent is not None and not self.isFunction:
            var = self.Parent.FindVariable(name)
        return var



    def CreateAndAppendFunctionReturnVariable(self, tok: token.LexToken) -> variable.Variable:
        returnVar = self.NewVariable(tok, f'?return_var{self.Name}')
        self.Variables[returnVar.Name] = returnVar
        return returnVar



    def GetFunctionReturnVariable(self) -> variable.Variable:
        return self.Variables[f'?return_var{self.Name}']



    def SetReturnValue(self, value: typing.Any) -> None:
        var = self.GetFunctionReturnVariable()
        var.SetValue(value)



    def SetHalt(self, value: bool) -> None:
        self.Halt = value
        if self.Parent is not None:
            self.Parent.SetHalt(value)



    def __repr__(self) -> str:
        return f'Scope(Name="{self.Name}");'