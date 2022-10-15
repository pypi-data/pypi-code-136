#
# Product:   Macal
# Author:    Marco Caspers
# Date:      07-09-2022
#


class LexTokenType(set):
    """Enum for lexer token types"""
    def __getattr__(self, name) -> str:
        if name in self:
            return name
        raise AttributeError(name)



LexTokenTypes = LexTokenType([
    'Operator',
    'Identifier',
    'Punctuation',
    'Comment',
    'String',
    'Number',
    'Whitespace',
    'InterpolationStart',
    'InterpolationEnd',
    'InterpolationOp',
    'Nil'])



class AstType(set):
    """Enum for parser AST types"""
    def __getattr__(self, name) -> str:
        if name in self:
            return name
        raise AttributeError(name)



AstTypes = AstType([
    'AST',
    'Expr',
    'FunctionDefinition',
    'FunctionCall',
    'Block',
    'Assignment',
    'If',
    'Elif',
    'Else',
    'Break',
    'Continue',
    'Halt',
    'Select',
    'SelectField',
    'Foreach',
    'While',
    'Return',
    'Include'
])



class ExprType(set):
    """Enum for Expression types"""
    def __getattr__(self, name) -> str:
        if name in self:
            return name
        raise AttributeError(name)


ExprTypes = ExprType([
    'Binary',
    'Unary',
    'Literal',
    'Grouping',
    'Variable',
    'FunctionCall',
    'FunctionArgument',
    'VariableIndexStart',
    'VariableIndex',
    'NewArrayIndex',
    'ArgumentList',
    'InterpolationPart'
])



class VariableType(set):
    """Enum for Variable value types"""
    def __getattr__(self, name) -> str:
        if name in self:
            return name
        raise AttributeError(name)



VariableTypes = VariableType([
    'Array',
    'Bool',
    'Int',
    'Float',
    'Function',
    'Nil',
    'Params',
    'Record',
    'String',
    'Type',
    'Variable'
])


