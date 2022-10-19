# Product:   Macal
# Author:    Marco Caspers
# Date:      27-09-2022
#

"""Macal system library implementation"""


import macal
from math import floor, ceil, cos, acos, sin, asin, tan, atan, pow, sqrt, log, log2, log10, exp, expm1



def math_round(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of round function"""
    x = scope.GetVariable("x")
    if x is None:
        raise macal.RuntimeError('Round requires at least one argument.', func.Token.Location, filename)
    rval = x.GetValue()
    digits = scope.GetVariable("digits")
    if digits is None:
        scope.SetReturnValue(round(rval))
    else:
        dval = digits.GetValue()
        scope.SetReturnValue(round(rval, dval))



def math_floor(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of floor function"""
    macal.ValidateFunctionArguments(func, scope, filename)
    x = scope.GetVariable("x")
    rval = x.GetValue()
    scope.SetReturnValue(floor(rval))



def math_ceil(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of ceil function"""
    macal.ValidateFunctionArguments(func, scope, filename)
    x = scope.GetVariable("x")
    rval = x.GetValue()
    scope.SetReturnValue(ceil(rval))



def math_cos(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of cos function"""
    macal.ValidateFunctionArguments(func, scope, filename)
    x = scope.GetVariable("x")
    rval = x.GetValue()
    scope.SetReturnValue(cos(rval))



def math_acos(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of acos function"""
    macal.ValidateFunctionArguments(func, scope, filename)
    x = scope.GetVariable("x")
    rval = x.GetValue()
    scope.SetReturnValue(acos(rval))



def math_sin(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of sin function"""
    macal.ValidateFunctionArguments(func, scope, filename)
    x = scope.GetVariable("x")
    rval = x.GetValue()
    scope.SetReturnValue(sin(rval))



def math_asin(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of asin function"""
    macal.ValidateFunctionArguments(func, scope, filename)
    x = scope.GetVariable("x")
    rval = x.GetValue()
    scope.SetReturnValue(asin(rval))



def math_tan(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of tan function"""
    macal.ValidateFunctionArguments(func, scope, filename)
    x = scope.GetVariable("x")
    rval = x.GetValue()
    scope.SetReturnValue(tan(rval))



def math_atan(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of atan function"""
    macal.ValidateFunctionArguments(func, scope, filename)
    x = scope.GetVariable("x")
    rval = x.GetValue()
    scope.SetReturnValue(atan(rval))



def math_sqrt(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of sqrt function"""
    macal.ValidateFunctionArguments(func, scope, filename)
    x = scope.GetVariable("x")
    rval = x.GetValue()
    scope.SetReturnValue(sqrt(rval))



def math_log(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of log function"""
    macal.ValidateFunctionArguments(func, scope, filename)
    x = scope.GetVariable("x")
    rval = x.GetValue()
    scope.SetReturnValue(log(rval))



def math_log2(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of log2 function"""
    macal.ValidateFunctionArguments(func, scope, filename)
    x = scope.GetVariable("x")
    rval = x.GetValue()
    scope.SetReturnValue(log2(rval))



def math_log10(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of log10 function"""
    macal.ValidateFunctionArguments(func, scope, filename)
    x = scope.GetVariable("x")
    rval = x.GetValue()
    scope.SetReturnValue(log10(rval))



def math_exp(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of exp function"""
    macal.ValidateFunctionArguments(func, scope, filename)
    x = scope.GetVariable("x")
    rval = x.GetValue()
    scope.SetReturnValue(exp(rval))



def math_expm1(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of expm1 function"""
    macal.ValidateFunctionArguments(func, scope, filename)
    x = scope.GetVariable("x")
    rval = x.GetValue()
    scope.SetReturnValue(expm1(rval))
