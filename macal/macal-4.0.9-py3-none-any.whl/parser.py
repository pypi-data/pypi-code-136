#
# Product:   Macal
# Author:    Marco Caspers
# Date:      09-09-2022
#

import typing
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
from . import types
from . import exceptions


class Parser:
    def __init__(self) -> None:
        """Initialize the Parser"""
        self.version: str = __about__.__version__
        self.source: typing.List[token.LexToken]
        self.filename: str
        self.length = 0
        self.Debug = False



    def Current(self, index: int) -> token.LexToken:
        """Retrieves the token at index"""
        if index < self.length:
            return self.source[index]
        return None



    def Next(self, index: int) -> typing.Tuple[int, token.LexToken]:
        """Increases the index and retrieves the token at that index"""
        index += 1
        if index >= 0 and index < self.length:
            return (index, self.source[index])
        return (index, None)



    def Peek(self, index: int, offset: int) -> token.LexToken:
        """Retrieves a token at index + offset"""
        if index + offset < self.length and index+offset >= 0:
            return self.source[index+offset]
        return None



    def Previous(self, index: int) -> token.LexToken:
        """Retrieves a token at index - 1"""
        return self.Peek(index, -1)



    def Match(self, index: int, type: types.LexTokenType, lex: str = None) -> typing.Tuple[int, bool]:
        # can't do | typing.List[str] for lex arg here, cause, versions..
        current = self.Current(index)
        if current is None:
            return (index, None)
        if current.Type == type:
            if lex is None:
                (index, _) = self.Next(index)
                return (index, True)
            if isinstance(lex, str):
                if current.Lexeme == lex:
                    (index, _) = self.Next(index)
                    return (index, True)
                return (index, False)
            if current.Lexeme in lex:
                (index, _) = self.Next(index)
                return (index, True)
        return (index, False)



    def Consume(self, index: int, message: str, type: types.LexTokenType, lex: str = None) -> int:
        (index, match) = self.Match(index, type, lex)
        if not match:
            current = self.Current(index)
            if current is None:
                raise exceptions.ParserError(message = f'{message} ({type}, {lex})', loc = None ,filename = self.filename)
            else:
                raise exceptions.ParserError(message = f'{message} ({type}, {current.Type}, {lex}, {current.Lexeme})', loc = current.Location ,filename = self.filename)
        return index



    def Reset(self) -> None:
        """Resets the current state. Do not Use."""
        self.source = []
        self.length = 0



    def Parse(self, source: typing.List[token.LexToken], filename: str) -> typing.List[ast.AST]:
        """Parse the provided source list of tokens"""
        if source is None or (isinstance(source, list) and len(source) == 0):
            raise exceptions.ParserError(message = "No source to parse.", loc = None, filename = filename)
        # we remove whitespace and comments because they have no syntactic meaning.
        # This means that we can end up with an empty list in case there was only whitespace and/or comments, but that is not a problem.
        self.source = [token for token in source if token.Type is not types.LexTokenTypes.Whitespace and token.Type is not types.LexTokenTypes.Comment]
        self.filename = filename
        self.length = len(self.source)
        index = 0
        instructions = []
        while index < self.length:
            #try:
            (index, instruction) = self.ParseInstruction(index)
            if instruction is not None:
                instructions.append(instruction)
            #except Exception as ex:
            #    if self.Debug: print(ex)
            #    break
            
        return instructions



    def Expression(self, index: int, inFnDef: bool = False) -> typing.Tuple[int, ast.AST]:
        if self.Debug: print("expr")
        if self.Debug: print(self.Current(index))
        (index, expr) = self.Boolean(index, inFnDef)
        return (index, expr)



    def Boolean(self, index: int, inFnDef: bool = False) -> typing.Tuple[int, ast.AST]:
        if self.Debug: print("bool")
        (index, expr) = self.Equality(index, inFnDef)
        (index, match) = self.Match(index, types.LexTokenTypes.Identifier, ['and', 'or'])
        while match:
            operator = self.Previous(index)
            (index, right) = self.Equality(index, inFnDef)
            expr = ast_expr.Expr(self.Previous(index)).Binary(expr, operator, right)
            (index, match) = self.Match(index, types.LexTokenTypes.Identifier, ['and', 'or'])
        return (index, expr)



    def Equality(self, index: int, inFnDef: bool = False) -> typing.Tuple[int, ast.AST]:
        if self.Debug: print("eq")
        (index, expr) = self.Comparison(index, inFnDef)
        (index, match) = self.Match(index, types.LexTokenTypes.Operator, ['!=', '=='])
        while match:
            operator = self.Previous(index)
            (index, right) = self.Comparison(index, inFnDef)
            expr = ast_expr.Expr(self.Previous(index)).Binary(expr, operator, right)
            (index, match) = self.Match(index, types.LexTokenTypes.Operator, ['!=', '=='])
        return (index, expr)


    
    def Comparison(self, index: int, inFnDef: bool = False) -> typing.Tuple[int, ast.AST]:
        if self.Debug: print("comp")
        (index, expr) = self.Term(index, inFnDef)
        (index, match) = self.Match(index, types.LexTokenTypes.Operator, ['<=', '<', '>', '>='])
        while match:
            operator = self.Previous(index)
            (index, right) = self.Term(index, inFnDef)
            expr = ast_expr.Expr(self.Previous(index)).Binary(expr, operator, right)
            (index, match) = self.Match(index, types.LexTokenTypes.Operator, ['<=', '<', '>', '>='])
        return (index, expr)



    def Term(self, index: int, inFnDef: bool = False) -> typing.Tuple[int, ast.AST]:
        if self.Debug: print("term")
        (index, expr) = self.Factor(index, inFnDef)
        (index, match) = self.Match(index, types.LexTokenTypes.Operator, ['+', '-'])
        while match:
            operator = self.Previous(index)
            (index, right) = self.Factor(index, inFnDef)
            expr = ast_expr.Expr(self.Previous(index)).Binary(expr, operator, right)
            (index, match) = self.Match(index, types.LexTokenTypes.Operator, ['+', '-'])
        return (index, expr)



    def Factor(self, index: int, inFnDef: bool = False) -> typing.Tuple[int, ast.AST]:
        if self.Debug: print("factor")
        (index, expr) = self.Pm(index, inFnDef)
        (index, match) = self.Match(index, types.LexTokenTypes.Operator, ['/', '*'])
        while match:
            operator = self.Previous(index)
            (index, right) = self.Pm(index, inFnDef)
            expr = ast_expr.Expr(self.Previous(index)).Binary(expr, operator, right)
            (index, match) = self.Match(index, types.LexTokenTypes.Operator, ['/', '*'])
        return (index, expr)



    def Pm(self, index: int, inFnDef: bool = False) -> typing.Tuple[int, ast.AST]:
        if self.Debug: print("pm")
        (index, expr) = self.Interpolate(index, inFnDef)
        (index, match) = self.Match(index, types.LexTokenTypes.Operator, ['^', '%'])
        while match:
            operator = self.Previous(index)
            (index, right) = self.Interpolate(index, inFnDef)
            expr = ast_expr.Expr(self.Previous(index)).Binary(expr, operator, right)
            (index, match) = self.Match(index, types.LexTokenTypes.Operator, ['^', '%'])
        return (index, expr)


    def Interpolate(self, index: int, inFnDef: bool = False) -> typing.Tuple[int, ast.AST]:
        if self.Debug: print("interpolate")
        (index, match) = self.Match(index, types.LexTokenTypes.InterpolationStart, '$')
        if match:
            left = self.Previous(index)
            operator = token.LexToken(lexeme = '$+', type=types.LexTokenTypes.InterpolationOp, loc=left.Location, index=index)
            (index, expr) = self.Unary(index, inFnDef) # we may need to revert back to skipping unary and going straight to primary, 
                                                       # but i think we need to preserve the structure of the algorithm.
            (index, match) = self.Match(index, types.LexTokenTypes.InterpolationEnd, '$')
            while not match:
                (index, right) = self.Expression(index, inFnDef) # This is very tricky, going all the way back up to expression.
                expr = ast_expr.Expr(right.Token).Binary(expr, operator, right)
                (index, match) = self.Match(index, types.LexTokenTypes.InterpolationEnd, '$')
            result = ast_expr.Expr(left).InterpolationPart(expr)
            if result.Right.ExprType != types.ExprTypes.Binary:
                raise exceptions.ParserError("Interpolation string doesn't contain interpolation.", expr.Token.Location, self.filename)
            return (index, result)
        (index, expr) = self.Unary(index, inFnDef)
        return (index, expr)

    

    def Unary(self, index: int, inFnDef: bool = False) -> typing.Tuple[int, ast.AST]:
        if self.Debug: print("unary")
        (index, match) = self.Match(index, types.LexTokenTypes.Operator, ['!', '+', '-'])
        if not match:
            (index, match) = self.Match(index, types.LexTokenTypes.Identifier, ['not'])
        if match:
            operator = self.Previous(index)
            (index, right) = self.Primary(index, inFnDef)
            expr = ast_expr.Expr(self.Previous(index)).Unary(operator, right)
            return (index, expr)
        (index, expr) = self.Primary(index, inFnDef)
        return (index, expr)



    def Grouping(self, index: int, inFnDef: bool = False) -> typing.Tuple[int, ast.AST]:
        if self.Debug: print("grouping")
        (index, expr) = self.Expression(index, inFnDef)
        index = self.Consume(index, 'Unbalanced grouping, ")" expected.', types.LexTokenTypes.Punctuation, ')')
        expr = ast_expr.Expr(self.Previous(index)).Grouping(expr)
        return (index, expr)



    def Primary(self, index: int, inFnDef: bool = False) -> typing.Tuple[int, ast.AST]:
        if self.Debug: print("primary")
        (index, match) = self.Match(index, types.LexTokenTypes.Identifier, ['true', 'false'])
        if match:
            if self.Debug: print("identifier")
            expr = ast_expr.Expr(self.Previous(index)).Literal(types.VariableTypes.Bool)
            return (index, expr)
        (index, match) = self.Match(index, types.LexTokenTypes.String)
        if match:
            if self.Debug: print("literal")
            expr = ast_expr.Expr(self.Previous(index)).Literal(types.VariableTypes.String)
            return (index, expr)
        (index, match) = self.Match(index, types.LexTokenTypes.Number)
        if match:
            if self.Debug: print("number literal")
            literal = self.Previous(index)
            valType = types.VariableTypes.Int
            if '.' in literal.Lexeme:
                valType = types.VariableTypes.Float
            expr = ast_expr.Expr(literal).Literal(valType)
            return (index, expr)
        (index, match) = self.Match(index, types.LexTokenTypes.Identifier, 'nil')
        if match:
            if self.Debug: print("nil")
            expr = ast_expr.Expr(self.Previous(index)).Literal(types.VariableTypes.Nil)
            return (index, expr)
        (index, match) = self.Match(index, 
                types.LexTokenTypes.Identifier, 
                [
                    'params',
                    'variable',
                    'any',
                    'string',
                    'int',
                    'float',
                    'bool',
                    'record',
                    'array',
                    'function'
                ])
        if inFnDef is True and match:
            if self.Debug: print("FnDefArg")
            (index, expr) = self.Argument(index)
            return (index, expr)
        elif match:
            if self.Debug: print("reserved words")
            tok = self.Previous(index)
            if tok.Lexeme == 'array':
                if self.Debug: print("array")
                expr = ast_expr.Expr(tok).Literal(types.VariableTypes.Array)
                return (index, expr)
            elif tok.Lexeme == 'record':
                if self.Debug: print("record")
                expr = ast_expr.Expr(tok).Literal(types.VariableTypes.Record)
                return (index, expr)
            else:
                raise exceptions.ParserError(message = f'Invalid use of reserved word. ({tok.Lexeme})', loc=tok.Location, filename=self.filename)       
        (index, match) = self.Match(index, types.LexTokenTypes.Identifier)
        if match:
            if self.Debug: print("Function Call or Variable")
            (index, expr) = self.FunctionCallOrVariable(index)
            return (index, expr)
        # grouping needs to be the last match, because technically a function call is also a grouping..
        (index, match) = self.Match(index, types.LexTokenTypes.Punctuation, '(')
        if match:
            if self.Debug: print("PRI_GRP")
            (index, expr) = self.Grouping(index)
            return (index, expr)        
        current = self.Current(index)
        raise exceptions.ParserError(message = f'Unexpected token ("{current.Lexeme}") in expression.', loc = current.Location, filename = self.filename)



    def __validateReservedWords(self, tok: token.LexToken):
        if tok.Lexeme in ['params', 'variable', 'int', 'bool', 'float', 'function', 'array', 'record', 'nil', 'any', 'string']:
            raise exceptions.ParserError(message = f'Invalid use of reserved word. ({tok.Lexeme})', loc=tok.Location, filename=self.filename)



    def Argument(self, index: int) -> typing.Tuple[int, ast.AST]:
        if self.Debug: print("Arg")
        tok = self.Previous(index)
        (index, match) = self.Match(index, types.LexTokenTypes.Identifier)
        if match:
            expr = ast_expr.Expr(tok).Argument(self.Previous(index))
            return (index, expr)
        self.__validateReservedWords(tok)
        raise exceptions.ParserError(message = f'Function argument definition requires an identifier. ({self.Current(index).Type})', loc=tok.Location, filename=self.filename)



    def getVariableIndexer(self, index: int) -> typing.Tuple[int, ast.AST]:
        (index, match) = self.Match(index, types.LexTokenTypes.Punctuation, '[')
        expr = ast_expr.Expr(self.Previous(index)).VariableIndexStart()

        (index, match) = self.Match(index, types.LexTokenTypes.Punctuation, ']')
        if match:
            nar = ast_expr.Expr(self.Previous(index)).NewArrayIndex()
            expr = ast_expr.Expr(self.Previous(index)).VariableIndex(expr, nar)
            return (index, expr)
        match = True
        while match:
            (index, match) = self.Match(index, types.LexTokenTypes.Punctuation, ']')
            if match:
                nar = ast_expr.Expr(self.Previous(index)).NewArrayIndex()
                expr = ast_expr.Expr(self.Previous(index)).VariableIndex(expr, nar)
                return (index, expr)
            (index, right) = self.Expression(index)
            expr = ast_expr.Expr(self.Previous(index)).VariableIndex(expr, right)
            (index, match) = self.Match(index, types.LexTokenTypes.Punctuation, ']')
            if not match:
                raise exceptions.ParserError(message = 'Unbalanced brackets, expected "]".', loc=self.Previous(index).Location, filename=self.filename)
            (index, match) = self.Match(index, types.LexTokenTypes.Punctuation, '[')
        #self.Consume(index, 'Unbalanced brackets, Expected "]" .', types.LexTokenTypes.Punctuation, ']')
        return (index, expr)



    def FunctionCallArgumentList(self, index: int, inFnDef: bool = False) -> typing.Tuple[int, ast.AST]:
        if self.Debug: print("FunctionCallArgumentList")
        (index, match) = self.Match(index, types.LexTokenTypes.Punctuation, '(')
        if not match:
            raise exceptions.ParserError(message='Missing parenthesis, expected "(".', loc=self.Previous(index).Location,filename = self.filename)
        expr = ast_expr.Expr(self.Previous(index))
        expr.ExprType = types.ExprTypes.ArgumentList
        expr.Left = []
        (index, match) = self.Match(index, types.LexTokenTypes.Punctuation, ')')
        while not match and index < self.length:
            (index, left) = self.Expression(index, inFnDef)
            expr.Left.append(left)
            (index, match) = self.Match(index, types.LexTokenTypes.Punctuation, ',')
            if match:
                (index, match) = self.Match(index, types.LexTokenTypes.Punctuation, ')')
                if match:
                    raise exceptions.ParserError(message='Unexpected ")", expected expression after comma (",").', loc=self.Previous(index).Location,filename = self.filename)
            else:
                (index, match) = self.Match(index, types.LexTokenTypes.Punctuation, ')')
        if not match:
            raise exceptions.ParserError(message='Unbalanced parenthesis, expected ")".', loc=expr.Token.Location, filename = self.filename)
        return (index, expr)



    def FunctionCallOrVariable(self, index: int, inFnDef: bool = False) -> typing.Tuple[int, ast.AST]:
        if self.Debug: print("FNCOV")
        expr = ast_expr.Expr(self.Previous(index)) # the identifier.
        if self.Current(index).Lexeme == '[':
            if self.Debug: print("VarIndexer")
            (index, varIndex) = self.getVariableIndexer(index)
            expr.Indexed = True
            expr.Left = varIndex
        if self.Current(index).Lexeme == '(':
            if self.Debug: print("FNCall")
            expr.ExprType = types.ExprTypes.FunctionCall
            (index, expr.Right) = self.FunctionCallArgumentList(index, inFnDef)
        else:
            if self.Debug: print("Var")
            expr.ExprType = types.ExprTypes.Variable
        return (index, expr)



    def ParseFunctionDefinition(self, index, identifier: token.LexToken) -> typing.Tuple[int, ast.AST]:
        if self.Debug: print("FunctionDefinition")
        instruction = ast_function_definition.FunctionDefinition(identifier)
        (index, instruction.Arguments) = self.FunctionCallArgumentList(index=index, inFnDef = True)
        (index, match) = self.Match(index, types.LexTokenTypes.Identifier, 'external')
        if match:
            instruction.IsExternal = True
            index = self.Consume(index=index, message = "Expected module name in external.", type = types.LexTokenTypes.String)
            instruction.ExternalModule = self.Previous(index)
            index = self.Consume(index, 'Expected ","', types.LexTokenTypes.Punctuation, ',')
            index = self.Consume(index=index, message = "Expected function name in external.", type = types.LexTokenTypes.String)
            instruction.ExternalFunction = self.Previous(index)
            index = self.Consume(index, 'Expected ";"', types.LexTokenTypes.Punctuation, ';')
            return(index, instruction)
        (index, instruction.Block) = self.ParseBlock(index)
        return (index, instruction)



    def ParseFunctionCall(self, index, identifier: token.LexToken, varIndex: ast_expr.Expr) -> typing.Tuple[int, ast.AST]:
        if self.Debug: print("ParseFunctionCall")
        instruction = ast_function_call.FunctionCall(identifier, varIndex)
        (index, expr) = self.FunctionCallArgumentList(index-1) # -1 because parse instruction consumed the opening bracket.
        if expr is None or expr.Left is None:
            raise exceptions.ParserError(message = 'Expected a function argument.', loc=self.Previous(index).Location, filename=self.filename)
        instruction.Args = expr.Left
        index = self.Consume(index, 'Expected ";"', types.LexTokenTypes.Punctuation, ';')
        return (index, instruction)

    

    def ParseInstruction(self, index: int) -> typing.Tuple[int, ast.AST]:
        if self.Debug: print()
        if self.Debug: print("Instruction")
        (index, match) = self.Match(index, types.LexTokenTypes.Punctuation, '{')
        if match:
            return self.ParseBlock(index)
        # any instruction starts with an identifier.
        index = self.Consume(
            index = index, 
            message ='Expected instruction identifier.', 
            type = types.LexTokenTypes.Identifier)
        identifier = self.Previous(index)
        if self.Debug: print(identifier)
        if self.Debug: print()
        if self.Debug: print("pk")
        (index, keyword) = self.ParseKeyword(index, identifier)
        if keyword is not None:
            return (index, keyword)
        varIndex = None       
        if self.Current(index).Lexeme == '[':
            if self.Debug: print("gvi")
            (index, varIndex) = self.getVariableIndexer(index)      
        (index, match) = self.Match(index, types.LexTokenTypes.Punctuation, '(')
        if match:
            if self.Debug: print("pfc")
            return self.ParseFunctionCall(index, identifier, varIndex)
        (index, match) = self.Match(index, types.LexTokenTypes.Operator, ['=', '+=', '-=', '/=', '*='])
        if match:
            if self.Debug: print("pa")
            return self.ParseAssign(index, identifier, varIndex)
        (index, match) = self.Match(index, types.LexTokenTypes.Operator, '=>')
        if match:
            if self.Debug: print("pfd")
            return self.ParseFunctionDefinition(index, identifier)
        if varIndex is not None:
            raise exceptions.ParserError(message = 'Invalid variable reference in instruction.', loc=identifier.Location, filename=self.filename)
        raise exceptions.ParserError(message = f'Unknown instruction or keyword ({identifier.Lexeme}).', loc=identifier.Location, filename=self.filename)



    def ParseKeyword(self, index: int, identifier: types.LexTokenType) -> typing.Tuple[int, ast.AST]:
        if self.Debug: print("Parse Keyword")
        if self.Debug: print(identifier.Lexeme)
        if identifier.Lexeme == 'if':
            return self.ParseIf(index, identifier)
        if identifier.Lexeme == 'foreach':
            return self.ParseForeach(index, identifier)
        if identifier.Lexeme == 'while':
            return self.ParseWhile(index, identifier)
        if identifier.Lexeme == 'halt':
            return self.ParseHalt(index, identifier)
        if identifier.Lexeme == 'break':
            return self.ParseBreak(index, identifier)
        if identifier.Lexeme == 'continue':
            return self.ParseContinue(index, identifier)
        if identifier.Lexeme == 'return':
            return self.ParseReturn(index, identifier)
        if identifier.Lexeme == 'include':
            return self.ParseInclude(index, identifier)
        if identifier.Lexeme == 'select':
            return self.ParseSelect(index, identifier)
        if identifier.Lexeme == 'const':
            return self.ParseConst(index, identifier)
        return (index, None)       



    def ParseBlock(self, index: int) -> typing.Tuple[int, ast.AST]:
        if self.Debug: print("Block")
        index = self.Consume(index=index, message='Expected block bracket "{".', type=types.LexTokenTypes.Punctuation, lex='{')
        block = ast_block.Block(self.Previous(index))
        (index, match) = self.Match(index, types.LexTokenTypes.Punctuation, '}')
        while not match and index < self.length:
            (index, instruction) = self.ParseInstruction(index)
            block.Add(instruction)
            (index, match) = self.Match(index, types.LexTokenTypes.Punctuation, '}')
        if not match:
            raise exceptions.ParserError(message = 'Unbalanced block bracket, expected "}".', loc=self.Previous(index).Location, filename=self.filename)
        return (index, block)



    def ParseAssign(self, index: int, identifier: types.LexTokenType, varIndex: ast_expr.Expr) -> typing.Tuple[int, ast.AST]:
        if self.Debug: print("Assign")
        operator = self.Previous(index)
        if operator.Lexeme not in ['=', '+=', '-=','/=', '*=']:
            raise exceptions.ParserError(message = f'Invalid assignment operator: {operator}.', loc=self.Previous(index).Location, filename=self.filename)
        assgn = ast_assignment.Assignment(identifier, varIndex, operator)
        (index, assgn.Value) = self.Expression(index)
        index = self.Consume(index, 'Expected ";"', types.LexTokenTypes.Punctuation, ';')
        return (index, assgn)



    def ParseConst(self, index: int, identifier: str) -> typing.Tuple[int, ast.AST]:
        if self.Debug: print("Const")
        (index, match) = self.Match(index, types.LexTokenTypes.Identifier)
        if match is False:
            raise exceptions.ParserError(message = f'Constant identifier required, got {self.Current(index).Type}.', loc=self.Current(index).Location, filename=self.filename)
        identifier = self.Previous(index)
        index = self.Consume(index, 'Expected "="', types.LexTokenTypes.Operator, '=')
        assgn = ast_assignment.Assignment(identifier, None, self.Previous(index))
        assgn.isConst = True
        (index, assgn.Value) = self.Expression(index)
        index = self.Consume(index, 'Expected ";"', types.LexTokenTypes.Punctuation, ';')
        return (index, assgn)



    def ParseIf(self, index: int, identifier: types.LexTokenType) -> typing.Tuple[int, ast.AST]:
        if self.Debug: print("If")
        instruction = ast_if.If(identifier)        
        (index, instruction.Condition) = self.Expression(index)
        if instruction.Condition is None:
            raise exceptions.ParserError(message = 'Expected a condition expression.', loc=self.Previous(index).Location, filename=self.filename)
        (index, instruction.Block) = self.ParseBlock(index)
        if instruction.Block is None:
            raise exceptions.ParserError(message = 'Expected a block ({}).', loc=self.Previous(index).Location, filename=self.filename)
        (index, match) = self.Match(index, types.LexTokenTypes.Identifier, 'elif')
        while match and index < self.length:
            elfi = ast_if.Elif(self.Previous(index))
            (index, elfi.Condition) = self.Expression(index)
            if elfi.Condition is None:
                raise exceptions.ParserError(message = 'Expected a condition expression.', loc=self.Previous(index).Location, filename=self.filename)
            (index, elfi.Block) = self.ParseBlock(index)
            if elfi.Block is None:
                raise exceptions.ParserError(message = 'Expected a block ({}).', loc=self.Previous(index).Location, filename=self.filename)
            instruction.Add(elfi)
            (index, match) = self.Match(index, types.LexTokenTypes.Identifier, 'elif')
        (index, match) = self.Match(index, types.LexTokenTypes.Identifier, 'else')
        if match:
            (index, instruction.Else) = self.ParseBlock(index)
            if instruction.Else is None:
                raise exceptions.ParserError(message = 'Expected a block ({}).', loc=self.Previous(index).Location, filename=self.filename)
        return (index, instruction)

    

    def ParseForeach(self, index: int, identifier: types.LexTokenType) -> typing.Tuple[int, ast.AST]:
        if self.Debug: print("Foreach")
        fe = ast_foreach.Foreach(identifier)
        (index, match) = self.Match(index, types.LexTokenTypes.Punctuation, '(')
        if match:
            raise exceptions.ParserError(message = 'Foreach is not a function, expected a variable.', loc=self.Previous(index).Location, filename=self.filename)
        (index, fe.Variable) = self.Expression(index)
        if fe.Variable is None:
            raise exceptions.ParserError(message = 'Expected a variable.', loc=self.Previous(index).Location, filename=self.filename)
        (index, fe.Block) = self.ParseBlock(index)
        if fe.Block is None:
            raise exceptions.ParserError(message = 'Expected a block ({}).', loc=self.Previous(index).Location, filename=self.filename)
        return (index, fe)



    def ParseBreak(self, index: int, identifier: types.LexTokenType) -> typing.Tuple[int, ast.AST]:
        brk = ast_break.Break(identifier)
        index = self.Consume(index, 'Expected ";"', types.LexTokenTypes.Punctuation, ';')
        return (index, brk)



    def ParseContinue(self, index: int, identifier: types.LexTokenType) -> typing.Tuple[int, ast.AST]:
        brk = ast_continue.Continue(identifier)
        index = self.Consume(index, 'Expected ";"', types.LexTokenTypes.Punctuation, ';')
        return (index, brk)



    def ParseHalt(self, index: int, identifier: types.LexTokenType) -> typing.Tuple[int, ast.AST]:
        brk = ast_halt.Halt(identifier)
        (index, match) = self.Match(index, types.LexTokenTypes.Punctuation, '(')
        if match:
            raise exceptions.ParserError(message = 'Halt is not a function, expected a variable or a literal value.', loc=self.Previous(index).Location, filename=self.filename)
        (index, brk.Exitcode) = self.Expression(index)
        if brk.Exitcode is None:
            raise exceptions.ParserError(message = 'Expected a variable or a literal value.', loc=self.Previous(index).Location, filename=self.filename)
        index = self.Consume(index, 'Expected ";"', types.LexTokenTypes.Punctuation, ';')
        return (index, brk)



    def ParseWhile(self, index: int, identifier: types.LexTokenType) -> typing.Tuple[int, ast.AST]:
        whl = ast_while.While(identifier)
        (index, match) = self.Match(index, types.LexTokenTypes.Punctuation, '(')
        if match:
            raise exceptions.ParserError(message = 'While is not a function, expected a condition.', loc=self.Previous(index).Location, filename=self.filename)
        (index, whl.Condition) = self.Expression(index)
        if whl.Condition is None:
            raise exceptions.ParserError(message = 'Expected a condition.', loc=self.Previous(index).Location, filename=self.filename)
        (index, whl.Block) = self.ParseBlock(index)
        if whl.Block is None:
            raise exceptions.ParserError(message = 'Expected a block ({}).', loc=self.Previous(index).Location, filename=self.filename)
        return (index, whl)
    


    def ParseReturn(self, index: int, identifier: types.LexTokenType) -> typing.Tuple[int, ast.AST]:
        if self.Debug: print("Return")
        ret = ast_return.Return(identifier)
        #if self.Debug: print("Match (")
        #(index, match) = self.Match(index, types.LexTokenTypes.Punctuation, '(')
        #if match:
        #    raise exceptions.ParserError(message = 'Return is not a function, expected a variable or a literal value.', loc=self.Previous(index).Location, filename=self.filename)
        if self.Debug: print("->e")            
        (index, ret.Value) = self.Expression(index)
        if self.Debug: print("vc")
        if ret.Value is None:
            raise exceptions.ParserError(message = 'Expected a variable or a literal value.', loc=self.Previous(index).Location, filename=self.filename)
        if self.Debug: print("vcc")            
        index = self.Consume(index, 'Expected ";"', types.LexTokenTypes.Punctuation, ';')
        return (index, ret)



    def ParseInclude(self, index: int, identifier: types.LexTokenType) -> typing.Tuple[int, ast.AST]:
        incl = ast_include.Include(identifier)
        (index, match) = self.Match(index, types.LexTokenTypes.Punctuation, '(')
        if match:
            raise exceptions.ParserError(message = 'Include is not a function, expected a module name.', loc=self.Previous(index).Location, filename=self.filename)
        (index, match) = self.Match(index, types.LexTokenTypes.Identifier)
        if not match:
            raise exceptions.ParserError(message = 'Expected a module name.', loc=self.Previous(index).Location, filename=self.filename)
        while match:
            incl.Add(self.Previous(index))
            (index, match) = self.Match(index, types.LexTokenTypes.Punctuation, ',')
            if match:
                (index, match) = self.Match(index, types.LexTokenTypes.Identifier)
                if not match:
                    raise exceptions.ParserError(message = 'Expected a module name.', loc=self.Previous(index).Location, filename=self.filename)
        index = self.Consume(index, 'Expected ";"', types.LexTokenTypes.Punctuation, ';')
        return (index, incl)



    def getSelectField(self, index: int) -> typing.Tuple[int, ast.AST]:
        all = False
        (index, match) = self.Match(index, types.LexTokenTypes.Identifier)
        if not match:
            (index, match) = self.Match(index, types.LexTokenTypes.Operator, '*')
            all = True
        if not match:
            raise exceptions.ParserError(message = 'Select requires a field name or *.', loc=self.Previous(index).Location, filename=self.filename)
        fld = ast_select_field.SelectField(self.Previous(index))
        if all:
            return (index, fld)
        (index, match) = self.Match(index, types.LexTokenTypes.Identifier, 'as')
        if not match:
            fld.As = fld.Token
            return (index, fld)
        (index, match) = self.Match(index, types.LexTokenTypes.Identifier)
        if not match:
            (index, match) = self.Match(index, types.LexTokenTypes.String)
        if not match:
            raise exceptions.ParserError(message = 'Select field as requires a field name or *.', loc=self.Previous(index).Location, filename=self.filename)
        fld.As = self.Previous(index)
        return (index, fld)



    def ParseSelect(self, index: int, identifier: types.LexTokenType) -> typing.Tuple[int, ast.AST]:
        sel = ast_select.Select(identifier)
        (index, match) = self.Match(index, types.LexTokenTypes.Identifier, 'distinct')
        if match:
            sel.Distinct = True
        (index, field) = self.getSelectField(index)
        sel.Fields.append(field)
        (index, match) = self.Match(index, types.LexTokenTypes.Punctuation, ',')
        while match and index < self.length:
            (index, field) = self.getSelectField(index)
            sel.Fields.append(field)
            (index, match) = self.Match(index, types.LexTokenTypes.Punctuation, ',')
        index = self.Consume(index=index, message = 'Select requires "from" after field names.', type=types.LexTokenTypes.Identifier, lex='from')
        (index, sel.From) = self.Expression(index)
        (index, match) = self.Match(index=index, type=types.LexTokenTypes.Identifier, lex='where')
        if match:
            (index, sel.Where) = self.Expression(index)       
        (index, match) = self.Match(index=index, type=types.LexTokenTypes.Identifier, lex='merge')
        if match:
            sel.Merge = True
        index = self.Consume(index=index, message = 'Select requires requires "into" <variable>.', type=types.LexTokenTypes.Identifier, lex='into')
        (index, sel.Into) = self.Expression(index)
        index = self.Consume(index, 'Expected ";"', types.LexTokenTypes.Punctuation, ';')
        return (index, sel)