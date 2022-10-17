#
# Product:   Macal
# Author:    Marco Caspers
# Date:      09-09-2022
#

from . import ast
from . import types
from . import token


class Expr(ast.AST):
    def __init__(self, tok: token.LexToken) -> None:
        super().__init__(tok, types.AstTypes.Expr)
        self.Left = None
        self.Operator: token.LexToken = None
        self.Right = None
        self.ExprType: types.ExprTypes = None
        self.LiteralValueType: types.VariableType = None
        self.Indexed: bool = False



    def Binary(self, left: token.LexToken, operator: token.LexToken, right: token.LexToken) -> None:
        self.Left = left
        self.Operator = operator
        self.Right = right
        self.ExprType = types.ExprTypes.Binary
        return self
    


    def Unary(self, operator: token.LexToken, right: token.LexToken) -> None:
        self.Right = right
        self.Operator = operator
        self.ExprType = types.ExprTypes.Unary
        return self


    
    def Literal(self, valType: types.VariableType) -> None:
        self.LiteralValueType = valType
        self.ExprType = types.ExprTypes.Literal
        return self



    def Grouping(self, left: token.LexToken) -> None:
        self.Left = left
        self.ExprType = types.ExprTypes.Grouping
        return self

    

    def Variable(self, valType: types.VariableType) -> None:
        self.LiteralValueType = valType
        self.ExprType = types.ExprTypes.Variable
        return self



    def VariableIndex(self, left: token.LexToken, right: token.LexToken) -> None:
        self.Left = left
        self.Right = right
        self.ExprType = types.ExprTypes.VariableIndex
        return self



    def VariableIndexStart(self):
        self.ExprType = types.ExprTypes.VariableIndexStart
        return self



    def NewArrayIndex(self) -> None:
        self.ExprType = types.ExprTypes.NewArrayIndex;
        return self



    def InterpolationPart(self, right: token.LexToken) -> None:
        self.Right = right
        self.ExprType = types.ExprTypes.InterpolationPart
        return self



    def Argument(self, left: token.LexToken) -> None:
        self.Left = left
        self.ExprType = types.ExprTypes.FunctionArgument
        return self



    def __str__(self):
        s = self
        if self.ExprType == types.ExprTypes.Binary:
            s= f'Expr.Binary: {self.Left} {self.Operator.Lexeme} {self.Right}'
        if self.ExprType == types.ExprTypes.Unary:
            s= f'Expr.Unary: {self.Operator.Lexeme}{self.Right}'
        if self.ExprType == types.ExprTypes.InterpolationPart:
            s= f'Expr.InterpolationPart: {self.Right}'
        if self.ExprType == types.ExprTypes.VariableIndex:
            s= f'Expr.VariableIndex: \n L: {self.Left} \n R: {self.Right}]'
        if self.ExprType == types.ExprTypes.Variable:
            s= f'Expr.Variable: {self.Token.Lexeme}'
        if self.ExprType == types.ExprTypes.Grouping:
            s= f'Expr.Grouping: ({self.Left})'
        if self.ExprType == types.ExprTypes.Literal:
            s= f'Expr.Literal: {self.Token.Lexeme} (Type: {self.Token.Type})'
        if self.ExprType == types.ExprTypes.FunctionCall:
            s= f'Expr.FunctionCall: {self.Token.Lexeme}{self.Right}'
        if self.ExprType == types.ExprTypes.ArgumentList:
            s= f"Expr.ArgumentList: ({', '.join(f'{item}' for item in self.Left)})"
        if self.ExprType == types.ExprTypes.FunctionArgument:
            s= f"Expr.FunctionArgument: ({self.Left})"
        if self.ExprType == types.ExprTypes.NewArrayIndex:
            s= 'Expr.NewArrayIndex: []'
        if self.ExprType == types.ExprTypes.VariableIndexStart:
            s = 'Expr.VariableIndexStart: ['
        return s