#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy
from SuPyMode.Tools.utils       import NA2nCore
from FiberFusing                import Geometry, Fused7, Circle, BackGround

from PyOptik                    import ExpData

from SuPyMode.Materials         import FusedSilica




def AddFiber(Cores, Fiber, Angles, Radius):
    for angle in Angles:
        if angle is None:
            P = (0,0)
        else:
            P = (Radius*numpy.cos(angle*numpy.pi/180), Radius*numpy.sin(angle*numpy.pi/180))
        Cores += Fiber.Get(Position=P)


class Fiber_DCF1300S_20():
    def __init__(self, Wavelength):
        Index = ExpData('FusedSilica').GetRI(Wavelength*1e-6)
        self.nClad = NA2nCore( 0.11, Index )
        self.nCore = NA2nCore( 0.12, self.nClad )
        self.rClad = 19.9/2
        self.rCore = 4.6

    def GetGeometries(self, Position):
        self.Fiber = [
                       Circle( Position=Position, Radius=self.rClad, Index=self.nClad ),
                       Circle( Position=Position, Radius=self.rCore, Index=self.nCore ),
                       ]
        return self.Fiber

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "DCF1300S_20"


class Fiber_DCF1300S_33():
    def __init__(self, Wavelength):
        Index = ExpData('FusedSilica').GetRI(Wavelength*1e-6)
        self.nClad = NA2nCore( 0.11, Index  )
        self.nCore = NA2nCore( 0.125, self.nClad )
        self.rClad = 33/2
        self.rCore = 4.5

    def GetGeometries(self, Position):
        self.Fiber = [
                       Circle( Position=Position, Radius=self.rClad, Index=self.nClad ),
                       Circle( Position=Position, Radius=self.rCore, Index=self.nCore ),
                       ]
        return self.Fiber


    def __str__(self):
        return "DCF1300S_33"

    def __repr__(self):
        return self.__str__()

class Fiber_New_A():
    def __init__(self, Wavelength):
        Index = ExpData('FusedSilica').GetRI(Wavelength*1e-6)
        self.nClad = NA2nCore( 0.11, Index  )
        self.nCore = NA2nCore( 0.13, self.nClad )
        self.rClad = 33/2
        self.rCore = 4.5

    
    def GetGeometries(self, Position):
        self.Fiber = [
                       Circle( Position=Position, Radius=self.rClad, Index=self.nClad ),
                       Circle( Position=Position, Radius=self.rCore, Index=self.nCore ),
                       ]
        return self.Fiber

    def __str__(self):
        return "New_fiber"

    def __repr__(self):
        return self.__str__()


class Fiber_New_B():
    def __init__(self, Wavelength):
        Index = ExpData('FusedSilica').GetRI(Wavelength*1e-6)
        self.nClad = NA2nCore( 0.11, Index  )
        self.nCore = NA2nCore( 0.115, self.nClad )
        self.rClad = 33/2
        self.rCore = 4.5

    def GetGeometries(self, Position):
        self.Fiber = [
                       Circle( Position=Position, Radius=self.rClad, Index=self.nClad ),
                       Circle( Position=Position, Radius=self.rCore, Index=self.nCore ),
                       ]
        return self.Fiber

    def __str__(self):
        return "New_fiber"

    def __repr__(self):
        return self.__str__()


class Fiber_2028M24():
    def __init__(self, Wavelength):
        self.nClad = NA2nCore( 0.19, ExpData('FusedSilica').GetRI(Wavelength*1e-6)  )
        self.nCore = NA2nCore( 0.11, self.nClad )
        self.rClad = 14.1/2
        self.rCore = 2.3/2

    def __str__(self):
        return "2028M24"

    def __repr__(self):
        return self.__str__()

class Fiber_2028M21():
    def __init__(self, Wavelength):
        self.nClad = NA2nCore( 0.19, ExpData('FusedSilica').GetRI(Wavelength*1e-6)  )
        self.nCore = NA2nCore( 0.11, self.nClad )
        self.rClad = 17.6/2
        self.rCore = 2.8/2

    def __str__(self):
        return "2028M21"

    def __repr__(self):
        return self.__str__()


class Fiber_2028M12():
    def __init__(self, Wavelength):
        self.nClad = NA2nCore( 0.19, ExpData('FusedSilica').GetRI(Wavelength*1e-6)  )
        self.nCore = NA2nCore( 0.11, self.nClad )
        self.rClad = 25.8/2
        self.rCore = 4.1/2

    def __str__(self):
        return "2028M12"

    def __repr__(self):
        return self.__str__()


class Fiber_SMF28():
    def __init__(self, Wavelength):
        self.NA    = 0.12
        self.nClad = ExpData('FusedSilica').GetRI(Wavelength*1e-6)
        self.nCore = ExpData('FusedSilica').GetRI(Wavelength*1e-6)+0.005#NA2nCore( 0.14, self.nClad )
        self.rClad = 62.5
        self.rCore = 4.1

    def GetGeometries(self, Position):
        self.Fiber = [ Circle( Position=Position, Radius=self.rCore, Index=self.nCore ) ]
        return self.Fiber

    def __str__(self):
        return "SMF28"

    def __repr__(self):
        return self.__str__()
