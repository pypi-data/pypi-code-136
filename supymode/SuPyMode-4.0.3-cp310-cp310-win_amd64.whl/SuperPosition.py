#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
from scipy.integrate       import solve_ivp
from scipy.interpolate     import interp1d

import SuPyMode.Tools.Plots as Plots


class SuperPosition():
    def __init__(self, SuperSet, InitialAmplitudes: list):
        self.SuperSet   = SuperSet
        self.InitialAmplitudes = numpy.asarray(InitialAmplitudes).astype(complex)
        self._CouplerLength    = None
        self._Amplitudes       = None
        self.Init()



    def Init(self):
        shape = [len(self.InitialAmplitudes)] + list(self.SuperSet[0].FullFields.shape)

        self.Fields = numpy.zeros(shape)
        for n, mode in enumerate(self.SuperSet.SuperModes):
            self.Fields[n] = mode.FullFields


    def Propagate(self, rTol: float = 1e-8, aTol: float = 1e-7, MaxStep: float = numpy.inf):
        Matrix = self.SuperSet.GetPropagationMatrix()

        Z_vs_ITR_Interp = interp1d(self.Distance, self.ITRProfile, axis=-1)

        self.ITR_vs_Matrix_Interp = interp1d(self.ITRList, Matrix, axis=-1, fill_value='extrapolate')

        def foo(z, y):
            ITR = Z_vs_ITR_Interp(z)
            return 1j * self.ITR_vs_Matrix_Interp(ITR).dot(y)

        sol = solve_ivp(foo,
                        y0       = self.InitialAmplitudes,
                        t_span   = [0, self.CouplerLength],
                        method   = 'RK45',
                        rtol     = rTol,
                        atol     = aTol,
                        max_step = MaxStep)

        self.RawAmplitudes, self.RawDistances = sol.y, sol.t

        self.AmplitudeInterpolation = interp1d(self.RawDistances, self.RawAmplitudes, axis=-1)

        self.Slice_vs_ITR_Interp = interp1d(self.RawDistances, numpy.arange(self.RawDistances.size), axis=-1)


    def CreateITRProfile(self, CouplerLength: float, ITRf: float, Type: str='linear', ITRi: float=1, Sigma: float=None, Num: int=100):
        self.CouplerLength = CouplerLength
        self.Distance = numpy.linspace(0, self.CouplerLength, Num)

        if Type.lower() in ['lin', 'linear']:
            segment = numpy.linspace(ITRi, ITRf, Num//2)
            self.ITRProfile = numpy.concatenate( [ segment, segment[::-1] ] )

        if Type.lower() in ['exp', 'exponential']:
            # TODO: add slope computing.
            segment = numpy.exp( - numpy.linspace(0, self.CouplerLength, Num//2)/100 )
            self.ITRProfile = numpy.concatenate( [ segment, segment[::-1] ] )
            Scale = abs( self.ITRProfile.max() - self.ITRProfile.min() )
            self.ITRProfile /= Scale / abs(ITRi - ITRf)
            self.ITRProfile -= self.ITRProfile.max() - ITRi


        if Type.lower() in ['gauss', 'gaussian']:
            assert Sigma is not None, "You must provide a value for Gaussian standard deviation, [Sigma]."
            self.ITRProfile = numpy.exp( ( ( self.Distance - self.Distance.mean() ) / Sigma )**2 )
            Scale = abs( self.ITRProfile.max() - self.ITRProfile.min() )
            self.ITRProfile /= Scale / abs(ITRi - ITRf)
            self.ITRProfile -= self.ITRProfile.max() - ITRi


    @property
    def ITRList(self):
        return self.SuperSet.ITRList


    def ITR2Slice(self, ITR: float):
        return int( self.Slice_vs_ITR_Interp(ITR) )



    def Amplitudes(self, Slice: int, ITR: float=None):
        amplitudes = self.RawAmplitudes[:, Slice]
        return amplitudes


    def PlotAmplitudes(self):
        Fig = Plots.Scene(Title='SuPyMode Figure', UnitSize=(10,4))

        ax0 = Plots.Axis(Row    = 0,
                   Col    = 0,
                   xLabel = 'Z-propagation distance',
                   yLabel = r'Mode amplitude',
                   Grid   = True,
                   Legend = True,
                   WaterMark = 'SuPyMode')

        ax1 = Plots.Axis(Row    = 1,
                   Col    = 0,
                   xLabel = 'Z-propagation distance',
                   yLabel = r'ITR profile',
                   Grid   = True,
                   Legend = True,
                   WaterMark = 'SuPyMode')

        A = self.InitialAmplitudes.dot(self.RawAmplitudes)

        artist0 = Plots.Line(X=self.RawDistances, Y=A.real, Label='real part', Fill=False)
        artist1 = Plots.Line(X=self.RawDistances, Y=A.imag, Label='imag part', Fill=False)
        artist2 = Plots.Line(X=self.Distance,     Y=self.ITRProfile, Label='', Fill=False)

        ax0.AddArtist(artist0, artist1)
        ax1.AddArtist(artist2)

        Fig.AddAxes(ax0, ax1)

        return Fig


    def PlotField(self, ITR: list):

        Slices = [ self.ITR2Slice(itr) for itr in ToList(ITR) ]

        Fig = Plots.Scene(Title='SuPyMode Figure', UnitSize=(4,4))

        amplitudes = self.Amplitudes(0)

        Colorbar = Plots.ColorBar(Discreet=False, Position='bottom')

        for n, slice in enumerate(Slices):

            ax = Plots.Axis(Row              = 0,
                      Col              = n,
                      xLabel           = r'x [$\mu m$]',
                      yLabel           = r'y [$\mu m$]',
                      Title            = f'Mode field  [ITR: {self.ITRList[slice]:.2f}]',
                      Legend           = False,
                      Grid             = False,
                      Equal            = True,
                      Colorbar         = Colorbar,
                      xScale           = 'linear',
                      yScale           = 'linear')


            artist = Plots.Mesh(X           = self.SuperSet.FullxAxis,
                          Y           = self.SuperSet.FullyAxis,
                          Scalar      = self.Fields[0,slice,...],
                          ColorMap    = FieldMap,
                          )

            ax.AddArtist(artist)

            Fig.AddAxes(ax)

        return Fig



    def PlotPropagation(self):
        if self._Amplitudes is None: self.ComputeAmpltiudes()

        y = self.AmplitudeInterpolation(self.Distance)

        z = self.Distance

        Field = self.SuperSet[0].FullFields.astype(complex)*0.

        for mode, _ in enumerate(self.InitialAmplitudes):
            a = y[mode].astype(complex)
            field = self.SuperSet[mode].FullFields.astype(complex)
            Field += numpy.einsum('i, ijk->ijk', a, field)

        surface = mlab.surf( numpy.abs( Field[0] ) , warp_scale="auto" )

        @mlab.animate(delay=100)
        def anim_loc():
            for n, _ in enumerate(self.Distance):
                surface.mlab_source.scalars = numpy.abs(numpy.abs( Field[n] ) )

                yield

        anim_loc()
        mlab.show()
