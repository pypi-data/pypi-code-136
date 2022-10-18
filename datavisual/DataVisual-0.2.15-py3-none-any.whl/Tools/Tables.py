from itertools import product
import numpy as np
from dataclasses import dataclass
from copy import deepcopy

from DataVisual.Tools.utils import ToList

@dataclass
class XParameter(object):
    Name: str  = None
    Values: str  = None
    Format: str  = ""
    LongLabel: str  = ""
    Unit: str  = ""
    Legend: str  = ""
    Type: type = float
    Position: int = None

    def __post_init__(self):
        self.Values  = ToList(self.Values).astype(self.Type) if self.Type is not None else ToList(self.Values)
        self.Init()

    def Init(self):
        self.Label  = self.LongLabel + f" [{self.Unit}]" if self.LongLabel != "" else self.Name
        self.Legend = self.Legend if self.Legend != "" else self.Name


    def UpdateUnit(self, Unit: str):

        if Unit is None:
            return

        if Unit.lower() == 'femto':
            self.Values *= 1e12
            self.Unit = f"f{self.Unit}" 

        if Unit.lower() == 'nano':
            self.Values *= 1e9
            self.Unit = f"n{self.Unit}" 

        if Unit.lower() == 'micro':
            self.Values *= 1e6
            self.Unit = u"\u03bc" + f"{self.Unit}" 

        if Unit.lower() == 'milli':
            self.Values *= 1e3
            self.Unit = f"$u${self.Unit}" 

        if Unit.lower() == 'kilo':
            self.Values *= 1e-3
            self.Unit = f"$k${self.Unit}" 

        if Unit.lower() == 'mega':
            self.Values *= 1e-6
            self.Unit = f"$M${self.Unit}" 

        if Unit.lower() == 'giga':
            self.Values *= 1e-9
            self.Unit = f"$G${self.Unit}" 

        if Unit.lower() == 'peta':
            self.Values *= 1e-12
            self.Unit = f"$M${self.Unit}" 

        self.Init()

    @property
    def Unique(self):
        if self.Values.shape[0] == 1:
            return True
        else:
            return False

    def Normalize(self):
        self.Unit = "[U.A.]"
        self.Init()


    def WrapValue(self, idx: int=None):
        if idx is None:
            return self.WrapValue(0) 

        if self.Format is None:
            return f" | {self.Legend} : {self.Values[idx]}"

        if self.Values[idx] is None:
            return f" | {self.Legend} : None"

        else:
            return f" | {self.Legend} : {self.Values[idx]:{self.Format}}"


    def GetLabels(self):
        return [self.WrapValue(idx) for idx in range(self.Values.shape[0])]


    def flatten(self):
        return np.array( [x for x in self.Values] ).flatten()

    def __getitem__(self, item):
        return self.Values[item]

    def __repr__(self):
        return self.Name

    def GetSize(self):
        return self.Values.shape[0]

    def __eq__(self, other):
        if other is None: return False

        return True if self.Name == other.Name else False

    def str(self, item):
        return f" | {self.LongLabel} : {self.Values[item]:{self.Format}}"

    def __str__(self):
        if self.Values.size == 1:
            return f" | {self.LongLabel} : {self.Values[0]:{self.Format}} {self.Unit}"
        else:
            return self.Values.__str__()


class XTable(object):
    def __init__(self, X, Settings):
        self.X         = np.array(X)
        self.Shape     = [x.GetSize() for x in self.X]
        self.Name2Idx  = { x.Name: order for order, x in enumerate(self.X) }
        self.Settings  = Settings

    def GetValues(self, Axis):
        return self[Axis].Value


    def GetPosition(self, Value):
        for order, x in enumerate(self.X):
            if x == Value:
                return order


    def __getitem__(self, Val):
        if Val is None: return None

        Idx = self.Name2Idx[Val] if isinstance(Val, str) else Val

        return self.X[Idx]


    def ExcludeTable(self, Axis, Exclude):
        Shape = np.where(self.X == Axis, None, self.Shape)

        Shape = Shape[self.X != Exclude]
        ExcludedTable = self.X[self.X != Exclude]

        return Shape.squeeze(), ExcludedTable.squeeze()


    def GetLegends(self, Axis, ExcludedTable):
        Fixed = [x for x in ExcludedTable if x.Unique]
        Variable = [x for x in ExcludedTable if not x.Unique and x != Axis]

        P = [x.GetLabels() for x in Variable]
        Variable = [ ''.join(p) for p in product(*P) ]

        return Fixed, Variable


    def GetSlicer(self, Axis, Exclude=None):
        Shape, ExcludedTable = self.ExcludeTable(Axis, Exclude)

        DimSlicer = [range(s) if s is not None else [slice(None)] for s in Shape]

        Fixed, Variable = self.GetLegends(Axis, ExcludedTable)

        self.Settings.CommonLabel = "".join( [ x.WrapValue() for x in Fixed ] )

        Slicer = product(*DimSlicer)

        return zip(Slicer, Variable)




class YTable(object):
    def __init__(self, Y):
        self.Y = Y
        self.Name2Idx = self.GetName2Idx()


    def GetShape(self):
        return [x.Size for x in self.Y] + [1]

    def GetName2Idx(self):
        return { x.Name: order for order, x in enumerate(self.Y) }


    def __getitem__(self, Val):
        if isinstance(Val, str):
            idx = self.Name2Idx[Val]
            return self.Y[idx]
        else:
            return self.Y[Val]

