# Product:   Macal
# Author:    Marco Caspers
# Date:      07-10-2022
#

import macal

def strRight(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of right function"""
    macal.ValidateFunctionArguments(func, scope, filename)
    arg = scope.GetVariable("arg")
    argl = scope.GetVariable("length")
    value = arg.GetValue()
    length = argl.GetValue()
    endpos = len(value)
    start = endpos - length
    result = scope.RunFunction('Mid', scope, arg=arg, start=start, length=length)
    scope.SetReturnValue(result)
    