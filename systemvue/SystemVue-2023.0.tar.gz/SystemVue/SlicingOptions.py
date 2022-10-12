from enum import Enum

class Return(Enum):
    ValueOnly = 0
    IndepsAndValue = 1
    IndepValue = 2

class SingleValueIndeps(Enum):
    Include = 0
    Exclude = 1

class RequireAllPointsExist(Enum):
    No = 0
    #Yes = 1

_SliceDataOptionsOrder = [Return, SingleValueIndeps, RequireAllPointsExist]
_SliceDataOptionsDefaults = {
    Return: Return.IndepsAndValue.value, 
    SingleValueIndeps: SingleValueIndeps.Exclude.value, 
    RequireAllPointsExist: RequireAllPointsExist.No.value
}
