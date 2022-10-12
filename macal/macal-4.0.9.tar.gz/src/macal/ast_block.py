#
# Product:   Macal
# Author:    Marco Caspers
# Date:      12-09-2022
#

from . import ast
from . import types
from . import token
import typing


class Block(ast.AST):
    def __init__(self, tok: token.LexToken) -> None:
        super().__init__(tok, types.AstTypes.Block)
        self.Instructions : typing.List[ast.AST]= []



    def Add(self, instruction: ast.AST) -> None:
        self.Instructions.append(instruction)


    
    def __iter__(self) -> typing.Iterator:
        return iter(self.Instructions)



    def __repr__(self) -> str:
        return f"block({{}}), {self.Location}"


    def __str__(self) -> str:
        instr = '\n'.join([f"{instr}" for instr in self.Instructions])
        return f'{{\n {instr} }}\n'        

        