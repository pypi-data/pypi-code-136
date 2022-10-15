# Product:   Macal
# Author:    Marco Caspers
# Date:      27-09-2022
#

import os
import json
import macal



def loadTextFile(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of Load function"""
    macal.ValidateFunctionArguments(func, scope, filename)
    var = scope.GetVariable("filename")
    fileName = var.GetValue()
    try:
        with open (fileName, "r") as tf:
            content=tf.read()
        scope.SetReturnValue(content)
    except Exception as ex:
        raise macal.RuntimeError(f"Load Exception: {ex}", var.Token.Location, filename)



def readJSONFile(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of Read JSON file function"""
    macal.ValidateFunctionArguments(func, scope, filename)
    var = scope.GetVariable("filename")
    fileName = var.GetValue()
    try:
        with open(fileName, 'r') as fp:
            content = json.load(fp)
        scope.SetReturnValue(content)
    except Exception as ex:
        raise macal.RuntimeError(f"ReadJSON Exception: {ex}", var.Token.Location, filename)
    


def existsFile(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of Exists function"""
    macal.ValidateFunctionArguments(func, scope, filename)
    filename = scope.GetVariable("filename").GetValue()
    result = os.path.exists(filename)
    scope.SetReturnValue(result)



def saveTextFile(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of Save function"""
    macal.ValidateFunctionArguments(func, scope, filename)
    content = scope.GetVariable("content").GetValue()
    var = scope.GetVariable("filename")
    fileName = var.GetValue()
    try:
        with open(fileName, "w") as tf:
            tf.write(content)
        scope.SetReturnValue(True)
    except Exception as ex:
        raise macal.RuntimeError(f"Save exception: {ex}", var.Token.Location, filename)



def writeJSONFile(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of Save function"""
    macal.ValidateFunctionArguments(func, scope, filename)
    content = scope.GetVariable("content").GetValue()
    var = scope.GetVariable("filename")
    fileName = var.GetValue()
    try:
        with open(fileName, 'w') as fp:
            json.dump(content, fp, indent=4)
        scope.SetReturnValue(True)
    except Exception as ex:
        raise macal.RuntimeError(f"WriteJSON exception: {ex}", var.Token.Location, filename)



def getLastRun(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of GetLastRun function"""
    macal.ValidateFunctionArguments(func, scope, filename)
    var = scope.GetVariable("name")
    org_name = var.GetValue()
    iso_now  = scope.GetVariable("defaultIsoNow").GetValue()
    fileName = f"/tmp/last_run_{org_name}.ctl"
    if os.name == "nt":
        fileName = f"c:/temp/last_run_{org_name}.ctl"
    try:
        if os.path.exists(fileName):
            with open (fileName, "r") as tf:
                result=tf.read()
            if result is None or result == '':
                result = iso_now
        else:
            result = iso_now
        scope.SetReturnValue(result)
    except Exception as ex:
        raise macal.RuntimeError(f'Get last run exception: {ex}', var.Token.Location, filename)


def setLastRun(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of SetLastRun function"""
    macal.ValidateFunctionArguments(func, scope, filename)
    var = scope.GetVariable("name")
    org_name = var.GetValue()
    iso_now  = scope.GetVariable("isoNow").GetValue()
    fileName = f"/tmp/last_run_{org_name}.ctl";
    if os.name == "nt":
        fileName = f"c:/temp/last_run_{org_name}.ctl"
    try:
        with open(fileName, "w") as tf:
            tf.write(iso_now)
    except Exception as ex:
        raise macal.RuntimeError(f"Set last run exception: {ex}", var.Token.Location, filename)
