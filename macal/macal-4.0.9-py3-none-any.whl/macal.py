#
# Product:   Macal
# Author:    Marco Caspers
# Date:      15-09-2022
#

from __future__ import annotations
import os
import pathlib
import pkg_resources
import typing
from . import mscope
from . import lexer
from . import parser
from . import interpreter
from . import exceptions
from . import types
from . import variable
from . import value_item
from . import ast_function_definition
from . import token
from . import location


class Macal:
    def __init__(self, debugParser: bool = False) -> Macal:
        self.debug: bool = True
        self.debugParser: bool = debugParser
        self.scriptExtension: str = 'mcl'
        self.Root: mscope.Scope = mscope.Scope('root')
        self.Root.Root = self.Root
        self.exitcode: variable.Variable = self.registerVariable("exitcode", 0)
        self.filePath: str = None
        fn = self.__registerEmbeddedFunction('getInfiniteLoopProtectionCount', self.Root)
        fn.registerArgument(None)
        fn = self.__registerEmbeddedFunction('setInfiniteLoopProtectionCount', self.Root)
        fn.registerArgument('count')


       
    def registerVariable(self, name: str, value: typing.Any) -> variable.Variable:
        tok = token.LexToken(name, types.LexTokenTypes.Identifier, location.nullLoc(), -1)
        var = variable.Variable(tok, name)
        tok = token.LexToken('?registered_var_value?', types.LexTokenTypes.Identifier, location.nullLoc(), -1)
        var.Value = value_item.ValueItem().setFromPython(tok, value)
        self.Root.addVariable(var)
        return var



    def __registerEmbeddedFunction(self, name: str, scope: mscope.Scope) -> ast_function_definition.FunctionDefinition:
        func = ast_function_definition.FunctionDefinition(
            token.LexToken(name, types.LexTokenTypes.Identifier, 
            location.SourceLocation(-1, -1), 
            -1))
        func.IsExternal = True
        scope.Functions.append(func)
        return func



    def __loadFile(self, filename: str) -> str:
        if os.path.exists(filename):
            with open (filename, mode = 'r', encoding = 'utf-8') as text_file:
                source = text_file.read()
            return source
        return None



    def _findIncludeFileName(self, include: str, scope: mscope.Scope) -> str:
        filename = f'{include}.{self.scriptExtension}'
        #first have a look in the package.
        path = pkg_resources.resource_filename(__name__, f'Library/{filename}')
        if pathlib.Path(path).is_file():
            return path
        path = os.path.join(scope.includeFolder, filename)
        if pathlib.Path(path).is_file():
            return path
        path = os.path.join(pathlib.Path(self.filePath).parent, filename)
        if pathlib.Path(path).is_file():
            return path
        return None



    def _RunInclude(self, filename: str, scope: mscope.Scope, iscope: mscope.Scope)-> typing.Tuple[bool, str]:
        incl = Macal()
        incl.Root = iscope
        (r, _) = incl.Run(filename)
        if r:
            scope.Includes.append(iscope)
        return (r, None)



    def _Include(self, include: str, scope: mscope.Scope) -> typing.Tuple[bool, str]:
        iscope = scope.createTempScope(include)
        iscope.Root = iscope  # we are our own root
        iscope.Parent = None
        iscope.Name = include # overwrite the name! We don't want it to be called as a regular child scope
        filename = self._findIncludeFileName(include, scope)
        debug = True
        if filename is None:
            return (False, f'File not found ({include}).')
        if debug:
            return self._RunInclude(filename, scope, iscope)
        try:
            return self._RunInclude(filename, scope, iscope)
        except Exception as ex:
            return (False, ex)
        


    def _Execute(self, source: str, filename: str, root: mscope.Scope, exitcode: variable.Variable) -> typing.Tuple[bool, mscope.Scope]:
        root.Source = source
        lex = lexer.Lexer()
        root.Tokens = lex.Lex(root.Source, filename)
        parse = parser.Parser()
        parse.Debug = self.debugParser
        root.AST = parse.Parse(root.Tokens, filename)
        intrprt = interpreter.Interpreter(self._Include)
        exitcode.setValue(0)
        return (True, intrprt.Interpret(root.AST, filename, root))



    def Run(self, filename: str)-> typing.Tuple[bool, mscope.Scope]:
        self.filePath = filename
        source = self.__loadFile(filename)
        if source is None:
            print("Failed to load file (", filename, ").")
            return (False, None)
        if self.debug:
            return self._Execute(source, filename, self.Root, self.exitcode)
        try:
            return self._Execute(source, filename, self.Root, self.exitcode)
        except exceptions.LexError as ex:
            self.exitcode.setValue(1)
            print(ex)
        except exceptions.ParserError as ex:
            self.exitcode.setValue(2)
            print(ex)
        except exceptions.RuntimeError as ex:
            self.exitcode.setValue(3)
            print(ex)
        return (False, self.Root)




