# Product:   Macal
# Author:    Marco Caspers
# Date:      27-09-2022
#

"""Macal system library implementation"""


import macal
from math import floor, ceil, cos, acos, sin, asin, tan, atan, pow, sqrt, log, log2, log10, exp, expm1



def math_round(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of round function"""
    x = scope.getVariable("x")
    if x is None:
        raise macal.RuntimeError('Round requires at least one argument.', func.Token.Location, filename)
    rval = x.getValue()
    digits = scope.getVariable(digits)
    if digits is None:
        scope.setReturnValue(round(rval))
    else:
        dval = digits.getValue()
        scope.setReturnValue(round(rval, dval))



def math_floor(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of floor function"""
    macal.validateFunctionArguments(func, scope, filename)
    x = scope.getVariable("x")
    rval = x.getValue()
    scope.setReturnValue(floor(rval))



def math_ceil(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of ceil function"""
    macal.validateFunctionArguments(func, scope, filename)
    x = scope.getVariable("x")
    rval = x.getValue()
    scope.setReturnValue(ceil(rval))



def math_cos(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of cos function"""
    macal.validateFunctionArguments(func, scope, filename)
    x = scope.getVariable("x")
    rval = x.getValue()
    scope.setReturnValue(cos(rval))



def math_acos(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of acos function"""
    macal.validateFunctionArguments(func, scope, filename)
    x = scope.getVariable("x")
    rval = x.getValue()
    scope.setReturnValue(acos(rval))



def math_sin(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of sin function"""
    macal.validateFunctionArguments(func, scope, filename)
    x = scope.getVariable("x")
    rval = x.getValue()
    scope.setReturnValue(sin(rval))



def math_asin(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of asin function"""
    macal.validateFunctionArguments(func, scope, filename)
    x = scope.getVariable("x")
    rval = x.getValue()
    scope.setReturnValue(asin(rval))



def math_tan(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of tan function"""
    macal.validateFunctionArguments(func, scope, filename)
    x = scope.getVariable("x")
    rval = x.getValue()
    scope.setReturnValue(tan(rval))



def math_atan(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of atan function"""
    macal.validateFunctionArguments(func, scope, filename)
    x = scope.getVariable("x")
    rval = x.getValue()
    scope.setReturnValue(atan(rval))



def math_sqrt(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of sqrt function"""
    macal.validateFunctionArguments(func, scope, filename)
    x = scope.getVariable("x")
    rval = x.getValue()
    scope.setReturnValue(sqrt(rval))



def math_log(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of log function"""
    macal.validateFunctionArguments(func, scope, filename)
    x = scope.getVariable("x")
    rval = x.getValue()
    scope.setReturnValue(log(rval))



def math_log2(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of log2 function"""
    macal.validateFunctionArguments(func, scope, filename)
    x = scope.getVariable("x")
    rval = x.getValue()
    scope.setReturnValue(log2(rval))



def math_log10(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of log10 function"""
    macal.validateFunctionArguments(func, scope, filename)
    x = scope.getVariable("x")
    rval = x.getValue()
    scope.setReturnValue(log10(rval))



def math_exp(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of exp function"""
    macal.validateFunctionArguments(func, scope, filename)
    x = scope.getVariable("x")
    rval = x.getValue()
    scope.setReturnValue(exp(rval))



def math_expm1(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of expm1 function"""
    macal.validateFunctionArguments(func, scope, filename)
    x = scope.getVariable("x")
    rval = x.getValue()
    scope.setReturnValue(expm1(rval))
