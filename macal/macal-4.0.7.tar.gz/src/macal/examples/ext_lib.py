# Product:   Macal
# Author:    Marco Caspers
# Date:      07-10-2022
#

import macal

def strRight(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of right function"""
    macal.validateFunctionArguments(func, scope, filename)
    arg = scope.getVariable("arg")
    argl = scope.getVariable("length")
    value = arg.getValue()
    length = argl.getValue()
    endpos = len(value)
    start = endpos - length
    result = scope.RunFunction('mid', scope, arg=arg, start=start, length=length)
    scope.setReturnValue(result)
    