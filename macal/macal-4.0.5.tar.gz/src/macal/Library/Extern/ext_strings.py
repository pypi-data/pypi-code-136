# Product:   Macal
# Author:    Marco Caspers
# Date:      27-09-2022
#

from unidecode import unidecode
import macal



def strLen(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of len function"""
    macal.validateFunctionArguments(func, scope, filename)
    arg = scope.getVariable("arg")
    at = arg.getType()
    if at != macal.VariableTypes.String and at != macal.VariableTypes.Record and at != macal.VariableTypes.Array:
        raise macal.RuntimeError(f"StrLen: Invalid argument type ({at}).", arg.Token.Location, filename)
    result = len(arg.getValue())
    scope.setReturnValue(result)



def strLeft(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of left function"""
    macal.validateFunctionArguments(func, scope, filename)
    arg = scope.getVariable("arg")
    argl = scope.getVariable("length")  
    result = arg.getValue()[0:argl.getValue()]
    scope.setReturnValue(result)



def strMid(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of mid function"""
    macal.validateFunctionArguments(func, scope, filename)
    arg = scope.getVariable("arg")
    args = scope.getVariable("start")
    argl = scope.getVariable("length")
    value = arg.getValue()
    start = args.getValue()
    length = argl.getValue()
    endpos = start+length
    result = value[start:endpos]
    scope.setReturnValue(result)



def toString(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of toString function"""
    macal.validateFunctionArguments(func, scope, filename)
    argvalue = scope.getVariable("arg")
    result = f"{argvalue.getValue()}"
    scope.setReturnValue(result);



def strContains(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of strContains function"""
    macal.validateFunctionArguments(func, scope, filename)
    needle = scope.getVariable("needle").getValue()
    haystack = scope.getVariable("haystack").getValue()
    result = needle in haystack
    scope.setReturnValue(result);



def strReplace(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of strReplace function"""
    macal.validateFunctionArguments(func, scope, filename)
    var = scope.getVariable("var").getValue()
    frm = scope.getVariable("frm")
    wth = scope.getVariable("with")
    result = var.getValue().replace(frm.getValue(), wth.getValue())
    scope.setReturnValue(result)



def startsWith(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of StartsWith function"""
    macal.validateFunctionArguments(func, scope, filename)
    haystack = scope.getVariable("haystack").getValue()
    needle = scope.getVariable("needle").getValue()  
    scope.setReturnValue(str.startswith(needle, haystack))



def removeNonAscii(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of RemoveNonAscii function"""
    macal.validateFunctionArguments(func, scope, filename)   
    txt = scope.getVariable("text")    
    result = unidecode(txt.getValue())
    scope.setReturnValue(result)



def replaceEx(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of ReplaceEx function"""
    macal.validateFunctionArguments(func, scope, filename)
    var  = scope.getVariable("var")
    repl = scope.getVariable("repl")
    by   = scope.getVariable("by")
    result = var.getValue().getValue()
    r = repl.getValue()    
    b = by.getValue()
    for ch in r:
        result = result.replace(ch, b)
    scope.setReturnValue(result)



def padLeft(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of ReplaceEx function"""
    macal.validateFunctionArguments(func, scope, filename)
    string = scope.getVariable("strng")
    char   = scope.getVariable("char")
    amount = scope.getVariable("amount")
    # this is counter intuitive, but the *just functions in python pad the character on the other end as what their name would imply.
    result = string.getValue().rjust(amount.getValue(), char.getValue())
    scope.setReturnValue(result)



def padRight(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of ReplaceEx function"""
    macal.validateFunctionArguments(func, scope, filename)
    string = scope.getVariable("strng")
    char   = scope.getVariable("char")
    amount = scope.getVariable("amount")
    # this is counter intuitive, but the *just functions in python pad the character on the other end as what their name would imply.
    result = string.getValue().ljust(amount.getValue(), char.getValue()) 
    scope.setReturnValue(result)
