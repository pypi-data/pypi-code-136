# Product:   Macal
# Author:    Marco Caspers
# Date:      16-09-2022
#

"""Macal time library implementation"""

from datetime import datetime
import time
import macal


NUM_SECONDS_FIVE_MINUTES = 300
NUM_SECONDS_ONE_HOUR = 3600
TIME_FORMAT = '%Y%m%d%H%M%S'
ISO_TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"
ISO_TIME_tzFORMAT = "%Y-%m-%dT%H:%M:%S.0Z"
__stopwatch__ = 0

def DateToUnix(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Convert a date_string of format YYYYMMDDhhmmss to unix time integer.
       Assumes the date string object is UTC time."""
    var = scope.getVariable("date_str")
    dt = datetime.strptime(var.getValue(), TIME_FORMAT)
    epoch = datetime(1970, 1, 1)
    result = int((dt - epoch).total_seconds())
    scope.setReturnValue(result)



def IsoToUnix(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Convert a date_string of format %Y-%m-%dT%H:%M:%S.%f to unix time integer.
       Assumes the date string object is in iso format."""
    var = scope.getVariable("date_str")
    dt = datetime.strptime(var.getValue(), ISO_TIME_FORMAT)
    epoch = datetime(1970, 1, 1)
    result = int((dt - epoch).total_seconds())
    scope.setReturnValue(result)



def DateFromUnix(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Converts time in seconds since UNIX EPOCH to UTC Time format"""
    var = scope.getVariable("seconds")
    result = time.strftime(TIME_FORMAT, time.gmtime(var.getValue()))
    scope.setReturnValue(result)



def IsoFromUnix(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Converts time in seconds since UNIX EPOCH to UTC Time format"""
    var = scope.getVariable("seconds")
    result = time.strftime(ISO_TIME_tzFORMAT, time.gmtime(var.getValue()))
    scope.setReturnValue(result)



def UtcNow(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    result = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    scope.setReturnValue(result)



def UtcIsoNow(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    result = "{}Z".format(datetime.utcnow().isoformat())
    scope.setReturnValue(result)



def IsoNow(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    result = datetime.now().isoformat()
    scope.setReturnValue(result)



def Now(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    result = datetime.now().strftime("%Y%m%d%H%M%S")
    scope.setReturnValue(result)

    

def PerfCounter(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    result = time.perf_counter()
    scope.setReturnValue(result)

