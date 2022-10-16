# Product:   Macal
# Author:    Marco Caspers
# Date:      27-09-2022
#

import macal

def headersToCsv(func:macal.FunctionDefinition, scope: macal.Scope, filename: str):
    """Implementation of HeadersToCsv function"""
    macal.ValidateFunctionArguments(func, scope, filename)
    rec = scope.GetVariable("rec")
    rec = rec.GetValue()
    result = None
    try:
        separator = '","'
        result = f'"{separator.join(rec)}"'
    except Exception as e:
        raise macal.RuntimeError(e, rec.Token.Location, filename)
    scope.SetReturnValue(result)



def valuesToCsv(func:macal.FunctionDefinition, scope: macal.Scope, filename: str):
    """Implementation of ValuesToCsv function"""
    macal.ValidateFunctionArguments(func, scope, filename)
    rec = scope.GetVariable("rec")
    rec = rec.GetValue()
    result = None
    try:
        temp = []
        for fld in rec:
            temp.append(f'"{rec[fld]}"')
        separator = ','
        result = separator.join(temp)
    except Exception as e:
        raise macal.RuntimeError(e, rec.Token.Location, filename)
    scope.SetReturnValue(result)



def arrayToCsv(func:macal.FunctionDefinition, scope: macal.Scope, filename: str):
    """Implementation of ArrayToCsv function"""
    macal.ValidateFunctionArguments(func, scope, filename)
    arr = scope.GetVariable("arr")
    arr = arr.GetValue()
    try:
        temp = []
        for fld in arr:
            temp.append(f'"{fld}"')
        separator = ','
        result = separator.join(temp)
    except Exception as e:
        raise macal.RuntimeError(e, arr.Token.Location, filename)
    scope.SetReturnValue(result)
