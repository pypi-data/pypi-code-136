#
# Product:   Macal
# Author:    Marco Caspers
# Date:      15-09-2022
#


import typing
import pkg_resources
import pathlib
import sys
import os


from . import __about__
from . import token
from . import ast
from . import ast_expr
from . import ast_function_definition
from . import ast_function_call
from . import ast_block
from . import ast_assignment
from . import ast_if
from . import ast_foreach
from . import ast_break
from . import ast_continue
from . import ast_halt
from . import ast_while
from . import ast_return
from . import ast_include
from . import ast_select_field
from . import ast_select
from . import mscope
from . import types
from . import exceptions
from . import value_item
from . import variable
from . import location



def validateFunctionArguments(func: ast_function_definition.FunctionDefinition, scope: mscope.Scope, filename: str) -> None:
    for arg in func.Arguments.Left:
        if arg.ExprType == types.ExprTypes.FunctionArgument:
            name = arg.Left.Lexeme
        else:
            name = arg.Token.Lexeme
        var = scope.findVariable(name)
        if var is None:
            if arg.Token.Lexeme == 'params': return
            raise exceptions.RuntimeError(f'Function argument {arg.Token.Lexeme} not found.', arg.Token.Location, filename)
        if arg.ExprType == types.ExprTypes.FunctionArgument:
            t = var.getType().lower()
            if arg.Token.Lexeme != 'any' and arg.Token.Lexeme != 'params' and arg.Token.Lexeme != t:
                raise exceptions.RuntimeError(f'Invalid function argument type {t}, {arg.Token.Lexeme} type was required.', arg.Token.Location, filename)


        
