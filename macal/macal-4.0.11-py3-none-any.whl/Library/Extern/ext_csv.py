# Product:   Macal
# Author:    Marco Caspers
# Date:      27-09-2022
#

import macal

def headersToCsv(func:macal.FunctionDefinition, scope: macal.Scope, filename: str):
    """Implementation of HeadersToCsv function"""
    macal.validateFunctionArguments(func, scope, filename)
    rec = scope.getVariable("rec")
    rec = rec.getValue()
    result = None
    try:
        separator = '","'
        result = f'"{separator.join(rec)}"'
    except Exception as e:
        raise macal.RuntimeError(e, rec.Token.Location, filename)
    scope.setReturnValue(result)



def valuesToCsv(func:macal.FunctionDefinition, scope: macal.Scope, filename: str):
    """Implementation of ValuesToCsv function"""
    macal.validateFunctionArguments(func, scope, filename)
    rec = scope.getVariable("rec")
    rec = rec.getValue()
    result = None
    try:
        temp = []
        for fld in rec:
            temp.append(f'"{rec[fld]}"')
        separator = ','
        result = separator.join(temp)
    except Exception as e:
        raise macal.RuntimeError(e, rec.Token.Location, filename)
    scope.setReturnValue(result)



def arrayToCsv(func:macal.FunctionDefinition, scope: macal.Scope, filename: str):
    """Implementation of ArrayToCsv function"""
    macal.validateFunctionArguments(func, scope, filename)
    arr = scope.getVariable("arr")
    arr = arr.getValue()
    try:
        temp = []
        for fld in arr:
            temp.append(f'"{fld}"')
        separator = ','
        result = separator.join(temp)
    except Exception as e:
        raise macal.RuntimeError(e, arr.Token.Location, filename)
    scope.setReturnValue(result)
