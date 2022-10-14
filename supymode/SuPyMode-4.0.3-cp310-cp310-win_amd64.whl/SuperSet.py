#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Iterable
import numpy, os, logging
from dataclasses import dataclass
from scipy.interpolate import interp1d
from scipy.integrate import solve_ivp


from SuPyMode.SuperMode import SuperMode
from SuPyMode.SuperPosition import SuperPosition
from SuPyMode.Tools.utils import DebugFunction
import SuPyMode.Tools.Plots as Plots
from SuPyMode.Tools import Directories

@dataclass
class SuperSet(object):
    """ 
    Solver to which is associated the computed SuperSet Modes

    .. note::
        This class is a representation of the fiber optic structures set of supermodes, hence the name. 
        This class has not ling to c++ codes, it is pure Python. 
        The items of this class are the supermodes generated from within the SuPySolver

    """

    ParentSolver: None=None

    def __post_init__(self):

        self._Coupling     = None
        self._Adiabatic    = None
        self._Index        = None
        self._Beta         = None
        self._Matrix       = None

        self.SuperModes     = []
        self._ITR2SliceInterp = interp1d( self.ITRList, numpy.arange(self.ITRList.size) )

    @property
    def Size(self):
        """
        Return number of supermodes computed
        """

        return len(self.SuperModes)

    @property
    def Geometry(self):
        """
        Return geometry of the coupler structure
        """

        return self.ParentSolver.Geometry

    @property
    def ITRList(self):
        """
        Return list of ITR value that are used to compute the supermodes
        """

        return self.ParentSolver.ITRList

    @property
    def Axes(self):
        """
        Return axes object of the geometry
        """

        return self.ParentSolver.Geometry.Axes

    @property
    def Matrix(self):
        """Return supermode transfert matrix"""
        if self._Matrix is None:
            self.ComputeMatrix()

        return self._Matrix

    @property
    def FullxAxis(self):
        """
        Return full x-axis taking account for the symmetries of the solve
        r"""

        if self._FullxAxis is None:
            self._FullxAxis, self._FullyAxis = self.GetFullAxis(self.Axes.X, self.Axes.Y)
        return self._FullxAxis


    @property
    def FullyAxis(self):
        """
        Return full y-axis taking account for the symmetries of the solver
        """

        if self._FullyAxis is None:
            self._FullxAxis, self._FullyAxis = self.GetFullAxis(self.Axes.X, self.Axes.Y)
        return self._FullyAxis

    @property
    def Geometry(self):
        """
        Return geometry of the coupler structure
        """

        return self.ParentSolver.Geometry

    @property
    def ITR(self):
        """
        Return list of the ITR values used for computation
        """

        return self.Geometry.ITRList


    def ITR2Slice(self, ITR: float | Iterable) -> float | Iterable:
        """
        Return slice number associated to ITR value

        Args:
            ITR: Inverse taper ration value to evaluate the slice.
        """


        if isinstance(ITR, Iterable):
            return self._ITR2SliceInterp(ITR).astype(int)

        else:
            return int(self._ITR2SliceInterp(ITR))


    def ComputeMatrix(self) -> numpy.ndarray:
        """
        Compute supermode transfert matrix
        """

        self._Matrix = numpy.zeros([self.Size, self.Size, len(self.ITRList)])

        for mode in self.SuperModes:
            self._Matrix[mode._ModeNumber, mode._ModeNumber, :] = mode.Betas


    def _ComputeMatrix(self, CouplingFactor):
        """
        Compute supermode transfert matrix with coupling coefficients
        """

        shape = self.Beta.shape
        M     = numpy.zeros( [shape[0], shape[1], shape[1]] )
        for iter in range(shape[0]):
            beta = self.Beta[iter]
            M[iter] = CouplingFactor[iter] * self.Coupling[iter] + beta * numpy.identity(shape[1])

        return M


    def ComputeCouplingFactor(self, Length: float) -> float:
        """
        Compute coupling factor
        """

        dx =  Length/(self.Geometry.ITRList.size)

        dITR = numpy.gradient(numpy.log(self.Geometry.ITRList), 1)

        return dITR/dx


    def GetSuperposition(self, Amplitudes) -> SuperPosition:
        return SuperPosition(SuperSet=self, InitialAmplitudes=Amplitudes)


    def Propagate(self, Amplitude=[1,1, 0, 0, 0], Length=1000, **kwargs) -> numpy.ndarray:
        """
        Plot coupling value of each mode as a function of ITR

        Args:
            Amplitude: Initial amplitude of the propagation.
            Length: Length of the coupler for propagation.

        """

        Amplitude = numpy.asarray(Amplitude)

        Distance = numpy.linspace(0, Length, self.ITRList.size)

        #Factor = self.ComputeCouplingFactor(Length)

        #M = self.ComputeM(CouplingFactor=Factor)

        Minterp = interp1d(Distance, self.Matrix, axis=-1)

        def foo(t, y):
            return 1j * Minterp(t).dot(y)

        sol = solve_ivp(foo,
                        y0       = Amplitude.astype(complex),
                        t_span   = [0, Length],
                        method   = 'RK45', **kwargs)

        return sol.y


    def _Propagate(self, Amplitude, Length, **kwargs):
        Amplitude = numpy.asarray(Amplitude)

        Distance = numpy.linspace(0, Length, self.Geometry.ITRList.size)

        Factor = self.ComputeCouplingFactor(Length)

        M = self.ComputeM(CouplingFactor=Factor)

        Minterp = interp1d(Distance, M, axis=0)

        def foo(t, y):
            return 1j * Minterp(t).dot(y)

        sol = solve_ivp(foo,
                        y0       = Amplitude.astype(complex),
                        t_span   = [0, Length],
                        method   = 'RK45',
                        **kwargs)

        return sol


    def AppendSuperMode(self, **kwargs) -> None:
        """
        Add a supermode to the SuperSet list of supermodes.
        """

        superMode = SuperMode(ParentSet=self, **kwargs)

        self.SuperModes.append( superMode )


    def __getitem__(self, N):
        return self.SuperModes[N]


    def __setitem__(self, N, val):
        self.SuperModes[N] = val



    def PlotIndex(self) -> Plots.Scene:
        """
        Plot effective refractive index of each mode as a function of ITR
        """

        Figure = Plots.Scene()

        Ax = Plots.Axis(Row=0, Col=0, Legend=True)

        for supermode in self.SuperModes:
            supermode.__render__index__(Figure=Figure, Ax=Ax)

        Figure.AddAxes(Ax)

        return Figure


    def PlotBeta(self) -> Plots.Scene:
        """
        Plot propagation constant of each mode as a function of ITR
        """
        
        Figure = Plots.Scene()

        Ax = Plots.Axis(Row=0, Col=0, Legend=True)

        for supermode in self.SuperModes:
            supermode.__render__beta__(Figure=Figure, Ax=Ax)

        Figure.AddAxes(Ax)

        return Figure



    def PlotCoupling(self, ModeOfInterest: list=None) -> Plots.Scene:
        """
        Plot coupling value of each mode as a function of ITR

        Args:
            ModeOfInterest: List of mode to be plotted in the graphics.
        """
        Figure = Plots.Scene()
        Ax = Plots.Axis(Row=0, Col=0, Legend=True)

        for Mode0, Mode1 in self.GetCombinations():
            if ModeOfInterest and Mode0.ID not in ModeOfInterest and Mode1.ID not in ModeOfInterest:
                continue

            else:
                Mode0.__render__coupling__(Figure=Figure, Ax=Ax, Other=Mode1)

        Figure.AddAxes(Ax)

        return Figure


    def PlotAdiabatic(self, ModeOfInterest: list=None) -> Plots.Scene:
        """
        Plot adiabatic criterion of each mode as a function of ITR
        """

        
        Figure = Plots.Scene()
        Ax = Plots.Axis(Row=0, Col=0, Legend=True)

        for Mode0, Mode1 in self.GetCombinations():

            if ModeOfInterest and Mode0.ID not in ModeOfInterest and Mode1.ID not in ModeOfInterest:
                continue
            else:
                Mode0.__render__adiabatic__(Figure=Figure, Ax=Ax, Other=Mode1)

        Figure.AddAxes(Ax)

        return Figure



    def GetCombinations(self) -> list:
        """
        Return list of all combination of fiber that respects the same symmetries
        """
        
        
        Combination = []
        for Mode0 in self.SuperModes:
            for Mode1 in self.SuperModes:
                if Mode0.SolverNumber != Mode1.SolverNumber: 
                    continue

                if Mode0.BindingNumber == Mode1.BindingNumber: 
                    continue

                if (Mode1, Mode0) in Combination: 
                    continue

                Combination.append((Mode0, Mode1))

        return Combination



    def PlotField(self, ITR: list=[1], Slice: list=[]) -> Plots.Scene:
        """
        Plot each of the mode field for different ITR value or Slice number
        """


        Figure = Plots.Scene(UnitSize = (3,3))

        if len(ITR) != 0:
            for m, Mode in enumerate(self.SuperModes):
                for n, itr in enumerate(ITR):
                    Ax = Plots.Axis(Row=n, Col=m, Equal=True)
                    Figure.AddAxes(Ax)

                    self[m].__render_field__(Figure=Figure, Ax=Ax, ITR=itr)


            return Figure

        if len(Slice) != 0:
            for m, Mode in enumerate(self.SuperModes):
                for n, slc in enumerate(Slice):
                    Ax = Plots.Axis(Row=n, Col=m, Equal=True)
                    Figure.AddAxes(Ax)

                    self[m].__render_field__(Figure=Figure, Ax=Ax, Slice=slc)


            return Figure


    def Plot(self, Type: str, **kwargs) -> Plots.Scene:
        """
        Generic plot function
        """


        assert Type.lower() in (TypeList := ['index', 'beta', 'adiabatic', 'coupling', 'field']), f'Type [{Type}] as to be in {TypeList}'

        match Type.lower():
            case 'index':
                return self.PlotIndex(**kwargs)
            case 'beta':
                return self.PlotBeta(**kwargs)
            case 'coupling':
                return self.PlotCoupling(**kwargs)
            case 'adiabatic':
                return self.PlotAdiabatic(**kwargs)
            case 'field':
                return self.PlotField(**kwargs)


    def GetReport(self, Filename :str='ReportTest', ITR: list=[1], dpi: int=300, ModeOfInterest: list=None) -> None:
        """
        Generate a full report of the coupler properties as a .pdf file
        """


        Figures = []
        Figures.append( self.Geometry.Plot().Render() )

        Figures.append( self.PlotField(ITR=ITR).Render() )

        Figures.append( self.PlotIndex().Render() )

        Figures.append( self.PlotBeta().Render() )

        Figures.append( self.PlotCoupling(ModeOfInterest=ModeOfInterest).Render() )

        Figures.append( self.PlotAdiabatic(ModeOfInterest=ModeOfInterest).Render() )

        directory = os.path.join(Directories.ReportPath, Filename) + '.pdf'

        logging.info(f'Saving report to {directory}')

        Plots.Multipage(directory, figs=Figures, dpi=dpi)














# - 