class Interpreter:
    def __init__(self, include: typing.Callable[[str, mscope.Scope], mscope.Scope]) -> None:
        self.filename: str = None
        self.Include: typing.Callable[[str, mscope.Scope], mscope.Scope] = include
        self.Halt: bool = False
        self.Source: str = None
        self.iter: int = 0
        self.INFINITE_LOOP_PROTECTION_COUNT: int = 25000 # limits a while loop to 25000 repeats before it gets terminated.



    def Interpret(self, source: typing.List[ast.AST], filename: str, scope: mscope.Scope) -> mscope.Scope:
        self.filename = filename
        scope.setHalt(False)
        self.Source = source
        for instruction in source:
            self.interpretInstruction(instruction, scope)
            if scope.Halt:
                return scope
        return scope



    def interpretInstruction(self, instruction: ast.AST, scope):
        if instruction.Type == types.AstTypes.Assignment:
            return self.interpretAssign(instruction, scope)
        if instruction.Type == types.AstTypes.Block:
            return self.interpretBlock(instruction, scope)
        if instruction.Type == types.AstTypes.Break:
            return self.interpretBreak(instruction, scope)
        if instruction.Type == types.AstTypes.Continue:
            return self.interpretContinue(instruction, scope)
        if instruction.Type == types.AstTypes.FunctionCall:
            return self.runFunctionCall(instruction.Name, instruction.Args, instruction.Token, scope)
        if instruction.Type == types.AstTypes.FunctionDefinition:
            return self.interpretFunctionDefinition(instruction, scope)
        if instruction.Type == types.AstTypes.If:
            return self.interpretIf(instruction, scope)
        if instruction.Type == types.AstTypes.Include:
            return self.interpretInclude(instruction, scope)
        if instruction.Type == types.AstTypes.Foreach:
            return self.interpretForeach(instruction, scope)
        if instruction.Type == types.AstTypes.Halt:
            return self.interpretHalt(instruction, scope)
        if instruction.Type == types.AstTypes.Return:
            return self.interpretReturn(instruction, scope)
        if instruction.Type == types.AstTypes.Select:
            return self.interpretSelect(instruction, scope)
        if instruction.Type == types.AstTypes.While:
            return self.interpretWhile(instruction, scope)
        raise exceptions.RuntimeError(f"Invalid instruction type ({instruction.Type}).", instruction.Token.Location, self.filename)



    def interpretInclude(self, instruction: ast_include.Include, scope: mscope.Scope) -> None:
        for include in instruction.Includes:
            incl = scope.findInclude(include.Lexeme)
            if incl is not None: # already included
                continue
            (result, ex) = self.Include(include.Lexeme, scope)
            var = scope.Root.getVariable('exitcode')
            if not result and ex is not None:
                var.setValue(4)
                raise exceptions.RuntimeError(ex, instruction.Token.Location, self.filename)
            elif not result:
                var.setValue(5)
                self.Halt = True



    def interpretFunctionDefinition(self, instruction: ast.AST, scope: mscope.Scope):
        scope.Functions.append(instruction)



    def interpretAssignToIndexedVar(self, var: variable.Variable, idx: ast_expr.Expr, value: value_item.ValueItem, scope: mscope.Scope):
        expr = idx
        vind = []
        while expr.ExprType != types.ExprTypes.VariableIndexStart:
            vind.insert(0, expr.Right)
            expr = expr.Left
        val = var.Value
        if val.Type not in [types.VariableTypes.Array, types.VariableTypes.Record, types.VariableTypes.String]:
            raise exceptions.RuntimeError(f'Type error, index not supported on {val.Type}', ind.Token.Location, self.filename)    
        lng = len(vind)
        cnt = 0
        for ind in vind:
            if val.Type not in [types.VariableTypes.Array, types.VariableTypes.Record, types.VariableTypes.String]:
                raise exceptions.RuntimeError(f'Type error, index not supported on {val.Type}', ind.Token.Location, self.filename)    
            if ind.ExprType == types.ExprTypes.NewArrayIndex:
                if val.Type != types.VariableTypes.Array:
                    raise exceptions.RuntimeError(f'Type error, append not supported on {val.Type}', ind.Token.Location, self.filename)    
                val.Value.append(value)
                return
            i = self.interpretExpression(ind, scope)
            if val.Type == types.VariableTypes.Record:
                if i.Value not in val.Value:
                    if cnt == lng -1:
                        val.Value[i.Value] = value
                        return
                    else:
                        raise exceptions.RuntimeError(f'Index ({i.Value}) not found.', ind.Token.Location, self.filename)
            elif val.Type == types.VariableTypes.Array or val.Type == types.VariableTypes.String:
                if i.Type != types.VariableTypes.Int:
                    raise exceptions.RuntimeError(f'Invalid index type ({i.Type}), Int index type required.', ind.Token.Location, self.filename)
                if i.Value < 0 or i.Value >= len(val.Value):
                    raise exceptions.RuntimeError(f'Index ({i.Value}) is out of range.', ind.Token.Location, self.filename)
            val = val.Value[i.Value]
            cnt+=1
        if expr.Right.ExprType == types.ExprTypes.NewArrayIndex:
            if val.Type != types.VariableTypes.Array:
                raise exceptions.RuntimeError(f'Type error, append not supported on {val.Type}', ind.Token.Location, self.filename)    
            val.Value.append(value)
        else:
            val.Value = value



    def interpretAssign(self, instruction: ast_assignment.Assignment, scope: mscope.Scope) -> None:
        var = scope.findVariable(instruction.Variable)
        if var is None:
            var = scope.newVariable(instruction.Token, instruction.Variable)
            var.isConst = instruction.isConst
            scope.addVariable(var)
        elif var.isConst:
            raise exceptions.RuntimeError(f'Illegal assignment to a constant ({instruction.Variable}).', instruction.Token.Location, self.filename)
        value = self.interpretExpression(instruction.Value, scope)
        if instruction.VarIndex is not None:
            return self.interpretAssignToIndexedVar(var, instruction.VarIndex, value, scope)
        if instruction.Operator.Lexeme == '=':
            var.Value = value.clone()
        elif instruction.Operator.Lexeme == '+=':
            var.Value = var.Value + value
        elif instruction.Operator.Lexeme == '-=':
            var.Value = var.Value - value
        elif instruction.Operator.Lexeme == '/=':
            var.Value = var.Value / value
        elif instruction.Operator.Lexeme == '*=':
            var.Value = var.Value * value
        else:
            raise exceptions.RuntimeError(message = f'Invalid instruction assign operator: {instruction.Operator.Lexeme}', location=instruction.Token.Location, filename=self.filename)



    def interpretExpression(self, expr: ast.AST, scope: mscope.Scope) -> value_item.ValueItem:
        if expr is None:
            raise exceptions.RuntimeError("Invalid argument exception, expr is None.", None, self.filename)
        if expr.ExprType == types.ExprTypes.Literal:
            return self.interpretLiteralExpression(expr, scope)
        if expr.ExprType == types.ExprTypes.Binary:
            return self.interpretBinaryExpression(expr, scope)
        if expr.ExprType == types.ExprTypes.Unary:
            return self.interpretUnaryExpression(expr, scope)
        if expr.ExprType == types.ExprTypes.Grouping:
            return self.interpretGroupingExpression(expr, scope)
        if expr.ExprType == types.ExprTypes.FunctionCall:
            return self.runFunctionCall(expr.Token.Lexeme, expr.Right.Left, expr.Right.Token, scope)
        if expr.ExprType == types.ExprTypes.FunctionArgument:
            raise exceptions.RuntimeError("Function Argument type should not end up in expression interpretation.", expr.Token.Location, self.filename)
        if expr.ExprType == types.ExprTypes.ArgumentList:
            raise exceptions.RuntimeError("Argument list type should not end up in expression interpretation.", expr.Token.Location, self.filename)
        if expr.ExprType == types.ExprTypes.Variable:
            return self.interpretVariableExpression(expr, scope)
        if expr.ExprType == types.ExprTypes.VariableIndex:
            return self.interpretLiteralExpression(expr.Left, scope)
        if expr.ExprType == types.ExprTypes.InterpolationPart:
            return self.interpretBinaryExpression(expr.Right, scope)
        raise Exception("Expression type evaluation not implemented yet: ", expr.ExprType)



    def typeCheck(self, left:value_item.ValueItem, right:value_item.ValueItem, operator:str):
        if left is None or right is None: return
        # This is for debugging, there's still bugs floating around that make it that the ValueItem arguments that are supposed to enter this function aren't actually of type ValueItem.
        if not isinstance(left, value_item.ValueItem):
            raise exceptions.RuntimeError(f'Binary Expression TypeCheck: Left is not a value item. ({type(left)}) Left: {left}, Right: {right}', None, self.filename)
        if not isinstance(right, value_item.ValueItem):
            raise exceptions.RuntimeError(f'Binary Expression TypeCheck: Right is not a value item. ({type(right)}) Left: {left}, Right: {right}', None, self.filename)
        if operator == '$+': return
        if left.Type != right.Type:
            if operator == '==' and (right.Type == types.VariableTypes.Bool or right.Type == types.VariableTypes.Nil):
                return
            if ((left.Type != types.VariableTypes.Int and left.Type != types.VariableTypes.Float) 
                 or (right.Type != types.VariableTypes.Int and right.Type != types.VariableTypes.Float)):
                raise exceptions.RuntimeError(f'Unsupported operand types for {operator}. ({left.Type} and {right.Type})', left.Token.Location, self.filename)



    def interpretLiteralExpression(self, expr: ast.AST, scope: mscope.Scope) -> value_item.ValueItem:
        if expr is None:
            raise exceptions.RuntimeError("Invalid argument exception, expr is None.", None, self.filename)
        value = value_item.ValueItem()
        if expr.LiteralValueType == types.VariableTypes.Array:
            value.Token = expr.Token
            value.Type = expr.LiteralValueType
            value.Value = []
        elif expr.LiteralValueType == types.VariableTypes.Record:
            value.Token = expr.Token
            value.Type = expr.LiteralValueType
            value.Value = {}
        else:
            value.setValue(expr.Token, expr.LiteralValueType, self.filename)
        return value



    def interpretBinaryExpression(self, expr: ast.AST, scope: mscope.Scope) -> value_item.ValueItem:
        if expr is None:
            raise exceptions.RuntimeError("Invalid argument exception, expr is None.", None, self.filename)
        left = self.interpretExpression(expr.Left, scope)
        if expr.Operator.Lexeme == 'and' and left.Value is False:
            return left
        if expr.Operator.Lexeme == 'or' and left.Value is True:
            return left
        right = self.interpretExpression(expr.Right, scope)
        self.typeCheck(left, right, expr.Operator.Lexeme)
        if expr.Operator.Lexeme == 'or' and right.Value is True:
            return right
        if expr.Operator.Lexeme == "+":
            return left + right
        if expr.Operator.Lexeme == "-":
            return left - right
        if expr.Operator.Lexeme == "/":
            return left / right
        if expr.Operator.Lexeme == "*":
            return left * right
        if expr.Operator.Lexeme == "^":
            return left ** right
        if expr.Operator.Lexeme == "%":
            return left % right
        if expr.Operator.Lexeme == ">":
            return left > right
        if expr.Operator.Lexeme == "<":
            return left < right
        if expr.Operator.Lexeme == ">=":
            return left >= right
        if expr.Operator.Lexeme == "<=":
            return left <= right
        if expr.Operator.Lexeme == "!=":
            return left != right
        if expr.Operator.Lexeme == "==":
            return left == right
        if expr.Operator.Lexeme == "and":
            return left and right
        if expr.Operator.Lexeme == "or":
            return left or right
        if expr.Operator.Lexeme == "$+":
            res = value_item.ValueItem()
            res.Type = types.VariableTypes.String
            res.Token = left.Token
            res.Value = f'{left.Value}{right.Value}'
            return res



    def interpretVariableExpression(self, expr: ast.AST, scope: mscope.Scope) -> value_item.ValueItem:
        var = scope.findVariable(expr.Token.Lexeme)
        if var is None:
            var = scope.findFunction(expr.Token.Lexeme, scope)
            if var is None:
                raise exceptions.RuntimeError(f'Variable or function ({expr.Token.Lexeme}) not found.', expr.Token.Location, self.filename)
            return value_item.ValueItem().setFromMacal(expr.Token, types.VariableTypes.Function, var)
        if expr.Left is not None and expr.Left.ExprType == types.ExprTypes.VariableIndex:
            return self.interpretIndexedVariableExpression(var, expr.Left, scope)
        return var.Value
        


    def interpretIndexedVariableExpression(self, var: variable.Variable, idx: ast_expr.Expr, scope: mscope.Scope)-> value_item.ValueItem:
        expr = idx
        vind = []
        while expr.ExprType != types.ExprTypes.VariableIndexStart:
            vind.insert(0, expr.Right)
            expr = expr.Left
        val = var.Value
        if val.Type not in [types.VariableTypes.Array, types.VariableTypes.Record, types.VariableTypes.String]:
            raise exceptions.RuntimeError(f'Type error, index not supported on {val.Type}', ind.Token.Location, self.filename)    
        for ind in vind:
            if val.Type not in [types.VariableTypes.Array, types.VariableTypes.Record, types.VariableTypes.String]:
                raise exceptions.RuntimeError(f'Type error, index not supported on {val.Type}', ind.Token.Location, self.filename)
            if ind.ExprType == types.ExprTypes.NewArrayIndex:
                raise exceptions.RuntimeError('Append not supported on right hand side.', ind.Token.Location, self.filename)
            i = self.interpretExpression(ind, scope)
            if val.Type == types.VariableTypes.Record:
                if i.Value not in val.Value:
                    raise exceptions.RuntimeError(f'Index ({i.Value}) not found.', ind.Token.Location, self.filename)
            elif val.Type == types.VariableTypes.Array or val.Type == types.VariableTypes.String:
                if i.Type != types.VariableTypes.Int:
                    raise exceptions.RuntimeError(f'Invalid index type ({i.Type}), Int index type required.', ind.Token.Location, self.filename)
                if i.Value < 0 or i.Value >= len(val.Value):
                    raise exceptions.RuntimeError(f'Index ({i.Value}) is out of range.', ind.Token.Location, self.filename)
            else:
                raise exceptions.RuntimeError(f'Type error, index not supported on {val.Type}', ind.Token.Location, self.filename)
            val = val.Value[i.Value]
        if expr.Right is not None and expr.Right.ExprType == types.ExprTypes.NewArrayIndex:
            raise exceptions.RuntimeError(f'Append not supported on right hand side', ind.Token.Location, self.filename)    
        return val



    def interpretUnaryExpression(self, expr: ast_expr.Expr, scope: mscope.Scope) -> value_item.ValueItem:
        val = self.interpretExpression(expr.Right, scope).clone()
        if expr.Operator.Lexeme == '-':
            val.Value *= -1
        if expr.Operator.Lexeme == '!':
            if val.Type != types.VariableTypes.Bool:
                raise exceptions.RuntimeError(f"Invalid type ({val.Type}), not a boolean.", val.Token.Location, self.filename)
            val.Value = not val.Value
        return val



    def interpretGroupingExpression(self, expr: ast_expr.Expr, scope: mscope.Scope) -> value_item.ValueItem:
        return self.interpretExpression(expr.Left, scope)
        


    def interpretBlock(self, expr: ast_block.Block, scope: mscope.Scope) -> None:
        for instruction in expr.Instructions:
            self.interpretInstruction(instruction, scope)
            if scope.Break or scope.Continue or scope.Return or scope.Halt:
                break



    def interpretReturn(self, instruction: ast_return.Return, scope: mscope.Scope) -> None:
        if not scope.isFunction:
            raise exceptions.RuntimeError("Invalid return instruction outside function.",instruction.Token.Location, self.filename)
        returnVar = scope.getVariable(f'?return_var{scope.Name}')
        returnVar.Value = self.interpretExpression(instruction.Value, scope)
        scope.Return = True



    def __HandleInfiniteLoopProtectionEmbeddedFunctions(self, func: ast_function_definition.FunctionDefinition, scope: mscope.Scope) -> value_item.ValueItem:
        if func.Name == 'setInfiniteLoopProtectionCount':
            var = scope.getVariable('count')
            if var.getType() != types.VariableTypes.Int:
                raise exceptions.RuntimeError(f"Function ({func.Name}) requires an integer value for the count argument.", func.Token.Location, self.filename)
            self.INFINITE_LOOP_PROTECTION_COUNT = var.getValue()
        return value_item.ValueItem().setFromMacal(func.Token, types.VariableTypes.Int, self.INFINITE_LOOP_PROTECTION_COUNT)



    def interpretFunctionArgList(self, args: typing.List[ast_expr.Expr], funcArgs: typing.List[ast_expr.Expr], etoken: token.LexToken, fnName: str, scope: mscope.Scope, fnScope: mscope.Scope) -> None:
        i=0
        params = False
        name = None
        if len(args) == 0 and len(funcArgs) > 0 and funcArgs[0].Token.Lexeme != 'params':
            name = funcArgs[0].Token.Lexeme
            if name in ['params', 'string', 'int', 'float', 'array', 'record', 'type', 'variable']:
                name = funcArgs[0].Left.Lexeme
            raise exceptions.RuntimeError(f'Required function argument ({name}) missing. ({fnName})', etoken.Location, self.filename)
        for v in args:
            if i < len(funcArgs):
                a = funcArgs[i]
            else:
                raise exceptions.RuntimeError(f'Function argument count exceeded ({len(args)} found, {len(funcArgs)} expected). ({fnName})', v.Token.Location, self.filename)
            if a.Token.Lexeme == 'variable':
                arg = scope.newVariable(a.Left, a.Left.Lexeme)
                fnScope.addVariable(arg)
                if v.ExprType != types.ExprTypes.Variable:
                    raise exceptions.RuntimeError(f'Variable required as function argument. ({fnName})', v.Token.Location, self.filename)
                var = scope.findVariable(v.Token.Lexeme)
                if var is None:
                    raise exceptions.RuntimeError(f'Variable ({v.Token.Lexeme}) not found. ({fnName})', v.Token.Location, self.filename)
                var = var.Clone()
                val = self.interpretExpression(v, scope)
                var.Token = v.Token
                var.Value = val
                arg.Value = value_item.ValueItem().setFromMacal(v.Token, types.VariableTypes.Variable, var)
                i += 1
            else:
                val = self.interpretExpression(v, scope)
                if params is False:
                    if a.ExprType == types.ExprTypes.Variable:
                        arg = fnScope.newVariable(a.Token, a.Token.Lexeme)
                    else:
                        arg = fnScope.newVariable(a.Left, a.Left.Lexeme)
                    fnScope.addVariable(arg)
                    if a.Token.Lexeme == 'params':
                        params = True
                        v = value_item.ValueItem().setFromMacal(a.Token, types.VariableTypes.Array, [])
                        v.Value.append(val)
                        arg.Value = v
                    else:
                        arg.Value = val
                        i += 1
                else:
                    arg.Value.Value.append(val)



    def runFunctionCall(self, name: str, args: typing.List[ast_expr.Expr], tok: token.LexToken, scope: mscope.Scope) -> value_item.ValueItem:
        func = scope.findFunction(name, scope)
        if func is None:
            var = scope.findVariable(name)
            if var is None:
                raise exceptions.RuntimeError(f"Function or variable ({name}) not found.", tok.Location, self.filename)            
            func = var.getFunction()
            if func is None:
                raise exceptions.RuntimeError(f"Function ({name}) not found.", tok.Location, self.filename)
        fnScope = scope.createTempScope(f'fnCall.{func.Name}')
        fnScope.isFunction = True
        returnVar = fnScope.createAndAppendFunctionReturnVariable(tok)
        returnVar.Value = value_item.ValueItem().setFromMacal(tok,types.VariableTypes.Nil, types.VariableTypes.Nil)
        self.interpretFunctionArgList(args, func.Arguments.Left, tok, name, scope, fnScope)
        if func.IsExternal is False:
            validateFunctionArguments(func, fnScope, self.filename)
            self.interpretBlock(func.Block, fnScope)
        elif func.Name == 'getInfiniteLoopProtectionCount' or func.Name == 'setInfiniteLoopProtectionCount':
            return self.__HandleInfiniteLoopProtectionEmbeddedFunctions(func, fnScope)
        else:
            fnScope.RunFunction = self.RunFunction
            self.interpretExternalFunction(func, fnScope)
        return returnVar.Value



    def RunFunction(self, funcName: str, scope: mscope.Scope, **kwargs) -> value_item.ValueItem:
        args = []
        func = scope.findFunction(funcName, scope)
        if func is None:
            raise exceptions.RuntimeError(f'Function ({funcName}) not found.', None, None)
        if kwargs is not None and len(kwargs) > 0:
            for arg in func.Arguments.Left:
                if arg.ExprType == types.ExprTypes.FunctionArgument:
                    an = arg.Left.Lexeme
                else:
                    an = arg.Token.Lexeme
                if an in kwargs:
                    vi = value_item.ValueItem().setFromPython(
                        token.LexToken(kwargs[an], types.LexTokenTypes.String, location.nullLoc(), -1),
                        kwargs[an])
                    if vi.Type == types.LexTokenTypes.String:
                        expr = ast_expr.Expr(token.LexToken(f'{kwargs[an]}', vi.Type, location.nullLoc(), -1))
                        expr.Type = vi.Type
                        expr.Left = vi
                    elif vi.Type == types.VariableTypes.Float or vi.Type == types.VariableTypes.Int:
                        expr = ast_expr.Expr(token.LexToken(f'{kwargs[an]}', types.LexTokenTypes.Number, location.nullLoc(), -1))
                        expr.Literal(vi.Type)
                        expr.Left = vi
                    elif vi.Type == types.VariableTypes.Bool:
                        expr = ast_expr.Expr(token.LexToken(f'{kwargs[an]}', types.LexTokenTypes.Identifier, location.nullLoc(), -1))
                        expr.Literal(vi.Type)
                        expr.Left = vi
                    elif isinstance(kwargs[an], variable.Variable):
                        expr = ast_expr.Expr(kwargs[an].Token).Variable(kwargs[an].Value.Type)
                    else:
                        raise exceptions.RuntimeError(f'Invalid argument type ({type(kwargs[an])}) in function ({funcName}).', None, None)
                    args.append(expr)
        result = self.runFunctionCall(funcName, args, 
            token.LexToken(funcName, types.LexTokenTypes.Identifier, location.nullLoc(), -1), scope)
        scope.setReturnValue(result.Value)
        return result.Value



    def findModuleFileName(self, module: str, scope: mscope.Scope):
        fileName = f'{module}.py'
        #first have a look in the package.
        path = pkg_resources.resource_filename(__name__, f'Library/Extern/{fileName}')
        fp = pathlib.Path(path).parent
        if pathlib.Path(path).is_file():
            return str(fp)
        # look in the extern folder set on the scope.
        path = f'{scope.externFolder}/{fileName}'
        fp = pathlib.Path(path).parent
        if pathlib.Path(path).is_file():
            return str(fp)
        # look in the folder based on the current executing file.
        fp = os.path.join(pathlib.Path(self.filename).parent.absolute())
        path = f'{str(fp)}/{fileName}'
        if pathlib.Path(path).is_file():
            return fp
        return None



    def loadModule(self, modulename, functionname, scope: mscope.Scope):
        filepath = self.findModuleFileName(modulename, scope)
        if filepath is not None:
            if filepath not in sys.path:
                sys.path.insert(0, filepath)
            module = __import__(modulename, locals(), globals() , [functionname])
            return module
        else:
            return None



    def interpretExternalFunction(self, func: ast_function_definition.FunctionDefinition, scope: mscope.Scope) -> value_item.ValueItem:
        module = self.loadModule(func.ExternalModule.Lexeme, func.ExternalFunction.Lexeme, scope)
        if module is None:
            raise exceptions.RuntimeError(f"Function ({func.Name}) not found.", func.Token.Location, self.filename)
        fn = getattr(module, func.ExternalFunction.Lexeme)
        fn(func, scope, self.filename)
        exitVar = scope.getVariable(f'?return_var{scope.Name}')
        return exitVar.Value



    def interpretBreak(self, instruction: ast_break.Break, scope: mscope.Scope) -> None:
        if not scope.isLoop:
            raise exceptions.RuntimeError("Invalid break instruction outside loop.", instruction.Token.Location, self.filename)
        scope.Break = True
        pscope = scope
        while pscope.isLoopRoot is False:
            pscope = pscope.Parent
            pscope.Break = True



    def interpretContinue(self, instruction: ast_continue.Continue, scope: mscope.Scope) -> None:
        if not scope.isLoop:
            raise exceptions.RuntimeError("Invalid continue instruction outside loop.",instruction.Token.Location, self.filename)
        scope.Continue = True
        pscope = scope
        while pscope.isLoopRoot is False and pscope.Parent is not None:
            pscope = pscope.Parent
            pscope.Continue = True



    def interpretHalt(self, instruction: ast_halt.Halt, scope: mscope.Scope) -> None:
        value = self.interpretExpression(instruction.Exitcode, scope)
        var = scope.Root.getVariable('exitcode')
        var.Value = value
        scope.setHalt(True)



    def resetContinue(self, scope: mscope.Scope):
        scope.Continue = False
        #for child in scope.Children:
        #    self.resetContinue(child)


    
    def interpretForeach(self, instruction: ast_foreach.Foreach, scope: mscope.Scope) -> None:
        val = self.interpretExpression(instruction.Variable, scope)
        fes = scope.createTempScope('foreach')
        fes.isLoop = True
        fes.isLoopRoot = True
        it = fes.newVariable(instruction.Variable.Token, 'it')
        fes.addVariable(it)
        if val.Type == types.VariableTypes.String or val.Type == types.VariableTypes.Record:
            for v in val.Value:
                vv = value_item.ValueItem().setFromMacal(val.Token, types.VariableTypes.String, v)
                if fes.Break or fes.Halt or fes.Return: break
                if fes.Continue: self.resetContinue(fes)
                it.Value = vv
                self.interpretBlock(instruction.Block, fes)
        else:
            for v in val.Value:
                if fes.Break or fes.Halt or fes.Return: break
                if fes.Continue: self.resetContinue(fes)
                it.Value = v
                self.interpretBlock(instruction.Block, fes)
        

    
    def interpretWhile(self, instruction: ast_while.While, scope: mscope.Scope) -> None:
        condition = self.interpretExpression(instruction.Condition, scope)
        whs = scope.createTempScope('while')
        whs.isLoop = True
        whs.isLoopRoot = True
        infiniteLoopProtection = self.INFINITE_LOOP_PROTECTION_COUNT
        if self.INFINITE_LOOP_PROTECTION_COUNT == 0:
            infiniteLoopProtection = 1
        while condition.Value is True and infiniteLoopProtection > 0:
            if whs.Break or whs.Halt or whs.Return: break
            if whs.Continue: self.resetContinue(whs)
            self.interpretBlock(instruction.Block, whs)
            condition = self.interpretExpression(instruction.Condition, whs)
            if self.INFINITE_LOOP_PROTECTION_COUNT != 0:
                infiniteLoopProtection -= 1
        if infiniteLoopProtection == 0:
            raise exceptions.RuntimeError("Infinite loop protection engaged.",instruction.Token.Location, self.filename)



    def interpretIf(self, instruction: ast_if.If, scope: mscope.Scope) -> None:
        condition = self.interpretExpression(instruction.Condition, scope)
        ifs = scope.createTempScope('if')
        if condition.Value is True:
            self.interpretBlock(instruction.Block, ifs)
        else:
            els = True
            if len(instruction.Elif) > 0:
                for elfi in instruction.Elif:
                    lifs = scope.createTempScope('elif')
                    condition = self.interpretExpression(elfi.Condition, lifs)
                    if condition.Value is True:
                        els = False
                        self.interpretBlock(elfi.Block, lifs)
                        break
            if els is True and instruction.Else is not None:
                esl = scope.createTempScope('else')
                self.interpretBlock(instruction.Else, esl)



    def interpretSelect(self, instruction: ast_select.Select, scope: mscope.Scope) -> None:
        data = self.interpretExpression(instruction.From, scope)       
        into = self.evaluateIntoVariable(instruction.Into, data, scope)
        if into is None:
            if instruction.Merge is True:
                raise exceptions.RuntimeError(f'Variable ({instruction.Into.Token.Lexeme}) not found.', instruction.Into.Token.Location, self.filename)
            intoVar = variable.Variable(instruction.Into.Token, instruction.Into.Token.Lexeme)
            if instruction.Distinct:
                intoVar.Value = value_item.ValueItem().setFromMacal(instruction.Token, types.VariableTypes.Record, {})
            else:
                intoVar.Value = value_item.ValueItem().setFromMacal(instruction.Token, types.VariableTypes.Array, [])
            scope.addVariable(intoVar)
            into = intoVar.Value
        if instruction.Where is not None and data is not None:
            data = self.interpretSelectWhere(instruction.Where, data, scope)
        if not(len(instruction.Fields) == 1 and instruction.Fields[0].Name == '*'):
            data = self.applyFieldFilters(data, instruction.Fields)
        if instruction.Distinct is True and data is not None and data.Type == types.VariableTypes.Array and len(data.Value) > 0:
            data = data.Value[0]
        if data is not None and data.Type == types.VariableTypes.Array and len(data.Value) == 1:
            data = value_item.ValueItem().setFromMacal(data.Value[0].Token, types.VariableTypes.Record, data.Value[0])
        if instruction.Merge is True and data is not None:
            data = self.interpretSelectMerge(into, data)
        # second time is needed, just in case merge returns an array of 1 record..
        if data is not None and data.Type == types.VariableTypes.Array and len(data.Value) == 1:
            data = value_item.ValueItem().setFromMacal(data.Token, types.VariableTypes.Record, data.Value[0])
        if data is not None:
            self.setIntoVariableValue(instruction.Into, data, scope)



    def setIntoVariableValue(self, expr: ast_expr.Expr, data: value_item.ValueItem, scope: mscope.Scope) -> None:
        var = scope.findVariable(expr.Token.Lexeme)
        if var is None:
            raise exceptions.RuntimeError(f'Variable ({expr.Token.Lexeme}) not found.', expr.Token.Location, self.filename)
        if expr.Left is None:
            var.Value = data
            return
        if expr.Left.ExprType == types.ExprTypes.VariableIndex:
            self.setIndexedIntoVariableValue(var, expr.Left, data, scope)
            return
        raise exceptions.RuntimeError(f'Variable ({expr.Token.Lexeme}) has an invalid left hand expression type: {expr.Left.ExprType}.', expr.Token.Location, self.filename)


    
    def setIndexedIntoVariableValue(self, var: variable.Variable, idx: ast_expr.Expr, data: value_item.ValueItem, scope: mscope.Scope)-> None:
        expr = idx
        vind = []
        while expr.ExprType != types.ExprTypes.VariableIndexStart:
            if expr.Right.ExprType == types.ExprTypes.NewArrayIndex:
                raise exceptions.RuntimeError('Append not supported in select.', ind.Token.Location, self.filename)
            vind.insert(0, expr.Right)
            expr = expr.Left
        val = var.Value
        if val.Type not in [types.VariableTypes.Array, types.VariableTypes.Record, types.VariableTypes.String]:
            raise exceptions.RuntimeError(f'Type error, index not supported on {val.Type}', ind.Token.Location, self.filename)    
        finalIndex = None
        finalVal = None
        for ind in vind:
            if val.Type not in [types.VariableTypes.Array, types.VariableTypes.Record, types.VariableTypes.String]:
                raise exceptions.RuntimeError(f'Type error, index not supported on {val.Type}', ind.Token.Location, self.filename)      
            i = self.interpretExpression(ind, scope)
            if val.Type == types.VariableTypes.Record:
                if i.Value not in val.Value:
                    raise exceptions.RuntimeError(f'Index ({i.Value}) not found.', ind.Token.Location, self.filename)
            elif val.Type == types.VariableTypes.Array or val.Type == types.VariableTypes.String:
                if i.Type != types.VariableTypes.Int:
                    raise exceptions.RuntimeError(f'Invalid index type ({i.Type}), Int index type required.', ind.Token.Location, self.filename)
                if i.Value < 0 or i.Value >= len(val.Value):
                    raise exceptions.RuntimeError(f'Index ({i.Value}) is out of range.', ind.Token.Location, self.filename)
            else:
                raise exceptions.RuntimeError(f'Type error, index not supported on {val.Type}', ind.Token.Location, self.filename)
            finalIndex = i.Value
            finalVal = val
            val = val.Value[i.Value]
        if expr.Right is not None and expr.Right.ExprType == types.ExprTypes.NewArrayIndex:
            raise exceptions.RuntimeError(f'Append not supported on right hand side', ind.Token.Location, self.filename)
        finalVal.Value[finalIndex] = data



    def applyFieldFilters(self, data: value_item.ValueItem, fields: typing.List[ast_select_field.SelectField]):
        if data is None:
            returnData = value_item.ValueItem().setFromMacal(rec.Token, rec.Type, {})
            for fld in fields:
                returnData.Value[fld.AsName] = value_item.ValueItem().setFromMacal(None, types.VariableTypes.Nil, types.VariableTypes.Nil)
        elif data.Type == types.VariableTypes.Array:
            returnData = value_item.ValueItem().setFromMacal(data.Token, data.Type, [])
            for rec in data.Value:
                r = value_item.ValueItem().setFromMacal(rec.Token, rec.Type, {})
                for fld in fields:
                    if fld.Name in rec.Value:
                        r.Value[fld.AsName] = rec.Value[fld.Name]
                    else:
                        r.Value[fld.AsName] = value_item.ValueItem().setFromMacal(None, types.VariableTypes.Nil, types.VariableTypes.Nil)
                returnData.Value.append(r)
        elif data.Type == types.VariableTypes.Record:
            rec = data
            r = value_item.ValueItem().setFromMacal(rec.Token, rec.Type, {})
            for fld in fields:
                if fld.Name in rec.Value:
                    r.Value[fld.AsName] = rec.Value[fld.Name]
                else:
                    r.Value[fld.AsName] = value_item.ValueItem().setFromMacal(None, types.VariableTypes.Nil, types.VariableTypes.Nil)
            returnData = r
        else: # just not filter if it's something we didn't anticipate.
            returnData = data
        return returnData



    def interpretSelectWhere(self, expr: ast_expr.Expr, data: value_item.ValueItem, scope:mscope.Scope)-> value_item.ValueItem:
        if data.Type == types.VariableTypes.Array:
            returnData = value_item.ValueItem().setFromMacal(data.Token, data.Type, [])
            for rec in data.Value:
                res = self.evaluateDatafieldExpression(expr, rec, scope)
                if res.Value is True:
                    returnData.Value.append(rec)
        else:
            returnData = value_item.ValueItem().setFromMacal(data.Token, types.VariableTypes.Record, {})
            self.evaluateDatafieldExpression(expr, data, scope)
            if res.Value is True:
                returnData = data
        return returnData



    def compareRecordFieldSets(self, rec1: value_item.ValueItem, rec2: value_item.ValueItem) -> bool:
        # returns true if both field sets are the same, false if not.
        if set(rec1.Value.keys()) == set(rec2.Value.keys()):
            return True
        return False



    def interpretSelectMerge(self, into: value_item.ValueItem, data: value_item.ValueItem)-> value_item.ValueItem:
        if (into.Type == types.VariableTypes.Record and data.Type == types.VariableTypes.Record):
            # both records, we need to check if the set of fields is the same.
            if self.compareRecordFieldSets(into, data):
                returnData = value_item.ValueItem().setFromMacal(into.Token, types.VariableTypes.Array, [])
                returnData.Value.append(into)
                returnData.Value.append(data)
                return returnData
            else:
                returnData = into
                for key, value in data.Value.items():
                    returnData.Value[key] = value
                return returnData
        returnData = value_item.ValueItem().setFromMacal(into.Token, types.VariableTypes.Array, [])
        if into.Type == types.VariableTypes.Array:
            for rec in into.Value:
                returnData.Value.append(rec)
        # Into can be nil here, so we must check.
        elif into.Type == types.VariableTypes.Record:
            returnData.Value.append(into.Value)
        if data.Type == types.VariableTypes.Array:
            for rec in data.Value:
                returnData.Value.append(rec)
        # Data should always be record or array, but just to be sure we check.
        elif data.Type == types.VariableTypes.Record:
            returnData.Value.append(data.Value)
        return returnData



    def evaluateDatafieldExpression(self, expr: ast_expr.Expr, rec: value_item.ValueItem, scope: mscope.Scope) -> value_item.ValueItem:
        if expr.ExprType == types.ExprTypes.Variable:
            return self.evaluateDatafieldVariable(expr, rec, scope)
        if expr.ExprType == types.ExprTypes.Literal:
            return self.evaluateDatafieldLiteral(expr, rec, scope)
        if expr.ExprType == types.ExprTypes.Binary:
            return self.evaluateDatafieldBinary(expr, rec, scope)
        if expr.ExprType == types.ExprTypes.Unary:
            return self.evaluateDatafieldUnary(expr, rec, scope)
        if expr.ExprType == types.ExprTypes.Grouping:
            return self.evaluateDatafieldGrouping(expr, rec, scope)
        if expr.ExprType == types.ExprTypes.Function:
            return self.evaluateDatafieldFunction(expr, rec, scope)
        raise exceptions.RuntimeError(f'Unknown datafield expression type ({expr.ExprType}).', expr.Token.Location, self.filename)



    def evaluateDatafieldLiteral(self, expr: ast_expr.Expr, rec: value_item.ValueItem, scope: mscope.Scope) -> value_item.ValueItem:
        value = value_item.ValueItem()
        if expr.LiteralValueType == types.VariableTypes.Array:
            value.Token = expr.Token
            value.Type = expr.LiteralValueType
            value.Value = []
        elif expr.LiteralValueType == types.VariableTypes.Record:
            value.Token = expr.Token
            value.Type = expr.LiteralValueType
            value.Value = {}
        else:
            value.setValue(expr.Token, expr.LiteralValueType, self.filename)
        return value



    def evaluateDatafieldBinary(self, expr: ast_expr.Expr, rec: value_item.ValueItem, scope: mscope.Scope) -> value_item.ValueItem:
        left = self.evaluateDatafieldExpression(expr.Left, rec, scope)
        if expr.Operator.Lexeme == 'and' and left.Value is False:
            return left
        if expr.Operator.Lexeme == 'or' and left.Value is True:
            return left
        right = self.evaluateDatafieldExpression(expr.Right, rec, scope)
        self.typeCheck(left, right, expr.Operator.Lexeme)
        if expr.Operator.Lexeme == 'or' and right.Value is True:
            return right
        if expr.Operator.Lexeme == "+":
            return left + right
        if expr.Operator.Lexeme == "-":
            return left - right
        if expr.Operator.Lexeme == "/":
            return left / right
        if expr.Operator.Lexeme == "*":
            return left * right
        if expr.Operator.Lexeme == "^":
            return left ** right
        if expr.Operator.Lexeme == "%":
            return left % right
        if expr.Operator.Lexeme == ">":
            return left > right
        if expr.Operator.Lexeme == "<":
            return left < right
        if expr.Operator.Lexeme == ">=":
            return left >= right
        if expr.Operator.Lexeme == "<=":
            return left <= right
        if expr.Operator.Lexeme == "!=":
            return left != right
        if expr.Operator.Lexeme == "==":
            return left == right
        if expr.Operator.Lexeme == "and":
            return left and right
        if expr.Operator.Lexeme == "or":
            return left or right
        if expr.Operator.Lexeme == "$+":
            res = value_item.ValueItem()
            res.Type = types.VariableTypes.String
            res.Token = left.Token
            res.Value = f'{left.Value}{right.Value}'
            return res



    def evaluateDatafieldVariable(self, expr: ast_expr.Expr, rec: value_item.ValueItem, scope: mscope.Scope) -> value_item.ValueItem:
        if expr.Token.Lexeme in rec.Value:
            return rec.Value[expr.Token.Lexeme]
        val = self.evaluateIntoVariable(expr, rec, scope)
        if val is None:
            raise exceptions.RuntimeError(f'Variable ({expr.Token.Lexeme}) not found.', expr.Token.Location, self.filename)
        return val
        


    def evaluateIntoVariable(self, expr: ast_expr.Expr, rec: value_item.ValueItem, scope: mscope.Scope) -> value_item.ValueItem:
        var = scope.findVariable(expr.Token.Lexeme)
        if var is None:
            return None
        if expr.Left is None:
            return var.Value
        if expr.Left.ExprType == types.ExprTypes.VariableIndex:
            return self.evaluateDatafieldIndexedVariable(var, expr.Left, rec, scope)
        raise exceptions.RuntimeError(f'Variable ({expr.Token.Lexeme}) has an invalid left hand expression type: {expr.Left.ExprType}.', expr.Token.Location, self.filename)



    def evaluateDatafieldIndexedVariable(self, var: variable.Variable, idx: ast_expr.Expr, rec: dict, scope: mscope.Scope)-> value_item.ValueItem:
        expr = idx
        vind = []
        while expr.ExprType != types.ExprTypes.VariableIndexStart:
            if expr.Right.ExprType == types.ExprTypes.NewArrayIndex:
                raise exceptions.RuntimeError('Append not supported on right hand side.', ind.Token.Location, self.filename)
            vind.insert(0, expr.Right)
            expr = expr.Left
        val = var.Value
        if val.Type not in [types.VariableTypes.Array, types.VariableTypes.Record, types.VariableTypes.String]:
            raise exceptions.RuntimeError(f'Type error, index not supported on {val.Type}', ind.Token.Location, self.filename)    
        for ind in vind:
            if val.Type not in [types.VariableTypes.Array, types.VariableTypes.Record, types.VariableTypes.String]:
                raise exceptions.RuntimeError(f'Type error, index not supported on {val.Type}', ind.Token.Location, self.filename)
            i = self.interpretExpression(ind, scope)
            if val.Type == types.VariableTypes.Record:
                if i.Value not in val.Value:
                    raise exceptions.RuntimeError(f'Index ({i.Value}) not found.', ind.Token.Location, self.filename)
            elif val.Type == types.VariableTypes.Array or val.Type == types.VariableTypes.String:
                if i.Type != types.VariableTypes.Int:
                    raise exceptions.RuntimeError(f'Invalid index type ({i.Type}), Int index type required.', ind.Token.Location, self.filename)
                if i.Value < 0 or i.Value >= len(val.Value):
                    raise exceptions.RuntimeError(f'Index ({i.Value}) is out of range.', ind.Token.Location, self.filename)
            else:
                raise exceptions.RuntimeError(f'Type error, index not supported on {val.Type}', ind.Token.Location, self.filename)
            val = val.Value[i.Value]
        if expr.Right is not None and expr.Right.ExprType == types.ExprTypes.NewArrayIndex:
            raise exceptions.RuntimeError(f'Append not supported on right hand side', ind.Token.Location, self.filename)    
        return val



    def evaluateDatafieldUnary(self, expr: ast_expr.Expr, rec: dict, scope: mscope.Scope) -> value_item.ValueItem:
        val = self.evaluateDatafieldExpression(expr.Right, rec, scope).clone()
        if expr.Operator.Lexeme == '-':
            val.Value *= -1
        if expr.Operator.Lexeme == '!':
            if val.Type != types.VariableTypes.Bool:
                raise exceptions.RuntimeError(f"Invalid type ({val.Type}), not a boolean.", val.Token.Location, self.filename)
            val.Value = not val.Value
        return val



    def evaluateDatafieldGrouping(self, expr: ast_expr.Expr, rec: dict, scope: mscope.Scope) -> value_item.ValueItem:
        return self.evaluateDatafieldExpression(expr.Left, rec, scope)
        
