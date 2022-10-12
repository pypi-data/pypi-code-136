from sys import argv 
import os.path
from typing import Union

def getArgByFlag(flag: Union[str, list, tuple], optional:bool = False, defaultValue:str = None, 
                 errorMessage:str = None, errorMessageIfNoArg:str = None, 
                 errorMessageIfNoFlag:str = None, defaultErrors:bool = True):
    # initiate stuff and convert types
    argValue = defaultValue
    argFlagIndex = None
    flagPresent = False
    argPresent = False
    
    if type(flag) is str: flag = [flag]
    
    for _flg in flag: 
        try:
            argFlagIndex = argv.index(_flg)
            flagPresent = True
            argValue = argv[argFlagIndex+1]
            argPresent = True
            return argValue
        except: 
            pass
        
    if optional: return argValue
    if defaultErrors: # we don't really need to do it if there is no error in the first place, right?
        if errorMessage == None: 
            errorMessage = f'Command line argument error: <{" | ".join(flag)}> <value>'
        if errorMessageIfNoArg == None: 
            errorMessageIfNoArg = f'Argument value  for flag <{" | ".join(flag)}> not provided'
        if errorMessageIfNoFlag == None and not optional: 
            errorMessageIfNoFlag = f'Required flag: <{" | ".join(flag)}> not provided'
    if errorMessage: print(errorMessage)
    if flagPresent and not argPresent and errorMessageIfNoArg: print(errorMessageIfNoArg)
    if not flagPresent and not optional and errorMessageIfNoFlag: print(errorMessageIfNoFlag)

    return argValue


def isFlagPresent(flag: Union[str, list, tuple], optional:bool=True, errorMessage:str=None,
                  defaultErrors:bool = True):
    
    # convert types for less branching
    if type(flag) is str: flag = [flag]
    # check if it is present:
    for _flg in flag:
        if _flg in argv: return True
    
    # if there is no flag:
    if optional: return False
    if not errorMessage and defaultErrors:
        print(f'Required flag: <{" | ".join(flag)}> not provided')
        return False
    if errorMessage:
        print(errorMessage)
        return False


def isPathValid(path:str, expectedFileExtensions: Union[str, list, tuple] = None,
                errorMessageWrongType: str=None, errorMessagePathInvalid: str=None,
                defaultErrors: bool=True):
    # check if the filepath was even passed first
    if type(path) is type(None): return False
    # convert stuff so we have less branching
    if type(expectedFileExtensions) is str: expectedFileExtensions = tuple([expectedFileExtensions])
    elif type(expectedFileExtensions) is list: expectedFileExtensions = tuple(expectedFileExtensions)
    # actual request to the os
    pathValid = os.path.exists(path)
    
    # if file doesn't exist
    if not pathValid: 
        if defaultErrors and errorMessagePathInvalid==None:
            print(f"Invalid path: {path}")
        elif errorMessagePathInvalid is not None: 
            print(errorMessagePathInvalid)
        return pathValid
    
    # if file exists check for type stuff
    if expectedFileExtensions == None: return pathValid
    if path.endswith(expectedFileExtensions): return pathValid
    else:  
        if defaultErrors and errorMessageWrongType==None:
            print(f"Expected file path extension type: {' or '.join(expectedFileExtensions)}") 
        else:
            print(errorMessageWrongType)
            
    return pathValid


def getAllArgs(): 
    return argv
