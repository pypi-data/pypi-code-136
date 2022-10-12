from enum import Enum

class Return(Enum):
    ValueOnly = 0
    IndepsAndValue = 1
    IndepValue = 2

class SingleValueIndeps(Enum):
    Include = 0
    Exclude = 1

class Interpolate(Enum):
    Linear = 0
    InterpolateSpline = 1
    InterpolateCubic = 2

class InterpolateDomain(Enum):
    Rectangular = 0
    Polar = 1
    dB = 2
    DataBased = 3

class Extrapolate(Enum):
    No = 0
    Zero = 1
    Constant = 2
    Interpolate = 3

class FreeVariables(Enum):
    All = 0
    #NearbyUnion = 1
    #NearbyIntersection = 2
    #NearbyNearest = 3

_InterpDataOptionsOrder = [Return, SingleValueIndeps, Interpolate, InterpolateDomain, Extrapolate, FreeVariables]
_InterpDataOptionsDefaults = {
    Return: Return.IndepsAndValue.value,
    SingleValueIndeps: SingleValueIndeps.Exclude.value,
    Interpolate: Interpolate.Linear.value,
    InterpolateDomain: InterpolateDomain.DataBased.value,
    Extrapolate: Extrapolate.Constant.value,
    FreeVariables: FreeVariables.All.value
}
