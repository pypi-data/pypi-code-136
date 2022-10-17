#
# Product:   Macal
# Author:    Marco Caspers
# Date:      17-10-2022
#

# AST tree printer

import typing
from . import ast

def PrintAST(tree: typing.List[ast.AST]):
    for leaf in tree:
        print(leaf)
