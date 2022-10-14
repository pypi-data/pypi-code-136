# Product:   Macal
# Author:    Marco Caspers
# Date:      16-09-2022
#

"""Macal system library implementation"""

import macal
import platform


def console(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    macal.validateFunctionArguments(func, scope, filename)
    args = scope.getVariable("args")
    if args is None:
        print()
        return
    val = args.getValue()
    txt = ' '.join([f'{arg}' for arg in val])
    print(txt)



def vartype(func: macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    macal.validateFunctionArguments(func, scope, filename)
    var = scope.getVariable("var")
    val = var.getValue()
    scope.setReturnValue(val.getType())
    rvar = scope.getFunctionReturnVariable()
    rvar.Value.Type = macal.VariableTypes.Type



def Array(func: macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    macal.validateFunctionArguments(func, scope, filename)
    args = scope.getVariable("args")
    if args is None:
        raise macal.RuntimeError('Required argument "args" not found.', func.Token.Location, filename)
    arr = []
    vargs = args.getValue()
    for arg in vargs:
        arr.append(arg)
    scope.setReturnValue(arr)
    

def record_has_field(func: macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    macal.validateFunctionArguments(func, scope, filename)
    var = scope.getVariable('fieldname')
    fieldname = var.getValue()
    var = scope.getVariable('rec')
    record = var.getValue()
    if record is None:
        result = False
    else:
        result =  fieldname in record
    scope.setReturnValue(result)



def isString(func: macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    macal.validateFunctionArguments(func, scope, filename)
    var = scope.getVariable("var")
    val = var.getValue()
    result = val.getType() == macal.VariableTypes.String
    scope.setReturnValue(result)



def isInt(func: macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    macal.validateFunctionArguments(func, scope, filename)
    var = scope.getVariable("var")
    val = var.getValue()
    result = val.getType() == macal.VariableTypes.Int    
    scope.setReturnValue(result)



def isFloat(func: macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    macal.validateFunctionArguments(func, scope, filename)
    var = scope.getVariable("var")
    val = var.getValue()
    result = val.getType() == macal.VariableTypes.Float
    scope.setReturnValue(result)



def isBool(func: macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    macal.validateFunctionArguments(func, scope, filename)
    var = scope.getVariable("var")
    val = var.getValue()
    result = val.getType() == macal.VariableTypes.Bool
    scope.setReturnValue(result)



def isRecord(func: macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    macal.validateFunctionArguments(func, scope, filename)
    var = scope.getVariable("var")
    val = var.getValue()
    result = val.getType() == macal.VariableTypes.Record
    scope.setReturnValue(result)



def isArray(func: macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    macal.validateFunctionArguments(func, scope, filename)
    var = scope.getVariable("var")
    val = var.getValue()
    result = val.getType() == macal.VariableTypes.Array
    scope.setReturnValue(result)



def isFunction(func: macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    macal.validateFunctionArguments(func, scope, filename)
    var = scope.getVariable("var")
    val = var.getValue()
    result = val.getType() == macal.VariableTypes.Function
    scope.setReturnValue(result)



def isNil(func: macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    macal.validateFunctionArguments(func, scope, filename)
    var = scope.getVariable("var")
    val = var.getValue()
    result = val.getType() == macal.VariableTypes.Nil
    scope.setReturnValue(result)



def getPlatform(func: macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    scope.setReturnValue(platform.system())


        
def showVersion(func: macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    print("Version: ",macal.__version__)
    print("Author:  ", macal.__author__)
    print("Credits:")
    print(macal.__credits__)



def items(func: macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of Items function used in conjunction with foreach for iterating over records.  Items returns key/value pairs."""
    macal.validateFunctionArguments(func, scope, filename)
    var = scope.getVariable("var")
    val = var.getValue()
    rec = val.getValue()
    t = val.getType()
    if t != macal.VariableTypes.Record:
        raise macal.RuntimeError(f'Invalid variable type ({t}) "record" type is required.', val.Token.Location, filename)
    pv = [{key: value} for key, value in rec.items()]
    scope.setReturnValue(pv)



def recordItemKey(func: macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of Key function used in conjunction the Items function that returns key/value pairs. Key returns the key part of a key value pair."""
    macal.validateFunctionArguments(func, scope, filename)
    var = scope.getVariable("var")
    val = var.getValue()
    rec = val.getValue()
    t = val.getType()
    if t != macal.VariableTypes.Record:
        raise macal.RuntimeError(f'Invalid variable type ({t}) "record" type is required.', val.Token.Location, filename)
    for k, v in rec.items(): #there are different ways, but this is by far the most simple and safe way to do it.
        key = k
    scope.setReturnValue(key)



def recordKeys(func: macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of Key function used in conjunction the Items function that returns key/value pairs. Key returns the key part of a key value pair."""
    macal.validateFunctionArguments(func, scope, filename)
    var = scope.getVariable("var")
    val = var.getValue()
    rec = val.getValue()
    t = val.getType()
    if t != macal.VariableTypes.Record:
        raise macal.RuntimeError(f'Invalid variable type ({t}) "record" type is required.', val.Token.Location, filename)
    val = [k for k in rec.keys()]
    scope.setReturnValue(val)

    

def recordItemValue(func: macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of Value function used in conjunction the Items function that returns key/value pairs. Value returns the value part of a key value pair."""
    macal.validateFunctionArguments(func, scope, filename)
    var = scope.getVariable("var")
    val = var.getValue()
    rec = val.getValue()
    t = val.getType()
    if t != macal.VariableTypes.Record:
        raise macal.RuntimeError(f'Invalid variable type ({t}) "record" type is required.', val.Token.Location, filename)
    for k, v in rec.items(): #there are different ways, but this is by far the most simple and safe way to do it.
        val = v
    scope.setReturnValue(val)



def recordValues(func: macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of Value function used in conjunction the Items function that returns key/value pairs. Value returns the value part of a key value pair."""
    macal.validateFunctionArguments(func, scope, filename)
    var = scope.getVariable("var")    
    val = var.getValue()
    rec = val.getValue()
    t = val.getType()
    if t != macal.VariableTypes.Record:
        raise macal.RuntimeError(f'Invalid variable type ({t}) "record" type is required.', val.Token.Location, filename)
    val = [v for v in rec.values()]
    scope.setReturnValue(val)
