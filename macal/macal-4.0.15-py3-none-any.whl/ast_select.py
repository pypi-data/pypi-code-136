#
# Product:   Macal
# Author:    Marco Caspers
# Date:      13-09-2022
#

import typing
from . import ast
from . import token
from . import types
from . import ast_expr
from . import ast_select_field

class Select(ast.AST):
    '''Contains the location in the source code.'''
    def __init__(self, tok: token.LexToken) -> None:
        super().__init__(tok, types.AstTypes.Select)
        self.Fields: typing.List[ast_select_field.SelectField] = []
        self.Distinct: bool = False
        self.From: ast_expr.Expr = None
        self.Where: ast_expr.Expr = None
        self.Merge: bool = False
        self.Into: ast_expr.Expr = None



    def __repr__(self):
        return f'Select(tok={self.Token})'



    def __str__(self):
        distinct = 'distinct ' if self.Distinct else ''
        fields = ', '.join([f'{field}' for field in self.Fields])
        where = f' {self.Where}' if self.Where is not None else ''
        merge = ' merge ' if self.Merge else ''
        return f'select {distinct}{fields} from {self.From}{where}{merge} into {self.Into}'
