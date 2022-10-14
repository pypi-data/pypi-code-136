# #!/usr/bin/env python
# # -*- coding: utf-8 -*-

import numpy, logging
from dataclasses import dataclass, field

from SuPyMode.Binary.SuperMode import SuperMode as _SuperMode
from SuPyMode.Binary.CppSolver import CppSolver

import SuPyMode.Tools.Plots as Plots
from SuPyMode.Tools.utils import DebugFunction



@dataclass
class SuperMode(object):
    """ 
    .. note::
        This class is a representation of the fiber optic structures SuperModes. 
        Those mode belongs to a SuperSet class and are constructed with the SuPySolver.
        It links to c++ SuperMode class.

    """

    ParentSet: None = field(repr=False)
    """SuperSet to which is associated the computed this mode"""

    CppSolver: None = field(repr=False)
    """c++ solver to which is linked this binded mode"""

    BindingNumber: int
    """Number which bind this mode to a specific c++ mode"""

    SolverNumber: int
    """Number which bind this mode to a specific python solver"""

    ModeNumber: int
    """Unique number associated to this mode"""



    def __post_init__(self):
        self.Binded = self.CppSolver.GetMode(self.BindingNumber)
        self.ID = [self.SolverNumber, self.BindingNumber]
        self.Name = f"Mode {self.ID[0]}:{self.ID[1]}"
        self._FullFields = None
        self._Fields, self._Index, self._Betas, self._Adiabatic, self._Coupling = (None,)*5


    @property
    def FullFields(self):
        if self._FullFields is None:
            self.ComputeFullFields()
        return self._FullFields

    @property
    def Adiabatic(self):
        if self._Adiabatic is None:
            self._Adiabatic = self.Binded.GetAdiabatic()

        return self._Adiabatic

    @property
    def Coupling(self):
        if self._Coupling is None:
            self._Coupling = self.Binded.GetCoupling()
        return self._Coupling

    @property
    def Fields(self):
        if self._Fields is None:
            self._Fields = self.Binded.GetFields()
        return self._Fields

    @property
    def Index(self):
        if self._Index is None:
            self._Index = self.Binded.GetIndex()
        return self._Index

    @property
    def Betas(self):
        if self._Betas is None:
            self._Betas = self.Binded.GetBetas()
        return self._Betas

    @property
    def RightSymmetry(self):
        return self.CppSolver.RightSymmetry

    @property
    def LeftSymmetry(self):
        return self.CppSolver.LeftSymmetry

    @property
    def TopSymmetry(self):
        return self.CppSolver.TopSymmetry

    @property
    def BottomSymmetry(self):
        return self.CppSolver.BottomSymmetry

    @property
    def Size(self):
        return len(self.ParentSet.ITRList)

    @property
    def Geometry(self):
        return self.ParentSet.Geometry

    @property
    def ITRList(self):
        return self.ParentSet.ITRList

    @property
    def Axes(self):
        return self.ParentSet.Axes

    @property
    def yAxis(self):
        return self.Axes.Y

    @property
    def xAxis(self):
        return self.Axes.X

    @property
    def Symmetries(self):
        return {'Left': self.LeftSymmetry, 'Right': self.RightSymmetry, 'Top': self.TopSymmetry, 'Bottom': self.BottomSymmetry}


    def AddSymmetries(self, FullField: numpy.ndarray) -> numpy.ndarray:
        """
        Return mode field taking account of the symmetries of the solver
        """


        match self.BottomSymmetry:
            case 0: pass

            case 1: FullField = numpy.concatenate((FullField[:, :, ::-1], FullField), axis=2)

            case -1: FullField = numpy.concatenate((-FullField[:, :, ::-1], FullField), axis=2)


        match self.TopSymmetry:
            case 0: pass

            case 1: FullField = numpy.concatenate((FullField, FullField[:, :, ::-1]), axis=2)

            case -1: FullField = numpy.concatenate((FullField, -FullField[:, :, ::-1]), axis=2)


        match self.RightSymmetry:
            case 0: pass

            case 1: FullField = numpy.concatenate((FullField[...], FullField[:, ::-1, :]), axis=1) 

            case -1: FullField = numpy.concatenate((FullField[...], -FullField[:, ::-1, :]), axis=1) 


        match self.LeftSymmetry:
            case 0: pass

            case 1: FullField = numpy.concatenate((FullField[:, ::-1, :], FullField[...]), axis=1) 

            case -1: FullField = numpy.concatenate((-FullField[:, ::-1, :], FullField[...]), axis=1)

        return FullField


    def ComputeFullFields(self) -> None:
        """
        Compute the full mode field taking account for the symmetries
        """


        self._FullFields = self.AddSymmetries(self.Fields)


    def GetAdiabatic(self, Other=None) -> numpy.ndarray:
        """
        Return the array of the adiabatic criterion for the mode
        """


        if Other is None:
            return self.Binded.GetAdiabatic()
        else:
            return self.Binded.GetAdiabaticSpecific(Other.Binded)


    def GetCoupling(self, Other=None) -> numpy.ndarray:
        """
        Return the array of the modal coupling for the mode
        """


        if Other is None:
            return self.Binded.GetCoupling()
        else:
            return self.Binded.GetCouplingSpecific(Other.Binded)


    def __render__index__(self, Figure, Ax) -> None:
        Figure.UnitSize = (10,4)
        Figure.Title    = ''
        Ax.yLabel       = r'Effective refraction index'
        Ax.xLabel       = 'ITR'

        artist = Plots.Line(X=self.ITRList, Y=self.Index, Label=self.Name)
        Ax.AddArtist( artist )


    def __render__beta__(self, Figure, Ax) -> None:
        Figure.UnitSize = (10,4)
        Ax.yLabel       = r'Propagation constante $\beta$'
        Ax.xLabel       = 'ITR'
        
        artist = Plots.Line(X=self.ITRList, Y=self.Betas, Label=self.Name)
        Ax.AddArtist( artist )
        

    def __render__adiabatic__(self, Figure, Ax, Other=None) -> None:
        Figure.UnitSize = (10,4)
        Ax.yLabel       = r'Adiabatic criterion'
        Ax.xLabel       = 'ITR'
        Ax.yLimits      = [1e-6, 1e-1]
        Ax.yScale       = 'log'

        if Other is None:
            for mode in self.ParentSet:
                self.__render__adiabatic__(Figure=Figure, Ax=Ax, Other=mode)

        else:
            artist = Plots.Line(X=self.ITRList, Y=self.GetAdiabatic(Other), Label=f'{self.Name} - {Other.Name}')
            Ax.AddArtist( artist )


    def __render__coupling__(self, Figure, Ax, Other=None) -> None:
        Figure.UnitSize = (10,4)
        Ax.yLabel       = r'Mode coupling'
        Ax.xLabel       = 'ITR'

        if Other is None:
            for mode in self.ParentSet:
                self.__render__coupling__(Figure=Figure, Ax=Ax, Other=mode)

        else:
            artist = Plots.Line(X=self.ITRList, Y=self.GetCoupling(Other), Label=f'{self.Name} - {Other.Name}')
            Ax.AddArtist( artist )


    def __render_field__(self, Figure, Ax, ITR: float=None, Slice: int=None) -> None:
        Figure.UnitSize = (3,3)
        Ax.yLabel   = r'Y-direction [$\mu m$]'
        Ax.xLabel   = r'X-Direction [$\mu m$]'
        Ax.Colorbar = Plots.ColorBar(Symmetric=True, Position='right')

        xAxis, yAxis = self.Axes.GetFullAxis(Symmetries=self.Symmetries)

        if ITR is not None:
            Ax.Title = f'{self.Name}\n[ITR: {ITR:.2f}]'
            field = self.FullFields[self.ParentSet.ITR2Slice(ITR)]

        if Slice is not None:
            Ax.Title = f'{self.Name}\n[Slice: {Slice}]'
            field = self.FullFields[Slice]
        
        artist = Plots.Mesh(X=xAxis, Y=yAxis, Scalar=field, ColorMap=Plots.FieldMap)
        
        Ax.AddArtist( artist )
        

    def Plot(self, Type: str, **kwargs) -> Plots.Scene:
        """
        Generic plot function
        """
        

        Figure = Plots.Scene()
        Ax = Plots.Axis(Row=0, Col=0, Legend=True)
        Figure.AddAxes(Ax)

        match Type.lower():
            case 'index':
                self.__render__index__(Figure=Figure, Ax=Ax, **kwargs)
            case 'beta':
                self.__render__beta__(Figure=Figure, Ax=Ax, **kwargs)
            case 'coupling':
                self.__render__coupling__(Figure=Figure, Ax=Ax, **kwargs)
            case 'adiabatic':
                self.__render__adiabatic__(Figure=Figure, Ax=Ax, **kwargs)
            case 'field':
                self.__render_field__(Figure=Figure, Ax=Ax, **kwargs)

        return Figure


    def __getitem__(self, N) -> _SuperMode:
        return self.Slice[N]


    def __setitem__(self, N, val):
        self.Slice[N] = val


    def GetArrangedFields(self) -> numpy.ndarray:
        sign = numpy.sign( numpy.sum(self.Fields[0]))
        Fields = [sign*self.Fields[0]]

        for field in self.Fields:
            overlap = numpy.sum(field*Fields[-1])
            if overlap > 0:
                Fields.append(field/numpy.max(numpy.abs(field)))

            if overlap <= 0:
                Fields.append(-field/numpy.max(numpy.abs(field)))

        return FullFields


    def PlotPropagation(self, SaveName: str='Annimation') -> None:
        FullFields = self.GetArrangedFields()

        FileName = f'{Directories.RootPath}/Animation/{SaveName}.gif'

        Plots.PlotPropagation(self.FullFields, SaveAs=FileName)








# -
