# Product:   Macal
# Author:    Marco Caspers
# Date:      16-09-2022
#

"""Macal system library implementation"""

import macal
import platform


def Console(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    macal.ValidateFunctionArguments(func, scope, filename)
    args = scope.GetVariable("args")
    if args is None:
        print()
        return
    val = args.GetValue()
    txt = ' '.join([f'{arg}' for arg in val])
    print(txt)



def VarType(func: macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    macal.ValidateFunctionArguments(func, scope, filename)
    var = scope.GetVariable("var")
    val = var.GetValue()
    scope.SetReturnValue(val.GetType())
    rvar = scope.GetFunctionReturnVariable()
    rvar.Value.Type = macal.VariableTypes.Type



def Array(func: macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    macal.ValidateFunctionArguments(func, scope, filename)
    args = scope.GetVariable("args")
    if args is None:
        raise macal.RuntimeError('Required argument "args" not found.', func.Token.Location, filename)
    arr = []
    vargs = args.GetValue()
    for arg in vargs:
        arr.append(arg)
    scope.SetReturnValue(arr)
    

def RecordHasField(func: macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    macal.ValidateFunctionArguments(func, scope, filename)
    var = scope.GetVariable('fieldname')
    fieldname = var.GetValue()
    var = scope.GetVariable('rec')
    record = var.GetValue()
    if record is None:
        result = False
    else:
        result =  fieldname in record
    scope.SetReturnValue(result)



def IsString(func: macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    macal.ValidateFunctionArguments(func, scope, filename)
    var = scope.GetVariable("var")
    val = var.GetValue()
    result = val.GetType() == macal.VariableTypes.String
    scope.SetReturnValue(result)



def IsInt(func: macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    macal.ValidateFunctionArguments(func, scope, filename)
    var = scope.GetVariable("var")
    val = var.GetValue()
    result = val.GetType() == macal.VariableTypes.Int    
    scope.SetReturnValue(result)



def IsFloat(func: macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    macal.ValidateFunctionArguments(func, scope, filename)
    var = scope.GetVariable("var")
    val = var.GetValue()
    result = val.GetType() == macal.VariableTypes.Float
    scope.SetReturnValue(result)



def IsBool(func: macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    macal.ValidateFunctionArguments(func, scope, filename)
    var = scope.GetVariable("var")
    val = var.GetValue()
    result = val.GetType() == macal.VariableTypes.Bool
    scope.SetReturnValue(result)



def IsRecord(func: macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    macal.ValidateFunctionArguments(func, scope, filename)
    var = scope.GetVariable("var")
    val = var.GetValue()
    result = val.GetType() == macal.VariableTypes.Record
    scope.SetReturnValue(result)



def IsArray(func: macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    macal.ValidateFunctionArguments(func, scope, filename)
    var = scope.GetVariable("var")
    val = var.GetValue()
    result = val.GetType() == macal.VariableTypes.Array
    scope.SetReturnValue(result)



def IsFunction(func: macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    macal.ValidateFunctionArguments(func, scope, filename)
    var = scope.GetVariable("var")
    val = var.GetValue()
    result = val.GetType() == macal.VariableTypes.Function
    scope.SetReturnValue(result)



def IsNil(func: macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    macal.ValidateFunctionArguments(func, scope, filename)
    var = scope.GetVariable("var")
    val = var.GetValue()
    result = val.GetType() == macal.VariableTypes.Nil
    scope.SetReturnValue(result)



def GetPlatform(func: macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    scope.SetReturnValue(platform.system())


        
def ShowVersion(func: macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    print("Version: ",macal.__version__)
    print("Author:  ", macal.__author__)
    print("Credits:")
    print(macal.__credits__)



def RecordItems(func: macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of Items function used in conjunction with foreach for iterating over records.  Items returns key/value pairs."""
    macal.ValidateFunctionArguments(func, scope, filename)
    var = scope.GetVariable("var")
    val = var.GetValue()
    rec = val.GetValue()
    t = val.GetType()
    if t != macal.VariableTypes.Record:
        raise macal.RuntimeError(f'Invalid variable type ({t}) "record" type is required.', val.Token.Location, filename)
    pv = [{key: value} for key, value in rec.items()]
    scope.SetReturnValue(pv)



def RecordItemKey(func: macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of Key function used in conjunction the Items function that returns key/value pairs. Key returns the key part of a key value pair."""
    macal.ValidateFunctionArguments(func, scope, filename)
    var = scope.GetVariable("var")
    val = var.GetValue()
    rec = val.GetValue()
    t = val.GetType()
    if t != macal.VariableTypes.Record:
        raise macal.RuntimeError(f'Invalid variable type ({t}) "record" type is required.', val.Token.Location, filename)
    for k, v in rec.items(): #there are different ways, but this is by far the most simple and safe way to do it.
        key = k
    scope.SetReturnValue(key)



def RecordKeys(func: macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of Key function used in conjunction the Items function that returns key/value pairs. Key returns the key part of a key value pair."""
    macal.ValidateFunctionArguments(func, scope, filename)
    var = scope.GetVariable("var")
    val = var.GetValue()
    rec = val.GetValue()
    t = val.GetType()
    if t != macal.VariableTypes.Record:
        raise macal.RuntimeError(f'Invalid variable type ({t}) "record" type is required.', val.Token.Location, filename)
    val = [k for k in rec.keys()]
    scope.SetReturnValue(val)

    

def RecordItemValue(func: macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of Value function used in conjunction the Items function that returns key/value pairs. Value returns the value part of a key value pair."""
    macal.ValidateFunctionArguments(func, scope, filename)
    var = scope.GetVariable("var")
    val = var.GetValue()
    rec = val.GetValue()
    t = val.GetType()
    if t != macal.VariableTypes.Record:
        raise macal.RuntimeError(f'Invalid variable type ({t}) "record" type is required.', val.Token.Location, filename)
    for k, v in rec.items(): #there are different ways, but this is by far the most simple and safe way to do it.
        val = v
    scope.SetReturnValue(val)



def RecordValues(func: macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of Value function used in conjunction the Items function that returns key/value pairs. Value returns the value part of a key value pair."""
    macal.ValidateFunctionArguments(func, scope, filename)
    var = scope.GetVariable("var")    
    val = var.GetValue()
    rec = val.GetValue()
    t = val.GetType()
    if t != macal.VariableTypes.Record:
        raise macal.RuntimeError(f'Invalid variable type ({t}) "record" type is required.', val.Token.Location, filename)
    val = [v for v in rec.values()]
    scope.SetReturnValue(val)
