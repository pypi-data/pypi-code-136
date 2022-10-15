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



def ValidateFunctionArguments(func: ast_function_definition.FunctionDefinition, scope: mscope.Scope, filename: str) -> None:
    for arg in func.Arguments.Left:
        if arg.ExprType == types.ExprTypes.FunctionArgument:
            name = arg.Left.Lexeme
        else:
            name = arg.Token.Lexeme
        var = scope.FindVariable(name)
        if var is None:
            if arg.Token.Lexeme == 'params': return
            raise exceptions.RuntimeError(f'Function argument {arg.Token.Lexeme} not found.', arg.Token.Location, filename)
        if arg.ExprType == types.ExprTypes.FunctionArgument:
            t = var.GetType().lower()
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
        scope.SetHalt(False)
        self.Source = source
        for instruction in source:
            self.InterpretInstruction(instruction, scope)
            if scope.Halt:
                return scope
        return scope



    def InterpretInstruction(self, instruction: ast.AST, scope):
        if instruction.Type == types.AstTypes.Assignment:
            return self.InterpretAssign(instruction, scope)
        if instruction.Type == types.AstTypes.Block:
            return self.InterpretBlock(instruction, scope)
        if instruction.Type == types.AstTypes.Break:
            return self.InterpretBreak(instruction, scope)
        if instruction.Type == types.AstTypes.Continue:
            return self.InterpretContinue(instruction, scope)
        if instruction.Type == types.AstTypes.FunctionCall:
            return self.RunFunctionCall(instruction.Name, instruction.Args, instruction.Token, scope)
        if instruction.Type == types.AstTypes.FunctionDefinition:
            return self.InterpretFunctionDefinition(instruction, scope)
        if instruction.Type == types.AstTypes.If:
            return self.InterpretIf(instruction, scope)
        if instruction.Type == types.AstTypes.Include:
            return self.InterpretInclude(instruction, scope)
        if instruction.Type == types.AstTypes.Foreach:
            return self.InterpretForeach(instruction, scope)
        if instruction.Type == types.AstTypes.Halt:
            return self.InterpretHalt(instruction, scope)
        if instruction.Type == types.AstTypes.Return:
            return self.InterpretReturn(instruction, scope)
        if instruction.Type == types.AstTypes.Select:
            return self.InterpretSelect(instruction, scope)
        if instruction.Type == types.AstTypes.While:
            return self.InterpretWhile(instruction, scope)
        raise exceptions.RuntimeError(f"Invalid instruction type ({instruction.Type}).", instruction.Token.Location, self.filename)



    def InterpretInclude(self, instruction: ast_include.Include, scope: mscope.Scope) -> None:
        for include in instruction.Includes:
            incl = scope.FindInclude(include.Lexeme)
            if incl is not None: # already included
                continue
            (result, ex) = self.Include(include.Lexeme, scope)
            var = scope.Root.GetVariable('exitcode')
            if not result and ex is not None:
                var.SetValue(4)
                raise exceptions.RuntimeError(ex, instruction.Token.Location, self.filename)
            elif not result:
                var.SetValue(5)
                self.Halt = True



    def InterpretFunctionDefinition(self, instruction: ast.AST, scope: mscope.Scope):
        scope.Functions.append(instruction)



    def InterpretAssignToIndexedVar(self, var: variable.Variable, idx: ast_expr.Expr, value: value_item.ValueItem, scope: mscope.Scope):
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
            i = self.InterpretExpression(ind, scope)
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
        if expr.Right is not None and expr.Right.ExprType == types.ExprTypes.NewArrayIndex:
            if val.Type != types.VariableTypes.Array:
                raise exceptions.RuntimeError(f'Type error, append not supported on {val.Type}', ind.Token.Location, self.filename)    
            val.Value.append(value)
        else:
            val.Value = value



    def InterpretAssign(self, instruction: ast_assignment.Assignment, scope: mscope.Scope) -> None:
        var = scope.FindVariable(instruction.Variable)
        if var is None:
            var = scope.NewVariable(instruction.Token, instruction.Variable)
            var.isConst = instruction.isConst
            scope.AddVariable(var)
        elif var.isConst:
            raise exceptions.RuntimeError(f'Illegal assignment to a constant ({instruction.Variable}).', instruction.Token.Location, self.filename)
        value = self.InterpretExpression(instruction.Value, scope)
        if instruction.VarIndex is not None:
            return self.InterpretAssignToIndexedVar(var, instruction.VarIndex, value, scope)
        if instruction.Operator.Lexeme == '=':
            var.Value = value.Clone()
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



    def InterpretExpression(self, expr: ast.AST, scope: mscope.Scope) -> value_item.ValueItem:
        if expr is None:
            raise exceptions.RuntimeError("Invalid argument exception, expr is None.", None, self.filename)
        if expr.ExprType == types.ExprTypes.Literal:
            return self.InterpretLiteralExpression(expr, scope)
        if expr.ExprType == types.ExprTypes.Binary:
            return self.InterpretBinaryExpression(expr, scope)
        if expr.ExprType == types.ExprTypes.Unary:
            return self.InterpretUnaryExpression(expr, scope)
        if expr.ExprType == types.ExprTypes.Grouping:
            return self.InterpretGroupingExpression(expr, scope)
        if expr.ExprType == types.ExprTypes.FunctionCall:
            return self.RunFunctionCall(expr.Token.Lexeme, expr.Right.Left, expr.Right.Token, scope)
        if expr.ExprType == types.ExprTypes.FunctionArgument:
            raise exceptions.RuntimeError("Function Argument type should not end up in expression interpretation.", expr.Token.Location, self.filename)
        if expr.ExprType == types.ExprTypes.ArgumentList:
            raise exceptions.RuntimeError("Argument list type should not end up in expression interpretation.", expr.Token.Location, self.filename)
        if expr.ExprType == types.ExprTypes.Variable:
            return self.InterpretVariableExpression(expr, scope)
        if expr.ExprType == types.ExprTypes.VariableIndex:
            return self.InterpretLiteralExpression(expr.Left, scope)
        if expr.ExprType == types.ExprTypes.InterpolationPart:
            return self.InterpretBinaryExpression(expr.Right, scope)
        raise Exception("Expression type evaluation not implemented yet: ", expr.ExprType)



    def InterpretLiteralExpression(self, expr: ast.AST, scope: mscope.Scope) -> value_item.ValueItem:
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
            value.SetValue(expr.Token, expr.LiteralValueType, self.filename)
        return value



    def BinaryExpressionOperandsTypeCheck(self, left:value_item.ValueItem, right:value_item.ValueItem, operator:str):
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



    def InterpretBinaryExpression(self, expr: ast.AST, scope: mscope.Scope) -> value_item.ValueItem:
        if expr is None:
            raise exceptions.RuntimeError("Invalid argument exception, expr is None.", None, self.filename)
        left = self.InterpretExpression(expr.Left, scope)
        if expr.Operator.Lexeme == 'and' and left.Value is False:
            return left
        if expr.Operator.Lexeme == 'or' and left.Value is True:
            return left
        right = self.InterpretExpression(expr.Right, scope)
        self.BinaryExpressionOperandsTypeCheck(left, right, expr.Operator.Lexeme)
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



    def InterpretVariableExpression(self, expr: ast.AST, scope: mscope.Scope) -> value_item.ValueItem:
        var = scope.FindVariable(expr.Token.Lexeme)
        if var is None:
            var = scope.FindFunction(expr.Token.Lexeme, scope)
            if var is None:
                raise exceptions.RuntimeError(f'Variable or function ({expr.Token.Lexeme}) not found.', expr.Token.Location, self.filename)
            return value_item.ValueItem().SetFromMacal(expr.Token, types.VariableTypes.Function, var)
        if expr.Left is not None and expr.Left.ExprType == types.ExprTypes.VariableIndex:
            return self.InterpretIndexedVariableExpression(var, expr.Left, scope)
        return var.Value
        


    def InterpretIndexedVariableExpression(self, var: variable.Variable, idx: ast_expr.Expr, scope: mscope.Scope)-> value_item.ValueItem:
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
            i = self.InterpretExpression(ind, scope)
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



    def InterpretUnaryExpression(self, expr: ast_expr.Expr, scope: mscope.Scope) -> value_item.ValueItem:
        val = self.InterpretExpression(expr.Right, scope).Clone()
        if expr.Operator.Lexeme == '-':
            val.Value *= -1
        if expr.Operator.Lexeme == '!':
            if val.Type != types.VariableTypes.Bool:
                raise exceptions.RuntimeError(f"Invalid type ({val.Type}), not a boolean.", val.Token.Location, self.filename)
            val.Value = not val.Value
        return val



    def InterpretGroupingExpression(self, expr: ast_expr.Expr, scope: mscope.Scope) -> value_item.ValueItem:
        return self.InterpretExpression(expr.Left, scope)
        


    def InterpretBlock(self, expr: ast_block.Block, scope: mscope.Scope) -> None:
        for instruction in expr.Instructions:
            self.InterpretInstruction(instruction, scope)
            if scope.Break or scope.Continue or scope.Return or scope.Halt:
                break



    def InterpretReturn(self, instruction: ast_return.Return, scope: mscope.Scope) -> None:
        if not scope.isFunction:
            raise exceptions.RuntimeError("Invalid return instruction outside function.",instruction.Token.Location, self.filename)
        returnVar = scope.GetVariable(f'?return_var{scope.Name}')
        returnVar.Value = self.InterpretExpression(instruction.Value, scope)
        scope.Return = True



    def __HandleInfiniteLoopProtectionEmbeddedFunctions(self, func: ast_function_definition.FunctionDefinition, scope: mscope.Scope) -> value_item.ValueItem:
        if func.Name == 'setInfiniteLoopProtectionCount':
            var = scope.GetVariable('count')
            if var.GetType() != types.VariableTypes.Int:
                raise exceptions.RuntimeError(f"Function ({func.Name}) requires an integer value for the count argument.", func.Token.Location, self.filename)
            self.INFINITE_LOOP_PROTECTION_COUNT = var.GetValue()
        return value_item.ValueItem().SetFromMacal(func.Token, types.VariableTypes.Int, self.INFINITE_LOOP_PROTECTION_COUNT)



    def InterpretFunctionArgList(self, args: typing.List[ast_expr.Expr], funcArgs: typing.List[ast_expr.Expr], etoken: token.LexToken, fnName: str, scope: mscope.Scope, fnScope: mscope.Scope) -> None:
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
                arg = scope.NewVariable(a.Left, a.Left.Lexeme)
                fnScope.AddVariable(arg)
                if v.ExprType != types.ExprTypes.Variable:
                    raise exceptions.RuntimeError(f'Variable required as function argument. ({fnName})', v.Token.Location, self.filename)
                var = scope.FindVariable(v.Token.Lexeme)
                if var is None:
                    raise exceptions.RuntimeError(f'Variable ({v.Token.Lexeme}) not found. ({fnName})', v.Token.Location, self.filename)
                var = var.Clone()
                val = self.InterpretExpression(v, scope)
                var.Token = v.Token
                var.Value = val
                arg.Value = value_item.ValueItem().SetFromMacal(v.Token, types.VariableTypes.Variable, var)
                i += 1
            else:
                val = self.InterpretExpression(v, scope)
                if params is False:
                    if a.ExprType == types.ExprTypes.Variable:
                        arg = fnScope.NewVariable(a.Token, a.Token.Lexeme)
                    else:
                        arg = fnScope.NewVariable(a.Left, a.Left.Lexeme)
                    fnScope.AddVariable(arg)
                    if a.Token.Lexeme == 'params':
                        params = True
                        v = value_item.ValueItem().SetFromMacal(a.Token, types.VariableTypes.Array, [])
                        v.Value.append(val)
                        arg.Value = v
                    else:
                        arg.Value = val
                        i += 1
                else:
                    arg.Value.Value.append(val)



    def RunFunctionCall(self, name: str, args: typing.List[ast_expr.Expr], tok: token.LexToken, scope: mscope.Scope) -> value_item.ValueItem:
        func = scope.FindFunction(name, scope)
        if func is None:
            var = scope.FindVariable(name)
            if var is None:
                raise exceptions.RuntimeError(f"Function or variable ({name}) not found.", tok.Location, self.filename)            
            func = var.GetFunction()
            if func is None:
                raise exceptions.RuntimeError(f"Function ({name}) not found.", tok.Location, self.filename)
        fnScope = scope.CreateTempScope(f'fnCall.{func.Name}')
        fnScope.isFunction = True
        returnVar = fnScope.CreateAndAppendFunctionReturnVariable(tok)
        returnVar.Value = value_item.ValueItem().SetFromMacal(tok,types.VariableTypes.Nil, types.VariableTypes.Nil)
        self.InterpretFunctionArgList(args, func.Arguments.Left, tok, name, scope, fnScope)
        if func.IsExternal is False:
            ValidateFunctionArguments(func, fnScope, self.filename)
            self.InterpretBlock(func.Block, fnScope)
        elif func.Name == 'getInfiniteLoopProtectionCount' or func.Name == 'setInfiniteLoopProtectionCount':
            return self.__HandleInfiniteLoopProtectionEmbeddedFunctions(func, fnScope)
        else:
            fnScope.RunFunction = self.RunFunction
            self.InterpretExternalFunction(func, fnScope)
        return returnVar.Value



    def RunFunction(self, funcName: str, scope: mscope.Scope, **kwargs) -> value_item.ValueItem:
        args = []
        func = scope.FindFunction(funcName, scope)
        if func is None:
            raise exceptions.RuntimeError(f'Function ({funcName}) not found.', None, None)
        if kwargs is not None and len(kwargs) > 0:
            for arg in func.Arguments.Left:
                if arg.ExprType == types.ExprTypes.FunctionArgument:
                    an = arg.Left.Lexeme
                else:
                    an = arg.Token.Lexeme
                if an in kwargs:
                    vi = value_item.ValueItem().SetFromPython(
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
        result = self.RunFunctionCall(funcName, args, 
            token.LexToken(funcName, types.LexTokenTypes.Identifier, location.nullLoc(), -1), scope)
        scope.SetReturnValue(result.Value)
        return result.Value



    def FindModuleFileName(self, module: str, scope: mscope.Scope):
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



    def LoadModule(self, modulename, functionname, scope: mscope.Scope):
        filepath = self.FindModuleFileName(modulename, scope)
        if filepath is not None:
            if filepath not in sys.path:
                sys.path.insert(0, filepath)
            module = __import__(modulename, locals(), globals() , [functionname])
            return module
        else:
            return None



    def InterpretExternalFunction(self, func: ast_function_definition.FunctionDefinition, scope: mscope.Scope) -> value_item.ValueItem:
        module = self.LoadModule(func.ExternalModule.Lexeme, func.ExternalFunction.Lexeme, scope)
        if module is None:
            raise exceptions.RuntimeError(f"Function ({func.Name}) not found.", func.Token.Location, self.filename)
        fn = getattr(module, func.ExternalFunction.Lexeme)
        fn(func, scope, self.filename)
        exitVar = scope.GetVariable(f'?return_var{scope.Name}')
        return exitVar.Value



    def InterpretBreak(self, instruction: ast_break.Break, scope: mscope.Scope) -> None:
        if not scope.isLoop:
            raise exceptions.RuntimeError("Invalid break instruction outside loop.", instruction.Token.Location, self.filename)
        scope.Break = True
        pscope = scope
        while pscope.isLoopRoot is False:
            pscope = pscope.Parent
            pscope.Break = True



    def InterpretContinue(self, instruction: ast_continue.Continue, scope: mscope.Scope) -> None:
        if not scope.isLoop:
            raise exceptions.RuntimeError("Invalid continue instruction outside loop.",instruction.Token.Location, self.filename)
        scope.Continue = True
        pscope = scope
        while pscope.isLoopRoot is False and pscope.Parent is not None:
            pscope = pscope.Parent
            pscope.Continue = True



    def InterpretHalt(self, instruction: ast_halt.Halt, scope: mscope.Scope) -> None:
        value = self.InterpretExpression(instruction.Exitcode, scope)
        var = scope.Root.GetVariable('exitcode')
        var.Value = value
        scope.SetHalt(True)


    
    def InterpretForeach(self, instruction: ast_foreach.Foreach, scope: mscope.Scope) -> None:
        val = self.InterpretExpression(instruction.Variable, scope)
        fes = scope.CreateTempScope('foreach')
        fes.isLoop = True
        fes.isLoopRoot = True
        it = fes.NewVariable(instruction.Variable.Token, 'it')
        fes.AddVariable(it)
        if val.Type == types.VariableTypes.String or val.Type == types.VariableTypes.Record:
            for v in val.Value:
                vv = value_item.ValueItem().SetFromMacal(val.Token, types.VariableTypes.String, v)
                if fes.Break or fes.Halt or fes.Return: break
                fes.Continue = False
                it.Value = vv
                self.InterpretBlock(instruction.Block, fes)
        else:
            for v in val.Value:
                if fes.Break or fes.Halt or fes.Return: break
                if fes.Continue: self.resetContinue(fes)
                it.Value = v
                self.InterpretBlock(instruction.Block, fes)
        

    
    def InterpretWhile(self, instruction: ast_while.While, scope: mscope.Scope) -> None:
        condition = self.InterpretExpression(instruction.Condition, scope)
        whs = scope.CreateTempScope('while')
        whs.isLoop = True
        whs.isLoopRoot = True
        infiniteLoopProtection = self.INFINITE_LOOP_PROTECTION_COUNT
        if self.INFINITE_LOOP_PROTECTION_COUNT == 0:
            infiniteLoopProtection = 1
        while condition.Value is True and infiniteLoopProtection > 0:
            if whs.Break or whs.Halt or whs.Return: break
            if whs.Continue: self.resetContinue(whs)
            self.InterpretBlock(instruction.Block, whs)
            condition = self.InterpretExpression(instruction.Condition, whs)
            if self.INFINITE_LOOP_PROTECTION_COUNT != 0:
                infiniteLoopProtection -= 1
        if infiniteLoopProtection == 0:
            raise exceptions.RuntimeError("Infinite loop protection engaged.",instruction.Token.Location, self.filename)



    def InterpretIf(self, instruction: ast_if.If, scope: mscope.Scope) -> None:
        condition = self.InterpretExpression(instruction.Condition, scope)
        ifs = scope.CreateTempScope('if')
        if condition.Value is True:
            self.InterpretBlock(instruction.Block, ifs)
        else:
            els = True
            if len(instruction.Elif) > 0:
                for elfi in instruction.Elif:
                    lifs = scope.CreateTempScope('elif')
                    condition = self.InterpretExpression(elfi.Condition, lifs)
                    if condition.Value is True:
                        els = False
                        self.InterpretBlock(elfi.Block, lifs)
                        break
            if els is True and instruction.Else is not None:
                esl = scope.CreateTempScope('else')
                self.InterpretBlock(instruction.Else, esl)



    def checkDataArray(self, arr, msg):
        if arr is None: return
        if not isinstance(arr, value_item.ValueItem):
            raise exceptions.RuntimeError(f'checkDataArray ({msg}), arr is not a value item and it should be.', None, self.filename)
        if isinstance(arr.Value, value_item.ValueItem):
            raise exceptions.RuntimeError(f'checkDataArray ({msg}), arr.Value is a value item and it should not be.', None, self.filename)
        if arr.Type == types.VariableTypes.Array and len(arr.Value) > 0:
            for rec in arr.Value:
                if not isinstance(rec, value_item.ValueItem):
                    raise exceptions.RuntimeError(f'checkDataArray ({msg}), arr.Value[n] is not a value item and it should be.', None, self.filename)



    def InterpretSelect(self, instruction: ast_select.Select, scope: mscope.Scope) -> None:
        data = self.InterpretExpression(instruction.From, scope)
        self.checkDataArray(data, 'data after init')
        into = self.EvaluateIntoVariable(instruction.Into, data, scope)
        
        if into is None:
            if instruction.Merge is True:
                raise exceptions.RuntimeError(f'Variable ({instruction.Into.Token.Lexeme}) not found.', instruction.Into.Token.Location, self.filename)
            intoVar = variable.Variable(instruction.Into.Token, instruction.Into.Token.Lexeme)
            if instruction.Distinct:
                intoVar.Value = value_item.ValueItem().SetFromMacal(instruction.Token, types.VariableTypes.Record, {})
            else:
                intoVar.Value = value_item.ValueItem().SetFromMacal(instruction.Token, types.VariableTypes.Array, [])
            scope.AddVariable(intoVar)
            into = intoVar.Value
        
        self.checkDataArray(into, 'into after init')

        
        if instruction.Where is not None and data is not None:
            data = self.InterpretSelectWhere(instruction.Where, data, scope)
        
        self.checkDataArray(data, 'data after where')

        if not(len(instruction.Fields) == 1 and instruction.Fields[0].Name == '*'):
            data = self.ApplyFieldFilters(data, instruction.Fields)
        self.checkDataArray(data, 'data after apply filters')

        if instruction.Distinct is True and data is not None and data.Type == types.VariableTypes.Array and len(data.Value) > 0:
            if isinstance(data.Value[0], value_item.ValueItem):
                data = data.Value[0]
            else:
                raise exceptions.RuntimeError(f'Debug Select (distinct): data.Value[0] is NOT ValueItem but it should!', data.Token.Location, self.filename)    

        self.checkDataArray(data, 'data after distinct')

        if data is not None and data.Type == types.VariableTypes.Array and len(data.Value) == 1:
            if isinstance(data.Value[0], value_item.ValueItem):
                data = data.Value[0]
            else:
                raise exceptions.RuntimeError(f'Debug Select (array of one 1, data.Value[0]): data.Value[0] is NOT ValueItem but it should!', data.Token.Location, self.filename)    
            
        self.checkDataArray(data, 'data after rec[0] 1st')

        if instruction.Merge is True and data is not None:
            data = self.InterpretSelectMerge(into, data)
        
        self.checkDataArray(data, 'data after merge')

        # second time is needed, just in case merge returns an array of 1 record..
        if data is not None and data.Type == types.VariableTypes.Array and len(data.Value) == 1:
            if isinstance(data.Value[0], value_item.ValueItem):
                data = data.Value[0]
            else:
                data = value_item.ValueItem().SetFromMacal(data.Token, types.VariableTypes.Record, data.Value[0])
                raise exceptions.RuntimeError(f'Debug Select line 8 (array of one 2, data.Value[0]): data.Value[0] is NOT ValueItem but it should!', data.Token.Location, self.filename)
        self.checkDataArray(data, 'data after rec[0] 2nd')
        if data is not None:
            self.SetIntoVariableValue(instruction.Into, data, scope)



    def SetIntoVariableValue(self, expr: ast_expr.Expr, data: value_item.ValueItem, scope: mscope.Scope) -> None:
        var = scope.FindVariable(expr.Token.Lexeme)
        if var is None:
            raise exceptions.RuntimeError(f'Variable ({expr.Token.Lexeme}) not found.', expr.Token.Location, self.filename)
        if expr.Left is None:
            var.Value = data
            return
        if expr.Left.ExprType == types.ExprTypes.VariableIndex:
            self.SetIndexedIntoVariableValue(var, expr.Left, data, scope)
            return
        raise exceptions.RuntimeError(f'Variable ({expr.Token.Lexeme}) has an invalid left hand expression type: {expr.Left.ExprType}.', expr.Token.Location, self.filename)


    
    def SetIndexedIntoVariableValue(self, var: variable.Variable, idx: ast_expr.Expr, data: value_item.ValueItem, scope: mscope.Scope)-> None:
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
            i = self.InterpretExpression(ind, scope)
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



    def ApplyFieldFilters(self, data: value_item.ValueItem, fields: typing.List[ast_select_field.SelectField]) -> value_item.ValueItem:
        # in select we already gate for * as field, so we don't have to check for that.
        if data is None:
            returnData = value_item.ValueItem().SetFromMacal(rec.Token, rec.Type, {})
            for fld in fields:
                returnData.Value[fld.AsName] = value_item.ValueItem().SetFromMacal(None, types.VariableTypes.Nil, types.VariableTypes.Nil)
        elif data.Type == types.VariableTypes.Array:
            returnData = value_item.ValueItem().SetFromMacal(data.Token, data.Type, [])
            for rec in data.Value:
                r = value_item.ValueItem().SetFromMacal(rec.Token, rec.Type, {})
                for fld in fields:
                    if fld.Name in rec.Value:
                        r.Value[fld.AsName] = rec.Value[fld.Name]
                    else:
                        r.Value[fld.AsName] = value_item.ValueItem().SetFromMacal(None, types.VariableTypes.Nil, types.VariableTypes.Nil)
                returnData.Value.append(r)
        elif data.Type == types.VariableTypes.Record:
            rec = data
            r = value_item.ValueItem().SetFromMacal(rec.Token, rec.Type, {})
            for fld in fields:
                if fld.Name in rec.Value:
                    r.Value[fld.AsName] = rec.Value[fld.Name]
                else:
                    r.Value[fld.AsName] = value_item.ValueItem().SetFromMacal(None, types.VariableTypes.Nil, types.VariableTypes.Nil)
            returnData = r
        else: # just not filter if it's something we didn't anticipate.
            returnData = data
        return returnData



    def InterpretSelectWhere(self, expr: ast_expr.Expr, data: value_item.ValueItem, scope:mscope.Scope)-> value_item.ValueItem:
        if data.Type == types.VariableTypes.Array:
            returnData = value_item.ValueItem().SetFromMacal(data.Token, data.Type, [])
            for rec in data.Value:
                res = self.EvaluateDatafieldExpression(expr, rec, scope)
                if res.Value is True:
                    returnData.Value.append(rec)
        else:
            returnData = value_item.ValueItem().SetFromMacal(data.Token, types.VariableTypes.Record, {})
            self.EvaluateDatafieldExpression(expr, data, scope)
            if res.Value is True:
                returnData = data
        return returnData



    def CompareRecordFieldSets(self, rec1: value_item.ValueItem, rec2: value_item.ValueItem) -> bool:
        # returns true if both field sets are the same, false if not.
        if set(rec1.Value.keys()) == set(rec2.Value.keys()):
            return True
        return False



    def InterpretSelectMerge(self, into: value_item.ValueItem, data: value_item.ValueItem)-> value_item.ValueItem:
        if (into.Type == types.VariableTypes.Record and data.Type == types.VariableTypes.Record):
            # both records, we need to check if the set of fields is the same.
            if self.CompareRecordFieldSets(into, data):
                returnData = value_item.ValueItem().SetFromMacal(into.Token, types.VariableTypes.Array, [])
                returnData.Value.append(into)
                returnData.Value.append(data)
                return returnData
            else:
                returnData = into
                for key, value in data.Value.items():
                    returnData.Value[key] = value
                return returnData
        returnData = value_item.ValueItem().SetFromMacal(into.Token, types.VariableTypes.Array, [])
        if into.Type == types.VariableTypes.Array:
            for rec in into.Value:
                returnData.Value.append(rec)
        # Into can be nil here, so we must check.
        elif into.Type == types.VariableTypes.Record:
            returnData.Value.append(into)
        if data.Type == types.VariableTypes.Array:
            for rec in data.Value:
                returnData.Value.append(rec)
        # Data should always be record or array, but just to be sure we check.
        elif data.Type == types.VariableTypes.Record:
            returnData.Value.append(data)
        return returnData



    def EvaluateDatafieldExpression(self, expr: ast_expr.Expr, rec: value_item.ValueItem, scope: mscope.Scope) -> value_item.ValueItem:
        if expr.ExprType == types.ExprTypes.Variable:
            return self.EvaluateDatafieldVariable(expr, rec, scope)
        if expr.ExprType == types.ExprTypes.Literal:
            return self.EvaluateDatafieldLiteral(expr, rec, scope)
        if expr.ExprType == types.ExprTypes.Binary:
            return self.EvaluateDatafieldBinary(expr, rec, scope)
        if expr.ExprType == types.ExprTypes.Unary:
            return self.EvaluateDatafieldUnary(expr, rec, scope)
        if expr.ExprType == types.ExprTypes.Grouping:
            return self.EvaluateDatafieldGrouping(expr, rec, scope)
        if expr.ExprType == types.ExprTypes.Function:
            return self.evaluateDatafieldFunction(expr, rec, scope)
        raise exceptions.RuntimeError(f'Unknown datafield expression type ({expr.ExprType}).', expr.Token.Location, self.filename)



    def EvaluateDatafieldLiteral(self, expr: ast_expr.Expr, rec: value_item.ValueItem, scope: mscope.Scope) -> value_item.ValueItem:
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
            value.SetValue(expr.Token, expr.LiteralValueType, self.filename)
        return value



    def EvaluateDatafieldBinary(self, expr: ast_expr.Expr, rec: value_item.ValueItem, scope: mscope.Scope) -> value_item.ValueItem:
        left = self.EvaluateDatafieldExpression(expr.Left, rec, scope)
        if expr.Operator.Lexeme == 'and' and left.Value is False:
            return left
        if expr.Operator.Lexeme == 'or' and left.Value is True:
            return left
        right = self.EvaluateDatafieldExpression(expr.Right, rec, scope)
        self.BinaryExpressionOperandsTypeCheck(left, right, expr.Operator.Lexeme)
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



    def EvaluateDatafieldVariable(self, expr: ast_expr.Expr, rec: value_item.ValueItem, scope: mscope.Scope) -> value_item.ValueItem:
        if expr.Token.Lexeme in rec.Value:
            return rec.Value[expr.Token.Lexeme]
        val = self.EvaluateIntoVariable(expr, rec, scope)
        if val is None:
            raise exceptions.RuntimeError(f'Variable ({expr.Token.Lexeme}) not found.', expr.Token.Location, self.filename)
        return val
        


    def EvaluateIntoVariable(self, expr: ast_expr.Expr, rec: value_item.ValueItem, scope: mscope.Scope) -> value_item.ValueItem:
        var = scope.FindVariable(expr.Token.Lexeme)
        if var is None:
            return None
        if expr.Left is None:
            return var.Value
        if expr.Left.ExprType == types.ExprTypes.VariableIndex:
            return self.EvaluateDatafieldIndexedVariable(var, expr.Left, rec, scope)
        raise exceptions.RuntimeError(f'Variable ({expr.Token.Lexeme}) has an invalid left hand expression type: {expr.Left.ExprType}.', expr.Token.Location, self.filename)



    def EvaluateDatafieldIndexedVariable(self, var: variable.Variable, idx: ast_expr.Expr, rec: dict, scope: mscope.Scope)-> value_item.ValueItem:
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
            i = self.InterpretExpression(ind, scope)
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



    def EvaluateDatafieldUnary(self, expr: ast_expr.Expr, rec: dict, scope: mscope.Scope) -> value_item.ValueItem:
        val = self.EvaluateDatafieldExpression(expr.Right, rec, scope).Clone()
        if expr.Operator.Lexeme == '-':
            val.Value *= -1
        if expr.Operator.Lexeme == '!':
            if val.Type != types.VariableTypes.Bool:
                raise exceptions.RuntimeError(f"Invalid type ({val.Type}), not a boolean.", val.Token.Location, self.filename)
            val.Value = not val.Value
        return val



    def EvaluateDatafieldGrouping(self, expr: ast_expr.Expr, rec: dict, scope: mscope.Scope) -> value_item.ValueItem:
        return self.EvaluateDatafieldExpression(expr.Left, rec, scope)
        
