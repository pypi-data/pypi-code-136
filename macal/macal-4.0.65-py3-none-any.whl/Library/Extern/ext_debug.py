import macal

def DebugPrintScope(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    for var in scope.Parent.Variables:
        print(var)


def DebugPrintVariable(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    name = scope.GetVariable("varname").GetValue()
    var = scope.Parent.FindVariable(name)
    print(var)