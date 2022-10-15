#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy, logging
from dataclasses import dataclass, field

from SuPyMode.SuperSet import SuperSet
from SuPyMode.Binary.CppSolver import CppSolver
from SuPyMode.Tools.utils import DebugFunction

from PyFinitDiff.Source import FiniteDifference2D


@dataclass()
class SuPySolver(object):
    """ 
    .. note::
        This solver class directly links to a c++ Eigensolver. 
        It solves the eigenvalues problems for a given geometry and return a collection of SuperModes.
    
    """
    Geometry: None = field(repr=False)
    """Geometry of the coupler structure"""

    Tolerance : float = 1e-5
    """Absolute tolerance on the propagation constant computation"""

    MaxIter : int = 10000
    """Maximum iteration for the c++ Eigensolver"""

    Accuracy: int = 2  
    """Accuracy of the finit difference methode"""

    def __post_init__(self):
        self.ModeNumber = 0
        self.SolverNumber = 0
        self.Geometry.GenerateMesh()

    @property
    def Axes(self):
        return self.Geometry.Axes


    def InitBinding(self, Wavelength: float, nComputedMode: int, nSortedMode: int, Symmetries: dict) -> CppSolver: 
        """
        Args:
            Wavelength: Wavelenght for the mode computation
            nComputedMode: Number of mode that are going to be solved using the c++ solver.
            nSortedMode: Number of mode that are outputed by the c++ solver. Has to be larger than nComputedMode.
            Symmetries: Symmetries of the finit-difference system. 
        """

        logging.info('Setting up the c++ solver...')

        self.FD = FiniteDifference2D(Nx         = self.Axes.x.N, 
                                     Ny         = self.Axes.y.N, 
                                     dx         = self.Axes.x.d, 
                                     dy         = self.Axes.y.d,
                                     Derivative = 2, 
                                     Accuracy   = self.Accuracy,
                                     Symmetries = Symmetries)

        self.FD.Compute()

        Solver = CppSolver(Mesh          = self.Geometry.Mesh,
                           Gradient      = self.Geometry.Gradient.ravel(),
                           FinitMatrix   = self.FD.ToTriplet(),
                           nComputedMode = nComputedMode,
                           nSortedMode   = nSortedMode,
                           MaxIter       = self.MaxIter,
                           Tolerance     = self.Tolerance,
                           dx            = self.Axes.x.d,
                           dy            = self.Axes.y.d,
                           Wavelength    = Wavelength,
                           Debug         = True)

        Solver.SetSymmetries(**Symmetries)
        Solver.ComputeLaplacian()

        return Solver


    def CreateSuperSet(self, Wavelength: float, NStep: int=300, ITRi: float=1.0, ITRf: float=0.1) -> None:
        """
        Args:
            Wavelength: Wavelenght for the mode computation
            NStep: Number of stop to iterate through the ITR (inverse taper ration) section.
            ITRi: Initial value of ITR.
            ITRf: Final value of ITR. 
        """
        
        self.Wavelength = Wavelength
        self.NStep      = NStep
        self.ITRi       = ITRi
        self.ITRf       = ITRf
        self.ITRList    = numpy.linspace(ITRi, ITRf, NStep)
        self.Set        = SuperSet(ParentSolver=self)


    def AddModes(self, nSortedMode: int, Symmetries: dict, Sorting: str='index', nComputedMode: int=None, Alpha: float=0) -> None:
        """
        Args:
            Symmetries: Symmetries of the finit-difference system. 
            nComputedMode: Number of mode that are going to be solved using the c++ solver.
            nSortedMode: Number of mode that are outputed by the c++ solver. Has to be larger than nComputedMode.
            Sorting: Sorting method used to classifiy the modes ['index', 'field']. 
            Alpha: Initial guess for mode solving (if 0, auto evaluated). 
        """
        
        if nComputedMode is None: nComputedMode = nSortedMode + 2

        assert Sorting.lower() in ['index', 'field'], f"Incorrect sorting method: {Sorting}; Sorting can be ['Index', 'Field']"
        
        CppSolver  = self.InitBinding(Symmetries=Symmetries, Wavelength=self.Wavelength, nComputedMode=nComputedMode, nSortedMode=nSortedMode)

        CppSolver.LoopOverITR(ITR=self.ITRList, ExtrapolationOrder=3, Alpha=Alpha)

        CppSolver.SortModes(Sorting=Sorting.lower())

        CppSolver.ComputeCouplingAdiabatic()

        for BindingNumber in range(CppSolver.nSortedMode):
            self.Set.AppendSuperMode(CppSolver=CppSolver, BindingNumber=BindingNumber, SolverNumber=self.SolverNumber, ModeNumber=self.ModeNumber)
            self.ModeNumber +=1

        self.SolverNumber += 1



    def GetSet(self):
        return self.Set



# ---
