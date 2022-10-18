import numpy as np

from .base import *
from .components import Element

class VarianGeometries(param.Parameterized):
    Y1 = param.Array(doc="""""",
                     default=np.array([[-20.0, 0], [20.0, 0.0], [20.0, -32.0], [-20.0, -32.0]]),
                     readonly=True
                     )
    Y2 = param.Array(doc="""""",
                     default=np.array([[-20.0, 0], [20.0, 0.0], [20.0, 32.0], [-20.0, 32.0]]),
                     readonly=True
                     )
    X1 = param.Array(doc="""""",
                     default=np.array([[0.0, -20.0], [0.0, 20.0], [-32.0, 20.0], [-32.0, -20.0]]),
                     readonly=True
                     )
    X2 = param.Array(doc="""""",
                     default=np.array([[0.0, -20.0], [0.0, 20.0], [32.0, 20.0], [32.0, -20.0]]),
                     readonly=True
                     )
    MLCCarriageA = param.Array(doc="""""",
                               default=np.array([[0.0, -20.0], [0.0, 20.0], [20.0, 20.0], [20.0, -20.0]]),
                               readonly=True
                               )
    MLCCarriageB = param.Array(doc="""""",
                               default=np.array([[0.0, -20.0], [0.0, 20.0], [-20.0, 20.0], [-20.0, -20.0]]),
                               readonly=True
                               )
    HDMLCCarriageA = param.Array(doc="""""",
                                 default=np.array([[0.0, -12.0], [0.0, 12.0], [20.0, 12.0], [20.0, -12.0]]),
                                 readonly=True
                                 )
    HDMLCCarriageB = param.Array(doc="""""",
                                 default=np.array([[0.0, -12.0], [0.0, 12.0], [-20.0, 12.0], [-20.0, -12.0]]),
                                 readonly=True
                                 )
    LeafAFull = param.Array(doc="""""",
                            default=np.array([[0.0, 0.0], [0.0, -1.0], [18.0, -1.0], [18.0, 0.0]]),
                            readonly=True
                            )
    LeafBFull = param.Array(doc="""""",
                            default=np.array([[0.0, 0.0], [0.0, -1.0], [-18.0, -1.0], [-18.0, 0.0]]),
                            readonly=True
                            )
    LeafAHalf = param.Array(doc="""""",
                            default=np.array([[0.0, 0.0], [0.0, -0.5], [18.0, -0.5], [18.0, 0.0]]),
                            readonly=True
                            )
    LeafBHalf = param.Array(doc="""""",
                            default=np.array([[0.0, 0.0], [0.0, -0.5], [-18.0, -0.5], [-18.0, 0.0]]),
                            readonly=True
                            )
    LeafAQuarter = param.Array(doc="""""",
                               default=np.array([[0.0, 0.0], [0.0, -0.25], [18.0, -0.25], [18.0, 0.0]]),
                               readonly=True
                               )
    LeafBQuarter = param.Array(doc="""""",
                               default=np.array([[0.0, 0.0], [0.0, -0.25], [-18.0, -0.25], [-18.0, 0.0]]),
                               readonly=True
                               )